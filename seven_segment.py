#Fungsi sevensegment

def sevensegment():
    list_angka = [int(i) for i in input('masukkan angka :').split()]

    z = ''
    for i in list_angka:
            if (i == 1 or i == 4):
                z += '      '
            else:
                z += '  __  '    
    z+='\n'
    
    for j in list_angka:
        if (j == 1 or j == 7):
            z += '    | '
        elif j == 0:
            z += ' |  | '
        elif (j == 2  or j == 3):
            z +='  __| '
        elif (j == 5 or j == 6):
            z += ' |__  '
        else:
            z += ' |__| '          
    z +='\n'

    for k in list_angka:
        if (k == 1 or k == 4 or k == 7):
            z += '    | '
        elif k == 2:
            z += ' |__  '
        elif (k == 3 or k ==5 or k == 9):
            z += '  __| '
        else:
            z += ' |__| ' 
    return print(z)                       
         
sevensegment()
