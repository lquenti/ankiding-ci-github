def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            print(" ".join(str(x) for x in arr[:j]) + " **" + " ".join(str(x) for x in arr[j:j+2]) + "** " + " ".join(str(x) for x in arr[j+2:]))
            j -= 1
    return arr

# Beispielaufruf
arr = [4, 2, 7, 1, 3, 5]
print(f"Unsortierter Array: `{arr}`")
sorted_arr = insertion_sort(arr)
print(f"Sortierter Array: `{sorted_arr}`")

