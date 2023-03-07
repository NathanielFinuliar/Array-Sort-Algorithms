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
    print("\t\t     ", data)                        
    return data                 

def merge(left, right): 
    result = []  
  
    while len(left) > 0 and len(right) > 0: 
        if(left[0] <= right[0]):            
            result.append(left[0])          
            left.pop(0)                    
        else:                             
            result.append(right[0])         
            right.pop(0)                   
  
    if(len(left) > 0):                    
        result.extend(left)               
    if(len(right) > 0):                   
        result.extend(right) 

    return result           
 
num_array = [81, 96, 77, 67, 43, 99, 65, 32, 62, 60]
print("\n\t MERGE SORT: ",merge_sort(num_array))
print("")