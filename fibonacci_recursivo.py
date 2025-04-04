def fibonacci_recursivo(n):
    if n == 1:
        return 0  # Primer término de la secuencia
    if n == 2:
        return 1  # Segundo término de la secuencia
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)  # Suma recursiva de los dos anteriores

# Solicitar al usuario el término deseado
n = int(input("Introduce el término n que deseas calcular: "))
print(f"El término número {n} de la serie de Fibonacci es: {fibonacci_recursivo(n)}")
