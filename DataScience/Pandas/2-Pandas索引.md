
### Pandas索引结构


```python
import pandas as pd
```


```python
df = pd.read_csv('./data/titanic.csv')
```


```python
print(df['Age'][:5])
```

    0    22.0
    1    38.0
    2    26.0
    3    35.0
    4    35.0
    Name: Age, dtype: float64


```python
print(df[['Age','Fare']][:5])
```

        Age     Fare
    0  22.0   7.2500
    1  38.0  71.2833
    2  26.0   7.9250
    3  35.0  53.1000
    4  35.0   8.0500


```python
# 指定显示行索引具体的数据需要用到loc和iloc
# loc：用label来定位去获取数据
# iloc：用位置来定位获取数据
```


```python
print(df.iloc[0])
```

    PassengerId                          1
    Survived                             0
    Pclass                               3
    Name           Braund, Mr. Owen Harris
    Sex                               male
    Age                                 22
    SibSp                                1
    Parch                                0
    Ticket                       A/5 21171
    Fare                              7.25
    Cabin                              NaN
    Embarked                             S
    Name: 0, dtype: object


```python
print(df.iloc[:5])
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
# 在显示指定的行数据上，再次过滤显示指定列的数据
print(df.iloc[:5,1:3])
```

       Survived  Pclass
    0         0       3
    1         1       1
    2         1       3
    3         1       1
    4         0       3


```python
df = df.set_index('Name')
```


```python
# 用标签名称做定位就用loc
# 用一个数值定位，就用iloc
print(df.loc['Heikkinen, Miss. Laina'])
```

    PassengerId                   3
    Survived                      1
    Pclass                        3
    Sex                      female
    Age                          26
    SibSp                         0
    Parch                         0
    Ticket         STON/O2. 3101282
    Fare                      7.925
    Cabin                       NaN
    Embarked                      S
    Name: Heikkinen, Miss. Laina, dtype: object


```python
# 用loc定位显示指定行中，指定列的数据
print(df.loc['Heikkinen, Miss. Laina','Fare'])
```

    7.925


```python
# print(df.loc['Heikkinen, Miss. Laina':'Allen, Mr. William Henry',:])
print(df.loc['Heikkinen, Miss. Laina':'Allen, Mr. William Henry'])
```

                                                  PassengerId  Survived  Pclass  \
    Name                                                                          
    Heikkinen, Miss. Laina                                  3         1       3   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)            4         1       1   
    Allen, Mr. William Henry                                5         0       3   
    
                                                     Sex   Age  SibSp  Parch  \
    Name                                                                       
    Heikkinen, Miss. Laina                        female  26.0      0      0   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0   
    Allen, Mr. William Henry                        male  35.0      0      0   
    
                                                            Ticket    Fare Cabin  \
    Name                                                                           
    Heikkinen, Miss. Laina                        STON/O2. 3101282   7.925   NaN   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)            113803  53.100  C123   
    Allen, Mr. William Henry                                373450   8.050   NaN   
    
                                                 Embarked  
    Name                                                   
    Heikkinen, Miss. Laina                              S  
    Futrelle, Mrs. Jacques Heath (Lily May Peel)        S  
    Allen, Mr. William Henry                            S  


```python
# 用loc定位具体的数据后，并修改数据
df.loc['Heikkinen, Miss. Laina','Fare'] = 1000
print(df.head())
```

                                                        PassengerId  Survived  \
    Name                                                                        
    Braund, Mr. Owen Harris                                       1         0   
    Cumings, Mrs. John Bradley (Florence Briggs Tha...            2         1   
    Heikkinen, Miss. Laina                                        3         1   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)                  4         1   
    Allen, Mr. William Henry                                      5         0   
    
                                                        Pclass     Sex   Age  \
    Name                                                                       
    Braund, Mr. Owen Harris                                  3    male  22.0   
    Cumings, Mrs. John Bradley (Florence Briggs Tha...       1  female  38.0   
    Heikkinen, Miss. Laina                                   3  female  26.0   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)             1  female  35.0   
    Allen, Mr. William Henry                                 3    male  35.0   
    
                                                        SibSp  Parch  \
    Name                                                               
    Braund, Mr. Owen Harris                                 1      0   
    Cumings, Mrs. John Bradley (Florence Briggs Tha...      1      0   
    Heikkinen, Miss. Laina                                  0      0   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)            1      0   
    Allen, Mr. William Henry                                0      0   
    
                                                                  Ticket  \
    Name                                                                   
    Braund, Mr. Owen Harris                                    A/5 21171   
    Cumings, Mrs. John Bradley (Florence Briggs Tha...          PC 17599   
    Heikkinen, Miss. Laina                              STON/O2. 3101282   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)                  113803   
    Allen, Mr. William Henry                                      373450   
    
                                                             Fare Cabin Embarked  
    Name                                                                          
    Braund, Mr. Owen Harris                                7.2500   NaN        S  
    Cumings, Mrs. John Bradley (Florence Briggs Tha...    71.2833   C85        C  
    Heikkinen, Miss. Laina                              1000.0000   NaN        S  
    Futrelle, Mrs. Jacques Heath (Lily May Peel)          53.1000  C123        S  
    Allen, Mr. William Henry                               8.0500   NaN        S  

### bool类型的索引


```python
print(df['Fare']>40)
```

    Name
    Braund, Mr. Owen Harris                                      False
    Cumings, Mrs. John Bradley (Florence Briggs Thayer)           True
    Heikkinen, Miss. Laina                                        True
    Futrelle, Mrs. Jacques Heath (Lily May Peel)                  True
    Allen, Mr. William Henry                                     False
    Moran, Mr. James                                             False
    McCarthy, Mr. Timothy J                                       True
    Palsson, Master. Gosta Leonard                               False
    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)            False
    Nasser, Mrs. Nicholas (Adele Achem)                          False
    Sandstrom, Miss. Marguerite Rut                              False
    Bonnell, Miss. Elizabeth                                     False
    Saundercock, Mr. William Henry                               False
    Andersson, Mr. Anders Johan                                  False
    Vestrom, Miss. Hulda Amanda Adolfina                         False
    Hewlett, Mrs. (Mary D Kingcome)                              False
    Rice, Master. Eugene                                         False
    Williams, Mr. Charles Eugene                                 False
    Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)      False
    Masselmani, Mrs. Fatima                                      False
    Fynney, Mr. Joseph J                                         False
    Beesley, Mr. Lawrence                                        False
    McGowan, Miss. Anna "Annie"                                  False
    Sloper, Mr. William Thompson                                 False
    Palsson, Miss. Torborg Danira                                False
    Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)    False
    Emir, Mr. Farred Chehab                                      False
    Fortune, Mr. Charles Alexander                                True
    O'Dwyer, Miss. Ellen "Nellie"                                False
    Todoroff, Mr. Lalio                                          False
                                                                 ...  
    Giles, Mr. Frederick Edward                                  False
    Swift, Mrs. Frederick Joel (Margaret Welles Barron)          False
    Sage, Miss. Dorothy Edith "Dolly"                             True
    Gill, Mr. John William                                       False
    Bystrom, Mrs. (Karolina)                                     False
    Duran y More, Miss. Asuncion                                 False
    Roebling, Mr. Washington Augustus II                          True
    van Melkebeke, Mr. Philemon                                  False
    Johnson, Master. Harold Theodor                              False
    Balkic, Mr. Cerin                                            False
    Beckwith, Mrs. Richard Leonard (Sallie Monypeny)              True
    Carlsson, Mr. Frans Olof                                     False
    Vander Cruyssen, Mr. Victor                                  False
    Abelson, Mrs. Samuel (Hannah Wizosky)                        False
    Najib, Miss. Adele Kiamie "Jane"                             False
    Gustafsson, Mr. Alfred Ossian                                False
    Petroff, Mr. Nedelio                                         False
    Laleff, Mr. Kristo                                           False
    Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)                 True
    Shelley, Mrs. William (Imanita Parrish Hall)                 False
    Markun, Mr. Johann                                           False
    Dahlberg, Miss. Gerda Ulrika                                 False
    Banfield, Mr. Frederick James                                False
    Sutehall, Mr. Henry Jr                                       False
    Rice, Mrs. William (Margaret Norton)                         False
    Montvila, Rev. Juozas                                        False
    Graham, Miss. Margaret Edith                                 False
    Johnston, Miss. Catherine Helen "Carrie"                     False
    Behr, Mr. Karl Howell                                        False
    Dooley, Mr. Patrick                                          False
    Name: Fare, Length: 891, dtype: bool


```python
print(df[df['Fare']>40][:5])
```

                                                        PassengerId  Survived  \
    Name                                                                        
    Cumings, Mrs. John Bradley (Florence Briggs Tha...            2         1   
    Heikkinen, Miss. Laina                                        3         1   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)                  4         1   
    McCarthy, Mr. Timothy J                                       7         0   
    Fortune, Mr. Charles Alexander                               28         0   
    
                                                        Pclass     Sex   Age  \
    Name                                                                       
    Cumings, Mrs. John Bradley (Florence Briggs Tha...       1  female  38.0   
    Heikkinen, Miss. Laina                                   3  female  26.0   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)             1  female  35.0   
    McCarthy, Mr. Timothy J                                  1    male  54.0   
    Fortune, Mr. Charles Alexander                           1    male  19.0   
    
                                                        SibSp  Parch  \
    Name                                                               
    Cumings, Mrs. John Bradley (Florence Briggs Tha...      1      0   
    Heikkinen, Miss. Laina                                  0      0   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)            1      0   
    McCarthy, Mr. Timothy J                                 0      0   
    Fortune, Mr. Charles Alexander                          3      2   
    
                                                                  Ticket  \
    Name                                                                   
    Cumings, Mrs. John Bradley (Florence Briggs Tha...          PC 17599   
    Heikkinen, Miss. Laina                              STON/O2. 3101282   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)                  113803   
    McCarthy, Mr. Timothy J                                        17463   
    Fortune, Mr. Charles Alexander                                 19950   
    
                                                             Fare        Cabin  \
    Name                                                                         
    Cumings, Mrs. John Bradley (Florence Briggs Tha...    71.2833          C85   
    Heikkinen, Miss. Laina                              1000.0000          NaN   
    Futrelle, Mrs. Jacques Heath (Lily May Peel)          53.1000         C123   
    McCarthy, Mr. Timothy J                               51.8625          E46   
    Fortune, Mr. Charles Alexander                       263.0000  C23 C25 C27   
    
                                                       Embarked  
    Name                                                         
    Cumings, Mrs. John Bradley (Florence Briggs Tha...        C  
    Heikkinen, Miss. Laina                                    S  
    Futrelle, Mrs. Jacques Heath (Lily May Peel)              S  
    McCarthy, Mr. Timothy J                                   S  
    Fortune, Mr. Charles Alexander                            S  


```python
print(df[df['Sex']=='male'][:5])
```

                                    PassengerId  Survived  Pclass   Sex   Age  \
    Name                                                                        
    Braund, Mr. Owen Harris                   1         0       3  male  22.0   
    Allen, Mr. William Henry                  5         0       3  male  35.0   
    Moran, Mr. James                          6         0       3  male   NaN   
    McCarthy, Mr. Timothy J                   7         0       1  male  54.0   
    Palsson, Master. Gosta Leonard            8         0       3  male   2.0   
    
                                    SibSp  Parch     Ticket     Fare Cabin  \
    Name                                                                     
    Braund, Mr. Owen Harris             1      0  A/5 21171   7.2500   NaN   
    Allen, Mr. William Henry            0      0     373450   8.0500   NaN   
    Moran, Mr. James                    0      0     330877   8.4583   NaN   
    McCarthy, Mr. Timothy J             0      0      17463  51.8625   E46   
    Palsson, Master. Gosta Leonard      3      1     349909  21.0750   NaN   
    
                                   Embarked  
    Name                                     
    Braund, Mr. Owen Harris               S  
    Allen, Mr. William Henry              S  
    Moran, Mr. James                      Q  
    McCarthy, Mr. Timothy J               S  
    Palsson, Master. Gosta Leonard        S  


```python
# 显示Sex为male数据，并且计算数据中age的平均值
print(df.loc[df['Sex']=='male','Age'].mean())
```

    30.72664459161148


```python
# 统计数据中Age大于70的数量
print((df['Age']>70).sum())
```

    5

