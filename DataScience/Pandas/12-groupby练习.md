

```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
```


```python
print(df)
```

         A      B         C         D
    0  foo    one  0.256187  1.405181
    1  bar    one -0.026901  2.172614
    2  foo    two -0.734997 -1.519650
    3  bar  three  0.779518  0.170890
    4  foo    two -0.313610 -1.041495
    5  bar    two -1.446488 -0.017230
    6  foo    one  0.847826 -2.353311
    7  foo  three -0.919955  0.805450
    


```python
grouped = df.groupby('A')
print(grouped.count())
```

         B  C  D
    A           
    bar  3  3  3
    foo  5  5  5
    


```python
grouped = df.groupby(['A', 'B'])
print(grouped.count())
```

               C  D
    A   B          
    bar one    1  1
        three  1  1
        two    1  1
    foo one    2  2
        three  1  1
        two    2  2
    


```python
def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'a'
    else:
        return 'b'
```


```python
grouped = df.groupby(get_letter_type,axis = 1)
print(grouped.count())
```

       a  b
    0  1  3
    1  1  3
    2  1  3
    3  1  3
    4  1  3
    5  1  3
    6  1  3
    7  1  3
    


```python
print(grouped.count().iloc[0])
```

    a    1
    b    3
    Name: 0, dtype: int64
    


```python
s = pd.Series([1,2,3,1,2,3],[8,7,5,8,7,5])
```


```python
print(s)
```

    8    1
    7    2
    5    3
    8    1
    7    2
    5    3
    dtype: int64
    


```python
# level=0 分组级别，其中0代表按照第一列分组。也可以直接写列的名字
grouped = s.groupby(level=0,sort=False)
```

    8    1
    7    2
    5    3
    8    1
    7    2
    5    3
    dtype: int64
    


```python
print(grouped.first())
```

    8    1
    7    2
    5    3
    dtype: int64
    


```python
print(grouped.last())
```

    8    1
    7    2
    5    3
    dtype: int64
    


```python
print(grouped.sum())
```

    8    2
    7    4
    5    6
    dtype: int64
    


```python
df2 = pd.DataFrame({'X':['A','B','A','B'],'Y':[1,2,3,4]})
```


```python
print(df2)
```

       X  Y
    0  A  1
    1  B  2
    2  A  3
    3  B  4
    


```python
print(df2.groupby('X').get_group('A'))
```

       X  Y
    0  A  1
    2  A  3
    


```python
print(df2.groupby('X').get_group('B'))
```

       X  Y
    1  B  2
    3  B  4
    


```python
arrays = [['bar','bar','baz','baz','foo','foo','qux','qux'],
          ['one','two','one','two','one','two','one','two']]
```


```python
index = pd.MultiIndex.from_arrays(arrays=arrays,names=['first','second'])
```


```python
s = pd.Series(np.random.randn(8),index=index)
```


```python
print(s)
```

    first  second
    bar    one      -0.592126
           two       0.053947
    baz    one       0.346955
           two       0.841465
    foo    one       2.278900
           two       0.583132
    qux    one      -0.460080
           two      -1.346499
    dtype: float64
    


```python
# groupby(level=0)  level属性分组级别，对应的值可以是数字，0代表第一列。或者直接写列的名字
grouped = s.groupby(level=0)
```


```python
print(grouped.sum())
```

    first
    bar   -0.538179
    baz    1.188420
    foo    2.862032
    qux   -1.806579
    dtype: float64
    


```python
grouped = s.groupby(level=1)
print(grouped.sum())
```

    second
    one    1.573648
    two    0.132045
    dtype: float64
    


```python
grouped = s.groupby(level='first')
print(grouped.sum())
```

    first
    bar   -0.538179
    baz    1.188420
    foo    2.862032
    qux   -1.806579
    dtype: float64
    


```python
print(df)
```

         A      B         C         D
    0  foo    one  0.256187  1.405181
    1  bar    one -0.026901  2.172614
    2  foo    two -0.734997 -1.519650
    3  bar  three  0.779518  0.170890
    4  foo    two -0.313610 -1.041495
    5  bar    two -1.446488 -0.017230
    6  foo    one  0.847826 -2.353311
    7  foo  three -0.919955  0.805450
    


```python
grouped = df.groupby(['A','B'])
print(grouped.aggregate(np.sum))
```

                      C         D
    A   B                        
    bar one   -0.026901  2.172614
        three  0.779518  0.170890
        two   -1.446488 -0.017230
    foo one    1.104013 -0.948130
        three -0.919955  0.805450
        two   -1.048607 -2.561145
    


```python
grouped = df.groupby(['A','B'],as_index=False)
print(grouped.aggregate(np.sum))
```

         A      B         C         D
    0  bar    one -0.026901  2.172614
    1  bar  three  0.779518  0.170890
    2  bar    two -1.446488 -0.017230
    3  foo    one  1.104013 -0.948130
    4  foo  three -0.919955  0.805450
    5  foo    two -1.048607 -2.561145
    


```python
# 分组求和后，进行重新构建索引
print(df.groupby(['A','B']).sum().reset_index())
```

         A      B         C         D
    0  bar    one -0.026901  2.172614
    1  bar  three  0.779518  0.170890
    2  bar    two -1.446488 -0.017230
    3  foo    one  1.104013 -0.948130
    4  foo  three -0.919955  0.805450
    5  foo    two -1.048607 -2.561145
    


```python
grouped = df.groupby(['A','B'])
print(grouped.size())
```

    A    B    
    bar  one      1
         three    1
         two      1
    foo  one      2
         three    1
         two      2
    dtype: int64
    


```python
# describe() 数据统计
print(grouped.describe().head())
```

                  C                                                              \
              count      mean       std       min       25%       50%       75%   
    A   B                                                                         
    bar one     1.0 -0.026901       NaN -0.026901 -0.026901 -0.026901 -0.026901   
        three   1.0  0.779518       NaN  0.779518  0.779518  0.779518  0.779518   
        two     1.0 -1.446488       NaN -1.446488 -1.446488 -1.446488 -1.446488   
    foo one     2.0  0.552006  0.418352  0.256187  0.404097  0.552006  0.699916   
        three   1.0 -0.919955       NaN -0.919955 -0.919955 -0.919955 -0.919955   
    
                            D                                                    \
                    max count      mean       std       min       25%       50%   
    A   B                                                                         
    bar one   -0.026901   1.0  2.172614       NaN  2.172614  2.172614  2.172614   
        three  0.779518   1.0  0.170890       NaN  0.170890  0.170890  0.170890   
        two   -1.446488   1.0 -0.017230       NaN -0.017230 -0.017230 -0.017230   
    foo one    0.847826   2.0 -0.474065  2.657655 -2.353311 -1.413688 -0.474065   
        three -0.919955   1.0  0.805450       NaN  0.805450  0.805450  0.805450   
    
                                   
                    75%       max  
    A   B                          
    bar one    2.172614  2.172614  
        three  0.170890  0.170890  
        two   -0.017230 -0.017230  
    foo one    0.465558  1.405181  
        three  0.805450  0.805450  
    


```python
# agg([np.sum,np.mean,np.std]) 自定义统计参数
grouped = df.groupby('A')
print(grouped['C'].agg([np.sum,np.mean,np.std]))
```

             sum     mean       std
    A                              
    bar -0.69387 -0.23129  1.126990
    foo -0.86455 -0.17291  0.727984
    


```python
print(grouped['C'].agg({'res_sum':np.sum,'res_mean':np.mean,'res_std':np.std}))
```

         res_sum  res_mean   res_std
    A                               
    bar -0.69387  -0.23129  1.126990
    foo -0.86455  -0.17291  0.727984
    

    d:\users\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: using a dict on a Series for aggregation
    is deprecated and will be removed in a future version
      """Entry point for launching an IPython kernel.
    
