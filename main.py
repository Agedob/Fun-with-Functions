def odd_even():
    for i in range(1,2001,1):
        if i % 2 == 0:
            print i, "this is an even number"
        else:
            print i, "this numberr is odd"
def multiply(arr,num):
    for x in range(0,len(arr)):
        arr[x] *= num
    return arr
def hacks(argu):
    newarr=[]
    for i in argu:
        cont = []
        for x in range(0, i, 1):
            cont.append(1)
        newarr.append(cont)
    return newarr
a = hacks(multiply([1,2,3],2))
print a