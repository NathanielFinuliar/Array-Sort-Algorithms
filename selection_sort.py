print("\t\t\t", "%"*37)
print("\t\t\t $"," "*7, "SELECTION SORTING", " " *7,"$")
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