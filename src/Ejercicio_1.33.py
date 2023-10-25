# Lee 3 números y dame los números ordenados de menor a mayor. 

print('Dame 3 números: ')
n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 < n2 and n1 < n3):
    if (n2 < n3):
        print(f'Tus números son {n1} {n2} {n3}')
    
    else:
        print(f'Tus números con {n1} {n3} {n2}')

else:
    if (n2 < n1 and n2 < n3):
        if (n1 < n3):
            print(f'Tus números son {n2} {n1} {n3}')
        
        else:
            print(f'Tus números son {n2} {n3} {n1}')
    
    else:
        if (n3 < n1 and n3 < n2):
            if (n1 < n2):
                print(f'Tus números son {n3} {n1} {n2}')
            
            else:
                print(f'Tus números son {n3} {n2} {n1}')