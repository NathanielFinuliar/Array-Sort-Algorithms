print("\t\t", "%"*37)
print("\t\t $"," "*7, "SELECTION SORTING", " " *7,"$")
print("\t\t $"," " * 2, "CODED BY NATHANIEL FINULIAR", " "*2,"$")
print("\t\t", "%"*37)

print("\n\tARRAY VALUES: [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]")

def ordinal_indicator(n):
    if n == 1:
        return "1st"
    elif n == 2:
        return "2nd"
    elif n == 3:
        return "3rd"
    elif n in [4, 5, 6, 7, 8, 9]:
        return str(n) + "th"
    else:
        return str(n)
    
def selection_sort(data):
    for x in range(9):                             
        min_val = x                                      
        for y in range(x, 10):                    
            if data[y] < data[min_val]:             
                min_val = y      

        temp = data[x]
        data [x] = data [min_val]
        data [min_val] = temp     

        print("\t ", ordinal_indicator(x+1), " Pass: ", data)
    print(f"\n\tSELECTION SORT: {data}\n")      

num_array = [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]
selection_sort(num_array)         