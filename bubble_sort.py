class Solution:
    def bubble_sort(arr):
        #比较相邻元素，经过一次循环，大的放到最后面去了
        for i in range(len(arr)):
            for j in range(0,len(arr)-i-1):  #内存循环交换数，每次交换后需要比较的少1，冒泡比较len(arr)-1次
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

    arr=[12,32,42,14,35,65,34,66]
    bubble_sort(arr)
    print(arr)