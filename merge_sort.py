print("\t\t", "%"*37)
print("\t\t $"," "* 9, "MERGE SORTING", " " *9,"$")
print("\t\t $"," " * 2, "CODED BY NATHANIEL FINULIAR", " "*2,"$")
print("\t\t", "%"*37)

print("\n\tARRAY VALUES: [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]")

def merge_sort(data): 
    if len(data) == 1:                   
        return data                      
    mid = len(data) // 2                   
    left = data[:mid]             
    right = data[mid:]                   

    left = merge_sort(left)              
    right = merge_sort(right)              
    data = merge(left, right)          
    print("\t\t\t\t ", data)                        
    return data                       