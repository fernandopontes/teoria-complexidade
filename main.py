import os, random, time, psutil, sys, csv
from datetime import date, datetime

try:
    BASE_PATH = os.path.abspath(".")
except Exception:
    BASE_PATH = sys._MEIPASS

file = open(BASE_PATH + '/entrada.txt', 'r')

lines = file.readlines()

def save_data_file(data):
    f = open('saida.csv', 'w', encoding='utf-8')
    fieldnames = ['date_time', 'algorithm', 'number_qty', 'quality', 'time', 'memory']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    date_time = datetime.now()
    w.writeheader()
    for k, v in data.items():
        v['date_time'] = date_time
        w.writerow(v)
    f.close()
    

def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

def sort_list(n):
    list = []
    for i in range(int(n)):
        list.append(i)
    return list

def selection_sort(list):
    n = len(list)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if list[minimo] > list[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        list[i], list[minimo] = list[minimo], list[i]

def merge(A, aux, esquerda, meio, direita):
    """
    Combina dois vetores ordenados em um único vetor (também ordenado).
    """
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1

def mergesort(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort(A, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort(A, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(A, aux, esquerda, meio, direita)

def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if list[bottom] > pivot:
                list[top] = list[bottom]
                break

        while not done:
            top = top-1

            if top == bottom:
                done = 1
                break

            if list[top] < pivot:
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top

def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
def heapsort(arr):
    n = len(arr)
  
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

n = lines[0]
algorithm = lines[1]

if algorithm == "selectionsort":
    print("Algoritmo: " + algorithm)
    
    print("\n")
    file_line = {}
    
    print("****************************************")
    print("*** Melhor caso ***")
    print("****************************************")
    list = sort_list(n)
    time_begin = time.time()
    selection_sort(list)
    time_end = time.time()
    
    print("Tempo de execução: ")
    time_best_case = time_end - time_begin
    print(time_best_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_best_case = memory_usage_psutil()
    print(memory_best_case)

    file_line[0] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'melhor', 'time': repr(time_best_case) + ' segundos', 'memory': repr(memory_best_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Médio caso ***")
    print("****************************************")
    half_number = int(int(n)/2)
    list = sort_list(half_number)
    list_two = random.sample(range(half_number+1, int(n)), half_number-1)
    list_three = list + list_two
    time_begin = time.time()
    selection_sort(list_three)
    time_end = time.time()
    
    print("Tempo de execução: ")
    time_average_case = time_end - time_begin
    print(time_average_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_average_case = memory_usage_psutil()
    print(memory_average_case)
    
    file_line[1] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'médio', 'time': repr(time_average_case) + ' segundos', 'memory': repr(memory_average_case) + ' MB'}

    print("\n")

    print("****************************************")
    print("*** Pior caso ***")
    print("****************************************")
    list = random.sample(range(0, int(n)), int(n))

    time_begin = time.time()
    selection_sort(list)
    time_end = time.time()
    
    print("****************************************")
    print("Tempo de execução: ")
    time_worst_case = time_end - time_begin
    print(time_worst_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_worst_case = memory_usage_psutil()
    print(memory_worst_case)

    file_line[2] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'pior', 'time': repr(time_worst_case) + ' segundos', 'memory': repr(memory_worst_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Casos randômicos ***")
    print("****************************************")
    
    execution_time_total = 0
    amount_memory_total = 0
    average_time_total = 0
    average_memory_total = 0

    for i in range(5):
        list = random.sample(range(0, int(n)), int(n))
        time_begin = time.time()
        selection_sort(list)
        time_end = time.time()
        execution_time_total += time_end - time_begin
        amount_memory_total += memory_usage_psutil()
    
    average_time_total = execution_time_total / 5
    average_memory_total = amount_memory_total / 5

    print("****************************************")
    print("Tempo médio de execução:")
    print(average_time_total)

    print("****************************************")
    print("Média de memória consumida:")
    print(average_memory_total)

    save_data_file(file_line)

if algorithm == "mergesort":
    print("Algoritmo: " + algorithm)
    
    print("\n")
    file_line = {}
    
    print("****************************************")
    print("*** Melhor caso ***")
    print("****************************************")
    list = sort_list(n)
    aux = [0] * len(list)
    time_begin = time.time()
    mergesort(list, aux, 0, len(list) - 1)
    time_end = time.time()
    
    print("Tempo de execução: ")
    time_best_case = time_end - time_begin
    print(time_best_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_best_case = memory_usage_psutil()
    print(memory_best_case)

    file_line[0] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'melhor', 'time': repr(time_best_case) + ' segundos', 'memory': repr(memory_best_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Médio caso ***")
    print("****************************************")
    half_number = int(int(n)/2)
    list = sort_list(half_number)
    list_two = random.sample(range(half_number+1, int(n)), half_number-1)
    list_three = list + list_two
    aux = [0] * len(list_three)
    time_begin = time.time()
    mergesort(list_three, aux, 0, len(list_three) - 1)
    time_end = time.time()

    print("Tempo de execução: ")
    time_average_case = time_end - time_begin
    print(time_average_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_average_case = memory_usage_psutil()
    print(memory_average_case)
    
    file_line[1] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'médio', 'time': repr(time_average_case) + ' segundos', 'memory': repr(memory_average_case) + ' MB'}

    print("\n")

    print("****************************************")
    print("*** Pior caso ***")
    print("****************************************")
    list = random.sample(range(0, int(n)), int(n))
    aux = [0] * len(list)
    
    time_begin = time.time()
    mergesort(list, aux, 0, len(list) - 1)
    time_end = time.time()

    print("****************************************")
    print("Tempo de execução: ")
    time_worst_case = time_end - time_begin
    print(time_worst_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_worst_case = memory_usage_psutil()
    print(memory_worst_case)

    file_line[2] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'pior', 'time': repr(time_worst_case) + ' segundos', 'memory': repr(memory_worst_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Casos randômicos ***")
    print("****************************************")
    
    execution_time_total = 0
    amount_memory_total = 0
    average_time_total = 0
    average_memory_total = 0

    for i in range(5):
        list = random.sample(range(0, int(n)), int(n))
        aux = [0] * len(list)
        time_begin = time.time()
        mergesort(list, aux, 0, len(list) - 1)
        time_end = time.time()
        execution_time_total += time_end - time_begin
        amount_memory_total += memory_usage_psutil()
    
    average_time_total = execution_time_total / 5
    average_memory_total = amount_memory_total / 5

    print("****************************************")
    print("Tempo médio de execução:")
    print(average_time_total)

    print("****************************************")
    print("Média de memória consumida:")
    print(average_memory_total)

    save_data_file(file_line)

if algorithm == "quicksort":
    print("Algoritmo: " + algorithm)
    
    print("\n")
    file_line = {}
    
    print("****************************************")
    print("*** Melhor caso ***")
    print("****************************************")
    list = random.sample(range(0, int(n)), int(n))
    start = 0
    end = len(list)-1
    time_begin = time.time()
    quicksort(list, start, end)
    time_end = time.time()

    print("Tempo de execução: ")
    time_best_case = time_end - time_begin
    print(time_best_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_best_case = memory_usage_psutil()
    print(memory_best_case)

    file_line[0] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'melhor', 'time': repr(time_best_case) + ' segundos', 'memory': repr(memory_best_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Médio caso ***")
    print("****************************************")
    half_number = int(int(n)/2)
    list = sort_list(half_number)
    list_two = random.sample(range(half_number+1, int(n)), half_number-1)
    list_three = list + list_two
    start = 0
    end = len(list_three)-1
    time_begin = time.time()
    quicksort(list_three, start, end)
    time_end = time.time()

    print("Tempo de execução: ")
    time_average_case = time_end - time_begin
    print(time_average_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_average_case = memory_usage_psutil()
    print(memory_average_case)
    
    file_line[1] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'médio', 'time': repr(time_average_case) + ' segundos', 'memory': repr(memory_average_case) + ' MB'}

    print("\n")

    print("****************************************")
    print("*** Pior caso ***")
    print("****************************************")
    list = sort_list(n)
    list.reverse()
    start = 0
    end = len(list)-1
    time_begin = time.time()
    quicksort(list, start, end)
    time_end = time.time()
    
    print("****************************************")
    print("Tempo de execução: ")
    time_worst_case = time_end - time_begin
    print(time_worst_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_worst_case = memory_usage_psutil()
    print(memory_worst_case)

    file_line[2] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'pior', 'time': repr(time_worst_case) + ' segundos', 'memory': repr(memory_worst_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Casos randômicos ***")
    print("****************************************")
    
    execution_time_total = 0
    amount_memory_total = 0
    average_time_total = 0
    average_memory_total = 0

    for i in range(5):
        list = random.sample(range(0, int(n)), int(n))
        start = 0
        end = len(list)-1
        time_begin = time.time()
        quicksort(list, start, end)
        time_end = time.time()
        execution_time_total += time_end - time_begin
        amount_memory_total += memory_usage_psutil()
    
    average_time_total = execution_time_total / 5
    average_memory_total = amount_memory_total / 5

    print("****************************************")
    print("Tempo médio de execução:")
    print(average_time_total)

    print("****************************************")
    print("Média de memória consumida:")
    print(average_memory_total)

    save_data_file(file_line)

if algorithm == "heapsort":
    print("Algoritmo: " + algorithm)
    
    print("\n")
    file_line = {}
    
    print("****************************************")
    print("*** Melhor caso ***")
    print("****************************************")
    list = random.sample(range(0, int(n)), int(n))
    time_begin = time.time()
    heapsort(list)
    time_end = time.time()

    print("Tempo de execução: ")
    time_best_case = time_end - time_begin
    print(time_best_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_best_case = memory_usage_psutil()
    print(memory_best_case)

    file_line[0] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'melhor', 'time': repr(time_best_case) + ' segundos', 'memory': repr(memory_best_case) + ' MB'}
 
    print("\n")

    print("****************************************")
    print("*** Médio caso ***")
    print("****************************************")
    half_number = int(int(n)/2)
    list = sort_list(half_number)
    list_two = random.sample(range(half_number+1, int(n)), half_number-1)
    list_three = list + list_two
    time_begin = time.time()
    heapsort(list_three)
    time_end = time.time()

    print("Tempo de execução: ")
    time_average_case = time_end - time_begin
    print(time_average_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_average_case = memory_usage_psutil()
    print(memory_average_case)
    
    file_line[1] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'médio', 'time': repr(time_average_case) + ' segundos', 'memory': repr(memory_average_case) + ' MB'}

    print("\n")

    print("****************************************")
    print("*** Pior caso ***")
    print("****************************************")
    list = sort_list(n)
    list.reverse()
    time_begin = time.time()
    heapsort(list)
    time_end = time.time()
    
    print("****************************************")
    print("Tempo de execução: ")
    time_worst_case = time_end - time_begin
    print(time_worst_case)
    print("****************************************")
    print("Memória consumida: ")
    memory_worst_case = memory_usage_psutil()
    print(memory_worst_case)

    file_line[2] = {'algorithm': algorithm, 'number_qty': repr(n), 'quality': 'pior', 'time': repr(time_worst_case) + ' segundos', 'memory': repr(memory_worst_case) + ' MB'}
    
    print("\n")

    print("****************************************")
    print("*** Casos randômicos ***")
    print("****************************************")
    
    execution_time_total = 0
    amount_memory_total = 0
    average_time_total = 0
    average_memory_total = 0

    for i in range(5):
        list = random.sample(range(0, int(n)), int(n))
        time_begin = time.time()
        heapsort(list)
        time_end = time.time()
        execution_time_total += time_end - time_begin
        amount_memory_total += memory_usage_psutil()
    
    average_time_total = execution_time_total / 5
    average_memory_total = amount_memory_total / 5

    print("****************************************")
    print("Tempo médio de execução:")
    print(average_time_total)

    print("****************************************")
    print("Média de memória consumida:")
    print(average_memory_total)

    save_data_file(file_line)

file.close()
input('Fim!')


