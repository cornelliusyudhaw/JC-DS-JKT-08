#nb_year

def nbYear(p0, percent, aug, p) :
    year = 0
    while p0 < p :
        p0 = p0 + (p0 * percent/100) + aug
        year += 1
    
    return year

# print(nbYear(1000,2,50,1200))





#people in line
def tickets(peopleInLine):
    check = 'YES'
    list = []
    money = {25:0, 50:0, 100:0}
    for j in peopleInLine:
        if j == 25:
            money[25] += 1
            list.append(j)
        elif j == 50 and money[25] > 0:
            money[25] -= 1
            money[50] += 1
            list.append(j)
        elif j == 50 and money[25] == 0:
            check = 'NO'
            break
        elif j == 100 and money[50] >= 1 and money[25] >= 1:
            money[100] += 1
            money[50] -= 1
            money[25] -= 1
            list.append(j)      
        elif j == 100 and money[25] >= 3:
            money[100] += 1
            money[25] -= 3
            list.append(j)
        else:
            check = 'NO'
            break            
    
    # if len(list) == len(peopleInLine):
    #     print('YES')
    print(check)

peopleInLine = [25, 25, 25, 100, 25, 50, 100, 100]              
# tickets(peopleInLine)   






#RowSumOddNumbers
def rowSumOddNumbers(n) :
    numbers  = []
    nilai = 1
    for i in range(1, n+1) :
        temp = []
        for j in range(i) :
            temp.append(nilai)
            nilai += 2
        numbers.append(temp)
    print(numbers)
    
    #ngeprint segitiga
    z = ''
    for num, i in zip(numbers, range(len(numbers))) :
        for j in range(n-i) :
            z += '  '
        for k in num :
            #ljust berfungsi kayak padding, nambahin spasi di sebelah kanan huruf (jumlahnya sampai 4)
            z += str(k)
            z += ' '*(4 - len(str(k)))
            z += str(k).ljust(4, ' ')
        z += '\n' 
    print(z)

    sum_row = ''
    
    for num in numbers[-1]:
        if num == numbers[-1][-1]:
            sum_row += str(num)
        else:    
            sum_row += str(num)
            sum_row += ' + '
    sum_row += ' = {}'.format(sum(numbers[-1]))       
    
    if sum(numbers[-1]) == 1:
        print(1)
    else:
        print(sum_row)    

# # rowSumOddNumbers(1)
# rowSumOddNumbers(2)
rowSumOddNumbers(10)

# list_kosong = []
# for i in range(4):
#     temp = []
#     for j in range(6):
#         temp.append(j)
#     list_kosong.append(temp)    

# print(list_kosong)    