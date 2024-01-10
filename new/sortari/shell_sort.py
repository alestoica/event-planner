# def shellSort(slist):
#     n = len(slist)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = slist[i]
#             j = i
#             while j >= gap and slist[j - gap] > temp:
#                 slist[j] = slist[j - gap]
#                 j -= gap
#             slist[j] = temp
#         gap //= 2


def cmp_el(a, b, key=None):
    if key(a)[0] < key(b)[0]:
        return True
    elif key(a)[0] == key(b)[0]:
        if key(a)[1] < key(b)[1]:
            return True
    return False


def shellSort(slist, key=None, reverse=False, cmp=cmp_el):
    n = len(slist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = slist[i]
            j = i
            try:
                if reverse is True:
                    while j >= gap and cmp(slist[j - gap], temp, key) is True:
                        slist[j] = slist[j - gap]
                        j -= gap
                    slist[j] = temp
                else:
                    while j >= gap and cmp(slist[j - gap], temp, key) is False:
                        slist[j] = slist[j - gap]
                        j -= gap
                    slist[j] = temp
            except TypeError:
                if reverse is True:
                    while j >= gap and slist[j - gap] < temp:
                        slist[j] = slist[j - gap]
                        j -= gap
                    slist[j] = temp
                else:
                    while j >= gap and slist[j - gap] > temp:
                        slist[j] = slist[j - gap]
                        j -= gap
                    slist[j] = temp
        gap //= 2
        return slist


# s_list = ['cherry', 'donut', 'Michigan', 'transcipt']
# shellSort(s_list, key=lambda el: len(el), reverse=False, cmp=cmp_el)
# print(s_list)
#
s_list = [5, 3, 7, 1, 3, 2, 4, 0]
shellSort(s_list)
print(s_list)

