print("\t\t\t", "%"*37)
print("\t\t\t $"," "*7, "INSERTION SORTING", " " *7,"$")
print("\t\t\t $"," " * 2, "CODED BY NATHANIEL FINULIAR", " "*2,"$")
print("\t\t\t", "%"*37)

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
    
def insertion_sort(data):
    for x in range(1, len(data)):               
        val = data[x]                         
        i = x-1                               
        while i >=0 and val < data[i] :       
            data[i+1] = data[i]                
            i -= 1                            
        data[i+1] = val                    
        print("\t ", ordinal_indicator(x), " Pass: ", data)
    print(f"\n\tINSERTION SORT: {data}")

num_array = [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]
insertion_sort(num_array)