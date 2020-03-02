def sum_triangular_numbers(n):
   if n < 0:
      return 0
   else:    
      number = []
      for i in range(1,n+1):
         number_temp = []
         for j in range(i,i*2):
            if i == 1 or i == 2:
               number_temp.append(j)
            else:
               number_temp.append(j + number[i-3][-1])
               # print(j)
               # print(number[i-3][-1])
               # print(number_temp)
         number.append(number_temp)
      sum_ = 0
      number_print = number.copy()
      z = ''
      for item in number:
         sum_ += item[-1]

      # for item in number_print:
      #    item[-1] = [item[-1]]

      for item in number_print:
         for val in item:
            if val == item[-1]:
               z  += '[{}]'.format(val)
            else:    
               z+=str(val)
               z+=' '
         z+='\n'
      print(z)        
      return print('sum of each last part of the triangle is {}'.format(sum_))

sum_triangular_numbers(5)