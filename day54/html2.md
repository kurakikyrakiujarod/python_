# 前端知识之HTML内容2



## 列表标签

### 无序列表ul

li不能单独存在，必须包裹在ul里面。ul的作用，并不是给文字增加小圆点的，而是增加无序列表的“语义”的。

**type属性：**

disc(实心原点，默认)

square(实心方点)

circle(空心圆)

```html
<body>
<ul>
    <li>aoa,默认</li>
    <li>clara,默认</li>
    <li>kuraki,默认</li>
</ul>
<ul type="square">
    <li>aoa,实心方点</li>
    <li>clara,实心方点</li>
    <li>kuraki,实心方点</li>
</ul>
<ul type="circle">
    <li>aoa,空心圆</li>
    <li>clara,空心圆</li>
    <li>kuraki,空心圆</li>
</ul>
</body>　
```

**列表之间是可以嵌套的**

```html
<html>

<body>

<h4>一个嵌套列表：</h4>
<ul>
    <li>咖啡</li>
    <li>茶
        <ul>
            <li>红茶</li>
            <li>绿茶
                <ul>
                    <li>中国茶</li>
                    <li>非洲茶</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>牛奶</li>
</ul>

</body>
</html>
```

li是一个容器级标签，li里面什么都能放。甚至可以再放一个ul。

### 有序列表ol

```html
<body>
<ol type="1">
    <li>aoa</li>
    <li>clara</li>
    <li>kuraki</li>
</ol>
<ol type="a">
    <li>aoa</li>
    <li>clara</li>
    <li>kuraki</li>
</ol>
<ol type="i" start="3">
    <li>aoa</li>
    <li>clara</li>
    <li>kuraki</li>
</ol>
<ol type="I" start="5">
    <li>aoa</li>
    <li>clara</li>
    <li>kuraki</li>
</ol>
</body>
```

**type属性：**

1 数字列表，默认值

A 大写字母

a 小写字母

Ⅰ大写罗马

ⅰ小写罗马

结合start属性表示初始值。

**去除ul的默认样式，使用如下样式：**

```html
 <style type="text/css">
        ul {
            list-style: none;
        }
    </style>
```

### 定义列表dl

dl：标签表示列表的整体。

dt：列表的标题，这个标签是必须的。
dd：列表的列表项，如果不需要它，可以不加。

dt、dd只能在dl里面；dl里面只能有dt、dd。

```html
<dl>
    <dt>Coffee</dt>
    <dd>Black hot drink</dd>
    <dt>Milk</dt>
    <dd>White cold drink</dd>
</dl>
```

定义列表用法非常灵活，可以一个dt配很多dd：

还可以拆开，让每一个dl里面只有一个dt和dd。

dt、dd都是容器级标签，想放什么都可以。所以，现在就应该更加清晰的知道：用什么标签，不是根据样子来决定，而是语义（语义本质上是结构）。

| 标签 | 描述           |
| ---- | -------------- |
| ol   | 定义有序列表   |
| ul   | 定义无序列表   |
| li   | 定义列表项     |
| dl   | 定义定义列表   |
| dt   | 定义定义项目   |
| dd   | 定义定义的描述 |

## 表格标签 

表格标签用table表示，一个表格table是由每行tr组成的，每行是由td组成的。
所以我们要记住，一个表格是由行组成的（行是由列组成的），而不是由行和列组成的。

td 指表格数据，即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```html
<table>
    <thead>
    <tr>
        <th>序号</th>
        <th>姓名</th>
        <th>爱好</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>Egon</td>
        <td>杠娘</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Yuan</td>
        <td>日天</td>
    </tr>
    </tbody>
</table>
```

### table标签

声明一个表格，它的常用属性如下：

| 属性        | 意义                                                         |
| ----------- | ------------------------------------------------------------ |
| border      | 表格边框。                                                   |
| bordercolor | 表格的边框颜色。                                             |
| align       | 设置整体表格相对于浏览器窗口的水平对齐方式，设置值有：left、center、right。 |
| cellpadding | 内边距，单元格内容到边的距离。默认情况下，文字是紧挨着左边那条线的，即默认情况下的值为0。默认是与左边那条线的距离。如果设置属性dir="rtl"，那就指的是内容到右边那条线的距离。 |
| cellspacing | 外边距，单元格和单元格之间的距离（外边距），像素为单位。 默认情况下的值为0。 |
| bgcolor     | 表格的背景颜色。                                             |
| background  | 背景图片，背景图片的优先级大于背景颜色。                     |
| width       | 宽度。像素为单位。                                           |
| height      | 高度。像素为单位。                                           |
| dir         | 公有属性， 规定元素内容的文本方向。可以取值：ltr：从左到右（left to right，默认），rtl：从右到左（right to left）。 |
| frame       | 规定外侧边框的哪个部分是可见的 ，可以取值void、above、below、hsides、lhs、rhs 、vsides、box、border。 |
| rules       | 规定内侧边框的哪个部分是可见的, 可以取值none、groups、rows、cols、all。 |

```html
<table frame="above" dir="rtl" border="2" bordercolor="#99ccff" cellspacing="5" cellpadding="5" width="800" height="100" background="https://dwz.cn/AqAVqqG2" bgcolor="blue" align="center">
```



### tr标签

定义表格中的一行

| 属性    | 值                                  | 描述                             |
| ------- | ----------------------------------- | -------------------------------- |
| align   | right、left、center、justify、char  | 定义表格行的内容对齐方式。       |
| bgcolor | rgb(x,x,x)、十六进制表示、colorname | 规定表格行的背景颜色。           |
| char    | character                           | 规定根据哪个字符来进行文本对齐。 |
| charoff | numeber                             | 规定第一个对齐字符的偏移量。     |
| valign  | top、middle、bottom、baseline       | 规定表格行中内容的垂直对齐方式。 |
| height  | number                              | 一行的高度。                     |

几乎没有浏览器支持 char、charoff 属性。

```html
<tr dir="rtl" height="100" bgcolor="aqua" align="center" valign="baseline">
```



### **td和th标签：**

定义一行中的一个单元格，td代表普通单元格，th表示表头单元格。

| 属性       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| align      | 设置单元格中内容的水平对齐方式，设置值有：left  \|  center \| right。 |
| valign     | 设置单元格中内容的垂直对齐方式，设置值有： top \| middle \| bottom。 |
| rowspan    | 单元格竖跨多少行。                                           |
| colspan    | 单元格横跨多少列。                                           |
| width      | 绝对值或者相对值(%)。                                        |
| height     | 单元格的高度。                                               |
| bgcolor    | 设置这个单元格的背景色。                                     |
| background | 设置这个单元格的背景图片。                                   |

```html
<th align="right" valign="bottom" width="30%" height="100" bgcolor="#ffebcd"
    background="https://dwz.cn/8XPw2wzO">
```



**细线表格**

```html
<!-- style="border-collapse:collapse;"即单元格的线和表格的边框线合并-->
<table border="1" style="border-collapse: collapse">
    <tr>
        <td>小马哥</td>
        <td>18</td>
        <td>男</td>
        <td>山东</td>
    </tr>

    <tr>
        <td>小岳岳</td>
        <td>45</td>
        <td>男</td>
        <td>河南</td>
    </tr>

    <tr>
        <td>邓紫棋</td>
        <td>23</td>
        <td>女</td>
        <td>香港</td>
    </tr>
</table>
```

**单元格的合并**

如果要将两个单元格合并，那肯定就要删掉一个单元格。
单元格的属性：

colspan：横向合并。例如colspan="2"表示当前单元格在水平方向上要占据两个单元格的位置。
rowspan：纵向合并。例如rowspan="2"表示当前单元格在垂直方向上。

```html
<html>

<body>

<h4>横跨两列的单元格：</h4>
<table border="1">
    <tr>
        <th>姓名</th>
        <th colspan="2">电话</th>
    </tr>
    <tr>
        <td>Bill Gates</td>
        <td>555 77 854</td>
        <td>555 77 855</td>
    </tr>
</table>

<h4>横跨两行的单元格：</h4>
<table border="1">
    <tr>
        <th>姓名</th>
        <td>Bill Gates</td>
    </tr>
    <tr>
        <th rowspan="2">电话</th>
        <td>555 77 854</td>
    </tr>
    <tr>
        <td>555 77 855</td>
    </tr>
</table>

</body>
</html>
```

***caption标签***

定义表格标题
caption 标签必须紧随 table 标签之后，只能对每个表格定义一个标题。通常这个标题会被居中于表格之上。

caption表格的标题，使用时和tr标签并列。

```html
<table border="1">
    <caption>人物介绍</caption>
    <tr>
        <td>aoa</td>
        <td>18</td>
        <td>女</td>
        <td rowspan="3">中国</td>
    </tr>
 
    <tr>
        <td>clara</td>
        <td>22</td>
        <td>女</td>
    </tr>
 
    <tr>
        <td>kuraki</td>
        <td>23</td>
        <td>女</td>
    </tr>
</table>
```

***frame属性***

```html
<html>
<body>

<p><b>注释：</b>frame 属性无法在 Internet Explorer 中正确地显示。</p>

<p>Table with frame="box":</p>
<table frame="box">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>

<p>Table with frame="above":</p>
<table frame="above">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>

<p>Table with frame="below":</p>
<table frame="below">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>

<p>Table with frame="hsides":</p>
<table frame="hsides">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>

<p>Table with frame="vsides":</p>
<table frame="vsides">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>

</body>
</html>
```

***thead、tbody、tfoot标签***

这三个标签有与没有的区别：

1、如果写了，那么这三个部分的代码顺序可以任意，浏览器显示的时候还是按照thead、tbody、tfoot的顺序依次来显示内容。如果不写thead、tbody、tfoot，那么浏览器解析并显示表格内容的时候是从按照代码的从上到下的顺序来显示。
2、当表格非常大内容非常多的时候，如果用thead、tbody、tfoot标签的话，那么数据可以边获取边显示。如果不写，则必须等表格的内容全部从服务器获取完成才能显示出来。

```html
<body>
<table border="1">
    <caption>人物介绍</caption>
    <tbody>
    <tr>
        <td>clara</td>
        <th>18</th>
        <td>女</td>
        <td rowspan="3">中国</td>
    </tr>
    </tbody>

    <tfoot>
    <tr>
        <td>kuraki</td>
        <td>22</td>
        <td>女</td>

    </tr>
    </tfoot>
    <thead>
    <tr>
        <td>aoa</td>
        <td>23</td>
        <td>女</td>
    </tr>
    </thead>

</table>
</body>
```

## 表单标签 

表单标签用form表示，用于与服务器的交互。表单就是收集用户信息的，就是让用户填写的、选择的。

### get提交和post提交

| 值   | 描述                                                        |
| ---- | ----------------------------------------------------------- |
| get  | 向 URL 追加表单数据（form-data）：URL?name=value&name=value |
| post | 以 HTTP post 事务的形式发送表单数据（form-data）            |

GET方式：将表单数据，以"name=value"形式追加到action指定的处理程序的后面，两者间用"?"隔开，每一个表单的"name=value"间用"&"号隔开。

特点：只适合提交少量信息，并且不太安全(不要提交敏感数据)、提交的数据类型只限于ASCII字符。如果表单提交是被动的（比如搜索引擎查询），并且没有敏感信息。当您使用 GET 时，表单数据在页面地址栏中是可见的。

POST方式：将表单数据直接发送(隐藏)到action指定的处理程序。POST 更加安全，因为在页面地址栏中被提交的数据是不可见的。Action指定的处理程序可以获取到表单数据。

特点：可以提交海量信息，相对来说安全一些，提交的数据格式是多样的(Word、Excel、rar、img)。如果表单正在更新数据，或者包含敏感信息（例如密码）。

### input标签

input 标签用于搜集用户信息。

根据不同的 type 属性值，输入字段拥有很多种形式。输入字段可以是文本字段、复选框、掩码后的文本控件、单选按钮、按钮等等。

<a href="http://www.w3school.com.cn/tags/tag_input.asp">HTML <input> 标签</a>

<a href="http://www.runoob.com/tags/tag-input.html">HTML <input> 标签</a>

| 属性           | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| accept         | 规定了可通过文件上传提交的服务器接受的文件类型。如需规定多个值，使用逗号分隔。audio/*	接受所有的声音文件。video/*	接受所有的视频文件。image/*	接受所有的图像文件。MIME_type	一个有效的 MIME 类型，不带参数。 |
| align          | 它规定图像输入相对于周围其他元素的对齐方式。可能的值left(默认)、right、top、middle、bottom。 |
| alt            | 定义图像输入的替代文本。为用户由于某些原因无法查看图像时提供了备选的信息。 |
| autocomplete   | 规定输入字段是否启用自动完成功能。on 启用、off禁用，默认开启。 |
| autofocus      | 规定当页面加载时 input 元素应该自动获得焦点。不适用于 type="hidden"。布尔属性。 |
| checked        | 规定在页面加载时应该被预先选定的 input 元素。与单选框、复选框配合使用。布尔属性。 |
| disabled       | 禁用一个 input 元素。被禁用的 input 元素是无法使用和无法点击的。表单中被禁用的 input 元素不会被提交。布尔属性。不适用于  type="hidden"。 |
| form           | 规定 input元素所属的一个或多个表单。值必须是其所属表单的 id。 如需引用一个以上的表单，用空格分隔。 |
| selected       | option标签的 selected 属性。布尔属性。规定在页面加载时预先选定该选项。被预选的选项会显示在下拉列表最前面的位置。 |
| formenctype    | 覆盖 form元素的 enctype 属性。适用于 type="submit" 和 type="image"。 |
| formnovalidate | 覆盖表单的 novalidate 属性。如果使用该属性，则提交表单时不进行验证。该属性适用于 form 以及以下类型的 input：text, search, url, telephone, email, password, date pickers, range 以及 color。 |
| height         | 只适用于 type="image"，它规定 image input 的高度。可能的值，pixels，以像素计的高度。（比如 "100px" 或 "100"）。%，以包含元素的百分比计的高度。（比如 "50%"） |
| max            | 规定输入字段所允许的最大值。max 属性与 min 属性配合使用，可创建合法值范围。可能的值，number数字值，date日期。 |
| maxlength      | 输入字段中允许的最大字符数。适用于type="text" 或 type="password"。 |
| min            | 规定输入字段所允许的最小值。可能的值，number数字值，date日期。 |
| multiple       | 输入字段可选择多个值。布尔属性。适用于type="email"和 type="file"。 |
| name           | input 元素的名称。用于对提交到服务器后的表单数据进行标识，或者在客户端通过 JavaScript 引用表单数据。只有设置了 name 属性的表单元素才能在提交表单时传递它们的值。 |
| pattern        | 规定用于验证输入字段的模式。模式指的是正则表达式。适用于以下 input 类型：text, search, url, telephone, email 以及 password 。 |
| placeholder    | 规定可描述输入字段预期值的简短的提示信息。该提示会在输入字段为空时显示，并会在字段获得焦点时消失。适用于下面的 input 类型：text、search、url、tel、email 和 password。 |
| readonly       | 把输入字段设置为只读。只读字段是不能修改的。不过，用户仍然可以使用 tab 键切换到该字段，还可以选中或拷贝其文本。可与 type="text"或 type="password" 配合使用。布尔属性。 |
| required       | 必需在提交之前填写输入字段。如果使用该属性，则字段是必填（或必选）的。布尔属性。 |
| size           | size 属性规定输入字段的宽度。对于文本输入框和密码输入框，size 属性定义的是可见的字符数。默认值是 20。对于其它类型，size属性以像素为单位。 |
| src            | src 属性只能与 type="image" 配合使用。它规定作为提交按钮显示的图像的 URL。可能的值：绝对 URL ，相对 URL 。 |
| step           | 规定输入字段的合法数字间隔。step 属性可以与 max 以及 min 属性配合使用，以创建合法值的范围。step、max 以及 min 属性适用于以下 input类型：number, range, date, datetime, datetime-local, month, time 以及 week。 |
| type           | 规定 input 元素的类型。input标签里唯一的必须输入的属性，不填，默认为text。可能的值，button、checkbox、color、date、datetime、datetime-local、email、file、hidden、image、month、number、password、radio、range、reset、search、submit、tel、text、time、url、week。 |
| value          | 为 input 元素设定值。对于不同的输入类型，value 属性的用法也不同：type="button", "reset", "submit" - 定义按钮上的显示的文本，type="text", "password", "hidden" - 定义输入字段的初始值，type="checkbox", "radio", "image" - 定义与输入相关联的值。type="checkbox"和 type="radio"中必须设置 value 属性。value 属性无法与 type="file" 一同使用。 |
| width          | 规定 image input 的宽度。                                    |
|                |                                                              |
|                |                                                              |
| form overrides | 表单重写属性，formaction, formenctype, formmethod, formnovalidate, formtarget，允许重写 form 元素的某些属性设定。 |
| formaction     | 覆盖表单的 action 属性。适用于 type="submit" 和 type="image"。 |
| formmethod     | 覆盖表单的 method 属性。适用于 type="submit" 和 type="image"。 |
| list           | 引用数据列表，其中包含输入字段的预定义选项。值必须是绑定到 input元素的 datalist 的 id。 |
| formtarget     | 覆盖表单的 target 属性。适用于 type="submit" 和 type="image"。 |



###  type标签

type 属性规定 input 元素的类型

| 值       | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| button   | 定义可点击按钮。                                             |
| checkbox | 定义复选框。名字相同的按钮作为一组进行选择。                 |
| file     | 文件选择框。                                                 |
| hidden   | 定义隐藏的输入字段。                                         |
| image    | 定义图像形式的提交按钮。                                     |
| password | 定义密码字段。密码字段中的字符会被掩码（显示为星号或原点）。 |
| radio    | 单选按钮。名字相同的按钮作为一组进行单选。                   |
| reset    | 重置按钮。清空当前表单的内容，并设置为最初的默认值。         |
| submit   | 定义提交按钮。提交按钮会把表单数据发送到服务器。             |
| text     | 定义单行的输入字段，用户可在其中输入文本。默认宽度为 20 个字符。 |

<a href="http://www.w3school.com.cn/tags/att_input_type.asp">HTML <input> 标签的 type 属性</a>

<a href="http://www.runoob.com/tags/att-input-type.html">HTML <input> type 属性</a>

<a href="http://www.runoob.com/tags/tag-input.html">HTML <input> 标签</a>

<a href="http://www.w3school.com.cn/tags/tag_input.asp">HTML <input> 标签</a>



### form标签

form 标签用于为用户输入创建 HTML 表单。

表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。

表单还可以包含 menus、textarea、fieldset、legend 和 label 元素。

表单用于向服务器传输数据。

| 属性           | 描述                                                         |
| :------------- | ------------------------------------------------------------ |
| accept-charset | 服务器可处理的一个或多个字符集。多个字符编码使用空格分隔。常用值：UTF-8 - Unicode 字符编码、ISO-8859-1 - 拉丁字母表的字符编码、gb2312 - 简体中文字符集。 |
| enctype        | 只有 method="post" 时才使用 enctype 属性。规定在发送表单数据之前如何对其进行编码。可能的值：application/x-www-form-urlencoded（默认）、multipart/form-data、text/plain。 |
| target         | 规定在何处打开 action URL。                                  |
| action         | 规定当提交表单时向何处发送表单数据。可能的值：绝对 URL - 指向其他站点、相对 URL - 指向站点内的文件。 |
| autocomplete   | 规定是否启用表单的自动完成功能。（默认开启）                 |
| name           | 规定表单的名称。                                             |
| novalidate     | 如果使用该属性，则提交表单时不进行验证。布尔属性。           |
| method         | 规定用于发送 form-data 的 HTTP 方法。可能的值：get、post。   |

| 值                                | 描述                                                         |
| :-------------------------------- | :----------------------------------------------------------- |
| application/x-www-form-urlencoded | 在发送前编码所有字符（默认）。（空格转换为 "+" 加号，特殊符号转换为 ASCII HEX 值） |
| multipart/form-data               | 不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。 |
| text/plain                        | 空格转换为 "+" 加号，但不对特殊字符编码。                    |

<a href="http://www.w3school.com.cn/tags/tag_form.asp">HTML <form> 标签</a>

<a href="http://www.runoob.com/tags/tag-form.html">HTML <form> 标签</a>



### **fieldset 标签**

fieldset 元素可将表单内的相关元素分组。

fieldset 标签将表单内容的一部分打包，生成一组相关表单的字段。

当一组表单元素放到 fieldset 标签内时，浏览器会以特殊方式来显示它们，它们可能有特殊的边界、3D 效果，或者甚至可创建一个子表单来处理这些元素。

fieldset标签没有必需的或唯一的属性。legend 标签为 fieldset 元素定义标题。

```html
<form>
    <fieldset>
        <legend>Personalia:</legend>
        Name: <input type="text"><br>
        Email: <input type="text"><br>
        Date of birth: <input type="text">
    </fieldset>
</form>
```

**属性**

| 属性     |
| -------- |
| disabled |
| form     |
| name     |

<a href="http://www.w3school.com.cn/tags/tag_fieldset.asp">HTML <fieldset> 标签</a>

<a href="http://www.runoob.com/tags/tag-fieldset.html">HTML <fieldset> 标签</a>



### 输入限制

常用的输入限制

| 属性      |
| --------- |
| disabled  |
| max       |
| maxlength |
| min       |
| pattern   |
| readonly  |
| required  |
| size      |
| step      |
| value     |

<a href="http://www.w3school.com.cn/html/html_form_input_types.asp">HTML 输入类型</a>



### Input类型

<a href="http://www.w3school.com.cn/html5/html_5_form_input_types.asp">HTML5 Input 类型</a>

<a href="http://www.runoob.com/tags/att-input-type.html">HTML <input> type 属性</a>

HTML5 拥有多个新的表单输入类型。这些新特性提供了更好的输入控制和验证。

| Input type   | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| email        | email 类型用于应该包含 e-mail 地址的输入域。在提交表单时，会自动验证 email 域的值。 |
| url          | url 类型用于应该包含 URL 地址的输入域。在提交表单时，会自动验证 url 域的值。 |
| number       | number 类型用于应该包含数值的输入域。还能够设定对所接受的数字的限定。 |
| range        | range 类型用于应该包含一定范围内数字值的输入域。range 类型显示为滑动条。还能够设定对所接受的数字的限定。 |
| Date pickers | 日期选择器。HTML5 拥有多个可供选取日期和时间的新输入类型：date ， month，week ，time，datetime，datetime-local。 |
| search       | search 类型用于搜索域，比如站点搜索或 Google 搜索。search 域显示为常规的文本域。 |
| color        | 定义拾色器。                                                 |
| tel          | 定义用于输入电话号码的字段。                                 |



| 值             | 描述                             |
| -------------- | -------------------------------- |
| date           | 选取日、月、年                   |
| month          | 选取月、年                       |
| week           | 选取周和年                       |
| time           | 选取时间（小时和分钟）           |
| datetime       | 选取时间、日、月、年（UTC 时间） |
| datetime-local | 选取时间、日、月、年（本地时间） |

### HTML5表单元素

HTML5 的新的表单元素：

HTML5 拥有若干涉及表单的元素和属性

### datalist元素

datalist 标签规定了 input 元素可能的选项列表。datalist 标签被用来在为 input 元素提供"自动完成"的特性。

用户能看到一个下拉列表，里边的选项是预先定义好的，将作为用户的输入数据。

datalist 元素规定输入域的选项列表。列表是通过 datalist 内的 option 元素创建的。把 datalist 绑定到输入域，用输入域的 list 属性引用 datalist 的 id即可。

**实例**

```html
Webpage: <input type="url" list="url_list" name="link"/>
<datalist id="url_list">
    <option label="W3School" value="http://www.W3School.com.cn"/>
    <option label="Google" value="http://www.google.com"/>
    <option label="Microsoft" value="http://www.microsoft.com"/>
</datalist>
```

### keygen元素

keygen 元素的作用是提供一种验证用户的可靠方法。keygen 元素是密钥对生成器。当提交表单时，会生成两个键，一个是私钥，一个公钥。私钥存储于客户端，公钥则被发送到服务器。公钥可用于之后验证用户的客户端证书。

### output元素

output 元素用于不同类型的输出，比如计算或脚本输出

```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
    <input type="range" id="a" value="50">100
    +<input type="number" id="b" value="50">
    =
    <output name="x" for="a b"></output>
</form>

<p><strong>注意:</strong> Internet Explorer 不支持 output 标签。</p>
```

| 属性 | 值         | 描述                                       |
| ---- | ---------- | ------------------------------------------ |
| for  | element_id | 描述计算中使用的元素与计算结果之间的关系。 |
| form | form_id    | 定义输入字段所属的一个或多个表单。         |
| name | name       | 定义对象的唯一名称（表单提交时使用）。     |

<a href="http://www.w3school.com.cn/html5/html_5_form_elements.asp">HTML5 表单元素</a>

<a href="http://www.runoob.com/tags/tag-output.html">HTML <output> 标签</a>

<a href="http://www.w3school.com.cn/tags/tag_output.asp">HTML <output> 标签</a>

<a href="http://www.runoob.com/tags/tag-datalist.html">HTML <datalist> 标签</a>

<a href="http://www.w3school.com.cn/tags/tag_datalist.asp">HTML <datalist> 标签</a>

<a href="http://www.w3school.com.cn/tags/tag_keygen.asp">HTML <keygen> 标签</a>

<a href="http://www.runoob.com/tags/tag-keygen.html">HTML <keygen> 标签</a>



### select标签

select元素用来创建下拉列表。select元素中的 option 标签定义了列表中的可用选项。

select标签和ul、ol、dl一样，都是组标签。

| 属性      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| autofocus |                                                              |
| disabled  |                                                              |
| form      |                                                              |
| multiple  | 规定可选择多个选项。对于 windows：按住 Ctrl 按钮来选择多个选项，对于 Mac：按住 command 按钮来选择多个选项。 |
| name      |                                                              |
| required  |                                                              |
| size      | 规定下拉列表中可见选项的数目。如果 size 属性的值大于 1，但是小于列表中选项的总数目，浏览器会显示出滚动条，表示可以查看更多选项。 |

<a href="http://www.runoob.com/tags/tag-select.html">HTML <select> 标签</a>

<a href="http://www.w3school.com.cn/tags/tag_select.asp">HTML <select> 标签</a>

```html
<body>
<form>
    <select>
        <option>小学</option>
        <option>初中</option>
        <option>高中</option>
        <option>大学</option>
        <option selected="">研究生</option>
    </select>
    <br><br>

    <select size="3">
        <option>小学</option>
        <option>初中</option>
        <option>高中</option>
        <option>大学</option>
        <option>研究生</option>
    </select>
    <br><br>

    <select multiple="">
        <option>小学</option>
        <option>初中</option>
        <option selected="">高中</option>
        <option selected="">大学</option>
        <option>研究生</option>
    </select>
    <br><br>
</form>
</body>
```

### textare标签

textarea 标签定义多行的文本输入控件。文本区域中可容纳无限数量的文本，其中的文本的默认字体是等宽字体（通常是 Courier）。可以通过 cols 和 rows 属性来规定 textarea 的尺寸，不过更好的办法是使用 CSS 的 height 和 width 属性。



| 属性        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| autofocus   |                                                              |
| cols        | 规定文本区内的可见宽度。                                     |
| disabled    |                                                              |
| form        |                                                              |
| maxlength   |                                                              |
| name        |                                                              |
| placeholder |                                                              |
| readonly    |                                                              |
| required    |                                                              |
| rows        | 规定文本区域内可见的行数。                                   |
| wrap        | 规定当在表单中提交时，文本区域中的文本如何换行。 默认值soft， 当在表单中提交时，textarea 中的文本不换行。hard，当在表单中提交时，textarea 中的文本换行（包含换行符）。当使用 "hard" 时，必须规定 cols 属性。 |

<a href="http://www.w3school.com.cn/tags/tag_textarea.asp">HTML <textarea> 标签</a>

<a href="http://www.runoob.com/tags/tag-textarea.html">HTML <textarea> 标签</a>

```html
<form>
<textarea rows="2" cols="20" name="usrtxt" wrap="hard">
 At W3School you will find free Web-building tutorials.
</textarea>
<input type="submit">
</form>
```



### label标签

label 标签为 input 元素定义标注。label 元素不会向用户呈现任何特殊效果。不过，它为鼠标用户改进了可用性。

在 label 元素内点击文本，就会触发此控件。当用户选择该标签时，浏览器就会自动将焦点转到和标签相关的表单控件上。label 标签的 for 属性应当与相关元素的 id 属性相同。

```html
<input type="radio" name="sex" /> 男
<input type="radio" name="sex" /> 女
```

对于上面这样的单选框，我们只有点击那个单选框（小圆圈）才可以选中，点击“男”、“女”这两个文字时是无法选中的；于是，label标签派上了用场。本质上来讲，“男”、“女”这两个文字和input标签时没有关系的，而label就是解决这个问题的。我们可以通过label把input和汉字包裹起来作为整体。

```html
<input type="radio" name="sex" id="nan" /> <label for="nan">男</label>
<input type="radio" name="sex" id="nv"  /> <label for="nv">女</label>　
```

上方代码中，input元素要有一个id，然后label标签有一个for属性，和id相同，那么这个label和input就有绑定关系了。当然了，复选框也有label：（任何表单元素都有label）

```html
<input type="checkbox" id="kk" />
<label for="kk">10天内免登陆</label> 
```

| 属性 | 值     | 描述                                  |
| ---- | ------ | ------------------------------------- |
| for  | id     | 规定 label 绑定到哪个表单元素。       |
| form | formid | 规定 label 字段所属的一个或多个表单。 |

```html
<p>第一个单选按钮在表单之外,但它仍属于该表单的一部分。尝试点击文本标签切换单选按钮。</p>

<form id="form1">
  <input type="radio" name="sex" id="male" value="male"><br>
  <label for="female">Female</label>
  <input type="radio" name="sex" id="female" value="female"><br><br>
  <input type="submit" value="提交">
</form>

<label for="male" form="form1">Male</label>
```

<a href="http://www.w3school.com.cn/tags/tag_label.asp">HTML <label> 标签</a>

<a href="http://www.runoob.com/tags/tag-label.html">HTML <label> 标签</a>

### 

## form表单示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>form表单示例</title>
</head>
<body>
<form enctype="multipart/form-data">
    <p>
        <label for="i1">用户名：</label>
        <input id="i1" name="username" type="text" placeholder="用户名" required>
    </p>

    <p>
        <label for="i2">密码：</label>
        <input id="i2" name="password" type="password" placeholder="密码" required>
    </p>
    <p>
        <label for="i3">邮箱：</label>
        <input id="i3" name="email" type="email" novalidate placeholder="邮箱" required>
    </p>
    <p>
        <input type="hidden" value="user_id" name="hidden">
    </p>
    <p>
        性别：
        <label for="g1">男</label>
        <input id="g1" type="radio" name="gender" value="0">
        <label for="g2">女</label>
        <input id="g2" type="radio" name="gender" value="1">
        <label for="g3">保密</label>
        <input id="g3" type="radio" name="gender" value="2" checked>
        <label>LGBTQ
            <input type="radio" name="gender" value="3">
        </label>
    </p>
    <p>
        爱好：
        <label for="i4">篮球</label>
        <input id="i4" name="hobby" value="baskerball" type="checkbox">
        <label for="i5">羽毛球</label>
        <input id="i5" name="hobby" value="badminton" type="checkbox">
        <label for="i6">足球</label>
        <input id="i6" name="hobby" value="soccer" type="checkbox">
        <label for="i7">计算机</label>
        <input id="i7" name="hobby" value="computer" type="checkbox">
        <label for="i8">其它</label>
        <input type="checkbox" value="others" name="hobby" id="i8" checked>
    </p>
    <p>
        <label for="i9">生日：</label>
        <input id="i9" type="date" name="birthday" max="2018-01-01" min="1918-01-01">
    </p>

    <select name="province" id="s1">
        <option value="bj">北京</option>
        <option value="sh">上海</option>
        <option value="sd">山东</option>
    </select>

    <select name="province2" id="s11" multiple>
        <option value="bj">北京</option>
        <option value="sh" selected>上海</option>
        <option value="sd">山东</option>
    </select>

    <select name="city" id="s2">
        <optgroup label="北京">
            <option value="chang_ping">
                昌平区
            </option>
            <option value="sha_he" selected>
                沙河区
            </option>
            <option value="min_hang">
                闵行区
            </option>
        </optgroup>
        <optgroup label="上海">
            <option value="pu_dong">
                浦东区
            </option>
            <option value="jing_an">
                静安区
            </option>
            <option value="bao_shan">
                宝山区
            </option>
        </optgroup>
        <optgroup label="浙江">
            <option value="shang_chen">
                上城区
            </option>
            <option value="xia_cheng">
                下城区
            </option>
            <option value="jiang_gan">
                江干区
            </option>
        </optgroup>
    </select>

    <p>
        <textarea name="personal_info" id="p_info" cols="30" rows="10">请输入个人介绍</textarea>
    </p>

    <p>
        上传头像&nbsp;&nbsp;<input name="file" type="file" accept="image/*">
    </p>

    <p>
        <input type="submit" value="提交">
    </p>
    <p>
        <input type="button" value="普通按钮">
    </p>
    <p>
        <input type="reset" value="重置">
    </p>
    <p>
        <input type="submit" value="不进行验证提交" formnovalidate>
    </p>
</form>
</body>
</html>
```

