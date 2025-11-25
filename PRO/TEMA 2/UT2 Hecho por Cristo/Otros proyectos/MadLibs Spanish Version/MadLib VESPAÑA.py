'''MadLibs pero version española'''
sujetos = [
    "Un funcionario con prisa",
    "Un diputado que nunca ha leído una ley",
    "Un juez que usa memes en sus sentencias",
    "El Rey buscando su cartera en Suiza",
    "Un político hablando de su máster inexistente",
    "Un alcalde inaugurando la misma rotonda por cuarta vez",
    "Un ministro defendiendo la subida del IVA como algo positivo",
    "Un tertuliano experto en absolutamente todo",
    "Un contratista público con un yate nuevo",
    "Un político prometiendo que no habrá recortes… todavía",
    "Un asesor que solo sabe usar PowerPoint",
    "El político que culpa a la herencia recibida de hace 50 años",
    "Un partido lanzando su programa electoral en TikTok",
    "El diputado que siempre está en la barra del Congreso",
    "Un presidente que culpa al algoritmo de sus problemas",
    "El concejal que cambió farolas por votos",
    "Un alcalde proponiendo una playa en mitad de Castilla",
    "El político que jamás ha cogido el transporte público",
    "Un portavoz que empieza todas sus frases con 'No es cierto'",
    "Un cargo público llamando 'error humano' a su cuenta en Suiza",
    "El economista que predijo la última crisis… después de que pasara",
    "Un asesor sugiriendo inflar globos como solución económica",
    "El ministro que confunde Twitter con su diario personal",
    "Un líder de la oposición criticando lo que él mismo aprobó",
    "El político que tiene un plan… pero no puede revelarlo aún",
    "Un tertuliano que defiende a muerte al partido que paga su sueldo",
    "Un exministro estrenando chalet en Marbella",
    "El alcalde que pinta un carril bici sobre adoquines",
    "Un cargo público prometiendo bajar impuestos pero subiendo tasas",
    "El presidente que habla inglés… en su cabeza"
]
verbo = [
    "inaugura",  # Siempre una nueva rotonda o farola.
    "promete",  # Promete lo imposible antes de cada elección.
    "miente",  # Miente con una sonrisa profesional.
    "sube",  # Sube impuestos mientras baja la transparencia.
    "niega",  # Niega cualquier evidencia incriminatoria.
    "culpa",  # Culpa al rival, al pasado o incluso al clima.
    "indulta",  # Indulta a amigos en apuros legales.
    "desvía",  # Desvía fondos y también la atención mediática.
    "justifica",  # Justifica errores como parte del "contexto".
    "pospone",  # Pospone las reformas para "más adelante".
    "recorta",  # Recorta derechos, pero nunca privilegios.
    "externaliza",  # Externaliza servicios a empresas amigas.
    "anuncia",  # Anuncia grandes planes que nunca se cumplen.
    "inflama",  # Inflama las redes sociales con declaraciones incendiarias.
    "tapa",  # Tapa escándalos con otras polémicas.
    "aparece",  # Aparece solo cuando hay cámaras.
    "reparte",  # Reparte cargos y favores entre sus aliados.
    "finge",  # Finge interés por los temas urgentes.
    "manipula",  # Manipula cifras para que todo parezca mejor.
    "inventa",  # Inventa datos para salir del paso.
    "desmiente",  # Desmiente filtraciones que luego resultan ser ciertas.
    "cobra",  # Cobra dietas, aunque viva al lado del Congreso.
    "acumula",  # Acumula excusas y promesas rotas.
    "boicotea",  # Boicotea proyectos del rival por deporte.
    "esconde",  # Esconde contratos hasta que es demasiado tarde.
    "reparte",  # Reparte subsidios como si fueran caramelos.
    "reniega",  # Reniega de alianzas pasadas cuando le conviene.
    "amenaza",  # Amenaza con recortes si no suben los impuestos.
    "confunde",  # Confunde intencionalmente para evitar responder.
    "controla",  # Controla narrativas mediáticas con precisión quirúrgica.
]
predicado= [
    "mientras sonríe para las cámaras",  
    "sin leer la letra pequeña",  
    "en una rueda de prensa sin preguntas",  
    "y culpa a la oposición de todo",  
    "pensando en su próxima campaña electoral",  
    "mientras inaugura la misma rotonda por cuarta vez",  
    "y promete que esta vez será diferente",  
    "enviando todo a su grupo de WhatsApp privado",  
    "mientras prepara su discurso para desmentirlo mañana",  
    "con una corbata que cuesta más que el salario mínimo",  
    "y pide paciencia a la población",  
    "porque es lo mejor para todos, según dice",  
    "en un evento financiado por un contratista misterioso",  
    "mientras desvía fondos a un proyecto 'prioritario'",  
    "y asegura que no tiene nada que ocultar",  
    "mientras sugiere que todo es un malentendido",  
    "en un informe que nadie puede verificar",  
    "y recibe aplausos de sus aliados",  
    "mientras promete transparencia total",  
    "y se va de vacaciones al terminar",  
    "sin mencionar cuánto costará al contribuyente",  
    "aunque sabe que no lo cumplirá",  
    "con la misma falta de vergüenza de siempre",  
    "mientras sube impuestos 'temporalmente'",  
    "y asegura que fue culpa de un error técnico",  
    "con la convicción de que nadie lo notará",  
    "y deja el problema para el siguiente gobierno",  
    "mientras firma contratos con condiciones opacas",  
    "y asegura que todo está bajo control",  
    "porque, al parecer, todo es culpa de Europa",  
    "sin saber que el micrófono está encendido",  
    "y da por cerrado el escándalo del día",  
    "sin que nadie se atreva a contradecirlo",  
    "mientras el público aplaude confundido",  
    "y luego lo borra todo de las redes sociales",  
    "pensando que nadie se dará cuenta",  
    "y lo celebra como un logro histórico",  
    "sin tener en cuenta las consecuencias",  
    "con un plan que aún no ha detallado",  
    "y se pregunta por qué nadie confía en él",  
    "porque, según dice, es culpa de los medios",  
    "mientras aprueba un presupuesto que no entiende",  
    "y promete que nunca volverá a pasar",  
    "con una rueda de prensa que dura 5 minutos",  
    "y se va antes de que empiecen las preguntas difíciles"
]

import random
oracion=(f"{random.choice(sujetos)} {random.choice(verbo)} {random.choice(predicado)}")
print(oracion)