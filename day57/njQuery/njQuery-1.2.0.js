(function (window, undefined) {
    var njQuery = function (selector) {
        return new njQuery.prototype.init(selector);
    };
    njQuery.prototype = {
        constructor: njQuery,
        init: function (selector) {
            /*
            1.传入 '' null undefined NaN  0  false, 返回空的jQuery对象
            2.字符串:
           代码片段:会将创建好的DOM元素存储到jQuery对象中返回
           选择器: 会将找到的所有元素存储到jQuery对象中返回
           3.数组:
           会将数组中存储的元素依次存储到jQuery对象中立返回
           4.除上述类型以外的:
           会将传入的数据存储到jQuery对象中返回
          */
            // 0.去除字符串两端的空格
            selector = njQuery.trim(selector);
            // 1.传入 '' null undefined NaN  0  false, 返回空的jQuery对象
            if (!selector) {
                return this;
            }
            // 方法处理
            else if (njQuery.isFunction(selector)) {
                // console.log("是方法");
                njQuery.ready(selector);
            }
            // 2.字符串:
            else if (njQuery.isString(selector)) {
                // 2.1判断是否是代码片段
                // console.log("字符串");
                // 代码片段:会将创建好的DOM元素存储到jQuery对象中返回
                if (njQuery.isHTML(selector)) {
                    // console.log("DOM元素");
                    // 1.根据代码片段创建所有的元素
                    var temp = document.createElement("div");
                    temp.innerHTML = selector;
                    // console.log(temp);
                    // console.log(temp.children);
                    // 2.将创建好的一级元素添加到jQuery当中
                    // for (var i = 0; i < temp.children.length; i++) {
                    //     this[i] = temp.children[i];
                    // }
                    // // 3.给jQuery对象添加length属性
                    // this.length = temp.children.length;
                    // console.log(temp.children);
                    [].push.apply(this, temp.children);
                    // 此时此刻的this是njQuery对象
                    // 4.返回加工好的this(jQuery)
                    // return this;
                }
                // 2.2判断是否是选择器
                else {
                    // 1.根据传入的选择器找到对应的元素
                    var res = document.querySelectorAll(selector);
                    // for (var i = 0; i < res.length; i++) {
                    //     this[i] = res[i];
                    // }
                    // // 3.给jQuery对象添加length属性
                    // this.length = res.length;
                    [].push.apply(this, res);
                    // 3.返回加工好的this
                    return this;
                }

            }
            // else if (typeof selector === "object"
            //     && "length" in selector && selector !== window)
            else if (njQuery.isArray(selector)) {
                /*
                // console.log("是数组");
                // 3.1真数组
                if(({}).toString.apply(selector) === "[object Array]") {
                    // console.log("真数组");
                    [].push.apply(this, selector);
                    return this;
                }
                else {
                    // console.log("伪数组");
                    // 将自定义的伪数组转换为真数组
                    var arr = [].slice.call(selector);
                    // 将真数组转换为伪数组
                    [].push.apply(this, arr);
                    return this;
                }
                */
                // 将自定义的伪数组转换为真数组
                var arr = [].slice.call(selector);
                // 将真数组转换为伪数组
                [].push.apply(this, arr);
                // return this;
            }
            // 除上述类型以外
            else {
                this[0] = selector;
                this.length = 1;
                // return this;
            }
            return this;
        },
        jquery: "1.1.0",
        selector: "",
        length: 0,
        // [].push找到数组的push方法
        // 冒号前面的push将来由njQuery对象调用
        // 相当于 [].push.apply(this);
        push: [].push,
        sort: [].sort,
        splice: [].splice,
        toArray: function () {
            return [].slice.call(this);
        },
        get: function (num) {
            // 没有传递参数
            if (arguments.length === 0) {
                return this.toArray();
            }
            // 传递不是负数
            else if (num >= 0) {
                return this[num];
            }
            // 传递负数
            else {
                return this[this.length + num];
            }
        },
        eq: function (num) {
            // 没有传递参数
            if (arguments.length === 0) {
                return new njQuery();
            } else {
                return njQuery(this.get(num));
            }
        },
        first: function () {
            return this.eq(0);
        },
        last: function () {
            return this.eq(-1);
        },
        each: function (fn) {
            return njQuery.each(this, fn);
        }
    };
    njQuery.extend = njQuery.prototype.extend = function (obj) {
        for (var key in obj) {
            this[key] = obj[key];
        }
    };
    njQuery.extend({
        isString: function (str) {
            return typeof str === "string"
        },
        isHTML: function (str) {
            return str.charAt(0) == "<" &&
                str.charAt(str.length - 1) == ">" &&
                str.length >= 3
        },
        trim: function (str) {
            if (!njQuery.isString(str)) {
                return str;
            }
            // 判断是否支持trim方法
            if (str.trim) {
                return str.trim();
            } else {
                return str.replace(/^\s+|\s+$/g, "");
            }
        },
        isObject: function (sele) {
            return typeof sele === "object"
        },
        isWindow: function (sele) {
            return sele === window;
        },
        isArray: function (sele) {
            if (njQuery.isObject(sele) &&
                !njQuery.isWindow(sele) &&
                "length" in sele) {
                return true;
            }
            return false;
        },
        isFunction: function (sele) {
            return typeof sele === "function";
        },
        ready: function (fn) {
            // 判断DOM是否加载完毕
            if (document.readyState == "complete") {
                fn();
            } else if (document.addEventListener) {
                document.addEventListener("DOMContentLoaded", function () {
                    fn();
                });
            } else {
                document.attachEvent("onreadystatechange", function () {
                    if (document.readyState == "complete") {
                        fn();
                    }
                });
            }
        },
        each: function (obj, fn) {
            // 1.判断是否是数组
            if (njQuery.isArray(obj)) {
                for (var i = 0; i < obj.length; i++) {
                    // var res = fn(i, obj[i]);
                    var res = fn.call(obj[i], i, obj[i]);
                    if (res === true) {
                        continue;
                    } else if (res === false) {
                        break;
                    }
                }
            }
            // 2.判断是否是对象
            else if (njQuery.isObject(obj)) {
                for (var key in obj) {
                    // var res = fn(key, obj[key]);
                    var res = fn.call(obj[key], key, obj[key]);
                    if (res === true) {
                        continue;
                    } else if (res === false) {
                        break;
                    }
                }
            }
            return obj;
        },
        map: function (obj, fn) {
            var res = [];
            // 1.判断是否是数组
            if (njQuery.isArray(obj)) {
                for (var i = 0; i < obj.length; i++) {
                    var temp = fn(obj[i], i);
                    if (temp) {
                        res.push(temp);
                    }
                }
            }
            // 2.判断是否是对象
            else if (njQuery.isObject(obj)) {
                for (var key in obj) {
                    var temp = fn(obj[key], key);
                    if (temp) {
                        res.push(temp);
                    }
                }
            }
            return res;
        }
    });
    // DOM操作相关方法
    njQuery.prototype.extend({
        empty: function () {
            // 1.遍历指定的元素
            this.each(function (key, value) {
                value.innerHTML = "";
            });
            // 2.方便链式编程
            return this;
        },
        remove: function (sele) {
            if (arguments.length === 0) {
                // 1.遍历指定的元素
                this.each(function (key, value) {
                    // 根据遍历到的元素找到对应的父元素
                    var parent = value.parentNode;
                    // 通过父元素删除指定的元素
                    parent.removeChild(value);
                });
            } else {
                var $this = this;
                // 1.根据传入的选择器找到对应的元素
                $(sele).each(function (key, value) {
                    // 2.遍历找到的元素, 获取对应的类型
                    var type = value.tagName;
                    // 3.遍历指定的元素
                    $this.each(function (k, v) {
                        // 4.获取指定元素的类型
                        var t = v.tagName;
                        // 5.判断找到元素的类型和指定元素的类型
                        if (t === type) {
                            // 根据遍历到的元素找到对应的父元素
                            var parent = value.parentNode;
                            // 通过父元素删除指定的元素
                            parent.removeChild(value);
                        }
                    });
                })
            }
            return this;
        },
        html: function (content) {
            if (arguments.length === 0) {
                return this[0].innerHTML;
            } else {
                this.each(function (key, value) {
                    value.innerHTML = content;
                })
            }
        },
        text: function (content) {
            if (arguments.length === 0) {
                var res = "";
                this.each(function (key, value) {
                    res += value.innerText;
                });
                return res;
            } else {
                this.each(function (key, value) {
                    value.innerText = content;
                });
            }
        },
        appendTo: function (sele) {
            // 1.统一的将传入的数据转换为jQuery对象
            var $target = $(sele);
            var $this = this;
            var res = [];
            // 2.遍历取出所有指定的元素
            $.each($target, function (key, value) {
                // 2.遍历取出所有的元素
                $this.each(function (k, v) {
                    // 3.判断当前是否是第0个指定的元素
                    if (key === 0) {
                        // 直接添加
                        value.appendChild(v);
                        res.push(v);
                    } else {
                        // 先拷贝再添加
                        var temp = v.cloneNode(true);
                        value.appendChild(temp);
                        res.push(temp);
                    }
                });
            });
            // 3.返回所有添加的元素
            return $(res);
        },
        prependTo: function (sele) {
            // 1.统一的将传入的数据转换为jQuery对象
            var $target = $(sele);
            var $this = this;
            var res = [];
            // 2.遍历取出所有指定的元素
            $.each($target, function (key, value) {
                // 2.遍历取出所有的元素
                $this.each(function (k, v) {
                    // 3.判断当前是否是第0个指定的元素
                    if (key === 0) {
                        // 直接添加
                        value.insertBefore(v, value.firstChild);
                        res.push(v);
                    } else {
                        // 先拷贝再添加
                        var temp = v.cloneNode(true);
                        value.insertBefore(temp, value.firstChild);
                        res.push(temp);
                    }
                });
            });
            // 3.返回所有添加的元素
            return $(res);
        },
        append: function (sele) {
            // 判断传入的参数是否是字符串
            if (njQuery.isString(sele)) {
                this.each(function (index, value) {
                    value.innerHTML += sele;
                })
            } else {
                $(sele).appendTo(this);
            }
            return this;
        },
        prepend: function (sele) {
            // 判断传入的参数是否是字符串
            if (njQuery.isString(sele)) {
                this.each(function (index, value) {
                    value.innerHTML = sele + value.innerHTML;
                });
            } else {
                $(sele).prependTo(this);
            }
            return this;
        },
        insertBefore: function (sele) {
            // 1.统一的将传入的数据转换为jQuery对象
            var $target = $(sele);
            var $this = this;
            var res = [];
            // 2.遍历取出所有指定的元素
            $.each($target, function (key, value) {
                var parent = value.parentNode;
                // 2.遍历取出所有的元素
                $this.each(function (k, v) {
                    // 3.判断当前是否是第0个指定的元素
                    if (key === 0) {
                        // 直接添加
                        parent.insertBefore(v, value);
                        res.push(v);
                    } else {
                        // 先拷贝再添加
                        var temp = v.cloneNode(true);
                        parent.insertBefore(temp, value);
                        res.push(temp);
                    }
                });
            });
            // 3.返回所有添加的元素
            return $(res);
        },
        replaceAll: function (sele) {
            // 1.统一的将传入的数据转换为jQuery对象
            var $target = $(sele);
            var $this = this;
            var res = [];
            // 2.遍历取出所有指定的元素
            $.each($target, function (key, value) {
                var parent = value.parentNode;
                // 2.遍历取出所有的元素
                $this.each(function (k, v) {
                    // 3.判断当前是否是第0个指定的元素
                    if (key === 0) {
                        // 1.将元素插入到指定元素的前面
                        $(v).insertBefore(value);
                        // 2.将指定元素删除
                        $(value).remove();
                        res.push(v);
                    }
                    else {
                        // 先拷贝再添加
                        var temp = v.cloneNode(true);
                        // 1.将元素插入到指定元素的前面
                        $(temp).insertBefore(value);
                        // 2.将指定元素删除
                        $(value).remove();
                        res.push(temp);
                    }
                });
            });
            // 3.返回所有添加的元素
            return $(res);
        }


    });


    njQuery.prototype.init.prototype = njQuery.prototype;
    window.njQuery = window.$ = njQuery;
})(window);
