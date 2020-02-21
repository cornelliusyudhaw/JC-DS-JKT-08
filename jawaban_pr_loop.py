#Hw1

# z = ''
# for i in range(5, 0, -1):
    
#     for j in range (0, i):
#         z += ' * '
    
#     z += '\n'    
# print(z)    







#Hw2

# z = ''
# for i in range(5, 0, -1):
    
#     if (i > 1):
#         for j in range (0, i):
#             z += ' * '
#         z += '\n'
    
#     elif i == 1:
#         for k in range (0, 5):
#             for l in range (0 , k+1):
#                 z += ' * '
#             z += '\n'        
# print (z)    




# Hw3  
#      
# z= ''
# for i in range (0,10,1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
            



#Hw4
# z= ''
# for i in range (10,-1, -1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
# print (z)         
# 
# 
#       

#Hw5 Bintang Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (10,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)       

#Hw5 Bintang Tidak Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (11,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)     





# HW Bonus




size = int(input('Masukkan Besar Bintang: '))
z = ''
for j in range (size+1):
    if j < size:
        for k in range (1,size*2):
            if k <=size-j or k >= size+j:
                z += ' * '
            else:
                z += '   '
        z += '\n'            
    else:
        for l in range (size-2, -1, -1):
            for m in range (1,size*2):
                if m <=size-l or m >= size+l:
                    z += ' * '
                else:
                    z += '   '
            z += '\n'

print(z)