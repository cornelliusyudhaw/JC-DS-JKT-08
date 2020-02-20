
#Homework

# No1
# x=4
# y=3
# z=2
# w = ((x+y*z)/(x*y))**z
# print(w)







# #No2
# angka = int(input("Silahkan masukkan angka berapapun: "))
# print("Kuadrat dari "+ str(angka) + " = " + str(angka**2))



# No3 (total hari dijadikan satu - satu ke tahun, bulan, etc.)
# import math
# total_hari1 = int(input("masukkan hari: "))
# tahun1 = str(math.floor(total_hari1/360))
# bulan1 = str(math.floor((total_hari1 % 360)/30))
# minggu1 = str(math.floor(((total_hari1 % 360)%30)/7))
# hari1 = str(math.floor(((total_hari1 % 360)%30)%7))
# print(tahun1 + " tahun " + bulan1 + " bulan " +  minggu1 + " minggu " + hari1 + " hari ")


# #No4
# total = int(input('Total umur Andi dan Budi?: '))
# rasio = float(input('Rasio umur Andi dan Budi?: '))

# umur_budi = (total * 10) /(10 + (rasio * 10))
# umur_andi = total - umur_budi
# print('Umur Andi {}'.format(umur_andi + 2))
# print('Umur Budi {}'.format(umur_budi + 2))

# angka1 = int(input('Masukkan angka 1: '))
# angka2 = int(input('Masukan angka 2: '))
# print('Angka anda adalah {} dan {}'.format(angka1,angka2))


# print('Hlo Dunia'.split('a'))

# No5
# word = input('Kata: ')
# cari = input('Karakter yang ingin dicari: ')
# print(int(len(word.split(cari)))-1)

# # No6
# import math

# jarak_dalam_km = int(input("Jarak antara kendaraan?: "))
# kecepatan_a_km_per_h = int(input("Kecepatan kendaraan a?: "))
# kecepatan_b_km_per_h = int(input("Kecepatan kendaraan b?: "))
# jam_berangkat = int(input('Jam Berangkat?: '))
# menit_berangkat = int(input('Menit Berangkat?: '))

# waktu_tabrakan_dalam_menit = (
#     jarak_dalam_km/(kecepatan_a_km_per_h + kecepatan_b_km_per_h))*60
# print(str(waktu_tabrakan_dalam_menit) + ' menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

# print('Waktu A & B bertabrakan adalah jam {}.{} WIB'.format(int(jam), int(menit)))
# #jam 10.12 WIB


#PR Tambahan

# 1. Given a four-digit number, perform its cyclic rotation by two digits

# a = int(input('Masukkan Angka:'))
# print(a % 100 * 100 + a // 100)


# 2. Given a radius of the circle, calculate the area of the circle

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 3. Given two two-digit numbers, merge their digits as shown in the tests below.

# a = int(input('Masukkan 2 angka pertama: '))
# b = int(input('Masukkan 2 angka kedua: '))
# tens_a = a // 10
# units_a = a % 10
# tens_b = b // 10
# units_b = b % 10
# print(tens_a * 1000 + tens_b * 100 + units_a * 10 + units_b)


# 4. Given a string. Create a program to remove the character you want

# a = input('Masukkan Kata: ')
# rep = input('Kata yang dihilangkan: ')
# # rep2 = input('Kata yang dihilangkan: ')
# print(a.replace(rep, ''))
# # print(hilang.replace(rep2, ''))


# 5. Given a string consisting of exactly two words separated by a space. 
# Print a new string with the first and second word positions swapped (the second word is printed first).

a = input('Masukkan Kata: ')
lis = a.split()
print(lis)
print(lis[1] +' '+ lis[0])