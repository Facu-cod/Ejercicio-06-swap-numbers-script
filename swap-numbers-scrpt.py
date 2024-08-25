numero1 = float(input("Ingresa el primer número y presiona enter: "))
numero2 = float(input("Ingresa el segundo número y presiona enter: "))

print(f"Antes del intercambio: Número 1 = {numero1}, Número 2 = {numero2}")

numero1, numero2 = numero2, numero1

print(f"Después del intercambio: Número 1 = {numero1}, Número 2 = {numero2}")