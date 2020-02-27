x = 5
y = '5'
z = 6

# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

# print(x == int(y) and int(y)<z )
# print(x == int(y) or int(y)>z)
# print(not(x == int(y) and int(y)<z))

nilai = 81

#Kita bisa melakukan conditional statement bertingkat
# #Jika 0 bisa dianggap False, selainnya bisa dianggap True
# if nilai > 80:
#     print('Excellent')
#     if nilai == 81:
#         print('Nilai ku 81')
#     elif nilai == 82:
#         print('Nilai ku 82')
#     else:
#         print('Nilai lebih dr 80')        
# elif nilai >= 60 and nilai <= 80:
#     print('Good Job')    
# elif nilai == 50:
#     print('Lain')    
# else:
#     print("Don't Give up")

# if nilai < 80:
#     print('Contoh')


# Soal 1
angka = int(input('Masukkan angka: '))
if (angka%2 == 0 ):
    print('Angka {} tergolong bilangan GENAP!'.format(angka))
else:
    print('Angka {} tergolong bilangan GANJIL!'.format(angka))    


#Soal 2
massa = float(input('Masukkan Massa(kg): '))
tinggi = float(input('Masukkan Tinggi(cm): '))
tinggi_m = tinggi/100
imt = massa/(tinggi_m**2)

imt1 = round(imt, 1)

if imt1 < 18.5:
    k= 'BERAT BADAN KURANG!'
elif (imt1 >= 18.5 and imt1 < 25):
    k= 'BERAT BADAN IDEAL!'
elif (imt1 >= 25 and imt1 <30):
    k= 'BB BERLEBIH!'
elif (imt1 >= 30 and imt1 < 40):
    k= 'BB SANGAT BERLEBIH!'
else: 
    k= 'OBESITAS'

print ('Massa {} kg & tinggi {} m'.format(massa, tinggi_m))
print ('IMT = {}, {}'.format(imt, k))
