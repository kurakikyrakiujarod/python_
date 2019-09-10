

```python
import time
import numpy as np
```


```python
x = np.random.random(1000000)
```


```python
start = time.time()
sum(x) / len(x)
print(time.time() - start)
```

    0.09430670738220215
    


```python
start = time.time()
np.mean(x)
print(time.time() - start)
```

    0.0030088424682617188
    


```python
x = np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x.dtype)
```

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    int32
    


```python
print(x.shape)
```

    (5,)
    


```python
Y = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(Y)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    


```python
Y.shape
```




    (4, 3)




```python
Y.size
```




    12




```python
x = np.array(['hello','world'])
print(x)
print('shape',x.shape)
print('type',type(x))
print('dtype',x.dtype)
```

    ['hello' 'world']
    shape (2,)
    type <class 'numpy.ndarray'>
    dtype <U5
    


```python
x = np.array([1,2, 'hello','world'])
print(x)
print('shape',x.shape)
print('type',type(x))
print('dtype',x.dtype)
```

    ['1' '2' 'hello' 'world']
    shape (4,)
    type <class 'numpy.ndarray'>
    dtype <U11
    


```python
x = np.array([1,2,4.5])
print(x,x.dtype)
```

    [1.  2.  4.5] float64
    


```python
x = np.array([1,2,4.5],dtype=np.int64)
print(x,x.dtype)
```

    [1 2 4] int64
    


```python
x = np.array([1,2,3,4,5])
np.save('my_array',x)
```


```python
y = np.load('my_array.npy')
print(y)
```

    [1 2 3 4 5]
    


```python
X = np.zeros((3,4),dtype=np.int32)
print(X)
```

    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    


```python
X = np.full((4,3),5)
print(X)
```

    [[5 5 5]
     [5 5 5]
     [5 5 5]
     [5 5 5]]
    


```python
X = np.eye(5)
print(X)
```

    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]]
    


```python
X = np.diag([10,20,30,40,50])
print(X)
```

    [[10  0  0  0  0]
     [ 0 20  0  0  0]
     [ 0  0 30  0  0]
     [ 0  0  0 40  0]
     [ 0  0  0  0 50]]
    


```python
x = np.arange(10)
print(x)
```

    [0 1 2 3 4 5 6 7 8 9]
    


```python
x = np.arange(4,10)
print(x)
```

    [4 5 6 7 8 9]
    


```python
x = np.arange(1,14,3)
print(x)
```

    [ 1  4  7 10 13]
    


```python
x = np.linspace(0,25)
print(x)
```

    [ 0.          0.51020408  1.02040816  1.53061224  2.04081633  2.55102041
      3.06122449  3.57142857  4.08163265  4.59183673  5.10204082  5.6122449
      6.12244898  6.63265306  7.14285714  7.65306122  8.16326531  8.67346939
      9.18367347  9.69387755 10.20408163 10.71428571 11.2244898  11.73469388
     12.24489796 12.75510204 13.26530612 13.7755102  14.28571429 14.79591837
     15.30612245 15.81632653 16.32653061 16.83673469 17.34693878 17.85714286
     18.36734694 18.87755102 19.3877551  19.89795918 20.40816327 20.91836735
     21.42857143 21.93877551 22.44897959 22.95918367 23.46938776 23.97959184
     24.48979592 25.        ]
    


```python
x = np.linspace(0,25,10)
print(x)
```

    [ 0.          2.77777778  5.55555556  8.33333333 11.11111111 13.88888889
     16.66666667 19.44444444 22.22222222 25.        ]
    


```python
x = np.linspace(0,25,10,endpoint=False)
print(x)
```

    [ 0.   2.5  5.   7.5 10.  12.5 15.  17.5 20.  22.5]
    


```python
x = np.arange(20)
x = np.reshape(x,(5,4))
print(x)
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]
     [16 17 18 19]]
    


```python
X = np.linspace(0,50,10,endpoint=False).reshape(5,2)
print(X)
```

    [[ 0.  5.]
     [10. 15.]
     [20. 25.]
     [30. 35.]
     [40. 45.]]
    


```python
X = np.random.random((3,3))
print(X)
```

    [[0.31309396 0.34904866 0.9040756 ]
     [0.85798833 0.05245108 0.43581507]
     [0.23688112 0.89904224 0.29408203]]
    


```python
X = np.random.randint(4,15,(3,2))
print(X)
```

    [[ 4  8]
     [10  4]
     [11  8]]
    


```python
X = np.random.normal(0,0.1,size=(1000,1000))
print(X)
```

    [[-0.2053559   0.27516369 -0.07106698 ...  0.14529723  0.05718106
       0.11626059]
     [-0.01345291 -0.01231754 -0.01273617 ... -0.22502213 -0.15273477
      -0.03145898]
     [ 0.05519806  0.03982312  0.08575806 ...  0.06680963  0.13418529
      -0.01298179]
     ...
     [ 0.08426123 -0.0402862  -0.00108656 ... -0.15171585 -0.12523051
       0.04513297]
     [-0.28412315 -0.12682913  0.00490241 ...  0.04650621  0.08061585
      -0.04811849]
     [-0.08242431 -0.00561295  0.18947854 ... -0.01225512  0.12447228
       0.02884101]]
    


```python
print('mean: ',X.mean())
print('std: ',X.std())
print('max: ',X.max())
print('min: ',X.min())
print('# positive: ',(X > 0).sum())
print('# negative: ',(X < 0).sum())
```

    mean:  3.8715325112373795e-05
    std:  0.09996314229727539
    max:  0.4857183881727196
    min:  -0.4817551381031189
    # positive:  500699
    # negative:  499301
    


```python
X = np.arange(1,10).reshape(3,3)
print(X)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
print('Element at (0,0):', X[0,0])
print('Element at (0,1):', X[0,1])
print('Element at (2,2):', X[2,2])
```

    Element at (0,0): 1
    Element at (0,1): 2
    Element at (2,2): 9
    


```python
X[0,0] = 20
print(X)
```

    [[20  2  3]
     [ 4  5  6]
     [ 7  8  9]]
    


```python
x = np.array([1,2,3,4,5])
print(x)
x = np.delete(x,[0,4])
print(x)
```

    [1 2 3 4 5]
    [2 3 4]
    


```python
Y = np.arange(1,10).reshape(3,3)
print(Y)

W = np.delete(Y,0,axis=0)
print('\n',W)

V = np.delete(Y,[0,2],axis=1)
print('\n',V)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
     [[4 5 6]
     [7 8 9]]
    
     [[2]
     [5]
     [8]]
    


```python
x = np.array([1,2,3,4,5])
print(x)
x = np.append(x,6)
print(x)
```

    [1 2 3 4 5]
    [1 2 3 4 5 6]
    


```python
x = np.append(x,[7,8])
print(x)
```

    [1 2 3 4 5 6 7 8]
    


```python
Y = np.arange(1,10).reshape(3,3)
print(Y)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
W = np.append(Y,[[10,11,12]],axis=0)
print(W)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    


```python
V = np.append(Y,[[10],[11],[12]],axis=1)
print(V)
```

    [[ 1  2  3 10]
     [ 4  5  6 11]
     [ 7  8  9 12]]
    


```python
x = np.array([1,2,5,6,7])
print(x)
```

    [1 2 5 6 7]
    


```python
x = np.insert(x,2,[3,4])
print(x)
```

    [1 2 3 4 5 6 7]
    


```python
Y = np.array([[1,2,3],[7,8,9]])
print(Y)
```

    [[1 2 3]
     [7 8 9]]
    


```python
W = np.insert(Y,1,[4,5,6],axis=0)
print(W)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
V = np.insert(Y,1,5,axis=1)
print(V)
```

    [[1 5 2 3]
     [7 5 8 9]]
    


```python
x = np.array([1,2])
print(x)
```

    [1 2]
    


```python
Y = np.array([[3,4],[5,6]])
print(Y)
```

    [[3 4]
     [5 6]]
    


```python
z = np.vstack((x,Y))
print(z)
```

    [[1 2]
     [3 4]
     [5 6]]
    


```python
w = np.hstack((Y,x.reshape(2,1)))
print(w)
```

    [[3 4 1]
     [5 6 2]]
    


```python
X = np.arange(1,21).reshape(4,5)
print(X)
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]
     [16 17 18 19 20]]
    


```python
z = X[1:4,2:5]
print(z)
```

    [[ 8  9 10]
     [13 14 15]
     [18 19 20]]
    


```python
z = X[1:,2:]
print(z)
```

    [[ 8  9 10]
     [13 14 15]
     [18 19 20]]
    


```python
z = X[:3,2:]
print(z)
```

    [[ 3  4  5]
     [ 8  9 10]
     [13 14 15]]
    


```python
z = X[:,2]
print(z)
```

    [ 3  8 13 18]
    


```python
z = X[:,2:3]
print(z)
```

    [[ 3]
     [ 8]
     [13]
     [18]]
    


```python
z = X[1:,2:]
print(z)
```

    [[ 8  9 10]
     [13 14 15]
     [18 19 20]]
    


```python
z[2,2] = 55
print(z)
```

    [[ 8  9 10]
     [13 14 15]
     [18 19 55]]
    


```python
print(X)
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]
     [16 17 18 19 55]]
    


```python
X = np.arange(20).reshape(4,5)
z = X[1:,2:].copy()
# z = np.copy(X[1:,2:])
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    


```python
z[2,2] = 55
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 55]]
    


```python
print(X)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
indices = np.array([1,3])
print(indices)
```

    [1 3]
    


```python
y = X[indices,:]
print(y)
```

    [[ 5  6  7  8  9]
     [15 16 17 18 19]]
    


```python
z = X[:,indices]
print(z)
```

    [[ 1  3]
     [ 6  8]
     [11 13]
     [16 18]]
    


```python
print(X)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
z = np.diag(X)
print(z)
```

    [ 0  6 12 18]
    


```python
z = np.diag(X,k=1)
print(z)
```

    [ 1  7 13 19]
    


```python
z = np.diag(X,k=-1)
print(z)
```

    [ 5 11 17]
    


```python
X = np.array([[1,2,3],[1,3,2],[3,4,5]])
print(X)
```

    [[1 2 3]
     [1 3 2]
     [3 4 5]]
    


```python
print(np.unique(X))
```

    [1 2 3 4 5]
    


```python
X = np.arange(25).reshape(5,5)
print(X)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]
     [20 21 22 23 24]]
    


```python
print(X[X > 10])
```

    [11 12 13 14 15 16 17 18 19 20 21 22 23 24]
    


```python
print(X[X <= 7])
```

    [0 1 2 3 4 5 6 7]
    


```python
print(X[(X > 10)&(X < 17)])
```

    [11 12 13 14 15 16]
    


```python
X[(X > 10)&(X < 17)] = -1
print(X)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 -1 -1 -1 -1]
     [-1 -1 17 18 19]
     [20 21 22 23 24]]
    


```python
x = np.array([1,2,3,4,5])
y = np.array([6,7,2,8,4])
print(np.intersect1d(x,y))
print(np.setdiff1d(x,y))
print(np.setdiff1d(y,x))
print(np.union1d(x,y))
```

    [2 4]
    [1 3 5]
    [6 7 8]
    [1 2 3 4 5 6 7 8]
    


```python
x = np.random.randint(1,11,size=(10,))
print(x)
```

    [ 4  4 10  8  1  9  5  9 10 10]
    


```python
print(np.sort(x))
print(x)
print(np.sort(np.unique(x)))
```

    [ 1  4  4  5  8  9  9 10 10 10]
    [ 1  4  4  5  8  9  9 10 10 10]
    [ 1  4  5  8  9 10]
    


```python
x.sort()
print(x)
```

    [ 1  4  4  5  8  9  9 10 10 10]
    


```python
X = np.random.randint(1,11,size=(5,5))
print(X)
```

    [[ 3  2  7 10  2]
     [ 9  8  6  5  2]
     [ 7 10  5  7  3]
     [ 6  8  6  8  4]
     [10  8  5  8  9]]
    


```python
print(np.sort(X,axis=0))
```

    [[ 3  2  5  5  2]
     [ 6  8  5  7  2]
     [ 7  8  6  8  3]
     [ 9  8  6  8  4]
     [10 10  7 10  9]]
    


```python
print(np.sort(X,axis=1))
```

    [[ 2  2  3  7 10]
     [ 2  5  6  8  9]
     [ 3  5  7  7 10]
     [ 4  6  6  8  8]
     [ 5  8  8  9 10]]
    


```python
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x)
print(y)
```

    [1 2 3]
    [4 5 6]
    


```python
print(x + y)
print(np.add(x, y))
```

    [5 7 9]
    [5 7 9]
    


```python
print(x - y)
print(np.subtract(x, y))
print(x * y)
print(np.multiply(x, y))
print(x / y)
print(np.divide(x, y))
```

    [-3 -3 -3]
    [-3 -3 -3]
    [ 4 10 18]
    [ 4 10 18]
    [0.25 0.4  0.5 ]
    [0.25 0.4  0.5 ]
    


```python
X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5,6,7,8]).reshape(2,2)
print(X)
print(Y)
```

    [[1 2]
     [3 4]]
    [[5 6]
     [7 8]]
    


```python
print(X + Y)
```

    [[ 6  8]
     [10 12]]
    


```python
print(np.sqrt(X))
```

    [[1.         1.41421356]
     [1.73205081 2.        ]]
    


```python
print(np.exp(X))
```

    [[ 2.71828183  7.3890561 ]
     [20.08553692 54.59815003]]
    


```python
print(np.power(X,2))
```

    [[ 1  4]
     [ 9 16]]
    


```python
print(np.mean(X,axis=0))
print(np.mean(X,axis=1))
```

    [2. 3.]
    [1.5 3.5]
    


```python
print(X.std())
```

    1.118033988749895
    


```python
print(np.median(X))
```

    2.5
    


```python
print(X.max())
```

    4
    


```python
print(X.min())
```

    1
    


```python
print(X * 3)
```

    [[ 3  6]
     [ 9 12]]
    


```python
Y = np.arange(9).reshape(3,3)
print(Y)
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    


```python
x = np.arange(3)
print(x)
```

    [0 1 2]
    


```python
print(Y + x)
```

    [[ 0  2  4]
     [ 3  5  7]
     [ 6  8 10]]
    


```python
Z = np.arange(3).reshape(3,1)
print(Z)
```

    [[0]
     [1]
     [2]]
    


```python
print(Y)
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    


```python
print(Z + Y)
```

    [[ 0  1  2]
     [ 4  5  6]
     [ 8  9 10]]
    
