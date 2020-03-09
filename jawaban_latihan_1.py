# def moveZeros(list):
#     new_list = []
#     zero = 0
#     for i in list:
#         if i != 0 or type(i) == type(False) :
#             new_list.append(i)
#         else:
#             zero += 1

#     for i in range(zero):
#         new_list.append(0)

#     return new_list               

# print(moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a']))  
# print(moveZeros([0,0,0,"Test",0,3,"a", True, False]))     



def spinWords(string):
    word = []
    for i in string.split():
        if len(i) >= 5:
            word.append(i[::-1])
        else:
            word.append(i)
        # print(word) 

    # z  = ''
    # for idx,val in enumerate(word):
    #     if idx == len(word)-1:
    #         z+= val 
    #     else:
    #         z+= val 
    #         z+= ' '
    return ' '.join(word)

print(spinWords('This is not easy but everyone is capable to pass the test'))