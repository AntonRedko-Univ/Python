list_1 = [21, 2, 3, [41, 13, 15, [7, 11, 9], 17], 81, [23, 6, 5], 1]
list_2 = []


def SumArr(list_to_summ):
    sum_1 = 0
    ln = len(list_to_summ)
    for elem in list_to_summ:
        index_taken_elem = list_to_summ.index(elem)
        if (index_taken_elem % 2 == 0):
            continue
        else:
            sum_1 += int(elem)
    print(sum_1)


def TurnToArr(taken_list):
    for each_elem in taken_list:
        if isinstance(each_elem, list):
            TurnToArr(each_elem)
        else:
            list_2.append(str(each_elem))


TurnToArr(list_1)
SumArr(list_2)
print(list_2)
