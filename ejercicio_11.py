import statistics

#Calcular la Mediana y Clasificar Números en Relación a Ella
def clasificar_numeros(lista):
    # Calcular la mediana
    mediana = statistics.median(lista)
    
    # Clasificar los números en relación a la mediana
    clasificacion = {
        "mayor": [num for num in lista if num > mediana],
        "menor": [num for num in lista if num < mediana],
        "igual": [num for num in lista if num == mediana]
    }
    
    return mediana, clasificacion

# Ejemplo de uso
numeros = [12, 7, 3, 10, 5, 14, 9]
mediana, clasificacion = clasificar_numeros(numeros)

print("Mediana:", mediana)
print("Números mayores que la mediana:", clasificacion["mayor"])
print("Números menores que la mediana:", clasificacion["menor"])
print("Números iguales a la mediana:", clasificacion["igual"])
