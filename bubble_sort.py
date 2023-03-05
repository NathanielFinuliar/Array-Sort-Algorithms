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
