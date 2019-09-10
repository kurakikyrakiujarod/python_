
# Groupby分组统计


```python
import pandas as pd
```


```python
df = pd.DataFrame({'key':['A','B','C','A','B','C','A','B','C'],
                    'data':[0,5,10,10,20,30,1,2,3]})
print(df)
```

      key  data
    0   A     0
    1   B     5
    2   C    10
    3   A    10
    4   B    20
    5   C    30
    6   A     1
    7   B     2
    8   C     3
    


```python
for key in ['A','B','C']:
    print(df[df['key']==key].sum())
```

    key     AAA
    data     11
    dtype: object
    key     BBB
    data     27
    dtype: object
    key     CCC
    data     43
    dtype: object
    


```python
print(df.groupby('key').sum())
```

         data
    key      
    A      11
    B      27
    C      43
    


```python
import numpy as np
```


```python
print(df.groupby('key').aggregate(np.sum))
print(df.groupby('key').aggregate(np.mean))
```

         data
    key      
    A      11
    B      27
    C      43
              data
    key           
    A     3.666667
    B     9.000000
    C    14.333333
    


```python
df = pd.read_csv('./data/titanic.csv')
```


```python
print(df.groupby('Sex')['Age'].mean())
```

    Sex
    female    27.915709
    male      30.726645
    Name: Age, dtype: float64
    


```python
print(df.groupby('Sex')['Survived'].mean())
```

    Sex
    female    0.742038
    male      0.188908
    Name: Survived, dtype: float64
    
