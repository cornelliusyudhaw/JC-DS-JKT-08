def prime_num(num):    
    # Memastikan angka tersebut prime atau bukan
    prime_tab = []
    for i in range(2,num+1):
        if num % i == 0:
            prime_tab.append(True)

    # Karena angka prima adalah angka yang hanya bisa dibagi angka itu sendiri maka jika 
    # total pembagian yang bisa habis dibagi hanya 1x maka angka tersebut angka prima, sisanya adalah
    # angka composite
    if sum(prime_tab) == 1:
        return True
    else:
        return False 

def fizzBuzz(num):
    for i in range(1, num+1):
        if prime_num(i):
            print('FizzPrime')
        elif i % 15 == 0:
            print('FizzBuzz')
        elif i %3 == 0:
            print('Fizz')
        elif i %5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzz(20)
