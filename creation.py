import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print(type(arr))
print(arr[0:3])
print(arr[0:])
print(arr[3:])
print(arr[:3])

ar=np.array([10,20,30,40],[50,60,70,80],[20,40,60,80])
print(ar[0:2,0:2])
print(ar[0,1:3])
print(ar[1,2:4])
print(np.shape(ar))
print(np.size(ar))
print(np.ndim(arr))
print(arr.dtype)