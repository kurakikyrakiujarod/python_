```python
import random

random.randint(1, 10)
```

语句的含义是产生1至10（包含1与10）的一个随机数（整数int型）。（参数为整数不可为浮点数否则会报错）

```python
random.randint(20, 10)
```

该语句是错误的，下限必须小于或等于上限。

```python
random.random()
```

生成一个0到1之间的随机浮点数，包括0但不包括1。

```
random.uniform(a, b)
```

生成a、b之间的随机浮点数。不过与randint不同的是，a、b可以不是整数，也不用考虑大小。

```python
print(random.uniform(3.65, 10.56))
print(random.uniform(10.56, 3.65))
```

```
random.choice(seq)
```

从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。

```python
print(random.choice([1, 2, 3, 4, 5, 6, 7]))
print(random.choice('abcde'))
print(random.choice((1, 2, 3)))
print(random.choice(['hello', 'world']))
```

```
random.randrange(start, stop, step)
```

生成一个从start到stop（不包括stop），间隔为step的一个随机整数。

start、stop、step都要为整数，且start<stop。

```python
print(random.randrange(10, 100, 3))
# 22
print(list(range(10, 0, -3)))
# [10, 7, 4, 1]
```

```
random.sample(p, k)
```

从p序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。

```python
print(random.sample([1, 2, 3, 4, 5], 2))
```

```
random.shuffle(x)
```

把序列x中的元素顺序打乱，shuffle直接改变原有的序列。

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("洗牌前:", items)
random.shuffle(items)
print("洗牌后:", items)
```

