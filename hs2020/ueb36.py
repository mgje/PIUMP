#ueb3.6
def max(L): # Funktion die das max sucht
    max_el = L[0] # Erstes Element nehmen

    for x in L:
        if x > max_el:
            max_el = x
            
    return max_el

# Liste von Zahlen
L=[5, -3, 37, -10, 7, -16, -18, 12, 15, 11, -5, -26, -27, 25, 29, -28, -21, 22, -26]
print(max(L))

# das gleiche für min
def min(L): # Funktion die das max sucht
    min_el = L[0] # Erstes Element nehmen

    for x in L:
        if x < min_el:
            min_el = x
            
    return min_el

print (min(L))