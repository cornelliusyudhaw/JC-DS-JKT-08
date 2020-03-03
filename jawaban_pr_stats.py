from math import floor, pow, sqrt, ceil

def bubblesort(list):
    for k in range(len(list)-1, 0, -1):
        for i in range(k):
            if (list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return list

def mean_list(list):
    return sum(list)/len(list)

def median_list(list):
    list = bubblesort(list)
    if len(list)%2 == 0:
        return (list[int(len(list)/2)-1] + list[int((len(list)/2))])/2
    else:
        return list[floor(len(list)/2)]

def mode_list(list1):
    ind = set(list1)
    counter = {}
    modus = []
    for angka_unik in ind:
        z = 0
        for angka_di_list in list1:
            if angka_unik == angka_di_list:
                z += 1
        counter[angka_unik] = z
    # max_count = max(counter.values())
    max_count = bubblesort(list(counter.values()))[-1]
    for Key in counter:
        if counter[Key] == max_count:
            modus.append(Key)
    if len(modus) == len(set(list1)):
        modus = []
    return modus

def variance_list(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 2)
    return z/(len(list))

def stdev_pop(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 2)
    return sqrt(z/(len(list)))    

def skewness(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 3)
    z /= len(list)
    return z/(pow(stdev_pop(list),3))

def kurtosis(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 4)
    z /= len(list)
    return (z/(pow(stdev_pop(list),4)))-3

def statistic_sample(list, type = 'skewness'):
    if type == 'variance_pop':
        return variance_list(list)
    elif type == 'stdev_pop':
        return sqrt(variance_list(list))
    elif type == 'mean':
        return mean_list(list)
    elif type == 'median':
        return median_list(list)
    elif type == 'mode':
        return mode_list(list)
    elif type == 'skewness':
        return skewness(list)
    elif type == 'excess kurtosis':
        return kurtosis(list)
    else:
        return 'Invalid Input'    



list_angka = [1,3,3,3,4,4,2,4,10]
print(statistic_sample(list_angka, 'skewness'))


# mean
# median
# mode
# stdev_pop
# variance_pop
# skewness
# excess kurtosis