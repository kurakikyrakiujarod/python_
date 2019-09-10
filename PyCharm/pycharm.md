油管地址 https://www.youtube.com/playlist?list=PLkIHDl7Rk4UTPW-B_7quZ0uJXg1M-Zht8

豆瓣镜像源 https://pypi.douban.com/simple/

模板

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    pass
```

MARKDOWN https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

导出和安装依赖包

```
pip freeze > requirements.txt
pip install -r requirement.txt
```

```python
"%.10f" % float(3.6e-7)
```

```python3
def as_num(x):
	y='{:.5f}'.format(x) # 5f表示保留5位小数点的float型
	return(y)
	
res = as_num(1.2e-4)
print(float(res))
```

