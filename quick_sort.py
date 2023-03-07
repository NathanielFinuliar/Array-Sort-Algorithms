print("\t\t  ","%"*37)
print("\t\t   $"," "*9, "QUICK SORTING", " " *9,"$")
print("\t\t   $"," " *2, "CODED BY NATHANIEL FINULIAR", " "*2,"$")
print("\t\t  ","%"*37)

print("\n   ARRAY VALUES: [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]")

def quick_sort(data, left, right):
    if left < right:
        partition_pos = partition(data, left, right)
        quick_sort(data, left, partition_pos - 1)
        quick_sort(data, partition_pos + 1, right)
    
def partition(data, left, right):
    i = left
    j = right - 1
    pivot = data[right]

    while i < j:
        while i < right and data[i] < pivot:
            i += 1
        while j > left and data[j] >= pivot:
            j -= 1

        if i < j:
            data[i], data[j] = data[j], data[i]
            print("\t        ",  data)


    if data[i] > pivot:
        data[i], data[right] = data[right], data[i]
        print("\t        ",  data)

    return i

data = [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]
quick_sort(data, 0, len(data) - 1)
print("\n     QUICK SORT:", data)
print("")