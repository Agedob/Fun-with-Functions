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
a = [2,4,10,16]
b = multiply(a, 5)
