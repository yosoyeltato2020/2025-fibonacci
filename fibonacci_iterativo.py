def fibonacci_iterativo(n):
    secuencia = []
    a= 0
    b= 1
    for i in range(n):  
        secuencia.append(a)
        c = a + b
        a = b
        b = c
        
        
    return secuencia

# sin input y poner n = 8 para la enesima posicion.
n = int(input("Introduce el número de posiciones para la secuencia hasta donde quieras llegar: "))
print(f"Secuencia de Fibonacci (Iterativa): {fibonacci_iterativo(n)}")
