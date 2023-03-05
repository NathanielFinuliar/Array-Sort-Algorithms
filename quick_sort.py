print("\t\t\t","%"*37)
print("\t\t\t $"," "*9, "QUICK SORTING", " " *9,"$")
print("\t\t\t $"," " *2, "CODED BY NATHANIEL FINULIAR", " "*2,"$")
print("\t\t\t","%"*37)
print(" ")

print("\t  ARRAY VALUES:[81, 96, 77, 67, 43, 99, 65, 32, 62, 60]")

def ordinal_indicator(n):
    if n == 1:
        return "1st"
    elif n == 2:
        return "2nd"
    elif n == 3:
        return "3rd"
    elif n in [4, 5, 6, 7, 8]:
        return str(n) + "th"
    else:
        return str(n)
    
def partition(data, left, right, counter):
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
            print("\t\t", ordinal_indicator(counter), "Pass:", data)
            counter += 1

    if data[i] > pivot:
        data[i], data[right] = data[right], data[i]
        print("\t\t", ordinal_indicator(counter), "Pass:", data)
        counter += 1

    return i