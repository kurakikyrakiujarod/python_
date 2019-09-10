import uiautomator2 as u2

d = u2.connect('127.0.0.1:62001')
elem = d.xpath('@cn.com.askparents.parentchart:id/head_img').get()
elem.screenshot().save('s.jpg')
