

```python
import pandas as pd
```


```python
left = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                     'key2':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                      'key2':['K0','K1','K2','K4'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
```


```python
print(left)
```

      key1 key2   A   B
    0   K0   K0  A0  B0
    1   K1   K1  A1  B1
    2   K2   K2  A2  B2
    3   K3   K3  A3  B3
    


```python
print(right)
```

      key1 key2   C   D
    0   K0   K0  C0  D0
    1   K1   K1  C1  D1
    2   K2   K2  C2  D2
    3   K3   K4  C3  D3
    


```python
# Meger合并多个表格中相同字段的数据
```


```python
# 使用meger将left表格和right表格同类合并
print(pd.merge(left=left,right=right))
```

      key1 key2   A   B   C   D
    0   K0   K0  A0  B0  C0  D0
    1   K1   K1  A1  B1  C1  D1
    2   K2   K2  A2  B2  C2  D2
    


```python
# meger方法中的on代表选择合并的字段
print(pd.merge(left=left,right=right,on='key1'))
```

      key1 key2_x   A   B key2_y   C   D
    0   K0     K0  A0  B0     K0  C0  D0
    1   K1     K1  A1  B1     K1  C1  D1
    2   K2     K2  A2  B2     K2  C2  D2
    3   K3     K3  A3  B3     K4  C3  D3
    


```python
# merge合并相同名称字段时候，两个字段的值不是完全一样。默认是采用交集方式合并
print(pd.merge(left=left,right=right,on=['key1','key2']))
```

      key1 key2   A   B   C   D
    0   K0   K0  A0  B0  C0  D0
    1   K1   K1  A1  B1  C1  D1
    2   K2   K2  A2  B2  C2  D2
    


```python
print(pd.merge(left=left,right=right,on=['key1','key2'],how='outer'))
```

      key1 key2    A    B    C    D
    0   K0   K0   A0   B0   C0   D0
    1   K1   K1   A1   B1   C1   D1
    2   K2   K2   A2   B2   C2   D2
    3   K3   K3   A3   B3  NaN  NaN
    4   K3   K4  NaN  NaN   C3   D3
    


```python
# indicator 参数表示显示表格每个字段合并的详细信息
# both:两个表左右值都显示。 left_only:左联接显示左边表格的数据 right_only:右链接，显示右边表格的数据
# how='表格名称' 当how参数填写表格名称时，就会指定以这个表格为基准显示数据
print(pd.merge(left=left,right=right,on=['key1','key2'],how='outer',indicator=True))
```

      key1 key2    A    B    C    D      _merge
    0   K0   K0   A0   B0   C0   D0        both
    1   K1   K1   A1   B1   C1   D1        both
    2   K2   K2   A2   B2   C2   D2        both
    3   K3   K3   A3   B3  NaN  NaN   left_only
    4   K3   K4  NaN  NaN   C3   D3  right_only
    


```python
print(pd.merge(left=left,right=right,on=['key1','key2'],how='left'))
```

      key1 key2   A   B    C    D
    0   K0   K0  A0  B0   C0   D0
    1   K1   K1  A1  B1   C1   D1
    2   K2   K2  A2  B2   C2   D2
    3   K3   K3  A3  B3  NaN  NaN
    


```python
print(pd.merge(left=left,right=right,on=['key1','key2'],how='right'))
```

      key1 key2    A    B   C   D
    0   K0   K0   A0   B0  C0  D0
    1   K1   K1   A1   B1  C1  D1
    2   K2   K2   A2   B2  C2  D2
    3   K3   K4  NaN  NaN  C3  D3
    
