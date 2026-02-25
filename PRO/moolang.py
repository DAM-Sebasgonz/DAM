#!/usr/bin/env python3
# =============================================================================
#  MOOlang - Intérprete Completo
#  Un lenguaje funcional puro con temática bovina 🐄
#
#  ARQUITECTURA:
#    1. Lexer    → convierte texto fuente en tokens
#    2. Parser   → construye un AST desde los tokens
#    3. AST      → nodos que representan la estructura del programa
#    4. Evaluador → recorre el AST y produce resultados
#    5. Entorno  → maneja el alcance léxico (scoping)
# =============================================================================

import re
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union


# =============================================================================
# SECCIÓN 1: TOKENS
# Definición de todos los tipos de tokens del lenguaje
# =============================================================================

class TokenType:
    # ── Palabras clave bovinas ──────────────────────────────────────────────
    MOO      = "MOO"        # Declaración de variable/valor inmutable
    LECHE    = "LECHE"      # Definición de función (produce algo, como la leche)
    PASTAR   = "PASTAR"     # Iniciar evaluación / punto de entrada principal
    RUMIAR   = "RUMIAR"     # Condicional IF (las vacas rumian antes de decidir)
    ORUMIR   = "ORUMIR"     # Condicional ELSE (el otro lado de la rumia)
    MUGIR    = "MUGIR"      # Imprimir / output (las vacas muguen para comunicar)
    ESTABLO  = "ESTABLO"    # Bloque de código / inicio de scope
    SALIR    = "SALIR"      # Fin de bloque / end (salir del establo)
    LLAMAR   = "LLAMAR"     # Aplicación de función (llamar a otra vaca)
    BOVINO   = "BOVINO"     # True booleano (es un bovino auténtico)
    NOBOVINO = "NOBOVINO"   # False booleano (no es bovino)
    RECUR    = "RECUR"      # Recursión explícita (auto-referencia)

    # ── Literales ───────────────────────────────────────────────────────────
    NUMBER   = "NUMBER"     # Número entero o flotante
    STRING   = "STRING"     # Cadena de texto entre comillas
    IDENT    = "IDENT"      # Identificador / nombre de variable o función

    # ── Operadores aritméticos ──────────────────────────────────────────────
    PLUS     = "PLUS"       # +
    MINUS    = "MINUS"      # -
    STAR     = "STAR"       # *
    SLASH    = "SLASH"      # /
    PERCENT  = "PERCENT"    # % (módulo)

    # ── Operadores de comparación ───────────────────────────────────────────
    EQ       = "EQ"         # ==
    NEQ      = "NEQ"        # !=
    LT       = "LT"         # <
    GT       = "GT"         # >
    LEQ      = "LEQ"        # <=
    GEQ      = "GEQ"        # >=

    # ── Operadores lógicos ──────────────────────────────────────────────────
    AND      = "AND"        # &&
    OR       = "OR"         # ||
    NOT      = "NOT"        # !

    # ── Puntuación ──────────────────────────────────────────────────────────
    LPAREN   = "LPAREN"     # (
    RPAREN   = "RPAREN"     # )
    LBRACKET = "LBRACKET"   # [
    RBRACKET = "RBRACKET"   # ]
    COMMA    = "COMMA"      # ,
    ARROW    = "ARROW"      # -> (retorno de función)
    ASSIGN   = "ASSIGN"     # = (asignación de binding)

    # ── Control ─────────────────────────────────────────────────────────────
    NEWLINE  = "NEWLINE"
    EOF      = "EOF"


@dataclass
class Token:
    """Unidad atómica producida por el Lexer."""
    type: str
    value: Any
    line: int
    col: int

    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, L{self.line}:C{self.col})"


# =============================================================================
# SECCIÓN 2: LEXER (Analizador Léxico)
# Transforma el código fuente en una secuencia de tokens
# =============================================================================

# Palabras reservadas del lenguaje → tipo de token correspondiente
KEYWORDS = {
    "MOO":      TokenType.MOO,
    "LECHE":    TokenType.LECHE,
    "PASTAR":   TokenType.PASTAR,
    "RUMIAR":   TokenType.RUMIAR,
    "ORUMIR":   TokenType.ORUMIR,
    "MUGIR":    TokenType.MUGIR,
    "ESTABLO":  TokenType.ESTABLO,
    "SALIR":    TokenType.SALIR,
    "LLAMAR":   TokenType.LLAMAR,
    "BOVINO":   TokenType.BOVINO,
    "NOBOVINO": TokenType.NOBOVINO,
    "RECUR":    TokenType.RECUR,
}


class LexerError(Exception):
    def __init__(self, msg, line, col):
        super().__init__(f"[LexerError L{line}:C{col}] {msg}")


class Lexer:
    """
    Analizador léxico de MOOlang.

    Recorre el código fuente carácter por carácter y produce tokens.
    Soporta:
      - Palabras clave bovinas
      - Números enteros y flotantes
      - Cadenas entre comillas dobles
      - Comentarios de línea con #
      - Todos los operadores y delimitadores
    """

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens: List[Token] = []

    def error(self, msg):
        raise LexerError(msg, self.line, self.col)

    def peek(self, offset=0) -> str:
        idx = self.pos + offset
        return self.source[idx] if idx < len(self.source) else '\0'

    def advance(self) -> str:
        ch = self.source[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return ch

    def match(self, expected: str) -> bool:
        if self.pos < len(self.source) and self.source[self.pos] == expected:
            self.advance()
            return True
        return False

    def skip_whitespace_and_comments(self):
        while self.pos < len(self.source):
            ch = self.peek()
            if ch in (' ', '\t', '\r'):
                self.advance()
            elif ch == '#':  # Comentario de línea
                while self.pos < len(self.source) and self.peek() != '\n':
                    self.advance()
            else:
                break

    def read_number(self) -> Token:
        start_col = self.col
        num_str = ""
        is_float = False
        while self.pos < len(self.source) and (self.peek().isdigit() or self.peek() == '.'):
            if self.peek() == '.':
                if is_float:
                    break
                is_float = True
            num_str += self.advance()
        value = float(num_str) if is_float else int(num_str)
        return Token(TokenType.NUMBER, value, self.line, start_col)

    def read_string(self) -> Token:
        start_col = self.col
        self.advance()  # consumir "
        result = ""
        while self.pos < len(self.source) and self.peek() != '"':
            ch = self.advance()
            if ch == '\\':
                esc = self.advance()
                result += {'n': '\n', 't': '\t', '"': '"', '\\': '\\'}.get(esc, esc)
            else:
                result += ch
        if self.pos >= len(self.source):
            self.error("Cadena no terminada (¿olvidaste cerrar las comillas?)")
        self.advance()  # consumir "
        return Token(TokenType.STRING, result, self.line, start_col)

    def read_identifier_or_keyword(self) -> Token:
        start_col = self.col
        ident = ""
        while self.pos < len(self.source) and (self.peek().isalnum() or self.peek() == '_'):
            ident += self.advance()
        tok_type = KEYWORDS.get(ident, TokenType.IDENT)
        return Token(tok_type, ident, self.line, start_col)

    def tokenize(self) -> List[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace_and_comments()
            if self.pos >= len(self.source):
                break

            ch = self.peek()
            start_line, start_col = self.line, self.col

            # ── Salto de línea (significativo como separador de sentencias)
            if ch == '\n':
                self.advance()
                # Evitar múltiples NEWLINE consecutivos
                if not self.tokens or self.tokens[-1].type != TokenType.NEWLINE:
                    self.tokens.append(Token(TokenType.NEWLINE, '\n', start_line, start_col))
                continue

            # ── Números
            if ch.isdigit():
                self.tokens.append(self.read_number())
                continue

            # ── Cadenas
            if ch == '"':
                self.tokens.append(self.read_string())
                continue

            # ── Identificadores / palabras clave
            if ch.isalpha() or ch == '_':
                self.tokens.append(self.read_identifier_or_keyword())
                continue

            # ── Operadores y puntuación
            self.advance()  # consumir el carácter actual
            tok = None

            if ch == '+': tok = Token(TokenType.PLUS, '+', start_line, start_col)
            elif ch == '*': tok = Token(TokenType.STAR, '*', start_line, start_col)
            elif ch == '%': tok = Token(TokenType.PERCENT, '%', start_line, start_col)
            elif ch == '(': tok = Token(TokenType.LPAREN, '(', start_line, start_col)
            elif ch == ')': tok = Token(TokenType.RPAREN, ')', start_line, start_col)
            elif ch == '[': tok = Token(TokenType.LBRACKET, '[', start_line, start_col)
            elif ch == ']': tok = Token(TokenType.RBRACKET, ']', start_line, start_col)
            elif ch == ',': tok = Token(TokenType.COMMA, ',', start_line, start_col)
            elif ch == '-':
                if self.match('>'):
                    tok = Token(TokenType.ARROW, '->', start_line, start_col)
                else:
                    tok = Token(TokenType.MINUS, '-', start_line, start_col)
            elif ch == '/': tok = Token(TokenType.SLASH, '/', start_line, start_col)
            elif ch == '=':
                if self.match('='):
                    tok = Token(TokenType.EQ, '==', start_line, start_col)
                else:
                    tok = Token(TokenType.ASSIGN, '=', start_line, start_col)
            elif ch == '!':
                if self.match('='):
                    tok = Token(TokenType.NEQ, '!=', start_line, start_col)
                else:
                    tok = Token(TokenType.NOT, '!', start_line, start_col)
            elif ch == '<':
                if self.match('='):
                    tok = Token(TokenType.LEQ, '<=', start_line, start_col)
                else:
                    tok = Token(TokenType.LT, '<', start_line, start_col)
            elif ch == '>':
                if self.match('='):
                    tok = Token(TokenType.GEQ, '>=', start_line, start_col)
                else:
                    tok = Token(TokenType.GT, '>', start_line, start_col)
            elif ch == '&':
                if self.match('&'):
                    tok = Token(TokenType.AND, '&&', start_line, start_col)
                else:
                    self.error(f"Carácter inesperado '{ch}' (¿quisiste escribir &&?)")
            elif ch == '|':
                if self.match('|'):
                    tok = Token(TokenType.OR, '||', start_line, start_col)
                else:
                    self.error(f"Carácter inesperado '{ch}' (¿quisiste escribir ||?)")
            else:
                self.error(f"Carácter desconocido: '{ch}'")

            if tok:
                self.tokens.append(tok)

        self.tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return self.tokens


# =============================================================================
# SECCIÓN 3: AST (Árbol de Sintaxis Abstracta)
# Nodos que representan la estructura lógica del programa
# =============================================================================

@dataclass
class ASTNode:
    """Clase base para todos los nodos del AST."""
    pass


@dataclass
class NumberNode(ASTNode):
    """Literal numérico: 42, 3.14"""
    value: Union[int, float]


@dataclass
class StringNode(ASTNode):
    """Literal de cadena: "Hola vaca" """
    value: str


@dataclass
class BoolNode(ASTNode):
    """Literal booleano: BOVINO / NOBOVINO"""
    value: bool


@dataclass
class IdentNode(ASTNode):
    """Referencia a variable o función por nombre."""
    name: str


@dataclass
class BinOpNode(ASTNode):
    """Operación binaria: izq OP der (aritmética o comparación)."""
    op: str
    left: ASTNode
    right: ASTNode


@dataclass
class UnaryOpNode(ASTNode):
    """Operación unaria: ! expr o - expr"""
    op: str
    operand: ASTNode


@dataclass
class BindingNode(ASTNode):
    """
    MOO nombre = expr
    Crea un binding inmutable en el entorno actual.
    """
    name: str
    value: ASTNode


@dataclass
class FunctionNode(ASTNode):
    """
    LECHE nombre(param1, param2, ...) ESTABLO
        cuerpo
    SALIR
    Define una función con sus parámetros y cuerpo.
    'name' puede ser None para lambdas (no implementado aquí).
    """
    name: str
    params: List[str]
    body: List[ASTNode]


@dataclass
class CallNode(ASTNode):
    """
    LLAMAR nombre(arg1, arg2, ...)
    Aplicación de función.
    """
    callee: str
    args: List[ASTNode]


@dataclass
class IfNode(ASTNode):
    """
    RUMIAR condicion ESTABLO
        rama_then
    SALIR
    ORUMIR ESTABLO
        rama_else
    SALIR
    Expresión condicional (retorna un valor como en lenguajes funcionales).
    """
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: Optional[List[ASTNode]]


@dataclass
class PrintNode(ASTNode):
    """
    MUGIR expr
    Imprime el valor de una expresión en stdout.
    """
    expr: ASTNode


@dataclass
class RecurNode(ASTNode):
    """
    RECUR(arg1, arg2, ...)
    Llamada recursiva explícita a la función actual.
    Separa la recursión del mecanismo de llamada general.
    """
    args: List[ASTNode]


@dataclass
class ProgramNode(ASTNode):
    """Nodo raíz: contiene todas las declaraciones del programa."""
    statements: List[ASTNode]


# =============================================================================
# SECCIÓN 4: PARSER (Analizador Sintáctico)
# Construye el AST a partir de la lista de tokens
# Implementa un parser recursivo descendente (LL(1) con lookahead)
# =============================================================================

class ParseError(Exception):
    def __init__(self, msg, token: Token):
        super().__init__(f"[ParseError L{token.line}:C{token.col}] {msg} (encontré: {token.type}={token.value!r})")


class Parser:
    """
    Parser recursivo descendente para MOOlang.

    Jerarquía de precedencia (de menor a mayor):
      1. expression  → or_expr
      2. or_expr     → and_expr (|| and_expr)*
      3. and_expr    → not_expr (&& not_expr)*
      4. not_expr    → comparison | ! not_expr
      5. comparison  → addition (OP addition)?
      6. addition    → multiplication ((+|-) multiplication)*
      7. multiplication → unary ((*|/|%) unary)*
      8. unary       → -atom | atom
      9. atom        → NUMBER | STRING | BOVINO | NOBOVINO | IDENT | LLAMAR | RECUR | ( expr )
    """

    def __init__(self, tokens: List[Token]):
        self.tokens = [t for t in tokens if t.type != TokenType.NEWLINE]
        self.pos = 0

    def error(self, msg):
        raise ParseError(msg, self.current())

    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek(self, offset=1) -> Token:
        idx = self.pos + offset
        return self.tokens[idx] if idx < len(self.tokens) else self.tokens[-1]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return tok

    def expect(self, type_: str) -> Token:
        tok = self.current()
        if tok.type != type_:
            self.error(f"Se esperaba '{type_}' pero se encontró '{tok.type}'")
        return self.advance()

    def check(self, *types) -> bool:
        return self.current().type in types

    def match(self, *types) -> Optional[Token]:
        if self.check(*types):
            return self.advance()
        return None

    # ── Punto de entrada ────────────────────────────────────────────────────

    def parse(self) -> ProgramNode:
        stmts = []
        while not self.check(TokenType.EOF):
            stmts.append(self.parse_statement())
        return ProgramNode(stmts)

    # ── Sentencias ──────────────────────────────────────────────────────────

    def parse_statement(self) -> ASTNode:
        tok = self.current()

        if tok.type == TokenType.MOO:
            return self.parse_binding()
        elif tok.type == TokenType.LECHE:
            return self.parse_function()
        elif tok.type == TokenType.MUGIR:
            return self.parse_print()
        elif tok.type == TokenType.RUMIAR:
            return self.parse_if()
        elif tok.type == TokenType.PASTAR:
            # PASTAR marca el bloque principal; lo ignoramos como token de control
            self.advance()
            return self.parse_block_as_sequence()
        else:
            # Expresión sola (p.ej. LLAMAR factorial(5))
            return self.parse_expression()

    def parse_block_as_sequence(self) -> ASTNode:
        """Para PASTAR, parsea hasta EOF como secuencia directa."""
        stmts = []
        while not self.check(TokenType.EOF) and not self.check(TokenType.SALIR):
            stmts.append(self.parse_statement())
        if self.check(TokenType.SALIR):
            self.advance()
        if len(stmts) == 1:
            return stmts[0]
        # Wrap como ProgramNode anidado
        return ProgramNode(stmts)

    def parse_binding(self) -> BindingNode:
        """MOO nombre = expresion"""
        self.expect(TokenType.MOO)
        name_tok = self.expect(TokenType.IDENT)
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        return BindingNode(name_tok.value, value)

    def parse_function(self) -> FunctionNode:
        """
        LECHE nombre(param1, param2, ...) ESTABLO
            sentencias
        SALIR
        """
        self.expect(TokenType.LECHE)
        name_tok = self.expect(TokenType.IDENT)
        self.expect(TokenType.LPAREN)
        params = []
        if not self.check(TokenType.RPAREN):
            params.append(self.expect(TokenType.IDENT).value)
            while self.match(TokenType.COMMA):
                params.append(self.expect(TokenType.IDENT).value)
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.ESTABLO)
        body = self.parse_block()
        self.expect(TokenType.SALIR)
        return FunctionNode(name_tok.value, params, body)

    def parse_block(self) -> List[ASTNode]:
        """Parsea sentencias hasta encontrar SALIR o ORUMIR."""
        stmts = []
        while not self.check(TokenType.SALIR) and \
              not self.check(TokenType.ORUMIR) and \
              not self.check(TokenType.EOF):
            stmts.append(self.parse_statement())
        return stmts

    def parse_print(self) -> PrintNode:
        """MUGIR expresion"""
        self.expect(TokenType.MUGIR)
        expr = self.parse_expression()
        return PrintNode(expr)

    def parse_if(self) -> IfNode:
        """
        RUMIAR condicion ESTABLO
            then_body
        SALIR
        [ORUMIR ESTABLO
            else_body
        SALIR]
        """
        self.expect(TokenType.RUMIAR)
        condition = self.parse_expression()
        self.expect(TokenType.ESTABLO)
        then_body = self.parse_block()
        self.expect(TokenType.SALIR)

        else_body = None
        if self.match(TokenType.ORUMIR):
            self.expect(TokenType.ESTABLO)
            else_body = self.parse_block()
            self.expect(TokenType.SALIR)

        return IfNode(condition, then_body, else_body)

    # ── Expresiones (jerarquía de precedencia) ──────────────────────────────

    def parse_expression(self) -> ASTNode:
        return self.parse_or()

    def parse_or(self) -> ASTNode:
        left = self.parse_and()
        while self.check(TokenType.OR):
            op = self.advance().value
            right = self.parse_and()
            left = BinOpNode(op, left, right)
        return left

    def parse_and(self) -> ASTNode:
        left = self.parse_not()
        while self.check(TokenType.AND):
            op = self.advance().value
            right = self.parse_not()
            left = BinOpNode(op, left, right)
        return left

    def parse_not(self) -> ASTNode:
        if self.check(TokenType.NOT):
            op = self.advance().value
            operand = self.parse_not()
            return UnaryOpNode(op, operand)
        return self.parse_comparison()

    def parse_comparison(self) -> ASTNode:
        left = self.parse_addition()
        if self.check(TokenType.EQ, TokenType.NEQ, TokenType.LT,
                      TokenType.GT, TokenType.LEQ, TokenType.GEQ):
            op = self.advance().value
            right = self.parse_addition()
            return BinOpNode(op, left, right)
        return left

    def parse_addition(self) -> ASTNode:
        left = self.parse_multiplication()
        while self.check(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.parse_multiplication()
            left = BinOpNode(op, left, right)
        return left

    def parse_multiplication(self) -> ASTNode:
        left = self.parse_unary()
        while self.check(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.advance().value
            right = self.parse_unary()
            left = BinOpNode(op, left, right)
        return left

    def parse_unary(self) -> ASTNode:
        if self.check(TokenType.MINUS):
            op = self.advance().value
            operand = self.parse_atom()
            return UnaryOpNode(op, operand)
        return self.parse_atom()

    def parse_atom(self) -> ASTNode:
        tok = self.current()

        if tok.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(tok.value)

        elif tok.type == TokenType.STRING:
            self.advance()
            return StringNode(tok.value)

        elif tok.type == TokenType.BOVINO:
            self.advance()
            return BoolNode(True)

        elif tok.type == TokenType.NOBOVINO:
            self.advance()
            return BoolNode(False)

        elif tok.type == TokenType.LLAMAR:
            return self.parse_call()

        elif tok.type == TokenType.RECUR:
            return self.parse_recur()

        elif tok.type == TokenType.IDENT:
            self.advance()
            return IdentNode(tok.value)

        elif tok.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr

        else:
            self.error(f"Se esperaba una expresión pero se encontró '{tok.type}'")

    def parse_call(self) -> CallNode:
        """LLAMAR nombre(arg1, arg2, ...)"""
        self.expect(TokenType.LLAMAR)
        name_tok = self.expect(TokenType.IDENT)
        self.expect(TokenType.LPAREN)
        args = []
        if not self.check(TokenType.RPAREN):
            args.append(self.parse_expression())
            while self.match(TokenType.COMMA):
                args.append(self.parse_expression())
        self.expect(TokenType.RPAREN)
        return CallNode(name_tok.value, args)

    def parse_recur(self) -> RecurNode:
        """RECUR(arg1, arg2, ...)"""
        self.expect(TokenType.RECUR)
        self.expect(TokenType.LPAREN)
        args = []
        if not self.check(TokenType.RPAREN):
            args.append(self.parse_expression())
            while self.match(TokenType.COMMA):
                args.append(self.parse_expression())
        self.expect(TokenType.RPAREN)
        return RecurNode(args)


# =============================================================================
# SECCIÓN 5: ENTORNO (Environment)
# Implementa alcance léxico con cadena de entornos padre-hijo
# =============================================================================

class Environment:
    """
    Entorno de ejecución con alcance léxico.

    Cada llamada a función crea un nuevo entorno hijo.
    La búsqueda de variables sube por la cadena hasta encontrar
    el binding o llegar al entorno global (parent=None).

    En MOOlang todos los bindings son INMUTABLES: una vez definido
    un nombre, no puede reasignarse en el mismo scope.
    """

    def __init__(self, parent: Optional['Environment'] = None, name: str = "global"):
        self.bindings: Dict[str, Any] = {}
        self.parent = parent
        self.name = name  # Para depuración

    def define(self, name: str, value: Any):
        """Define un nuevo binding inmutable en este scope."""
        if name in self.bindings:
            raise RuntimeError(f"'{name}' ya fue definido en este scope (los bindings son inmutables en MOOlang)")
        self.bindings[name] = value

    def lookup(self, name: str) -> Any:
        """Busca un nombre en el scope actual y sus ancestros."""
        if name in self.bindings:
            return self.bindings[name]
        if self.parent:
            return self.parent.lookup(name)
        raise RuntimeError(f"'{name}' no está definido (¿olvidaste declararlo con MOO?)")

    def extend(self, name: str = "local") -> 'Environment':
        """Crea un entorno hijo (para llamadas a funciones)."""
        return Environment(parent=self, name=name)

    def __repr__(self):
        return f"Env({self.name}, {list(self.bindings.keys())})"


# =============================================================================
# SECCIÓN 6: VALORES DE RUNTIME
# Representación interna de funciones
# =============================================================================

@dataclass
class MOOFunction:
    """
    Representa una función de primera clase en MOOlang.

    name:    nombre de la función (para recursión)
    params:  lista de parámetros formales
    body:    lista de nodos AST del cuerpo
    closure: entorno en el que fue definida (captura léxica)
    """
    name: str
    params: List[str]
    body: List[ASTNode]
    closure: Environment

    def __repr__(self):
        return f"<función MOOlang '{self.name}' ({', '.join(self.params)})>"


# =============================================================================
# SECCIÓN 7: EVALUADOR
# Recorre el AST y produce valores
# =============================================================================

class RuntimeError_(Exception):
    """Error en tiempo de ejecución de MOOlang."""
    def __init__(self, msg):
        super().__init__(f"[RuntimeError] {msg}")


class Evaluator:
    """
    Evaluador por interpretación directa del AST (tree-walk interpreter).

    Patrón: visita cada nodo del AST y devuelve su valor.
    El estado global se mantiene en un único entorno raíz.
    Las funciones capturan su entorno de definición (closure léxico).

    Recursión:
      Cuando se evalúa RECUR, el evaluador re-invoca eval_function_body
      con los nuevos argumentos, reutilizando el objeto MOOFunction.
      Esto permite recursión sin necesidad de que la función esté
      en su propio closure (aunque también funciona mediante LLAMAR).
    """

    def __init__(self, verbose: bool = False):
        self.global_env = Environment(name="global")
        self.verbose = verbose
        self._current_function: Optional[MOOFunction] = None  # Para RECUR
        self._call_depth = 0
        self._max_depth = 1000  # Límite de recursión

    def log(self, msg):
        if self.verbose:
            indent = "  " * self._call_depth
            print(f"[TRACE]{indent} {msg}")

    def evaluate(self, node: ASTNode, env: Environment) -> Any:
        """Dispatcher principal: despacha al método correcto según tipo de nodo."""

        if isinstance(node, ProgramNode):
            result = None
            for stmt in node.statements:
                result = self.evaluate(stmt, env)
            return result

        elif isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, StringNode):
            return node.value

        elif isinstance(node, BoolNode):
            return node.value

        elif isinstance(node, IdentNode):
            return env.lookup(node.name)

        elif isinstance(node, BinOpNode):
            return self.eval_binop(node, env)

        elif isinstance(node, UnaryOpNode):
            return self.eval_unaryop(node, env)

        elif isinstance(node, BindingNode):
            value = self.evaluate(node.value, env)
            env.define(node.name, value)
            self.log(f"MOO {node.name} = {value!r}")
            return value

        elif isinstance(node, FunctionNode):
            # Capturar el entorno léxico actual como closure
            fn = MOOFunction(node.name, node.params, node.body, env)
            env.define(node.name, fn)
            self.log(f"LECHE {node.name} definida con {len(node.params)} parámetro(s)")
            return fn

        elif isinstance(node, CallNode):
            return self.eval_call(node, env)

        elif isinstance(node, RecurNode):
            return self.eval_recur(node, env)

        elif isinstance(node, IfNode):
            return self.eval_if(node, env)

        elif isinstance(node, PrintNode):
            value = self.evaluate(node.expr, env)
            print(self.format_value(value))
            return value

        else:
            raise RuntimeError_(f"Nodo AST desconocido: {type(node).__name__}")

    def eval_binop(self, node: BinOpNode, env: Environment) -> Any:
        left = self.evaluate(node.left, env)
        right = self.evaluate(node.right, env)
        op = node.op

        try:
            if op == '+':
                # Concatenación de strings o suma numérica
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif op == '-': return left - right
            elif op == '*': return left * right
            elif op == '/':
                if right == 0:
                    raise RuntimeError_("División por cero (¡las vacas no dividen entre cero!)")
                return left / right
            elif op == '%': return left % right
            elif op == '==': return left == right
            elif op == '!=': return left != right
            elif op == '<':  return left < right
            elif op == '>':  return left > right
            elif op == '<=': return left <= right
            elif op == '>=': return left >= right
            elif op == '&&': return bool(left) and bool(right)
            elif op == '||': return bool(left) or bool(right)
            else:
                raise RuntimeError_(f"Operador desconocido: '{op}'")
        except TypeError as e:
            raise RuntimeError_(f"Tipos incompatibles para operador '{op}': {type(left).__name__} y {type(right).__name__}")

    def eval_unaryop(self, node: UnaryOpNode, env: Environment) -> Any:
        operand = self.evaluate(node.operand, env)
        if node.op == '-':
            return -operand
        elif node.op == '!':
            return not bool(operand)
        raise RuntimeError_(f"Operador unario desconocido: '{node.op}'")

    def eval_call(self, node: CallNode, env: Environment) -> Any:
        """Evalúa una llamada de función: LLAMAR nombre(args...)"""
        fn = env.lookup(node.callee)
        if not isinstance(fn, MOOFunction):
            raise RuntimeError_(f"'{node.callee}' no es una función (es un {type(fn).__name__})")

        args = [self.evaluate(arg, env) for arg in node.args]
        self.log(f"LLAMAR {fn.name}({', '.join(repr(a) for a in args)})")
        return self.apply_function(fn, args)

    def eval_recur(self, node: RecurNode, env: Environment) -> Any:
        """
        Evalúa una llamada recursiva explícita RECUR(...).
        Re-usa el objeto función actual capturado en _current_function.
        """
        if self._current_function is None:
            raise RuntimeError_("RECUR solo puede usarse dentro de una función")
        fn = self._current_function
        args = [self.evaluate(arg, env) for arg in node.args]
        self.log(f"RECUR {fn.name}({', '.join(repr(a) for a in args)})")
        return self.apply_function(fn, args)

    def apply_function(self, fn: MOOFunction, args: List[Any]) -> Any:
        """
        Aplica una función a sus argumentos.
        Crea un nuevo entorno hijo del closure de definición (no del
        entorno de llamada), garantizando alcance léxico correcto.
        """
        if len(args) != len(fn.params):
            raise RuntimeError_(
                f"'{fn.name}' espera {len(fn.params)} argumento(s), "
                f"recibió {len(args)}"
            )

        self._call_depth += 1
        if self._call_depth > self._max_depth:
            raise RuntimeError_("Stack overflow bovino: demasiada recursión (el establo se desbordó)")

        # Crear entorno de ejecución anidado en el closure léxico
        call_env = fn.closure.extend(name=f"call:{fn.name}")
        for param, arg in zip(fn.params, args):
            call_env.define(param, arg)

        # Registrar función actual para permitir RECUR
        prev_fn = self._current_function
        self._current_function = fn

        result = None
        try:
            result = self.eval_body(fn.body, call_env)
        finally:
            self._current_function = prev_fn
            self._call_depth -= 1

        return result

    def eval_body(self, stmts: List[ASTNode], env: Environment) -> Any:
        """Evalúa una lista de sentencias; retorna el valor de la última."""
        result = None
        for stmt in stmts:
            result = self.evaluate(stmt, env)
        return result

    def eval_if(self, node: IfNode, env: Environment) -> Any:
        """
        Evalúa una expresión condicional.
        Como en los lenguajes funcionales, el condicional ES una expresión
        y retorna el valor de la rama ejecutada.
        """
        condition = self.evaluate(node.condition, env)
        self.log(f"RUMIAR condición = {condition!r}")

        if bool(condition):
            return self.eval_body(node.then_body, env)
        elif node.else_body is not None:
            return self.eval_body(node.else_body, env)
        return None  # RUMIAR sin ORUMIR retorna None si la condición es falsa

    def format_value(self, value: Any) -> str:
        """Formatea un valor para salida por pantalla (MUGIR)."""
        if isinstance(value, bool):
            return "BOVINO" if value else "NOBOVINO"
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def run(self, source: str) -> Any:
        """
        Pipeline completo: source → tokens → AST → evaluación.
        Punto de entrada principal del intérprete.
        """
        try:
            # Fase 1: Análisis léxico
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            if self.verbose:
                print("\n=== TOKENS ===")
                for t in tokens:
                    if t.type not in (TokenType.NEWLINE, TokenType.EOF):
                        print(f"  {t}")

            # Fase 2: Análisis sintáctico
            parser = Parser(tokens)
            ast = parser.parse()
            if self.verbose:
                print("\n=== AST ===")
                self._print_ast(ast)

            # Fase 3: Evaluación
            if self.verbose:
                print("\n=== EJECUCIÓN ===")
            return self.evaluate(ast, self.global_env)

        except LexerError as e:
            print(f"\n🐄 ERROR LÉXICO: {e}", file=sys.stderr)
        except ParseError as e:
            print(f"\n🐄 ERROR SINTÁCTICO: {e}", file=sys.stderr)
        except RuntimeError_ as e:
            print(f"\n🐄 ERROR EN EJECUCIÓN: {e}", file=sys.stderr)
        except RecursionError:
            print("\n🐄 ERROR: Desbordamiento del establo (recursión infinita)", file=sys.stderr)

    def _print_ast(self, node, indent=0):
        """Imprime el AST con sangría (para modo verbose)."""
        prefix = "  " * indent
        if isinstance(node, ProgramNode):
            print(f"{prefix}ProgramNode ({len(node.statements)} stmts)")
            for s in node.statements:
                self._print_ast(s, indent + 1)
        elif isinstance(node, FunctionNode):
            print(f"{prefix}FunctionNode '{node.name}'({', '.join(node.params)})")
            for s in node.body:
                self._print_ast(s, indent + 1)
        elif isinstance(node, BindingNode):
            print(f"{prefix}BindingNode '{node.name}'")
            self._print_ast(node.value, indent + 1)
        elif isinstance(node, CallNode):
            print(f"{prefix}CallNode '{node.callee}'")
            for a in node.args:
                self._print_ast(a, indent + 1)
        elif isinstance(node, IfNode):
            print(f"{prefix}IfNode")
            print(f"{prefix}  [condition]")
            self._print_ast(node.condition, indent + 2)
            print(f"{prefix}  [then]")
            for s in node.then_body:
                self._print_ast(s, indent + 2)
            if node.else_body:
                print(f"{prefix}  [else]")
                for s in node.else_body:
                    self._print_ast(s, indent + 2)
        elif isinstance(node, BinOpNode):
            print(f"{prefix}BinOp '{node.op}'")
            self._print_ast(node.left, indent + 1)
            self._print_ast(node.right, indent + 1)
        elif isinstance(node, PrintNode):
            print(f"{prefix}PrintNode")
            self._print_ast(node.expr, indent + 1)
        elif isinstance(node, RecurNode):
            print(f"{prefix}RecurNode")
            for a in node.args:
                self._print_ast(a, indent + 1)
        else:
            print(f"{prefix}{type(node).__name__}: {node}")


# =============================================================================
# SECCIÓN 8: PROGRAMAS DE EJEMPLO EN MOOlang
# =============================================================================

EXAMPLE_HELLO_WORLD = '''
# ============================================================
# Programa 1: Hola Mundo en MOOlang 🐄
# MUGIR imprime en pantalla
# ============================================================
MUGIR "¡MOO! Hola desde el Establo de MOOlang"
'''

EXAMPLE_FACTORIAL = '''
# ============================================================
# Programa 2: Factorial Recursivo en MOOlang 🐄
# Usa RUMIAR (if), ORUMIR (else) y RECUR (recursión)
# ============================================================

LECHE factorial(n) ESTABLO
    RUMIAR n <= 1 ESTABLO
        1
    SALIR
    ORUMIR ESTABLO
        n * RECUR(n - 1)
    SALIR
SALIR

MUGIR LLAMAR factorial(0)
MUGIR LLAMAR factorial(1)
MUGIR LLAMAR factorial(5)
MUGIR LLAMAR factorial(10)
'''

EXAMPLE_SUMA = '''
# ============================================================
# Programa 3: Función Suma Simple en MOOlang 🐄
# ============================================================

LECHE suma(a, b) ESTABLO
    a + b
SALIR

MOO resultado = LLAMAR suma(15, 27)
MUGIR resultado
MUGIR LLAMAR suma(100, 200)
'''

EXAMPLE_FIBONACCI = '''
# ============================================================
# Programa 4: Fibonacci Recursivo en MOOlang 🐄
# ============================================================

LECHE fib(n) ESTABLO
    RUMIAR n <= 1 ESTABLO
        n
    SALIR
    ORUMIR ESTABLO
        LLAMAR fib(n - 1) + LLAMAR fib(n - 2)
    SALIR
SALIR

MOO i = 0
MUGIR "Fibonacci de 0 a 9:"
MUGIR LLAMAR fib(0)
MUGIR LLAMAR fib(1)
MUGIR LLAMAR fib(2)
MUGIR LLAMAR fib(3)
MUGIR LLAMAR fib(4)
MUGIR LLAMAR fib(5)
MUGIR LLAMAR fib(6)
MUGIR LLAMAR fib(7)
MUGIR LLAMAR fib(8)
MUGIR LLAMAR fib(9)
'''

EXAMPLE_POTENCIA = '''
# ============================================================
# Programa 5: Potencia (base^exp) en MOOlang 🐄
# ============================================================

LECHE potencia(base, exp) ESTABLO
    RUMIAR exp == 0 ESTABLO
        1
    SALIR
    ORUMIR ESTABLO
        base * RECUR(base, exp - 1)
    SALIR
SALIR

MUGIR LLAMAR potencia(2, 10)
MUGIR LLAMAR potencia(3, 5)
'''

EXAMPLE_BOOLEANOS = '''
# ============================================================
# Programa 6: Lógica booleana en MOOlang 🐄
# BOVINO = true, NOBOVINO = false
# ============================================================

LECHE es_par(n) ESTABLO
    n % 2 == 0
SALIR

MUGIR LLAMAR es_par(4)
MUGIR LLAMAR es_par(7)

LECHE mayor_de_edad(edad) ESTABLO
    edad >= 18
SALIR

MUGIR LLAMAR mayor_de_edad(20)
MUGIR LLAMAR mayor_de_edad(15)
'''

EXAMPLE_PASO_A_PASO = '''
# ============================================================
# Programa 7: Factorial con traza paso a paso (verbose)
# ============================================================
LECHE factorial(n) ESTABLO
    RUMIAR n <= 1 ESTABLO
        1
    SALIR
    ORUMIR ESTABLO
        n * RECUR(n - 1)
    SALIR
SALIR

MUGIR LLAMAR factorial(5)
'''


# =============================================================================
# SECCIÓN 9: RUNNER INTERACTIVO Y MAIN
# =============================================================================

def run_example(title: str, code: str, verbose: bool = False):
    """Ejecuta un programa de ejemplo y muestra su salida."""
    print("\n" + "=" * 60)
    print(f"  🐄 {title}")
    print("=" * 60)
    print("── Código fuente ──")
    # Mostrar código sin líneas vacías iniciales
    lines = [l for l in code.strip().split('\n')]
    for l in lines:
        print(f"  {l}")
    print("\n── Salida ──")
    ev = Evaluator(verbose=verbose)
    ev.run(code)


def interactive_repl():
    """REPL interactivo de MOOlang."""
    print("=" * 60)
    print("  🐄 MOOlang REPL - Intérprete Interactivo")
    print("  Escribe código MOOlang (línea por línea)")
    print("  Escribe 'SALIR' para terminar")
    print("  Escribe 'VERBOSE' para activar/desactivar trazas")
    print("=" * 60)

    env = Evaluator()
    verbose = False

    while True:
        try:
            line = input("🐄 MOO> ").strip()
            if not line:
                continue
            if line.upper() == "SALIR":
                print("¡Hasta la próxima, vaca programadora! 🐄")
                break
            if line.upper() == "VERBOSE":
                verbose = not verbose
                print(f"Modo verbose: {'ON' if verbose else 'OFF'}")
                continue

            ev = Evaluator(verbose=verbose)
            # Preservar el entorno entre líneas del REPL
            ev.global_env = env.global_env
            result = ev.run(line)
            if result is not None and not isinstance(result, MOOFunction):
                print(f"  => {ev.format_value(result)}")
            env = ev

        except KeyboardInterrupt:
            print("\n(usa 'SALIR' para terminar)")
        except EOFError:
            print("\n¡Hasta la próxima!")
            break


def main():
    """Punto de entrada principal."""

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        # Ejecutar archivo .moo
        if cmd.endswith('.moo') or cmd.endswith('.moolang'):
            verbose = '--verbose' in sys.argv or '-v' in sys.argv
            try:
                with open(cmd, 'r', encoding='utf-8') as f:
                    source = f.read()
                ev = Evaluator(verbose=verbose)
                ev.run(source)
            except FileNotFoundError:
                print(f"🐄 Error: No se encontró el archivo '{cmd}'", file=sys.stderr)
            return

        # Modo demo
        if cmd == '--demo':
            run_example("Hola Mundo", EXAMPLE_HELLO_WORLD)
            run_example("Factorial Recursivo", EXAMPLE_FACTORIAL)
            run_example("Función Suma", EXAMPLE_SUMA)
            run_example("Fibonacci", EXAMPLE_FIBONACCI)
            run_example("Potencia", EXAMPLE_POTENCIA)
            run_example("Lógica Booleana", EXAMPLE_BOOLEANOS)
            run_example("Factorial con Traza", EXAMPLE_PASO_A_PASO, verbose=True)
            return

        # Modo REPL
        if cmd == '--repl':
            interactive_repl()
            return

    # Sin argumentos: ejecutar demo completo
    print("╔══════════════════════════════════════════════════════════╗")
    print("║        🐄  MOOlang - Lenguaje Funcional Bovino  🐄        ║")
    print("║            Intérprete v1.0 - Hecho con leche             ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    print("Uso:")
    print("  python moolang.py --demo          # Ejecutar todos los ejemplos")
    print("  python moolang.py --repl          # REPL interactivo")
    print("  python moolang.py archivo.moo     # Ejecutar un archivo")
    print("  python moolang.py archivo.moo -v  # Ejecutar con trazas")
    print()

    # Ejecutar demo por defecto
    print("Ejecutando demo completo...\n")
    run_example("Hola Mundo", EXAMPLE_HELLO_WORLD)
    run_example("Factorial Recursivo", EXAMPLE_FACTORIAL)
    run_example("Función Suma", EXAMPLE_SUMA)
    run_example("Fibonacci (primeros 10)", EXAMPLE_FIBONACCI)
    run_example("Potencia", EXAMPLE_POTENCIA)
    run_example("Lógica Booleana", EXAMPLE_BOOLEANOS)
    run_example("Factorial(5) paso a paso", EXAMPLE_PASO_A_PASO, verbose=True)


if __name__ == "__main__":
    main()