# def find_email(str):
#     import re
#     emails = re.findall(r'[\w]+@[\w]+.[\w]+', str)
#     for email in emails:
#         print(email)

# string = 'Cat Dog  Kamper monkeyeye bobby@abcde.com dishwasher kasses@yahoo.com sup rarara@google.com,' 

# find_email(string)


def fungsi(x):
    return 0

def fungsi2(x, y):
    return 0

def fungsi3(z):
    return [0]

def fungsi4():
    return 0

Contoh = [ { 'Test_1': [ { 0 : print('Berhasil') } ] } ]
z = 0
x = 0
y = 1797676



Contoh[fungsi(x)]['Test_1'][fungsi2(x, y)][fungsi3(z)[fungsi4()]]


def get_highest_xnum(num, sequence):
   from math import pow, floor
   if num < pow(10,sequence) or sequence >5:
      print('Input valid num or sequence')
   else:
      angka = str(num)[::-1]
    #   angka = [] 
    #   while (num > 0):
    #      angka.append(num%10)   
    #      num = floor(num/10)

      highest = 0
      print(angka)
      for idx in range(len(angka)-1,sequence-2,-1):
         test = ''
         for i in range(sequence):
            test += angka[idx-i]  
            print(test)
         if int(test) > highest:
            highest = int(test)

      print('The highest {}-number is {}'.format(sequence,highest))
      
get_highest_xnum(987179, 5)


