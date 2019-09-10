
### Pandas 数据分析处理库


```python
import pandas as pd
```


```python
df = pd.read_csv('./data/MSFT.csv')
```


```python
# print(df)
```

.head()可以读取前几条数据，指定前几条都可以


```python
# head()方法默认显示5条数据，可以通过输入数字来控制显示条数
print(df.head(2))
```

             Date   Open   High    Low  Close      Volume  Ex-Dividend  \
    0  2017-12-29  85.63  86.05  85.50  85.54  18162779.0          0.0   
    1  2017-12-28  85.90  85.93  85.55  85.72   9872795.0          0.0   
    
       Split Ratio  Adj. Open  Adj. High  Adj. Low  Adj. Close  Adj. Volume  
    0          1.0      85.63      86.05     85.50       85.54   18162779.0  
    1          1.0      85.90      85.93     85.55       85.72    9872795.0  
    

.info返回当前的信息


```python
df.info() # 返回数据当前的信息
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 147 entries, 0 to 146
    Data columns (total 13 columns):
    Date           147 non-null object
    Open           147 non-null float64
    High           147 non-null float64
    Low            147 non-null float64
    Close          147 non-null float64
    Volume         147 non-null float64
    Ex-Dividend    147 non-null float64
    Split Ratio    147 non-null float64
    Adj. Open      147 non-null float64
    Adj. High      147 non-null float64
    Adj. Low       147 non-null float64
    Adj. Close     147 non-null float64
    Adj. Volume    147 non-null float64
    dtypes: float64(12), object(1)
    memory usage: 15.0+ KB
    


```python
print(df.index)
```

    RangeIndex(start=0, stop=147, step=1)
    


```python
print(df.columns)
```

    Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend',
           'Split Ratio', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close',
           'Adj. Volume'],
          dtype='object')
    


```python
# 查看数据类型
print(df.dtypes)
```

    Date            object
    Open           float64
    High           float64
    Low            float64
    Close          float64
    Volume         float64
    Ex-Dividend    float64
    Split Ratio    float64
    Adj. Open      float64
    Adj. High      float64
    Adj. Low       float64
    Adj. Close     float64
    Adj. Volume    float64
    dtype: object
    


```python
# 查看数值
print(df.values)
```

    [['2017-12-29' 85.63 86.05 ... 85.5 85.54 18162779.0]
     ['2017-12-28' 85.9 85.93 ... 85.55 85.72 9872795.0]
     ['2017-12-27' 85.65 85.98 ... 85.215 85.71 13000828.0]
     ...
     ['2017-06-05' 71.97 72.89 ... 71.069819656189 71.534975139247 29507429.0]
     ['2017-06-02' 70.44 71.86 ... 69.516002404271 71.020335030332 34586054.0]
     ['2017-06-01' 70.24 70.61 ... 68.735135008244 69.377445451871 21066468.0]]
    


### 创建Dataframe类型数据


```python
data = {'country':['USSR','USA','UK'],
       'population':[12,14,16]}
```


```python
df_data = pd.DataFrame(data)
print(df_data)
```

      country  population
    0    USSR          12
    1     USA          14
    2      UK          16
    


```python
df_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3 entries, 0 to 2
    Data columns (total 2 columns):
    country       3 non-null object
    population    3 non-null int64
    dtypes: int64(1), object(1)
    memory usage: 128.0+ bytes
    


```python
# 指定查看数据中某一列数据
# Series数据结构:dataFrame中的一行/一列数据拿出来就是一个Series数据
print(df['Date'].head(10))
```

    0    2017-12-29
    1    2017-12-28
    2    2017-12-27
    3    2017-12-26
    4    2017-12-22
    5    2017-12-21
    6    2017-12-20
    7    2017-12-19
    8    2017-12-18
    9    2017-12-15
    Name: Date, dtype: object
    


```python
print(df['Date'][:6])
```

    0    2017-12-29
    1    2017-12-28
    2    2017-12-27
    3    2017-12-26
    4    2017-12-22
    5    2017-12-21
    Name: Date, dtype: object
    


```python
print(df.head())
```

             Date   Open     High     Low  Close      Volume  Ex-Dividend  \
    0  2017-12-29  85.63  86.0500  85.500  85.54  18162779.0          0.0   
    1  2017-12-28  85.90  85.9300  85.550  85.72   9872795.0          0.0   
    2  2017-12-27  85.65  85.9800  85.215  85.71  13000828.0          0.0   
    3  2017-12-26  85.31  85.5346  85.030  85.40   9737412.0          0.0   
    4  2017-12-22  85.40  85.6300  84.920  85.51  14033977.0          0.0   
    
       Split Ratio  Adj. Open  Adj. High  Adj. Low  Adj. Close  Adj. Volume  
    0          1.0      85.63    86.0500    85.500       85.54   18162779.0  
    1          1.0      85.90    85.9300    85.550       85.72    9872795.0  
    2          1.0      85.65    85.9800    85.215       85.71   13000828.0  
    3          1.0      85.31    85.5346    85.030       85.40    9737412.0  
    4          1.0      85.40    85.6300    84.920       85.51   14033977.0  
    


```python
# 更改索引名称：将数据中Date列名称设置为行索引名称
df = df.set_index('Date')
```


```python
print(df.head())
```

                 Open     High     Low  Close      Volume  Ex-Dividend  \
    Date                                                                 
    2017-12-29  85.63  86.0500  85.500  85.54  18162779.0          0.0   
    2017-12-28  85.90  85.9300  85.550  85.72   9872795.0          0.0   
    2017-12-27  85.65  85.9800  85.215  85.71  13000828.0          0.0   
    2017-12-26  85.31  85.5346  85.030  85.40   9737412.0          0.0   
    2017-12-22  85.40  85.6300  84.920  85.51  14033977.0          0.0   
    
                Split Ratio  Adj. Open  Adj. High  Adj. Low  Adj. Close  \
    Date                                                                  
    2017-12-29          1.0      85.63    86.0500    85.500       85.54   
    2017-12-28          1.0      85.90    85.9300    85.550       85.72   
    2017-12-27          1.0      85.65    85.9800    85.215       85.71   
    2017-12-26          1.0      85.31    85.5346    85.030       85.40   
    2017-12-22          1.0      85.40    85.6300    84.920       85.51   
    
                Adj. Volume  
    Date                     
    2017-12-29   18162779.0  
    2017-12-28    9872795.0  
    2017-12-27   13000828.0  
    2017-12-26    9737412.0  
    2017-12-22   14033977.0  
    


```python
Volume = df['Volume']
```


```python
# 根据索引名称获取对应的值
print(Volume['2017-12-29'])
```

    18162779.0
    


```python
# 数据进行运算
Volume = Volume+10000
print(Volume.head())
```

    Date
    2017-12-29    18172779.0
    2017-12-28     9882795.0
    2017-12-27    13010828.0
    2017-12-26     9747412.0
    2017-12-22    14043977.0
    Name: Volume, dtype: float64
    


```python
print(Volume.mean())
print(Volume.max())
print(Volume.min())
```

    21380538.897959184
    70887350.0
    7435503.0
    


```python
# 显示数据统计指标
print(df.describe())
```

                 Open        High         Low       Close        Volume  \
    count  147.000000  147.000000  147.000000  147.000000  1.470000e+02   
    mean    76.405952   76.890656   75.897979   76.439966  2.137054e+07   
    std      5.513928    5.515937    5.487758    5.469510  8.570116e+06   
    min     68.255000   68.780000   68.020000   68.170000  7.425503e+06   
    25%     72.375000   72.875000   72.005000   72.495000  1.638913e+07   
    50%     74.180000   74.600000   73.810000   74.260000  2.021370e+07   
    75%     83.055000   83.425000   82.470000   82.880000  2.333349e+07   
    max     87.120000   87.499900   86.230000   86.850000  7.087735e+07   
    
           Ex-Dividend  Split Ratio   Adj. Open   Adj. High    Adj. Low  \
    count   147.000000        147.0  147.000000  147.000000  147.000000   
    mean      0.005510          1.0   75.977569   76.459470   75.472544   
    std       0.047111          0.0    5.738728    5.742828    5.711511   
    min       0.000000          1.0   67.551463   68.071051   67.318885   
    25%       0.000000          1.0   71.844172   72.217863   71.417154   
    50%       0.000000          1.0   73.657187   74.224317   73.428345   
    75%       0.000000          1.0   82.970126   83.379094   82.356309   
    max       0.420000          1.0   87.120000   87.499900   86.230000   
    
           Adj. Close   Adj. Volume  
    count  147.000000  1.470000e+02  
    mean    76.011246  2.137054e+07  
    std      5.694605  8.570116e+06  
    min     67.467339  7.425503e+06  
    25%     71.809269  1.638913e+07  
    50%     73.886029  2.021370e+07  
    75%     82.761108  2.333349e+07  
    max     86.850000  7.087735e+07  
    
