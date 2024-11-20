from primos import generar_primo
from mcd import mcd
from inverso_modular import inverso_modular
from rsa import generar_llaves, encriptar, desencriptar

def menu():
    """
    Muestra un menú para interactuar con las funciones implementadas.
    """
    while True:
        print("\n=== Menú Principal ===")
        print("1. Generar un número primo en un rango")
        print("2. Calcular el MCD de dos números")
        print("3. Calcular el inverso modular")
        print("4. Generar llaves RSA")
        print("5. Encriptar un mensaje")
        print("6. Desencriptar un mensaje")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            rango_inferior = int(input("Ingrese el límite inferior del rango: "))
            rango_superior = int(input("Ingrese el límite superior del rango: "))
            primo = generar_primo(rango_inferior, rango_superior)
            if primo:
                print(f"Número primo generado: {primo}")
            else:
                print("No se encontró ningún número primo en el rango especificado.")
        
        elif opcion == "2":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            resultado = mcd(a, b)
            print(f"El MCD de {a} y {b} es: {resultado}")
        
        elif opcion == "3":
            e = int(input("Ingrese el número a invertir: "))
            n = int(input("Ingrese el módulo: "))
            inverso = inverso_modular(e, n)
            if inverso is not None:
                print(f"El inverso modular de {e} módulo {n} es: {inverso}")
            else:
                print(f"No existe un inverso modular para {e} módulo {n}.")
        
        elif opcion == "4":
            rango_inferior = int(input("Ingrese el límite inferior del rango de primos: "))
            rango_superior = int(input("Ingrese el límite superior del rango de primos: "))
            llaves = generar_llaves(rango_inferior, rango_superior)
            if isinstance(llaves, str):
                print(llaves)  # Mensaje de error si no se pueden generar llaves
            else:
                clave_publica, clave_privada = llaves
                print("Clave pública:", clave_publica)
                print("Clave privada:", clave_privada)
        
        elif opcion == "5":
            mensaje = int(input("Ingrese el mensaje (entero menor que n): "))
            e = int(input("Ingrese el valor de 'e' de la clave pública: "))
            n = int(input("Ingrese el valor de 'n' de la clave pública: "))
            cifrado = encriptar(mensaje, (e, n))
            print(f"Mensaje encriptado: {cifrado}")
        
        elif opcion == "6":
            mensaje_cifrado = int(input("Ingrese el mensaje encriptado: "))
            d = int(input("Ingrese el valor de 'd' de la clave privada: "))
            n = int(input("Ingrese el valor de 'n' de la clave privada: "))
            descifrado = desencriptar(mensaje_cifrado, (d, n))
            print(f"Mensaje desencriptado: {descifrado}")
        
        elif opcion == "7":
            print("Saliendo del programa. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
