# 前端知识之HTML内容



**Web服务本质**

```python
import socket


sk = socket.socket()

sk.bind(("127.0.0.1", 8080))
sk.listen(5)


while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"<h1>Hello world!</h1>")
    conn.close()
```

浏览器发送请求 --> HTTP协议 --> 服务端接收请求 --> 服务端返回响应 --> 服务端把HTML文件内容发给浏览器 --> 浏览器渲染页面

HTTP的全称叫做 Hypertext Transfer Protocal，超文本传输协议。就是浏览器和服务器之间传输文件用的。

HTTP是有两部分，请求request、响应response。当你输入网址的时候，此时浏览器会发出一个HTTP请求，请求服务器上的响应页面。服务器收到请求之后，会再次通过HTTP将页面传输回来。

## HTML

### HTML是什么

HTML指的是超文本标记语言（Hypertext Markup Language），是一种用于创建网页的标记语言。

本质上是浏览器可识别的规则，我们按照规则写网页，浏览器根据规则渲染我们的网页。

对于不同的浏览器，对同一个标签可能会有不同的解释。（兼容性问题）

**浏览器内核**

| 浏览器  | 内核    |
| ------- | ------- |
| IE      | trident |
| Chrome  | blink   |
| Firefox | gecko   |
| Safari  | webkit  |

「浏览器内核」也就是浏览器所采用的「渲染引擎」，渲染引擎决定了浏览器如何显示网页的内容以及页面的格式信息。渲染引擎是兼容性问题出现的根本原因。

网页文件的扩展名：.html或.htm

HTML语言不是一个编程语言，而是一个标记语言。html是一个纯文本文件，用一些标签来描述文字的语义。Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容。HTML标签在浏览器里面是看不到的，所以称为“超文本”，所以就是"超文本标记语言"了。

### HTML颜色

**颜色表示:** 

第一种：单词表示的方法。比如red，yellow，black。

第二种：rgb函数表示颜色。rgb(数字1，数字2，数字3)，其中数字1代表的是红颜色，数字2代表的是绿颜色，数字3代表的是蓝颜色。并且这三个数字的范围在0-255之间。

第三种：6位16进制的代码表示法。比如#ff0000，#只是表示使用16进制的颜色代码声明颜色，代码的头两位即ff表示三原色中的红色，范围当然是16进制的00-ff，中间两位即00表示绿色，最后两位即00表示蓝色，00表示没有颜色，ff表示颜色最强。所以000000表示黑色，ffffff表示白色，同样ff0000表示纯红色，00ff00表示纯绿色，0000ff表示纯蓝色。

相对于使用rgb(255,255,0)，使用rgba(255,255,0,0.5)可以实现设置颜色透明度的功能，这里的0.5表示透明度，范围0~1。

### HTML规范 

- 所有标记元素都要正确的嵌套，不能交叉嵌套。
- 所有的标记都必须小写。
- 所有的标记都必须关闭。
- 所有的属性值必须加引号。
- 所有的属性必须有值。

### **HTML基本语法特征**

**1、HTML对换行不敏感，对tab不敏感**

HTML只在乎标签的嵌套结构，嵌套的关系。谁嵌套了谁，谁被谁嵌套了，和换行、tab无关。也就是说，HTML不是依靠缩进来表示嵌套的，就是看标签的包裹关系。但是，有良好的缩进，代码更易读。要求大家都正确缩进标签。

**2、空白折叠现象**

HTML中所有的文字之间，如果有空格、换行、tab都将被折叠为一个空格显示。

 举例：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <span>今天
 
        2222</span>
</body>
</html>
```

![](https://images2018.cnblogs.com/blog/1341090/201805/1341090-20180521153323104-1166389158.png)

**3、标签要严格封闭**



## **HTML文档结构**

```html
<!DOCTYPE html>  
<html lang="zh-CN">  
<head>	
  <meta charset="UTF-8">  <!-- 对于中文网页需要声明编码，否则会出现乱码-->
  <title>网页标题</title>
</head>
<body>
	网页显示内容
</body>
</html>
```

1. 第一行是文档声明，声明为HTML5文档，声明必须是HTML文档的第一行。

2. 第二行html标签和最后一行html定义，是文档的开始标记和结束标记。

3. html标签中的lang="zh-CN"定义网页的语言为中文，定义成英文是lang="en"，不定义也没什么影响，它一般作为分析统计用。

4. head标签和body标签是它的第一层子元素。

5. head标签里面负责对网页进行一些设置以及定义标题，设置包括定义网页的编码格式，外链css样式文件和javascript文件等，包含了文档的元数据。设置的内容不会显示在网页上，标题的内容会显示在标题栏。

6. body内编写网页上显示的内容。

   ​

## **HTML标签格式**

HTML标签是由尖括号包围的关键字。

HTML标签通常是成对出现的，第一个标签是开始，第二个标签是结束。结束标签会有斜线。

也有一部分标签是单独呈现的，如br，hr,img标签等。标签里面可以有若干属性，也可以不带属性。

**标签的语法：**

<标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>

<标签名 属性1=“属性值1” 属性2=“属性值2”…… />

**几个很重要的属性：**

id：定义标签的唯一ID，HTML文档树中唯一

class：为html元素定义一个或多个类名(CSS样式类名)

style：规定元素的行内样式（CSS样式）

**HTML注释**

```html
<!--注释内容-->
```



## **HTML常用标签**

## **head内常用标签**

| 标签   | 意义                       |
| ------ | -------------------------- |
| title  | 定义网页标题               |
| style  | 定义内部样式表             |
| script | 定义JS代码或引入外部JS文件 |
| link   | 引入外部样式表文件         |
| meta   | 定义网页原信息             |

### **Meta标签**

meta标签是html语言head区的一个辅助性标签。

meta元素可提供有关页面的元信息，用户不可见。

meta标签共有两个属性，它们分别是http-equiv和name。

***http-equiv属性***

http-equiv顾名思义，相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确和精确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。 

```html
<!--2秒后跳转到对应的网址，注意引号-->
<meta http-equiv="refresh" content="2; URL=https://www.jianshu.com/">
```

```html
<!--告诉IE以最高级模式渲染文档-->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

***name属性***

name属性主要用于描述网页，比如网页的关键词，叙述等。与之对应的属性值为content，content中的内容是对name填入类型的具体描述，便于搜索引擎抓取。

```html
<!-- keywords用来告诉搜索引擎你网页的关键字是什么 -->
<meta name="keywords" content="science,education,culture,politics,ecnomics">

<!-- description用来告诉搜索引擎你的网站主要内容-->
<meta name="description" content="This page is about the meaning of science,education,culture.">

<!-- 让我们网页支持移动端，移动设备优先-->
<meta name="viewport" content="width=device-width, initial-scale=1">
```

<a href="https://www.jb51.net/web/562966.html">HTML meta 详解</a>

<a href="https://www.cnblogs.com/yumo1627129/p/7198968.html">关于meta标签中的http-equiv属性使用介绍</a>

<a href="https://www.cnblogs.com/wangyang108/p/5995379.html">HTML meta标签总结与属性使用介绍</a>

<a href="https://www.cnblogs.com/gwcyulong/p/6674454.html">HTML中Meta标签中http-equiv属性小结</a>

### title标签 

title标签定义文档的标题，在所有 HTML 文档中是必需的。

- 定义浏览器工具栏中的标题
- 提供页面被添加到收藏夹时的标题
- 显示在搜索引擎结果中的页面标题

### h系标签 

h1- h6标签被用来定义 HTML 标题。h1定义重要等级最高的标题。h6定义重要等级最低的标题。

| 属性  | 值                              |
| ----- | ------------------------------- |
| align | left、 center、 right、 justify |

h系是块级标签，独占一行。

搜索引擎会使用标题将网页的结构和内容编制索引，所以网页上使用标题是很重要的。

### font标签

规定文本的字体、字体尺寸、字体颜色。

| 属性  | 描述           |
| ----- | -------------- |
| color | 规定文本的颜色 |
| face  | 规定文本的字体 |
| size  | 规定文本的尺寸 |

```html
<font face="微软雅黑" color="green" size="8">字体</font>
```



### **短语标签**

以下元素都是短语元素。虽然这些标签定义的文本大多会呈现出特殊的样式，但这些标签也都拥有确切的语义。

|  定义  | 用法                                                         |
| :----: | ------------------------------------------------------------ |
|   em   | 把文本定义为强调的内容                                       |
| strong | 把文本定义为语气更强的强调的内容。                           |
|  dfn   | 定义一个定义项目。                                           |
|  code  | 定义计算机代码文本。                                         |
|  samp  | 定义样本文本。                                               |
|  kbd   | 定义键盘文本。它表示文本是从键盘上键入的。它经常用在与计算机相关的文档或手册中。 |
|  var   | 定义变量。您可以将此标签与 pre 及 code>标签配合使用。        |
|  cite  | 定义引用。可使用该标签对参考文献的引用进行定义，比如书籍或杂志的标题。 |

```html
<em>强调文本</em><br>
<strong>加粗文本</strong><br>
<dfn>定义项目</dfn><br>
<code>一段电脑代码</code><br>
<samp>计算机样本</samp><br>
<kbd>键盘输入</kbd><br>
<var>变量</var>
```

```html
<img src="http://www.runoob.com/try/demo_source/img_the_scream.jpg"
     width="220" height="277" alt="The Scream">
<p><cite>The Scream</cite> by Edward Munch. Painted in 1893.</p>
```

<a href="https://blog.csdn.net/eeeecw/article/details/80591511">什么是HTML语义化标签？常见HTML语义化标签大全</a>

### i标签

显示斜体文本效果

### b标签

规定粗体文本

```html
<p>这是普通文本 - <b>这是粗体文本</b>。</p>
```

### 下划线标记u中划线标记s

为文本添加下划线。如果文本不是超链接，就不要对其使用下划线。

```html
<p>如果文本不是超链接，就不要<u>对其使用下划线</u>。</p>
```

删除线文本定义。s标签是 strike标签的缩写版本。

```html
<p>在 HTML 5 中，<s>仍然支持</s>已经不支持这个标签了。</p>
```

```html
<p>
    <u>刘诗诗</u>
    <s>刘诗诗</s>
</p>
```



### 上标sup下标sub

```html
<p>
    This text contains <sub>subscript</sub>
</p>

<p>
    This text contains <sup>superscript</sup>
</p>

```



```html
<p>
    5<sup>2</sup>
    8<sub>2</sub>
</p>
```

![](https://images2018.cnblogs.com/blog/1341090/201805/1341090-20180521155719391-854816540.png)

### 水平线标签

| 属性    | 值                  | 描述                           |
| ------- | ------------------- | ------------------------------ |
| align   | center、left、right | 规定 hr 元素的对齐方式。       |
| noshade | noshade             | 规定 hr 元素的颜色呈现为纯色。 |
| size    | pixels              | 规定 hr 元素的高度（厚度）。   |
| width   | pixels、%           | 规定 hr 元素的宽度。           |

```html
<p>hr 标签定义水平线：</p>
<hr size="10" noshade/>
<p>这是段落。</p>
<hr width="6%" noshade/>
<p>这是段落。</p>
<hr size="20" align="center" noshade/>
<p>这是段落。</p>
```

### 换行标签

代码中成段的文字，直接在代码中回车换行，在渲染成网页时候不认这种换行，如果真想换行，可以在代码的段落中插入br 来强制换行，代码如下：

```html
<p>
To break<br />lines<br />in a<br />paragraph,<br />use the br tag.
</p>
```

### **特殊字符**

```html
<!--空格-->&nbsp; <!--大于号-->&gt; <!--小于号-->&lt; <!--符号&-->&amp;
<!--符合¥-->&yen; <!--版权-->&copy; <!--注册-->&reg; <!--双引号-->&quot;
<!--单引号-->&apos; <!--商标™-->&trade;
```

<a href="http://tool.chinaz.com/Tools/HtmlChar.aspx">HTML特殊字符</a>

<a href="http://www.webhek.com/post/html-enerty-code.html">HTML特殊字符符号大全</a>

```html
<p>
    3 &lt; 5 <br/>
    10 &gt; 5
</p>
```



### html段落标签

p标签定义一个文本段落，一个段落含有默认的上下间距，段落之间会用这种默认间距隔开，代码如下：

```html
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```

**可选的属性**

| 属性  | 值                           | 描述                     |
| ----- | ---------------------------- | ------------------------ |
| align | left、right、center、justify | 规定段落中文本的对齐方式 |

**右对齐的段落：**

```html
<p align="right">This is some text in a very short paragraph</p>
```



> **HTML将所有的标签分为两种：**
>
> **文本级标签：p、span、a、b、i、u、em。文本标签里只能放文字、图片、表单元素。**
>
> **容器级标签：div、h系列、li、dt、dd。容器级标签里可以放任何东西。**

### div标签和span标签

div标签用来定义一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。
span标签用来定义内联元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。

div在浏览器中，默认是不会增加任何的效果的，但是语义变了，div中的所有元素是一个小区域。

> **div标签是一个容器级标签，里面什么都能放，甚至可以放div自己。**
>
> **span也是表达“小区域、小跨度”的标签，但是是一个文本级的标签。**
>
> **span里面只能放置文字、图片、表单元素， span里面不能放p、h、ul、dl、ol、div。**
>

### 块级元素与行内元素

所谓块元素，是以另起一行开始渲染的元素，行内元素则不需另起一行。如果单独在网页中插入这两个元素，不会对页面产生任何的影响。这两个元素是专门为定义CSS样式而生的。

**标签嵌套**

通常块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。p标签不能包含块级标签，p标签也不能包含p标签。

**块儿级标签**           

h1~h6、div、p、hr 
默认占浏览器宽度
能设置长和宽

**行内标签**   	

a、img、u、s、i、b、span				

根据内容决定长度

不能设置长和宽

### 内容居中标签 center

对其所包括的文本进行水平居中。

此时center代表是一个标签，而不是一个属性值了。只要是在这个标签里面的内容，都会居于浏览器的中间。

```html
<center>
    <p>小凳子</p>
</center>
```

center标签支持如下标准属性：

```
id, class, title, style, dir, lang, xml:lang
```

事件属性：

```
onclick, ondblclick, onmousedown, onmouseup, onmouseover, 
onmousemove, onmouseout, onkeypress, onkeydown, onkeyup
```



### 预定义标签pre

pre 元素可定义预格式化的文本。被包围在 pre 元素中的文本通常会保留空格和换行符。而文本也会呈现为等宽字体。pre标签的一个常见应用就是用来表示计算机的源代码。

```html
<pre>
这是
预格式文本。
它保留了      空格
和换行。
</pre>

<p>pre 标签很适合显示计算机代码：</p>

<pre>
for i = 1 to 10
     print i
next i
</pre>
```

<a href="http://www.w3school.com.cn/tags/tag_pre.asp">HTML <pre> 标签</a>

### **img标签**

向网页中嵌入一幅图像。

**必需的属性**

| 属性 | 值   | 描述               |
| ---- | ---- | ------------------ |
| alt  | text | 规定图像的替代文本 |
| src  | URL  | 规定显示图像的 URL |

**可选的属性**

| 属性     | 值                               | 描述                             |
| -------- | -------------------------------- | -------------------------------- |
| align    | top、bottom、middle、left、right | 规定如何根据周围的文本来排列图像 |
| border   | pixels                           | 定义图像周围的边框               |
| height   | pixels、%                        | 定义图像的高度                   |
| hspace   | pixels                           | 定义图像左侧和右侧的空白         |
| ismap    | URL                              | 将图像定义为服务器端图像映射     |
| longdesc | URL                              | 指向包含长的图像描述文档的 URL   |
| usemap   | URL                              | 将图像定义为客户器端图像映射     |
| vspace   | pixels                           | 定义图像顶部和底部的空白         |
| width    | pixels、%                        | 设置图像的宽度                   |

```html
<img src="图片的路径" alt="图片未加载成功时的提示" title="鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">
```

alt属性定义图片加载失败时显示的文字，搜索引擎会使用这个文字收录图片、盲人读屏软件会读取这个文字让盲人识别图片，所以此属性非常重要。

<a href="http://www.w3school.com.cn/tags/tag_img.asp">HTML <img> 标签</a>

### html链接标签

a标签定义超链接，用于从一张页面链接到另一张页面。a元素最重要的属性是 href 属性，它指示链接的目标。

所谓的超链接是指从一个网页指向一个目标的连接关系，这个目标可以是另一个网页，也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序。

```html
<a href="http://www.w3school.com.cn">W3School</a>

<a href="http://www.itcast.cn/" title="跳转的传智播客网站">传智播客</a>
```

**href属性**

指定目标网页地址

该地址可以有几种类型：

- 绝对URL -  指向另一个站点
- 相对URL -  指向当前站点中确切的路径
- 锚URL     -  指向页面中的锚

**超链接有三种形式：**

**1、外部链接**

链接到外部文件

```html
<!--链接到外部文件-->
<a href="new.html">点击进入到新网页</a>

<!--访问一个网址-->
<a href="http://www.baidu.com" target="_blank">进入百度</a>
```

**2、锚链接**

指给超链接起一个名字，作用是在本页面或者其他页面的的不同位置进行跳转。比如说，在网页底部有一个向上箭头，点击箭头后回到顶部，这个就是利用到了锚链接。首先我们要创建一个锚点，也就是说，使用name属性或者id属性给那个特定的位置起个名字。效果如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>萌宠集结号</title>
</head>
<body>
<ul type="circle">
    <li><a href="#miao">去找喵星人</a></li>
    <li><a href="#wang">去找汪星人</a></li>
    <li><a href="#meng">其他萌物</a></li>
</ul>

<a name="miao"></a><!--设置锚点方法1-->
<h3 id="miao">喵星人基地</h3><!--设置锚点方法2-->
<p>喵喵喵~</p>
<p>喵喵喵~</p>
<p>喵喵喵~</p>
<p>喵喵喵~</p>
<p>喵喵喵~</p>
<p>喵喵喵~</p>

<a name="wang"></a>
<p>汪汪汪~</p>
<p>汪汪汪~</p>
<p>汪汪汪~</p>
<p>汪汪汪~</p>
<p>汪汪汪~</p>
<p>汪汪汪~</p>

<a name="meng"></a>
<p>萌萌萌~</p>
<p>萌萌萌~</p>
<p>萌萌萌~</p>
<p>萌萌萌~</p>
<p>萌萌萌~</p>
<p>萌萌萌~</p>
</body>
</html>
```

如果少了#号，点击之后，就会跳到miao、wang、meng这个文件或者这个文件夹中去。

**跳转外部页面的锚链接**

如果我们将上图中的回到顶部那一行代码写成：

```html
<a href="new.hml#top">外部页面的锚链接</a>
```

就表示，点击之后，跳转到new.html页面的top锚点中去。

**3、邮件链接**

举例：

```html
<a href="mailto:zhaoxu@tedu.cn">联系我们</a>
```

**几个特殊链接：**

```html
<!--返回页面顶部的位置-->
<a href="#">跳转到顶部</a>

 <!--javascript:是表示在触发<a>默认动作时，执行一段JavaScript代码-->
<a href="javascript:alert(1)">内容</a>

 <!--javascript:;表示什么都不执行，这样点击<a>时就没有任何反应-->
<a href="javascript:;">内容</a>
```

**属性**

| 属性     | 值                                          | 描述                                  |
| -------- | ------------------------------------------- | ------------------------------------- |
| charset  | char_encoding                               | 规定被链接文档的字符集                |
| coords   | coordinates                                 | 规定链接的坐标                        |
| download | filename                                    | 规定被下载的超链接目标                |
| href     | URL                                         | 规定链接指向的页面的 URL              |
| hreflang | language_code                               | 规定被链接文档的语言                  |
| media    | media_query                                 | 规定被链接文档是为何种媒介/设备优化的 |
| name     | section_name                                | 规定锚的名称                          |
| rel      | text                                        | 规定当前文档与被链接文档之间的关系    |
| rev      | text                                        | 规定被链接文档与当前文档之间的关系    |
| shape    | default、rect、circle、poly                 | 规定链接的形状                        |
| target   | _blank、 _parent、 _self、 _top 、framename | 规定在何处打开链接文档                |
| type     | MIME type                                   | 规定被链接文档的的 MIME 类型          |

title：悬停文本

**a标签的 target 属性**

| 值        | 描述                                 |
| --------- | ------------------------------------ |
| _blank    | 在新窗口中打开被链接文档。           |
| _self     | 在相同的框架中打开被链接文档。默认。 |
| _parent   | 在父框架集中打开被链接文档。         |
| _top      | 在整个窗口中打开被链接文档。         |
| framename | 在指定的框架中打开被链接文档。       |

**download 属性**

```html
<!DOCTYPE html>
<html>
<body>

<p>点击 W3School 的 logo 来下载该图片：
<p>

    <a href="https://dwz.cn/i0DqS7Yd" download="w3logo">
        <img border="0" src="https://dwz.cn/i0DqS7Yd" alt="W3School">
    </a>

</body>
</html>

```

<a href="http://www.w3school.com.cn/tags/tag_a.asp">HTML <a> 标签</a>

快速生成表格

```
table>caption+(thead>tr*2>th*2)+(tbody>tr*2>td*2)
```

```
<del>这是一个del标签</del>
```