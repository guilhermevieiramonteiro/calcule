def calculadora():
    print("--- CALCULADORA BÁSICA ---")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")

        elif opcion == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")

        elif opcion == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")

        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")

# Ejecutar la calculadora
calculadora()