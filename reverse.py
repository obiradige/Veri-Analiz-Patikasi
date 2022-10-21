arr = [[1, 2], [3, 4], [5, 6, 7]]

def rev(x):
    arr.reverse()
    for i in range(len(x)):
        arr[i] = arr[i][::-1]

rev(arr)
print(arr)


