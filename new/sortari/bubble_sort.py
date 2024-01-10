# def bubbleSort(slist):
#     for j in range(1, len(slist)):
#         for i in range(len(slist)-j):
#             if slist[i+1] < slist[i]:
#                 slist[i], slist[i + 1] = slist[i + 1], slist[i]

from sortari.shell_sort import cmp_el


def bubbleSort(slist, key=None, reverse=False, cmp=cmp_el):
    for j in range(1, len(slist)):
        for i in range(len(slist) - j):
            try:
                if reverse is True:
                    if cmp(slist[i + 1], slist[i], key) is True:
                        slist[i], slist[i + 1] = slist[i + 1], slist[i]
                else:
                    if cmp(slist[i + 1], slist[i], key) is False:
                        slist[i], slist[i + 1] = slist[i + 1], slist[i]
            except TypeError:
                if reverse is True:
                    if slist[i + 1] < slist[i]:
                        slist[i], slist[i + 1] = slist[i + 1], slist[i]
                else:
                    if slist[i + 1] > slist[i]:
                        slist[i], slist[i + 1] = slist[i + 1], slist[i]
    return slist


# s_list = ['cherry', 'donut', 'Michigan', 'transcipt']
# bubbleSort(s_list, key=len, reverse=False)
# print(s_list)
#
# s_list = [5, 3, 7, 1, 3, 2, 4, 0]
# bubbleSort(s_list, key=len)
# print(s_list)
