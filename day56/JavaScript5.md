# 前端基础之JS

## 滚轮事件

```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>滚轮事件</title>
		<style type="text/css">
			
			#box1{
				width: 100px;
				height: 100px;
				background-color: red;
			}
			
		</style>
		<script type="text/javascript">
			
			window.onload = function(){
				
				
				//获取id为box1的div
				var box1 = document.getElementById("box1");
				
				//为box1绑定一个鼠标滚轮滚动的事件
				/*
				 * onmousewheel鼠标滚轮滚动的事件，会在滚轮滚动时触发，
				 * 但是火狐不支持该属性
				 * 
				 * 在火狐中需要使用 DOMMouseScroll 来绑定滚动事件
				 * 注意该事件需要通过addEventListener()函数来绑定
				 */
				
				
				box1.onmousewheel = function(event){
					
					event = event || window.event;
					
					
					//event.wheelDelta 可以获取鼠标滚轮滚动的方向
					//向上滚 120   向下滚 -120
					//wheelDelta这个值我们不看大小，只看正负
					
					//alert(event.wheelDelta);
					
					//wheelDelta这个属性火狐中不支持
					//在火狐中使用event.detail来获取滚动的方向
					//向上滚 -3  向下滚 3
					//alert(event.detail);
					
					
					/*
					 * 当鼠标滚轮向下滚动时，box1变长
					 * 当滚轮向上滚动时，box1变短
					 */
					//判断鼠标滚轮滚动的方向
					if(event.wheelDelta > 0 || event.detail < 0){
						//向上滚，box1变短
						box1.style.height = box1.clientHeight - 10 + "px";
						
					}else{
						//向下滚，box1变长
						box1.style.height = box1.clientHeight + 10 + "px";
					}
					
					/*
					 * 使用addEventListener()方法绑定响应函数，取消默认行为时不能使用return false
					 * 需要使用event来取消默认行为，event.preventDefault();
					 * 但是IE8不支持event.preventDefault();，如果直接调用会报错
					 */
					event.preventDefault && event.preventDefault();
					
					
					/*
					 * 当滚轮滚动时，如果浏览器有滚动条，滚动条会随之滚动，
					 * 这是浏览器的默认行为，如果不希望发生，则可以取消默认行为
					 */
					return false;

				};
				
				//为火狐绑定滚轮事件
				bind(box1,"DOMMouseScroll",box1.onmousewheel);
				
				
			};
			
			
			function bind(obj , eventStr , callback){
				if(obj.addEventListener){
					//大部分浏览器兼容的方式
					obj.addEventListener(eventStr , callback , false);
				}else{
					/*
					 * this是谁由调用方式决定
					 * callback.call(obj)
					 */
					//IE8及以下
					obj.attachEvent("on"+eventStr , function(){
						//在匿名函数中调用回调函数
						callback.call(obj);
					});
				}
			}
			
		</script>
	</head>
	<body style="height: 2000px;">
		
		<div id="box1"></div>
		
	</body>
</html>
```

## 键盘事件



```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>键盘事件</title>
		<script type="text/javascript">
			
			window.onload = function(){
				
				/*
				 * 键盘事件：
				 * 	onkeydown
				 * 	- 按键被按下
				 *  - 对于onkeydown来说如果一直按着某个按键不松手，则事件会一直触发
				 * 	- 当onkeydown连续触发时，第一次和第二次之间会间隔稍微长一点，其他的会非常的快
				 * 		  这种设计是为了防止误操作的发生。
				 * 	onkeyup
				 * 	- 按键被松开
				 * 
				 *  键盘事件一般都会绑定给一些可以获取到焦点的对象或者是document
				 */
				
				document.onkeydown = function(event){
					event = event || window.event;
					
					/*
					 * 可以通过keyCode来获取按键的编码
					 * 通过它可以判断哪个按键被按下
					 * 除了keyCode，事件对象中还提供了几个属性
					 * 	altKey
					 * 	ctrlKey
					 * 	shiftKey
					 * 		- 这三个用来判断alt ctrl 和 shift是否被按下
					 * 		  如果按下则返回true，否则返回false
					 */
					
					//console.log(event.keyCode);
					
					//判断一个y是否被按下
					//判断y和ctrl是否同时被按下
					if(event.keyCode === 89 && event.ctrlKey){
						console.log("ctrl和y都被按下了");
					}
					
					
				};
				
				/*document.onkeyup = function(){
					console.log("按键松开了");
				};*/
				
				//获取input
				var input = document.getElementsByTagName("input")[0];
				
				input.onkeydown = function(event){
					
					event = event || window.event;
					
					//console.log(event.keyCode);
					//数字 48 - 57
					//使文本框中不能输入数字
					if(event.keyCode >= 48 && event.keyCode <= 57){
						//在文本框中输入内容，属于onkeydown的默认行为
						//如果在onkeydown中取消了默认行为，则输入的内容，不会出现在文本框中
						return false;
					}
					
					
				};
			};
			
			
		</script>
	</head>
	<body>
		
		<input type="text" />
		
	</body>
</html>
```



## BOM

浏览器对象模型

BOM可以使我们通过JS来操作浏览器，在BOM中为我们提供了一组对象，用来完成对浏览器的操作。

**BOM对象**

Window：代表的是整个浏览器的窗口，同时window也是网页中的全局对象

Navigator： 代表的当前浏览器的信息，通过该对象可以来识别不同的浏览器

Location：代表当前浏览器的地址栏信息，通过Location可以获取地址栏信息，或者操作浏览器跳转页面

History：代表浏览器的历史记录，可以通过该对象来操作浏览器的历史记录，由于隐私原因，该对象不能获取到

具体的历史记录，只能操作浏览器向前或向后翻页，而且该操作只在当次访问时有效

Screen：代表用户的屏幕的信息，通过该对象可以获取到用户的显示器的相关的信息

这些BOM对象在浏览器中都是作为window对象的属性保存的，可以通过window对象来使用，也可以直接使用。

```javascript
console.log(window); // [object Window]
console.log(window.navigator); // [object Navigator]
console.log(navigator);	// [object Navigator]
console.log(location); // http://127.0.0.1:8020/JS2/bom.html
console.log(history); // [object History]
```

## **Navigator**

代表的当前浏览器的信息，通过该对象可以来识别不同的浏览器，由于历史原因，Navigator对象中的大部分属性

都已经不能帮助我们识别浏览器了。一般我们只会使用userAgent来判断浏览器的信息，userAgent是一个字符

串，这个字符串中包含有用来描述浏览器信息的内容，不同的浏览器会有不同的userAgent。

| 属性      | 描述                                           |
| --------- | ---------------------------------------------- |
| appName   | 返回浏览器的名称。                             |
| userAgent | 返回由客户机发送服务器的 user-agent 头部的值。 |
|           |                                                |

```javascript
console.log(navigator.userAgent);

// Chrome
/*
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
*/

// FireFox
/*
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0
*/

// IE 11
/*
Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko
*/

// IE 10
/*
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)
*/

// IE 9
/*
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)
*/

// IE 8
/*
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)
*/

```

```javascript
var ua = navigator.userAgent;

console.log(ua);

if (/firefox/i.test(ua)) {
    alert("你是火狐！！！");
} else if (/chrome/i.test(ua)) {
    alert("你是Chrome");
} else if (/msie/i.test(ua)) {
    alert("你是IE浏览器~~~");
} else if ("ActiveXObject" in window) {
    alert("你是IE11，枪毙了你~~~");
}

/*
* 如果通过UserAgent不能判断，还可以通过一些浏览器中特有的对象，来判断浏览器的信息
* 比如：ActiveXObject
*/
/*if("ActiveXObject" in window){
alert("你是IE，我已经抓住你了~~~");
}else{
alert("你不是IE~~~");
}*/

/*alert("ActiveXObject" in window);*/
```

## History

History 对象属性

| 属性   | 描述                              |
| ------ | --------------------------------- |
| length | 返回浏览器历史列表中的 URL 数量。 |

History 对象方法

| 方法      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| back()    | 加载 history 列表中的前一个 URL。                            |
| forward() | 加载 history 列表中的下一个 URL。                            |
| go()      | 可以用来跳转到指定的页面，它需要一个整数作为参数。1:表示向前跳转一个页面，相当于forward() 2:表示向前跳转两个页面 -1:表示向后跳转一个页面  -2:表示向后跳转两个页面 |

```javascript
history.length;
history.back();
history.forward();
history.go(-2);
```

## Location

如果直接打印location，则可以获取到地址栏的信息（当前页面的完整路径）。

```javascript

console.log(location);

/*
Location {replace: ƒ, assign: ƒ, href: "https://www.youtube.com/", ancestorOrigins: DOMStringList, origin: "https://www.youtube.com", …}
ancestorOrigins: DOMStringList {length: 0}
assign: ƒ ()
hash: ""
host: "www.youtube.com"
hostname: "www.youtube.com"
href: "https://www.youtube.com/"
origin: "https://www.youtube.com"
pathname: "/"
port: ""
protocol: "https:"
reload: ƒ reload()
replace: ƒ ()
search: ""
toString: ƒ toString()
valueOf: ƒ valueOf()
Symbol(Symbol.toPrimitive): undefined
__proto__: Location
*/
```

如果直接将location属性修改为一个完整的路径，或相对路径，页面会自动跳转到该路径，并且会生成相应的历史

记录。

```javascript
location = "http://www.baidu.com";
```



| 方法    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| assign  | 用来跳转到其他的页面，作用和直接修改location一样。           |
| reload  | 用于重新加载当前页面，作用和刷新按钮一样。如果在方法中传递一个true，作为参数，则会强制清空缓存刷新页面。 |
| replace | 可以使用一个新的页面替换当前页面，调用完毕也会跳转页面。会生成历史记录，不能使用回退按钮回退。 |

```javascript
location.assign("http://www.baidu.com");
location.reload(true);
location.replace("http://www.zhihu.com");
```

## 定时器简介

```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>定时器简介</title>
		<script type="text/javascript">
			
			window.onload = function(){
				
				//获取count
				var count = document.getElementById("count");
				
				//使count中的内容，自动切换
				/*
				 * JS的程序的执行速度是非常非常快的
				 * 如果希望一段程序，可以每间隔一段时间执行一次，可以使用定时调用
				 */
				/*for(var i=0 ; i<10000 ; i++){
					count.innerHTML = i;
					
					alert("hello");
				}*/
				
				/*
				 * setInterval()
				 * 	- 定时调用
				 * 	- 可以将一个函数，每隔一段时间执行一次
				 * 	- 参数：
				 * 		1.回调函数，该函数会每隔一段时间被调用一次
				 * 		2.每次调用间隔的时间，单位是毫秒
				 * 
				 * 	- 返回值：
				 * 		返回一个Number类型的数据
				 * 		这个数字用来作为定时器的唯一标识
				 */
				var num = 1;
				
				var timer = setInterval(function(){
					
					count.innerHTML = num++;
					
					if(num == 10000){
						//关闭定时器
						clearInterval(timer);
					}
					
				},1000);
				
				//console.log(timer);
				
				//clearInterval()可以用来关闭一个定时器
				//方法中需要一个定时器的标识作为参数，这样将关闭标识对应的定时器
				//clearInterval(timer);
				
			};
			
			
		</script>
	</head>
	<body>
		<h1 id="count"></h1>
	</body>
</html>
```

## 切换图片练习

```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>切换图片练习</title>
		<script type="text/javascript">
			
			window.onload = function(){
				
				/*
				 * 使图片可以自动切换
				 */
				
				//获取img标签
				var img1 = document.getElementById("img1");
				
				//创建一个数组来保存图片的路径
				var imgArr = ["img/1.jpg","img/2.jpg","img/3.jpg","img/4.jpg","img/5.jpg"];
				
				//创建一个变量，用来保存当前图片的索引
				var index = 0;
				
				//定义一个变量，用来保存定时器的标识
				var timer;
				
				//为btn01绑定一个单击响应函数
				var btn01 = document.getElementById("btn01");
				btn01.onclick = function(){
					
					/*
					 * 目前，我们每点击一次按钮，就会开启一个定时器，
					 * 点击多次就会开启多个定时器，这就导致图片的切换速度过快，
					 * 并且我们只能关闭最后一次开启的定时器
					 */
					
					//在开启定时器之前，需要将当前元素上的其他定时器关闭
					clearInterval(timer);
					
					/*
					 * 开启一个定时器，来自动切换图片
					 */
					timer = setInterval(function(){
						//使索引自增
						index++;
						//判断索引是否超过最大索引
						/*if(index >= imgArr.length){
							//则将index设置为0
							index = 0;
						}*/
						index %= imgArr.length;
						//修改img1的src属性
						img1.src = imgArr[index];
						
					},1000);
				};
				
				//为btn02绑定一个单击响应函数
				var btn02 = document.getElementById("btn02");
				btn02.onclick = function(){
					//点击按钮以后，停止图片的自动切换，关闭定时器
					/*
					 * clearInterval()可以接收任意参数，
					 * 如果参数是一个有效的定时器的标识，则停止对应的定时器
					 * 如果参数不是一个有效的标识，则什么也不做
					 */
					clearInterval(timer);
					
				};
				
				
			};
			
		</script>
	</head>
	<body>
		
		<img id="img1" src="img/1.jpg"/>
		<br /><br />
		<button id="btn01">开始</button>
		<button id="btn02">停止</button>
	</body>
</html>
```

## 移动DIV练习

```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>移动DIV练习</title>
		<style type="text/css">
			#box1{
				width: 100px;
				height: 100px;
				background-color: red;
				position: absolute;
			}
			
			
		</style>
		
		<script type="text/javascript">
			
			//使div可以根据不同的方向键向不同的方向移动
			/*
			 * 按左键，div向左移
			 * 按右键，div向右移
			 */
			window.onload = function(){
				
					
				//定义一个变量，来表示移动的速度
				var speed = 10;
				
				//创建一个变量表示方向
				//通过修改dir来影响移动的方向
				var dir = 0;
				
				//开启一个定时器，来控制div的移动
				setInterval(function(){
					/*
					 * 37 左
					 * 38 上
					 * 39 右
					 * 40 下
					 */
					switch(dir){
						case 37:
							//alert("向左"); left值减小
							box1.style.left = box1.offsetLeft - speed + "px";
							break;
						case 39:
							//alert("向右");
							box1.style.left = box1.offsetLeft + speed + "px";
							break;
						case 38:
							//alert("向上");
							box1.style.top = box1.offsetTop - speed + "px";
							break;
						case 40:
							//alert("向下");
							box1.style.top = box1.offsetTop + speed + "px";
							break;
					}
				},30);
				
				
				
				//为document绑定一个按键按下的事件
				document.onkeydown = function(event){
					event = event || window.event;
					
					//当用户按了ctrl以后，速度加快
					if(event.ctrlKey){
						speed = 500;
					}else{
						speed = 10;
					}
					
					//使dir等于按键的值
					dir = event.keyCode;
				};
				
				//当按键松开时，div不再移动
				document.onkeyup = function(){
					//设置方向为0
					dir = 0;
				};
				
			};
			
			
		</script>
	</head>
	<body>
		<div id="box1"></div>
	</body>
</html>
```

## 延时调用

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>延时调用</title>
    <script type="text/javascript">

        var num = 1;

        //开启一个定时器
        /*setInterval(function(){
            console.log(num++);
        },3000);*/


        /*
         * 延时调用，
         * 延时调用一个函数不马上执行，而是隔一段时间以后在执行，而且只会执行一次
         * 
         * 延时调用和定时调用的区别，定时调用会执行多次，而延时调用只会执行一次
         * 
         * 延时调用和定时调用实际上是可以互相代替的，在开发中可以根据自己需要去选择
         */
        var timer = setTimeout(function () {
            console.log(++num);
        }, 3000);

        //使用clearTimeout()来关闭一个延时调用
        //clearTimeout(timer);

    </script>
</head>
<body>
</body>
</html>
```

## 定时器

tools.js

```javascript
//尝试创建一个可以执行简单动画的函数
/*
 * 参数：
 * 	obj:要执行动画的对象
 * 	attr:要执行动画的样式，比如：left top width height
 * 	target:执行动画的目标位置
 * 	speed:移动的速度(正数向右移动，负数向左移动)
 *  callback:回调函数，这个函数将会在动画执行完毕以后执行
 */

function move(obj, attr, target, speed, callback) {
    //关闭上一个定时器
    clearInterval(obj.timer);

    //获取元素目前的位置
    var current = parseInt(getStyle(obj, attr));

    //判断速度的正负值
    //如果从0 向 800移动，则speed为正
    //如果从800向0移动，则speed为负
    if (current > target) {
        //此时速度应为负值
        speed = -speed;
    }

    //开启一个定时器，用来执行动画效果
    //向执行动画的对象中添加一个timer属性，用来保存它自己的定时器的标识
    obj.timer = setInterval(function () {

        //获取box1的原来的left值
        var oldValue = parseInt(getStyle(obj, attr));

        //在旧值的基础上增加
        var newValue = oldValue + speed;

        //判断newValue是否大于800
        //从800 向 0移动
        //向左移动时，需要判断newValue是否小于target
        //向右移动时，需要判断newValue是否大于target
        if ((speed < 0 && newValue < target) || (speed > 0 && newValue > target)) {
            newValue = target;
        }

        //将新值设置给box1
        obj.style[attr] = newValue + "px";

        //当元素移动到0px时，使其停止执行动画
        if (newValue == target) {
            //达到目标，关闭定时器
            clearInterval(obj.timer);
            //动画执行完毕，调用回调函数
            callback && callback();
        }

    }, 30);
}

/*
 * 定义一个函数，用来获取指定元素的当前的样式
 * 参数：
 * 		obj 要获取样式的元素
 * 		name 要获取的样式名
 */
function getStyle(obj, name) {

    if (window.getComputedStyle) {
        //正常浏览器的方式，具有getComputedStyle()方法
        return getComputedStyle(obj, null)[name];
    } else {
        //IE8的方式，没有getComputedStyle()方法
        return obj.currentStyle[name];
    }

}
```

html

```html
<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<title>定时器</title>
		<style type="text/css">
			
			*{
				margin: 0;
				padding: 0;
			}
			
			#box1{
				width: 100px;
				height: 100px;
				background-color: red;
				position: absolute;
				left: 0;
			}
			
			#box2{
				width: 100px;
				height: 100px;
				background-color: yellow;
				position: absolute;
				left: 0;
				top: 200px;
			}
			
		</style>
		<script type="text/javascript" src="js/tools.js"></script>
		<script type="text/javascript">
			
			window.onload = function(){
				
				//获取box1
				var box1 = document.getElementById("box1");
				//获取btn01
				var btn01 = document.getElementById("btn01");
				
				//获取btn02
				var btn02 = document.getElementById("btn02");
				
				
				//点击按钮以后，使box1向右移动（left值增大）
				btn01.onclick = function(){
					move(box1 ,"left", 800 , 20);
				};
				
				
				//点击按钮以后，使box1向左移动（left值减小）
				btn02.onclick = function(){
					move(box1 ,"left", 0 , 10);
				};
				
				
				//获取btn03
				var btn03 = document.getElementById("btn03");
				btn03.onclick = function(){
					move(box2 , "left",800 , 10);
				};
				
				//测试按钮
				var btn04 = document.getElementById("btn04");
				btn04.onclick = function(){
					//move(box2 ,"width", 800 , 10);
					//move(box2 ,"top", 800 , 10);
					//move(box2 ,"height", 800 , 10);
					move(box2 , "width" , 800 , 10 , function(){
						move(box2 , "height" , 400 , 10 , function(){
							move(box2 , "top" , 0 , 10 , function(){
								move(box2 , "width" , 100 , 10 , function(){
							
								});
							});
						});
					});
				};
			};
			
			//定义一个变量，用来保存定时器的标识
			/*
			 * 目前我们的定时器的标识由全局变量timer保存，
			 * 	所有的执行正在执行的定时器都在这个变量中保存
			 */
			//var timer;
			
			
			
			
		</script>
	</head>
	<body>
		
		<button id="btn01">点击按钮以后box1向右移动</button>
		<button id="btn02">点击按钮以后box1向左移动</button>
		<button id="btn03">点击按钮以后box2向右移动</button>
		<button id="btn04">测试按钮</button>
		
		<br /><br />
		
		<div id="box1"></div>
		<div id="box2"></div>
		
		<div style="width: 0; height: 1000px; border-left:1px black solid; position: absolute; left: 800px;top:0;"></div>
		
	</body>
</html>
```

## 轮播图

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>轮播图</title>

    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        /*
         * 设置outer的样式
         */
        #outer {
            /*设置宽和高*/
            width: 520px;
            height: 333px;
            /*居中*/
            margin: 50px auto;
            /*设置背景颜色*/
            background-color: bisque;
            /*设置padding*/
            padding: 10px 0;
            /*开启相对定位*/
            position: relative;
            /*裁剪溢出的内容*/
            overflow: hidden;
        }

        /*设置imgList*/
        #imgList {
            /*去除项目符号*/
            list-style: none;
            /*设置ul的宽度*/
            /*width: 2600px;*/
            /*开启绝对定位*/
            position: absolute;
            /*设置偏移量*/
            /*
             * 每向左移动520px，就会显示到下一张图片
             */
            left: 0;
        }

        /*设置图片中的li*/
        #imgList li {
            /*设置浮动*/
            float: left;
            /*设置左右外边距*/
            margin: 0 10px;
        }

        /*设置导航按钮*/
        #navDiv {
            /*开启绝对定位*/
            position: absolute;
            /*设置位置*/
            bottom: 15px;
            /*设置left值
                 outer宽度  520
                 navDiv宽度 25*5 = 125
                     520 - 125 = 395/2 = 197.5
             * */
            /*left: 197px;*/
        }

        #navDiv a {
            /*设置超链接浮动*/
            float: left;
            /*设置超链接的宽和高*/
            width: 15px;
            height: 15px;
            /*设置背景颜色*/
            background-color: red;
            /*设置左右外边距*/
            margin: 0 5px;
            /*设置透明*/
            opacity: 0.5;
            /*兼容IE8透明*/
            filter: alpha(opacity=50);
        }

        /*设置鼠标移入的效果*/
        #navDiv a:hover {
            background-color: black;
        }
    </style>

    <!--引用工具-->
    <script type="text/javascript" src="js/tools.js"></script>
    <script type="text/javascript">
        window.onload = function () {
            //获取imgList
            var imgList = document.getElementById("imgList");
            //获取页面中所有的img标签
            var imgArr = document.getElementsByTagName("img");
            //设置imgList的宽度
            imgList.style.width = 520 * imgArr.length + "px";


            /*设置导航按钮居中*/
            //获取navDiv
            var navDiv = document.getElementById("navDiv");
            //获取outer
            var outer = document.getElementById("outer");
            //设置navDiv的left值
            navDiv.style.left = (outer.offsetWidth - navDiv.offsetWidth) / 2 + "px";


            //默认显示图片的索引
            var index = 0;
            //获取所有的a
            var allA = document.getElementsByTagName("a");
            //设置默认选中的效果
            allA[index].style.backgroundColor = "black";

            /*
                 点击超链接切换到指定的图片
                 点击第一个超链接，显示第一个图片
                 点击第二个超链接，显示第二个图片
             */

            //为所有的超链接都绑定单击响应函数
            for (var i = 0; i < allA.length; i++) {

                //为每一个超链接都添加一个num属性
                allA[i].num = i;

                //为超链接绑定单击响应函数
                allA[i].onclick = function () {

                    //关闭自动切换的定时器
                    clearInterval(timer);
                    //获取点击超链接的索引,并将其设置为index
                    index = this.num;

                    //切换图片
                    /*
                     * 第一张  0 0
                     * 第二张  1 -520
                     * 第三张  2 -1040
                     */
                    //imgList.style.left = -520*index + "px";
                    
                    //设置选中的a
                    setA();

                    //使用move函数来切换图片
                    move(imgList, "left", -520 * index, 20, function () {
                        //动画执行完毕，开启自动切换
                        autoChange();
                    });

                };
            }


            //开启自动切换图片
            autoChange();


            //创建一个方法用来设置选中的a
            function setA() {

                //判断当前索引是否是最后一张图片
                if (index >= imgArr.length - 1) {
                    //则将index设置为0
                    index = 0;
				  
                    //此时显示的最后一张图片，而最后一张图片和第一张一摸一样
                    // 亮的是第一个按钮
                    //通过CSS将最后一张切换成第一张
                    imgList.style.left = 0;
                }

                //遍历所有a，并将它们的背景颜色设置为红色
                for (var i = 0; i < allA.length; i++) {
                    allA[i].style.backgroundColor = "";
                }

                //将选中的a设置为黑色
                allA[index].style.backgroundColor = "black";
            }

            //定义一个自动切换的定时器的标识
            var timer;

            //创建一个函数，用来开启自动切换图片
            function autoChange() {

                //开启一个定时器，用来定时去切换图片
                timer = setInterval(function () {

                    //使索引自增
                    index++;

                    //判断index的值
                    index %= imgArr.length;

                    //执行动画，切换图片
                    move(imgList, "left", -520 * index, 20, function () {
                        //修改导航按钮
                        setA();
                    });

                }, 3000);

            }


        };

    </script>
</head>
<body>
<!-- 创建一个外部的div，来作为大的容器 -->
<div id="outer">
    <!-- 创建一个ul，用于放置图片 -->
    <ul id="imgList">
        <li><img src="img/1.jpg"/></li>
        <li><img src="img/2.jpg"/></li>
        <li><img src="img/3.jpg"/></li>
        <li><img src="img/4.jpg"/></li>
        <li><img src="img/5.jpg"/></li>
        <li><img src="img/1.jpg"/></li>
    </ul>
    <!--创建导航按钮-->
    <div id="navDiv">
        <a href="javascript:;"></a>
        <a href="javascript:;"></a>
        <a href="javascript:;"></a>
        <a href="javascript:;"></a>
        <a href="javascript:;"></a>
    </div>
</div>
</body>
</html>
```

## 类的操作

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>类的操作</title>
    <style type="text/css">

        .b1 {
            width: 100px;
            height: 100px;
            background-color: red;
        }

        .b2 {
            height: 300px;
            background-color: yellow;
        }

    </style>

    <script type="text/javascript">

        window.onload = function () {
            //获取box
            var box = document.getElementById("box");
            //获取btn01
            var btn01 = document.getElementById("btn01");

            //为btn01绑定单击响应函数
            btn01.onclick = function () {
                //修改box的样式
                /*
                 * 通过style属性来修改元素的样式，每修改一个样式，浏览器就需要重新渲染一次页面
                 * 这样的执行的性能是比较差的，而且这种形式当我们要修改多个样式时，也不太方便
                 */

                //box.style.width = "200px";
                //box.style.height = "200px";
                //box.style.backgroundColor = "yellow";

                /*
                 * 我希望一行代码，可以同时修改多个样式
                 */

                //修改box的class属性
                /*
                 * 我们可以通过修改元素的class属性来间接的修改样式
                 * 这样一来，我们只需要修改一次，即可同时修改多个样式，
                 * 浏览器只需要重新渲染页面一次，性能比较好，
                 * 并且这种方式，可以使表现和行为进一步的分离
                 */
                //box.className += " b2";
                //addClass(box,"b2");

                //alert(hasClass(box,"hello"));

                //removeClass(box,"b2");

                toggleClass(box, "b2");
            };

        };

        //定义一个函数，用来向一个元素中添加指定的class属性值
        /*
         * 参数:
         * 	obj 要添加class属性的元素
         *  cn 要添加的class值
         *
         */
        function addClass(obj, cn) {

            //检查obj中是否含有cn
            //没有才添加
            if (!hasClass(obj, cn)) {
                obj.className += " " + cn;
            }

        }

        /*
         * 判断一个元素中是否含有指定的class属性值
         * 如果有该class，则返回true，没有则返回false
         *
         */
        function hasClass(obj, cn) {

            //判断obj中有没有cn class
            //创建一个正则表达式
            //var reg = /\bb2\b/;
            var reg = new RegExp("\\b" + cn + "\\b");

            return reg.test(obj.className);

        }

        /*
         * 删除一个元素中的指定的class属性
         */
        function removeClass(obj, cn) {
            //创建一个正则表达式
            var reg = new RegExp("\\b" + cn + "\\b");

            //删除class
            obj.className = obj.className.replace(reg, "");

        }

        /*
         * toggleClass可以用来切换一个类
         * 如果元素中具有该类，则删除
         * 如果元素中没有该类，则添加
         */
        function toggleClass(obj, cn) {

            //判断obj中是否含有cn
            if (hasClass(obj, cn)) {
                //有，则删除
                removeClass(obj, cn);
            } else {
                //没有，则添加
                addClass(obj, cn);
            }

        }

    </script>
</head>
<body>

<button id="btn01">点击按钮以后修改box的样式</button>

<br/><br/>

<div id="box" class="b1 b2"></div>
</body>
</html>
```

## 二级菜单

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <title>二级菜单</title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
            list-style-type: none;
        }

        a, img {
            border: 0;
            text-decoration: none;
        }

        body {
            font: 12px/180% Arial, Helvetica, sans-serif, "新宋体";
        }
    </style>

    <link rel="stylesheet" type="text/css" href="css/sdmenu.css"/>

    <script type="text/javascript" src="js/tools.js"></script>
    <script type="text/javascript">
        window.onload = function () {

            /*
             * 我们的每一个菜单都是一个div
             * 当div具有collapsed这个类时，div就是折叠的状态
             * 当div没有这个类时，div就是展开的状态
             */

            /*
             * 点击菜单，切换菜单的显示状态
             */
            //获取所有的class为menuSpan的元素
            var menuSpan = document.querySelectorAll(".menuSpan");

            //定义一个变量，来保存当前打开的菜单
            var openDiv = menuSpan[0].parentNode;

            //为span绑定单击响应函数
            for (var i = 0; i < menuSpan.length; i++) {
                menuSpan[i].onclick = function () {

                    //this代表我当前点击的span
                    //获取当前span的父元素
                    var parentDiv = this.parentNode;

                    //切换菜单的显示状态
                    toggleMenu(parentDiv);


                    //判断openDiv和parentDiv是否相同
                    //不相同，且openDiv没有折叠，关闭它 即添加collapsed类
                    if (openDiv != parentDiv && !hasClass(openDiv, "collapsed")) {
                        //打开菜单以后，应该关闭之前打开的菜单
                        //为了可以统一处理动画过渡效果，我们希望在这将addClass改为toggleClass
                        //addClass(openDiv , "collapsed");
                        //此处toggleClass()不需要有移除的功能
                        //toggleClass(openDiv , "collapsed");
                        //切换菜单的显示状态
                        toggleMenu(openDiv);
                    }

                    //修改openDiv为当前打开的菜单
                    openDiv = parentDiv;

                };
            }

            /*
             * 用来切换菜单折叠和显示状态
             */
            function toggleMenu(obj) {
                //在切换类之前，获取元素的高度
                var begin = obj.offsetHeight;

                //切换parentDiv的显示
                toggleClass(obj, "collapsed");

                //在切换类之后获取一个高度
                var end = obj.offsetHeight;
				
                //动画效果就是将高度从begin向end过渡
                //将元素的高度重置为begin
                obj.style.height = begin + "px";

                //执行动画，从bengin向end过渡
                move(obj, "height", end, 10, function () {
                    //动画执行完毕，删除掉内联样式
                    obj.style.height = "";
                });

            }


        };


    </script>
    <script src="js/json2.js"></script>

</head>

<body>

<div id="my_menu" class="sdmenu">
    <div>
        <span class="menuSpan">在线工具</span>
        <a href="#">图像优化</a>
        <a href="#">收藏夹图标生成器</a>
        <a href="#">邮件</a>
        <a href="#">htaccess密码</a>
        <a href="#">梯度图像</a>
        <a href="#">按钮生成器</a>
    </div>
    <div class="collapsed">
        <span class="menuSpan">支持我们</span>
        <a href="#">推荐我们</a>
        <a href="#">链接我们</a>
        <a href="#">网络资源</a>
    </div>
    <div class="collapsed">
        <span class="menuSpan">合作伙伴</span>
        <a href="#">JavaScript工具包</a>
        <a href="#">CSS驱动</a>
        <a href="#">CodingForums</a>
        <a href="#">CSS例子</a>
    </div>
    <div class="collapsed">
        <span class="menuSpan">测试电流</span>
        <a href="#">Current or not</a>
        <a href="#">Current or not</a>
        <a href="#">Current or not</a>
        <a href="#">Current or not</a>
    </div>
</div>
</body>
</html>
```

## JSON

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>JSON</title>

    <!--
        如果需要兼容IE7及以下的JSON操作，则可以通过引入一个外部的js文件来处理
    -->
    <script type="text/javascript" src="js/json2.js"></script>
    <script type="text/javascript">

        /*
         * JSON
         * 	- JS中的对象只有JS自己认识，其他的语言都不认识
         * 	- JSON就是一个特殊格式的字符串，这个字符串可以被任意的语言所识别，
         * 	  并且可以转换为任意语言中的对象，JSON在开发中主要用来数据的交互
         * 	- JSON
         * 		- JavaScript Object Notation JS对象表示法
         * 		- JSON和JS对象的格式一样，只不过JSON字符串中的属性名必须加双引号
         * 		  其他的和JS语法一致
         *
         * 		JSON分类：
         * 			1.对象 {}
         * 			2.数组 []
         * 
         * 		JSON中允许的值：
         * 			1.字符串
         * 			2.数值
         * 			3.布尔值
         * 			4.null
         * 			5.对象
         * 			6.数组
         */

        //创建一个对象


        var arr = '[1,2,3,"hello",true]';

        var obj2 = '{"arr":[1,2,3]}';

	   var arr2 = '[{"name":"孙悟空","age":18,"gender":"男"},' +
    			 '{"name":"孙悟空","age":18,"gender":"男"}]';

        /*
         * 将JSON字符串转换为JS中的对象
         * 在JS中，为我们提供了一个工具类，就叫JSON
         * 这个对象可以帮助我们将一个JSON转换为JS对象，也可以将一个JS对象转换为JSON
         */

        var json = '{"name":"孙悟空","age":18,"gender":"男"}';

        /*
         * json --> js对象
         * 	 JSON.parse()
         * 		- 可以将以JSON字符串转换为js对象
         * 		- 它需要一个JSON字符串作为参数，会将该字符串转换为JS对象并返回
         */

        var o = JSON.parse(json);
        var o2 = JSON.parse(arr);

        //console.log(o.gender);
        //console.log(o2[1]);

        var obj3 = {name: "猪八戒", age: 28, gender: "男"};


        /*
         * JS对象 ---> JSON
         * 	JSON.stringify()
         * 		- 可以将一个JS对象转换为JSON字符串
         * 		- 需要一个js对象作为参数，会返回一个JSON字符串
         */

        var str = JSON.stringify(obj3);
        //console.log(str);

        /*
         * JSON这个对象在IE7及以下的浏览器中不支持，所以在这些浏览器中调用时会报错
         */


    </script>
</head>
<body>
</body>
</html>
```

## eval



```javascript
var str = '{"name":"孙悟空","age":18,"gender":"男"}';

/*
* eval()
* 	- 这个函数可以用来执行一段字符串形式的JS代码，并将执行结果返回
* 	- 如果使用eval()执行的字符串中含有{},它会将{}当成是代码块
* 	  如果不希望将其当成代码块解析，则需要在字符串前后各加一个()
* 
* 	- eval()这个函数的功能很强大，可以直接执行一个字符串中的js代码，
* 	  但是在开发中尽量不要使用，首先它的执行性能比较差，然后它还具有安全隐患
*/

var str2 = "alert('hello');";
eval(str2);

var obj = eval("(" + str + ")");

//console.log(obj);

```

快捷键

```
F12，Ctrl+Shift+P，
```

```javascript
document.body.contentEditable = true;
```

正则表达式坑

```javascript
// 坑1 (正则表达式中间一定不可以有空格)
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("xiaoqiang"));
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("1xiaoqiang"));

// 坑2
// test()不传值相当于传了一个undefined进去
// 然后test()就把这个undefined当成是"undefined"来判断
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("undefined"));
console.log(/^[0-9a-zA-Z][a-zA-Z0-9_]{5,11}$/.test());
console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test(undefined));
console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test("undefined"));

// 坑3
// 当正则表达式使用了全局模式(g)的时候,并且你还让它去检测一个字符串,此时会引出来一个lastIndex
// lastIndex会记住上一次匹配成功的位置,并把下一次要开始椒盐的位置记住
//
console.log("===============================");
var r = /alex/g;
console.log(r.test("alex"));  // true
console.log(r.lastIndex);  // 4
console.log(r.test("alex"));  // false
console.log(r.lastIndex);
console.log(r.test("alex"));  // true
console.log(r.lastIndex);
console.log(r.test("alex"));  // false
```

JS对象

```javascript
//在JS的对象中,键(属性)默认不用加引号;并且自动把单引号转成双引号
var person = {name: '小强', age: 38}; 
console.log(person);
// 单独取对象的属性
console.log("name:", person.name);
console.log("age:", person.age);

// 遍历对象的属性
for (var i in person){
    console.log(i);
    console.log(person[i]);
}
```

class相关操作

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>class相关操作</title>
    <style>
        .c1 {
            height: 200px;
            width: 200px;
            border-radius: 50%;
            background-color: grey;
        }
        .c2 {
            background-color: yellow;
        }
    </style>
</head>
<body>

<div class="c1 c2 c3" onclick="change(this);">div</div>
<div class="c1 c2 c3">div</div>
<div class="c1 c2 c3">div</div>
<div class="c1 c2 c3">div</div>

<script>
    function change(ths) {
        ths.classList.toggle("c2");
    }

//    第二种绑定事件的方式
    var divEles = document.getElementsByTagName("div");
    for (var i=0;i<divEles.length;i++){
        divEles[i].onclick=function () {
            this.classList.toggle("c2");
        }
    }
</script>
</body>
</html>
```

定时器练习

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>定时器练习</title>
</head>
<body>
<input id="i1" type="text">
<input id="start" type="button" value="开始">
<input id="stop" type="button" value="停止">
<script>

    // 声明一个全局的t,保存定时器的ID
    var t;
    // 在input框里显示当前时间
    // 1. 获取当前时间
    function foo() {
        var now = new Date();
        var nowStr = now.toLocaleString();
        // 2. 把时间字符串填到input框里
        var i1Ele = document.getElementById("i1");
        i1Ele.value = nowStr;
    }


    // 点开始让时间动起来
    // 找到开始按钮,给它绑定事件
    var startButton = document.getElementById("start");
    startButton.onclick=function () {
        foo();
        // 每隔一秒钟执行foo
        if (t===undefined){
            t = setInterval(foo, 1000);  // 把定时器的ID复制给之前声明的全局变量t
        }
    };
    // 点停止
    // 找到停止按钮,给它绑定事件
    var stopButton = document.getElementById("stop");
    stopButton.onclick=function () {
        // 清除之前设置的定时器
        clearInterval(t);  // 清除t对应的那个定时器,t的值还在
        console.log(t);
        t = undefined;
    }

</script>
</body>
</html>
```

搜索框示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>搜索框示例</title>
</head>
<body>

<input type="text" id="i1" value="对子哈特">
<input type="button" value="搜索">

<script>
    // 找到input框
    var i1Ele = document.getElementById("i1");
    i1Ele.onfocus=function () {
        // 把value清空
        this.value="";
    };
    i1Ele.onblur=function () {
        // 失去焦点之后把如果值为空就填回去
        if (!this.value.trim()){
            this.value="对子哈特";
        }
    }
</script>


</body>
</html>
```

select联动示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>select联动示例</title>
</head>
<body>

<select id="s1">
    <option value="0">--请选择--</option>
    <option value="1">北京</option>
    <option value="2">上海</option>
</select>

<select id="s2"></select>

<script>

    var data = {1: ["昌平区", "朝阳区", "海淀区"], 2: ["静安区", "闵行区", "浦东区"]};
    // 给第一个select绑定事件,绑定的是onchange事件
    var s1Ele = document.getElementById("s1");
    s1Ele.onchange = function () {
        // 取到你选的是哪一个市
        console.log(this.value);
        // 把对应市的区填到第二个select框里面
        var areas = data[this.value];  // 取到市对应的区
        // 找到s2
        var s2Ele = document.getElementById("s2");
        // 清空之前的
        s2Ele.innerHTML="";
        // 生成option标签
        for (var i = 0; i < areas.length; i++) {
            var opEle = document.createElement("option");
            opEle.innerText = areas[i];
            // 添加到select内部
            s2Ele.appendChild(opEle);
        }
    }
</script>
</body>
</html>
```

```
2. 使用classList操作样式
1. .classList.contains("样式类")  --> 判断包不包含指定的样式类
2. .classList.add("样式类")       --> 添加指定的样式类
4. .classList.toggle("样式类")    --> 有就删除没有就添加
```

```
2. 常用的事件
1. onclick        当用户点击某个对象时调用的事件句柄。
2. ondblclick     当用户双击某个对象时调用的事件句柄。

3. onfocus        元素获得焦点。   // 练习：搜索框
4. onblur         元素失去焦点。   应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了
				
5. onchange       域的内容被改变。 (select联动示例)
			
```

面试题

```python
"""
问:执行完下面的代码后,  l,m的内容分别是什么?
"""


def func(m):
    for k, v in m.items():
        m[k + 2] = v + 2


m = {1: 2, 3: 4}
m_c = m  # 浅拷贝
from copy import deepcopy

m_cc = deepcopy(m)
m_c[9] = 10
m_cc[90] = 100
# func(m_c)
m[7] = 8

# 1. 在Python中遍历字典的时候能不能对字典本身做涉及键(key)的操作
# 2. 深浅拷贝的理解

print("l:", m_c)
print("l2:", m_cc)
print("m:", m)
```

