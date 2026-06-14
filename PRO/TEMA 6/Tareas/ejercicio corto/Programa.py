import psycopg2
from psycopg2 import Error
from getpass import getpass

conexion = None


def conectar():
    global conexion
    try:
        contrasena = getpass("Contraseña de usrpostgre: ")
        conexion = psycopg2.connect(
            user="usrpostgre",
            password=contrasena,
            host="localhost",
            port="5432",
            database="ej01"
        )
        print("Conectado a la base de datos con éxito.\n")
        return True
    except (Exception, Error) as error:
        print("Error de conexión:", error)
        return False

def desconectar():
    global conexion
    if conexion:
        conexion.close()
        print("Conexión con PostgreSQL cerrada.")


def insertarEmpleado():
    print("INSERTAR EMPLEADO")
    nif = input("NIF: ").upper()
    nombre = input("Nombre completo: ")
    direccion = input("Dirección: ")
    municipio = input("Municipio: ")
    estadoCivil = input("Estado civil: ")
    nroHijos = int(input("Número de hijos: "))

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO Empleados (nif, nombre_completo, direccion, municipio, estado_civil, nro_hijos)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (nif, nombre, direccion, municipio, estadoCivil, nroHijos))
        conexion.commit()
        print("¡Empleado insertado correctamente!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al insertar empleado:", error)

def insertarEmpresa():
    print("INSERTAR EMPRESA")
    cif = input("CIF: ").upper()
    nombre = input("Nombre: ")
    fechaCreacion = input("Fecha creación (YYYY-MM-DD): ")
    municipio = input("Municipio: ")

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO Empresas (cif, nombre, fecha_creacion, municipio)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(consulta, (cif, nombre, fechaCreacion, municipio))
        conexion.commit()
        print("¡Empresa insertada correctamente!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al insertar empresa:", error)

def insertarRelacion():
    print("INSERTAR RELACIÓN LABORAL")
    nif = input("NIF del empleado: ").upper()
    cif = input("CIF de la empresa: ").upper()
    fechaInicio = input("Fecha inicio (YYYY-MM-DD): ")
    salario = float(input("Salario: "))
    tipoTrabajo = input("Tipo de trabajo: ")

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO Trabajan (nif_empleado, cif_empresa, fecha_inicio, salario_paga, tipo_trabajo)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (nif, cif, fechaInicio, salario, tipoTrabajo))
        conexion.commit()
        print("¡Relación laboral insertada correctamente!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al insertar relación laboral:", error)


def consultarModificarEmpleado():
    print("CONSULTAR/MODIFICAR EMPLEADO")
    nif = input("NIF del empleado a buscar: ").upper()

    try:
        cursor = conexion.cursor()
        consultaSelect = "SELECT * FROM Empleados WHERE nif = %s"
        cursor.execute(consultaSelect, (nif,))
        empleado = cursor.fetchone()

        if empleado is None:
            print("Empleado no encontrado.")
            cursor.close()
            return

        print("\nDatos actuales del empleado:")
        print(f"NIF: {empleado[0]} | Nombre: {empleado[1]} | Dirección: {empleado[2]} | Municipio: {empleado[3]} | Estado Civil: {empleado[4]} | Hijos: {empleado[5]}")

        respuesta = input("\n¿Desea modificar los datos de este empleado? (s/n): ")
        if respuesta.lower() == 's':
            nuevoNombre = input("Nuevo nombre (Intro para mantener actual): ")
            if nuevoNombre == "":
                nuevoNombre = empleado[1]

            nuevaDireccion = input("Nueva dirección (Intro para mantener actual): ")
            if nuevaDireccion == "":
                nuevaDireccion = empleado[2]

            nuevoMunicipio = input("Nuevo municipio (Intro para mantener actual): ")
            if nuevoMunicipio == "":
                nuevoMunicipio = empleado[3]

            nuevoEstado = input("Nuevo estado civil (Intro para mantener actual): ")
            if nuevoEstado == "":
                nuevoEstado = empleado[4]

            nuevosHijos = input("Nuevo número de hijos (Intro para mantener actual): ")
            if nuevosHijos == "":
                nuevosHijos = empleado[5]
            else:
                nuevosHijos = int(nuevosHijos)

            consultaUpdate = """
                UPDATE Empleados 
                SET nombre_completo=%s, direccion=%s, municipio=%s, estado_civil=%s, nro_hijos=%s
                WHERE nif=%s
            """
            cursor.execute(consultaUpdate, (nuevoNombre, nuevaDireccion, nuevoMunicipio, nuevoEstado, nuevosHijos, nif))
            conexion.commit()
            print("¡Empleado modificado con éxito!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al modificar empleado:", error)

def consultarModificarEmpresa():
    print("CONSULTAR/MODIFICAR EMPRESA")
    cif = input("CIF de la empresa a buscar: ").upper()

    try:
        cursor = conexion.cursor()
        consultaSelect = "SELECT * FROM Empresas WHERE cif = %s"
        cursor.execute(consultaSelect, (cif,))
        empresa = cursor.fetchone()

        if empresa is None:
            print("Empresa no encontrada.")
            cursor.close()
            return

        print("\nDatos actuales de la empresa:")
        print(f"CIF: {empresa[0]} | Nombre: {empresa[1]} | Fecha Creación: {empresa[2]} | Municipio: {empresa[3]}")

        respuesta = input("\n¿Desea modificar los datos de esta empresa? (s/n): ")
        if respuesta.lower() == 's':
            nuevoNombre = input("Nuevo nombre (Intro para mantener actual): ")
            if nuevoNombre == "":
                nuevoNombre = empresa[1]

            nuevaFecha = input("Nueva fecha YYYY-MM-DD (Intro para mantener actual): ")
            if nuevaFecha == "":
                nuevaFecha = str(empresa[2])

            nuevoMunicipio = input("Nuevo municipio (Intro para mantener actual): ")
            if nuevoMunicipio == "":
                nuevoMunicipio = empresa[3]

            consultaUpdate = """
                UPDATE Empresas 
                SET nombre=%s, fecha_creacion=%s, municipio=%s
                WHERE cif=%s
            """
            cursor.execute(consultaUpdate, (nuevoNombre, nuevaFecha, nuevoMunicipio, cif))
            conexion.commit()
            print("¡Empresa modificada con éxito!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al modificar empresa:", error)

def consultarModificarRelacion():
    print("CONSULTAR/MODIFICAR RELACIÓN LABORAL")
    nif = input("NIF del empleado: ").upper()
    cif = input("CIF de la empresa: ").upper()
    fechaInicio = input("Fecha inicio (YYYY-MM-DD): ")

    try:
        cursor = conexion.cursor()
        consultaSelect = """
            SELECT * FROM Trabajan 
            WHERE nif_empleado=%s AND cif_empresa=%s AND fecha_inicio=%s
        """
        cursor.execute(consultaSelect, (nif, cif, fechaInicio))
        relacion = cursor.fetchone()

        if relacion is None:
            print("Relación laboral no encontrada.")
            cursor.close()
            return

        print("\nDatos actuales de la relación laboral:")
        print(f"Empleado: {relacion[0]} | Empresa: {relacion[1]} | Inicio: {relacion[2]} | Salario: {relacion[3]} | Puesto: {relacion[4]}")

        respuesta = input("\n¿Desea modificar esta relación? (s/n): ")
        if respuesta.lower() == 's':
            nuevoSalario = input("Nuevo salario (Intro para mantener actual): ")
            if nuevoSalario == "":
                nuevoSalario = relacion[3]
            else:
                nuevoSalario = float(nuevoSalario)

            nuevoTipo = input("Nuevo tipo de trabajo (Intro para mantener actual): ")
            if nuevoTipo == "":
                nuevoTipo = relacion[4]

            consultaUpdate = """
                UPDATE Trabajan 
                SET salario_paga=%s, tipo_trabajo=%s
                WHERE nif_empleado=%s AND cif_empresa=%s AND fecha_inicio=%s
            """
            cursor.execute(consultaUpdate, (nuevoSalario, nuevoTipo, nif, cif, fechaInicio))
            conexion.commit()
            print("¡Relación laboral modificada con éxito!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al modificar relación laboral:", error)


def borrarEmpleado():
    print("BORRAR EMPLEADO")
    nif = input("NIF del empleado a eliminar: ").upper()

    try:
        cursor = conexion.cursor()
        consultaSelect = "SELECT nombre_completo FROM Empleados WHERE nif = %s"
        cursor.execute(consultaSelect, (nif,))
        empleado = cursor.fetchone()

        if empleado is None:
            print("Empleado no encontrado.")
            cursor.close()
            return

        print("Empleado localizado:", empleado[0])
        respuesta = input("¿Está seguro de querer borrar este empleado? (s/n): ")

        if respuesta.lower() == 's':
            consultaDelete = "DELETE FROM Empleados WHERE nif = %s"
            cursor.execute(consultaDelete, (nif,))
            conexion.commit()
            print("¡Empleado eliminado correctamente!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al borrar empleado:", error)

def borrarEmpresa():
    print("BORRAR EMPRESA")
    cif = input("CIF de la empresa a eliminar: ").upper()

    if cif == '9999':
        print("Acción denegada: No se puede eliminar la empresa ficticia del sistema ('Paro').")
        return

    try:
        cursor = conexion.cursor()
        consultaSelect = "SELECT nombre FROM Empresas WHERE cif = %s"
        cursor.execute(consultaSelect, (cif,))
        empresa = cursor.fetchone()

        if empresa is None:
            print("Empresa no encontrada.")
            cursor.close()
            return

        print("Empresa localizada:", empresa[0])
        respuesta = input("¿Está seguro de querer borrar esta empresa? (s/n): ")

        if respuesta.lower() == 's':
            consultaDelete = "DELETE FROM Empresas WHERE cif = %s"
            cursor.execute(consultaDelete, (cif,))
            conexion.commit()
            print("¡Empresa borrada correctamente!")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al borrar empresa:", error)

def borrarRelacion():
    print("BORRAR RELACIÓN LABORAL")
    nif = input("NIF del empleado: ").upper()
    cif = input("CIF de la empresa: ").upper()
    fechaInicio = input("Fecha inicio (YYYY-MM-DD): ")

    try:
        respuesta = input("¿Seguro que desea eliminar esta relación laboral? (s/n): ")
        if respuesta.lower() == 's':
            cursor = conexion.cursor()
            consultaDelete = """
                DELETE FROM Trabajan 
                WHERE nif_empleado=%s AND cif_empresa=%s AND fecha_inicio=%s
            """
            cursor.execute(consultaDelete, (nif, cif, fechaInicio))
            conexion.commit()
            print("¡Relación laboral eliminada con éxito!")
            cursor.close()
    except (Exception, Error) as error:
        print("Error al borrar relación laboral:", error)


def informeParoTrabajando():
    print("\n=== % DE PERSONAS EN PARO Y TRABAJANDO ===\n")
    try:
        cursor = conexion.cursor()

        consultaTotal = "SELECT COUNT(*) FROM Empleados"
        cursor.execute(consultaTotal)
        total = cursor.fetchone()[0]

        if total == 0:
            print("No existen datos de empleados en el sistema.")
            cursor.close()
            return

        consultaParo = "SELECT COUNT(DISTINCT nif_empleado) FROM Trabajan WHERE cif_empresa = '9999'"
        cursor.execute(consultaParo)
        enParo = cursor.fetchone()[0]

        consultaTrabajando = "SELECT COUNT(DISTINCT nif_empleado) FROM Trabajan WHERE cif_empresa != '9999'"
        cursor.execute(consultaTrabajando)
        trabajando = cursor.fetchone()[0]

        porcentajeParo = (enParo / total) * 100
        porcentajeTrabajando = (trabajando / total) * 100

        print(f"Total registrados en el sistema: {total}")
        print(f"-> Desempleados (Empresa 'Paro'): {enParo} ({porcentajeParo:.2f}%)")
        print(f"-> Trabajadores activos: {trabajando} ({porcentajeTrabajando:.2f}%)")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al generar el informe general:", error)

def informeParoMunicipio():
    print("\n=== % DE PARO EN UN MUNICIPIO ===\n")
    municipio = input("Introduzca el municipio a consultar: ")

    try:
        cursor = conexion.cursor()

        consultaTotal = "SELECT COUNT(*) FROM Empleados WHERE municipio = %s"
        cursor.execute(consultaTotal, (municipio,))
        total = cursor.fetchone()[0]

        if total == 0:
            print(f"No hay registros geográficos para el municipio '{municipio}'.")
            cursor.close()
            return

        consultaParo = """
            SELECT COUNT(DISTINCT Empleados.nif) 
            FROM Empleados 
            JOIN Trabajan ON Empleados.nif = Trabajan.nif_empleado
            WHERE Empleados.municipio = %s AND Trabajan.cif_empresa = '9999'
        """
        cursor.execute(consultaParo, (municipio,))
        enParo = cursor.fetchone()[0]

        porcentaje = (enParo / total) * 100

        print(f"\nLocalidad: {municipio}")
        print(f"Población total registrada: {total}")
        print(f"Personas desempleadas: {enParo}")
        print(f"Tasa de desempleo local: {porcentaje:.2f}%")
        cursor.close()
    except (Exception, Error) as error:
        print("Error al procesar el informe del municipio:", error)

def informeOcupacionMunicipios():
    print("\n=== % OCUPACIÓN EN TODOS LOS MUNICIPIOS ===\n")
    try:
        cursor = conexion.cursor()

        consultaMunicipios = "SELECT DISTINCT municipio FROM Empleados WHERE municipio IS NOT NULL"
        cursor.execute(consultaMunicipios)
        municipios = cursor.fetchall()

        if len(municipios) == 0:
            print("No existen datos geográficos suficientes.")
            cursor.close()
            return

        print(f"{'Municipio':<25} {'Habitantes':<15} {'Ocupados':<12} {'% Ocupación'}")
        print("-" * 65)

        consultaTotal = "SELECT COUNT(*) FROM Empleados WHERE municipio = %s"
        consultaOcupados = """
            SELECT COUNT(DISTINCT Empleados.nif) 
            FROM Empleados 
            JOIN Trabajan ON Empleados.nif = Trabajan.nif_empleado
            WHERE Empleados.municipio = %s AND Trabajan.cif_empresa != '9999'
        """

        for fila in municipios:
            mun = fila[0]
            cursor.execute(consultaTotal, (mun,))
            total = cursor.fetchone()[0]

            cursor.execute(consultaOcupados, (mun,))
            ocupados = cursor.fetchone()[0]

            porcentaje = (ocupados / total) * 100 if total > 0 else 0.0
            print(f"{mun:<25} {total:<15} {ocupados:<12} {porcentaje:.2f}%")

        cursor.close()
    except (Exception, Error) as error:
        print("Error al procesar el listado de municipios:", error)


def main():
    if not conectar():
        return

    ejecutando = True
    while ejecutando:
        print("\n===================================")
        print("1. Insertar")
        print("2. Consultar/Modificar")
        print("3. Borrar")
        print("4. Informes")
        print("5. Salir")
        print("===================================")
        opcion = input("Elija una opción del menú: ")

        match opcion:
            case "1":
                print("SUBMENÚ INSERTAR")
                print("1. Empleado")
                print("2. Empresa")
                print("3. Relación laboral")
                print("4. Regresar")
                subOpcion = input("Opción: ")

                match subOpcion:
                    case "1":
                        insertarEmpleado()
                    case "2":
                        insertarEmpresa()
                    case "3":
                        insertarRelacion()
                    case "4":
                        pass
                    case _:
                        print("Opción incorrecta.")

            case "2":
                print("SUBMENÚ CONSULTAR/MODIFICAR")
                print("1. Empleado")
                print("2. Empresa")
                print("3. Relación laboral")
                print("4. Regresar")
                subOpcion = input("Opción: ")

                match subOpcion:
                    case "1":
                        consultarModificarEmpleado()
                    case "2":
                        consultarModificarEmpresa()
                    case "3":
                        consultarModificarRelacion()
                    case "4":
                        pass
                    case _:
                        print("Opción incorrecta.")

            case "3":
                print("SUBMENÚ BORRAR")
                print("1. Empleado")
                print("2. Empresa")
                print("3. Relación laboral")
                print("4. Regresar")
                subOpcion = input("Opción: ")

                match subOpcion:
                    case "1":
                        borrarEmpleado()
                    case "2":
                        borrarEmpresa()
                    case "3":
                        borrarRelacion()
                    case "4":
                        pass
                    case _:
                        print("Opción incorrecta.")

            case "4":
                print("SUBMENÚ INFORMES")
                print("1. Porcentaje de personas en Paro y Trabajando")
                print("2. Porcentaje de paro en un municipio")
                print("3. Porcentaje de ocupación en todos los municipios")
                print("4. Regresar")
                subOpcion = input("Opción: ")

                match subOpcion:
                    case "1":
                        informeParoTrabajando()
                    case "2":
                        informeParoMunicipio()
                    case "3":
                        informeOcupacionMunicipios()
                    case "4":
                        pass
                    case _:
                        print("Opción incorrecta.")

            case "5":
                print("\n¡Cerrando la aplicación!")
                ejecutando = False

            case _:
                print("Opción del menú inválida. Intente de nuevo.")

    desconectar()

main()