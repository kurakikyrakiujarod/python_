
### 数据透视表


```python
import pandas as pd
```


```python
example = pd.DataFrame({'Month':['January','January','January','January',
                                 'February','February','February','February',
                                 'March','March','March','March'],
                        'Category':['Transportation','Grocery','Household','Entertainment',
                                    'Transportation','Grocery','Household','Entertainment',
                                    'Transportation','Grocery','Household','Entertainment'],
                        'Amount':[11,22,33,44,55,66,77,88,99,100,1111,1212]})
print(example)
```

           Month        Category  Amount
    0    January  Transportation      11
    1    January         Grocery      22
    2    January       Household      33
    3    January   Entertainment      44
    4   February  Transportation      55
    5   February         Grocery      66
    6   February       Household      77
    7   February   Entertainment      88
    8      March  Transportation      99
    9      March         Grocery     100
    10     March       Household    1111
    11     March   Entertainment    1212
    


```python
example_pivot = example.pivot(index='Category',columns='Month',values='Amount')
print(example_pivot)
```

    Month           February  January  March
    Category                                
    Entertainment         88       44   1212
    Grocery               66       22    100
    Household             77       33   1111
    Transportation        55       11     99
    


```python
print(example_pivot.sum(axis=1))
```

    Category
    Entertainment     1344
    Grocery            188
    Household         1221
    Transportation     165
    dtype: int64
    


```python
print(example_pivot.sum(axis=0))
```

    Month
    February     286
    January      110
    March       2522
    dtype: int64
    


```python
df = pd.read_csv('./data/titanic.csv')
```


```python
print(df.head())
```

       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    2            3         1       3   
    3            4         1       1   
    4            5         0       3   
    
                                                    Name     Sex   Age  SibSp  \
    0                            Braund, Mr. Owen Harris    male  22.0      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
    2                             Heikkinen, Miss. Laina  female  26.0      0   
    3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
    4                           Allen, Mr. William Henry    male  35.0      0   
    
       Parch            Ticket     Fare Cabin Embarked  
    0      0         A/5 21171   7.2500   NaN        S  
    1      0          PC 17599  71.2833   C85        C  
    2      0  STON/O2. 3101282   7.9250   NaN        S  
    3      0            113803  53.1000  C123        S  
    4      0            373450   8.0500   NaN        S  
    


```python
# 默以值就是求平均
print(df.pivot_table(index='Sex',columns='Pclass',values='Fare'))
```

    Pclass           1          2          3
    Sex                                     
    female  106.125798  21.970121  16.118810
    male     67.226127  19.741782  12.661633
    


```python
print(df.pivot_table(index='Sex',columns='Pclass',values='Fare',aggfunc='max'))
```

    Pclass         1     2      3
    Sex                          
    female  512.3292  65.0  69.55
    male    512.3292  73.5  69.55
    


```python
print(df.pivot_table(index='Sex',columns='Pclass',values='Fare',aggfunc='count'))
```

    Pclass    1    2    3
    Sex                  
    female   94   76  144
    male    122  108  347
    


```python
print(pd.crosstab(index=df['Sex'],columns=df['Pclass']))
```

    Pclass    1    2    3
    Sex                  
    female   94   76  144
    male    122  108  347
    


```python
print(df.pivot_table(index='Pclass',columns='Sex',values='Survived',aggfunc='mean'))
```

    Sex       female      male
    Pclass                    
    1       0.968085  0.368852
    2       0.921053  0.157407
    3       0.500000  0.135447
    


```python
df['Underaged'] = df['Age'] <= 18
```


```python
print(df.pivot_table(index='Underaged',columns='Sex',values='Survived',aggfunc='mean'))
```

    Sex          female      male
    Underaged                    
    False      0.760163  0.167984
    True       0.676471  0.338028
    
