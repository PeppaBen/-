def quick_sort(arr):
    #基本思想：找出一个基准值，把小的放在左边，大的放在右边，中间的放中间，列表生成式(x不跟,if后不跟:)拼接

    if len(arr)<=1: #先考虑只有一个数的特殊情况
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

arr=[13,23,41,25,41,53]
arr_sort=quick_sort(arr)
print(arr_sort)
    

