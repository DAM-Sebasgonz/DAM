#Manejo de excepciones

# # # # try:
# # # #     Valor = int(input("escriba un numero -->"))
# # # # except ValueError:
# # # #     print("Debe... introducir un numero")
# # # # except KeyboardInterrupt:
# # # #     print("\nPrograma finalizado por el usuario")
# # # # except:
# # # #     print("Error... interrupcion no esperada")
# # # # else:
# # # #     print(f"El numero leido es {Valor}")
# # # # finally:
# # # #     print("fin de ejecuccion")

# EJEMPLO CON BUCLE WHILE

while True:
    try:
        Valor = int(input("diga numero-->"))
    except ValueError:
        print("Debe introducir un numero")
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario")
    except:
        print("Error... interrupcion no esperada")
    else:
        if Valor > 0:
            print(f"El numero leido es {Valor}")
            break
        else:
            print("el numero debe ser positivo")
    finally:
        print("fin de ejecuccion")
