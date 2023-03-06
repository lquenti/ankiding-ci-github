import math
import random

def mean(arr):
    return sum(arr) / len(arr)

def median(arr):
    n = len(arr)
    s_arr = sorted(arr)
    mid = n // 2
    if n % 2 == 0:
        return (s_arr[mid - 1] + s_arr[mid]) / 2
    else:
        return s_arr[mid]

def mode(arr):
    s_arr = sorted(arr)
    max_count = 0
    mode = None
    curr_count = 1
    for i in range(1, len(s_arr)):
        if s_arr[i] == s_arr[i-1]:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count
                mode = s_arr[i-1]
            curr_count = 1
    if curr_count > max_count:
        max_count = curr_count
        mode = s_arr[-1]
    return mode

def stdev(arr):
    n = len(arr)
    if n <= 1:
        return 0
    mean_val = mean(arr)
    deviations = [(x - mean_val)**2 for x in arr]
    variance = sum(deviations) / (n - 1)
    return math.sqrt(variance)

def variance(arr):
    n = len(arr)
    if n <= 1:
        return 0
    mean_val = mean(arr)
    deviations = [(x - mean_val)**2 for x in arr]
    return sum(deviations) / (n - 1)

for i in range(5):
    arr = [random.randint(0, 10) for j in range(10)]
    print(f"> Q: Folgender Array: {i+1}:", arr)
    print("> - Mittelwert")
    print("> - Median")
    print("> - Modus")
    print("> - Standardabweichung")
    print("> - Varianz")
    print("> A: - Mittelwert:", mean(arr))
    print("> - Median:", median(arr))
    print("> - Modus:", mode(arr))
    print("> - Standardabweichung:", stdev(arr))
    print("> - Varianz:", variance(arr))
    print()

