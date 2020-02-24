#Fungsi sort
#[1,2,425,3,0]
def fungsi_sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def fungsi_sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr    

# Fungsi minimum maximum

def minmax(list):
    angka_min = fungsi_sort_ascending(list)[0]
    angka_max = fungsi_sort_descending(list)[0]
    return print('Nilai tertinggi {} dan nilai terendah {}'.format(angka_max,angka_min))

#Fungsi odd and even count

def odd_even(list):
    genap = 0
    ganjil = 0
    for i in list:
        if i % 2 == 0:
            genap += 1
        else:
            ganjil += 1    
    return print('Jumlah angka ganjil ada {} dan angka genap ada {}'.format(ganjil, genap))

#Fungsi Insert Word to array
def insert_word(list):
    jumlah = int(input('Berapa kali memasukkan angka: '))
    for l in range(jumlah):
        while(True):
            try:
                a = int(input('Masukkan angka: '))
                list.append(a) 
                break
            except:
                print('Invalid input')
                 


#Fungsi menu utama
# def menuarray():
#     x = []
#     pilihan = 1
#     while(pilihan < 6):
#         print ('Main menu \n')
#         print ('1. Isi Array' + '\n'+ '2. Lihat Array' + '\n'+ '3. Sort Array' + '\n'+ '4. Nilai tertinggi dan terendah' 
#             +'\n'+'5. Jumlah Ganjil dan Genap' + '\n'+ '6. Keluar')
        
#         pilihan = int(input('Piilh yang mana?: '))

#         if (pilihan == 1):
#             jumlah = int(input('Berapa kali memasukkan angka: '))
#             for l in range(jumlah):
#                 a = int(input('Masukkan angka: '))
#                 x.append(a)  

#         if (pilihan == 2):
#             print (x)

#         if (pilihan == 3):
#             c = int(input('1. Ascending' + '\n'+ '2. Descending' + '\n'+ 'Pilih yang mana: '))
#             if c == 2:       
#                 fungsi_sort_descending(x)
#             elif c == 1:
#                 fungsi_sort_ascending(x)
#             else: 
#                 print('Invalid input, coba lagi')
#                 pilihan = 1    

#         if (pilihan == 4):
#             minmax(x)

#         if (pilihan == 5):
#             odd_even(x)

#         if (pilihan == 6):
#             print('Terima kasih')

#         if (pilihan <= 0 or pilihan > 6):
#             print('Invalid input, coba lagi')
#             pilihan = 1
               
# menuarray()


list_function = [insert_word, print, fungsi_sort_ascending, fungsi_sort_descending, minmax, odd_even]
def menu_lain():
    x = []
    pilihan = 1
    while(pilihan < 7):
        print ('Main menu \n')
        print ('1. Isi List' + '\n'+ '2. Lihat List' + '\n'+ '3. Sort List Ascending' + 
               '\n'+ '4. Sort List Desscending' + '\n' +
                '5. Nilai tertinggi dan terendah' 
                +'\n'+'6. Jumlah Ganjil dan Genap' + '\n'+ '7. Keluar')
        
        pilihan = int(input('Piilh yang mana?: '))      
        if (pilihan == 7):
            print('Terima kasih')
        elif (pilihan <= 0 or pilihan > 6):
            print('Invalid input, coba lagi')
            pilihan = 2
        else:
            list_function[pilihan-1](x)    

menu_lain()



















