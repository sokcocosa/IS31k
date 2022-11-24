import math


class Work:
    pass


def worked(str1, str2):
    count = 0
    ind = 1
    while ind != -1:
        ind = str1.find(str2)
        if ind >= 0:
            count += 1
        str1 = str1[ind + 1:]
    return "Вывод: " + str(count)
