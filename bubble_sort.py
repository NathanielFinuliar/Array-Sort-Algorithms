print("\t\t", "%"*36)
print("\t\t $"," "*8, "BUBBLE SORTING", " " *8,"$")
print("\t\t $"," " *2, "CODED BY NATHANIEL FINULIAR", " "*1,"$")
print("\t\t", "%"*36)

print("\n\tARRAY VALUES: [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]")

def ordinal_indicator(n):
    if n == 1:
        return "1st"
    elif n == 2:
        return "2nd"
    elif n == 3:
        return "3rd"
    else:
        return f"{n}th"

def bubble_sort(data):
    for x in range(len(data)):                 
      for i in range(len(data)-x-1):             
        if data[i] > data[i+1]:                 
         data[i], data[i+1] = data[i+1], data[i] 
      print("\t ", ordinal_indicator(x + 1), " Pass: ", data)
    print(f"\n\tBUBBLE SORT: {data}") 

num_array = [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]
bubble_sort(num_array)