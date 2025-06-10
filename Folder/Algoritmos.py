import random      # Librería para generar números aleatorios
import time        # Librería para medir tiempo de ejecución

# 1. Algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)                             # Longitud de la lista
    for i in range(n):                       # Repite el proceso n veces
        for j in range(0, n - i - 1):        # Evita los elementos ya ordenados
            if arr[j] > arr[j + 1]:          # Compara elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia si están en orden incorrecto

# 2. Algoritmo Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):             # Comienza desde el segundo elemento
        key = arr[i]                         # Elemento actual
        j = i - 1
        while j >= 0 and key < arr[j]:       # Desplaza elementos mayores hacia la derecha
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key                     # Inserta el elemento en su lugar correcto

# 3. Algoritmo Merge Sort
def merge_sort(arr):
    if len(arr) > 1:                         # Si hay más de un elemento
        mid = len(arr) // 2                  # Punto medio
        L = arr[:mid]                        # Mitad izquierda
        R = arr[mid:]                        # Mitad derecha

        merge_sort(L)                        # Ordena la mitad izquierda
        merge_sort(R)                        # Ordena la mitad derecha

        i = j = k = 0                        # Índices para recorrer L, R y arr

        # Mezcla los elementos de L y R en orden
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copia elementos restantes de L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copia elementos restantes de R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 4. Genera una lista de números aleatorios
def generar_lista_numeros(tamaño, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(tamaño)]

# 5. Mide el tiempo de ejecución de un algoritmo
def medir_tiempo(funcion, lista):
    copia = lista.copy()                    # Copia la lista original para no modificarla
    inicio = time.time()                    # Tiempo inicial
    funcion(copia)                          # Ejecuta el algoritmo
    fin = time.time()                       # Tiempo final
    return fin - inicio                     # Retorna la duración

# 6. Ejecuta los algoritmos sobre una misma lista y muestra los tiempos
def probar_algoritmos(lista):
    print(f"\n🔍 Pruebas con lista de números (tamaño {len(lista)}):")

    # Lista de tuplas: nombre del algoritmo y su función
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort)
    ]

    for nombre, algoritmo in algoritmos:
        tiempo = medir_tiempo(algoritmo, lista)    # Mide el tiempo
        print(f"⏱ {nombre}: {tiempo:.6f} segundos")          # Muestra el resultado

# 7. Función principal
def main():
    lista = generar_lista_numeros(500)      # Genera una lista de 500 números aleatorios
    probar_algoritmos(lista)                # Prueba los algoritmos con esa lista

# 8. Ejecuta el programa
if __name__ == "__main__":
    main()
