# Ini function untuk ngeprint

# print('test')
# # print('a123')
# print('hello world')

# nama = 'Andi'
# print(nama)

# usia = 22
# usia = 23
# print(usia)

# test = 45
# test = 'text'
# print(type(test))

# nama = input('What is your name?: ')
#String ditambah string
# print('nama saya adalah' * 2)


# usiaAndi = 40
# usiaBudi = 12
# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaAndi ** usiaBudi)
# #Floor Division
# print(usiaAndi // usiaBudi) 

# # Cara 1, inputan tetap string tapi di dalam printan dijadikan integer 
# # baru jadi string lagi
# nama = input('Masukkan Nama: ')
# umur = input('Masukkan Umur: ')
# print('Umur saya 5 tahun kedepan adalah: ' + str(int(umur)+5))
# print('Umur saya jika di modulus 2 adalah: ' +str(int(umur)%2))

# # Cara 2, inputan dijadikan Integer terlebih dahulu
# nama = input('Masukkan Nama: ')
# umur = int(input('Masukkan Umur: '))
# print('Umur saya 5 tahun kedepan adalah: ' +str(umur+5))
# print('Umur saya jika di modulus 2 adalah: ' +str(umur%2))

# usiaAndi = 40
# usiaBudi = 20
# usiaAndi /= 3
# #UsiaAndi = usiaAndi + 3
# usiaBudi -= 4
# #usiaBudi = usiaBudi * 4
# print(usiaAndi)
# print(usiaBudi)

import math
import new

# print(new.value)

# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(8,2))
# print(math.sqrt(64))

#Jika angka sebelum decimal adalah ganjil, maka pembulatan ke atas 
# kalau genap maka ke bawah (dalam kasus .5)

# print(round(5.523456789876543, 2))
# # print(round(4.4))


# print(math.floor(4.7))
# print(math.ceil(4.4))


# x = 'Halo Dunia'
# print(len(x))
# print(x.index('a'))
# print(x.split())
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.replace('Dunia', 'Apa'))


# # Kita juga bisa melakukan index terbalik dengan cara menggunakan angka negatif di dalam index
text = "I'm Baron Nice to meet you"
# print(text[1])
# print(text[2:])
# print(text[:6])
# print(text[2:5])
# print(text[-4:-1])
# print(text[::-1])








# # Soal latihan
nama = input('Masukkan Nama: ').capitalize()
umur = int(input('Masukkan Umur: '))

print('Nama saya jika dimunculkan 2x: '+ nama*2 )

print('Karakter di nama saya pada posisi modulus 2 umur saya: ' + nama[umur%2])

print("""Karakter di nama saya pada posisi negatif modulus 2 umur saya lalu 
        ditambah 5 hingga sebelum -1 adalah """ + nama[ (-1*(umur%2))-5 : -1])


