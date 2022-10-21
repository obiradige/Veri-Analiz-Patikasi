
arr = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty_arr = []
def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            empty_arr.append(i)

flatten(arr)
print(empty_arr)

