def mayor(n1, n2):
    if n1 == n2:
        return 0
    
    elif n1 > n2:
        return n1
    
    else:
        return n2
    
#############################################

n1 = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))

print(mayor(n1, n2))