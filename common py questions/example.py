def function(input_list):
    mid_point = len(input_list)//2
    low = 0
    high = len(input_list) - 1
    while input_list[mid_point] < input_list[low]:
        low = low + 1

    if low < high:
        temp = input_list[low]
        input_list[low] = input_list[high]
        input_list[high] = temp
    return input_list


list1 = [39, 91, 77, 51, 33, 84]
sub_list = function(list1[:4])
print(sub_list)
