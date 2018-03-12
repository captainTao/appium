
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
refer to :
虫师, 教程：
http://www.testclass.net/appium/

乙醇, 原理: 
http://www.testclass.net/appium/about_appium/

查看package name, content-description
http://www.testclass.net/appium/tools/

查看app activity
http://www.testclass.net/appium/get_activity/


1.要看一个apk文件的相关信息最简单实用的方法是：
aapt dump badging [yourapp.apk]

2.如果只是想查看手机上应用的packageName：
adb shell pm list packages

3.获取APP包名
adb logcat | grep START

然后启动对应的应用：
cmp=包名/线程名
cmp=photo.studio.editor.selfie.camera/us.pinguo.icecream.homepage.HomePageActivity

'''


from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()




'''
Desired Capabilities:

Desired Capabilities 在启动 session 的时候是必须提供的。

Desired Capabilities 本质上是以 key value 字典的方式存放，客户端将这些键值对发给服务端，告诉服务端我们想要怎么测试。它告诉 appium Server这样一些事情：

本次测试是启动浏览器还是启动移动设备。

是启动Andorid还是启动iOS。

启动Android时，app的package是什么。

启动Android时，app的activity是什么。

…

Desired Capabilities 配置
Appium 的 Desired Capabilities 基本配置如下：


'''

DesiredCapabilities capabilities = new DesiredCapabilities();
capabilities.setCapability("deviceName", "Android Emulator");
capabilities.setCapability("automationName", "Appium");
capabilities.setCapability("platformName", "Android");
capabilities.setCapability("platformVersion", "5.1");
capabilities.setCapability("appPackage", "com.android.calculator2");
capabilities.setCapability("appActivity", ".Calculator");

WebDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

'''
deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator，iPad Simulator，iPhone Retina 4-inch，Android Emulator，Galaxy S4…

automationName：使用哪种自动化引擎。appium（默认）还是Selendroid。

platformName：使用哪种移动平台。iOS, Android, orFirefoxOS。

platformVersion：指定平台的系统版本。例如指的Android平台，版本为5.1。

appActivity：待测试的app的Activity名字。比如MainActivity、.Settings。注意，原生app的话要在activity前加个”.“。

appPackage：待测试的app的Java package。比如com.example.android.myApp, com.android.settings。

app：应用的绝对路径，注意一定是绝对路径。如果指定了appPackage和appActivity的话，这个属性是可以不设置的。另外这个属性和browserName属性是冲突的。

browserName：移动浏览器的名称。比如Safari’ for iOS and ‘Chrome’, ‘Chromium’, or ‘Browser’ for Android；与app属性互斥。

udid：物理机的id。比如1ae203187fc012g。

更多参数配置参考：

https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
'''





'''

id 定位:

appium 通过 uiautomatorviewer.bat 工具来查看控件的属性。该工具位于 Android SDK 的 /tools/bin/ 目录下。

通过uiautomatorviewer.bat 工具可以查看对象的id属性。

如果目标设备的API Level低于18则UIAutomatorViewer不能获得对应的Resource ID，只有等于大于18的时候才能使用。

打开uiautomatorviewer.bat工具：


'''


# name定位：

driver.findElement(By.name("9"))



# class name 定位：

WebElement button = driver.findElement(By.className("android.widget.Button"));
# // 使用 Class Name 一般获得的 view 都不止一个，所以应该需要遍历一遍得到的 views，然后缩小搜索条件来获得目标控件



# XPath定位:

# 用class的属性来替代做标签的名字。
driver.findElement(By.xpath("//android.view.ViewGroup/android.widget.Button"))  //7

# 当如果出现class 相同的情况下可以用控件的属性值进行区分。

driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click(); //7
driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'times')]")).click(); //*
driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click();  //7
driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'equals')]")).click(); //=




# Accessibility ID定位:

# 这个方法属于Appium扩展的定位方法。
# 核心是要找到元素的contentDescription属性。它就是元素的 content-desc 

driver.findElementByAccessibilityId("plus").click();




# android uiautomator定位:

# 这个方法也属于 Appium（Android）扩展的定位方法。同样使用 UIAutomatorViewer.bat 工具直接查看。
# 也就是说一个元素的任意属性都可以通过android uiautomator方法来进行定位，但要保证这种定位方式的唯一性。

driver.findElementByAndroidUIAutomator("new UiSelector().text(\"clr\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"8\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().description(\"plus\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"5\")").click();
driver.findElementByAndroidUIAutomator("new UiSelector().description(\"equals\")").click();

# // 需要注意的是 description() 方法用的是content-desc属性。



#---------------------------appium API 之应用操作---------------------------#


# 安装app：

driver.installApp("path/to/my.apk");
driver.installApp("D:\\android\\apk\\ContactManager.apk");



# 卸载：
driver.removeApp("com.example.android.apis");



# 关闭：
closeApp()

# 这个方法并非真正的关闭应用，相当于按home键将应用置于后台，可以通过launchApp()再次启动。



# 关闭，启动
driver.closeApp();
driver.launchApp();



# 是否安装：
# 返回结果为Ture或False
driver.isAppInstalled('com.example.android.apis');



# 置于后台：
driver.runAppInBackground(2); #括号数字为时长



# 重置应用：
driver.resetApp();




#---------------------------aappium API 之上下文操作---------------------------#


# 获取当前所有的可用的上下文：
# getContext()

String ct = driver.getContext();
System.out.println(ct);

-----------计算器应用的打印结果-----------------------
NATIVE_APP



# 当前所有上下文句柄
getContextHandles()



# 切换上下文
# context()
# 切换到特定的上下文中。需要指定上下文的名称。

driver.context('NATIVE_APP')
driver.context('WEBVIEW_1')




#---------------------------appium API 之键盘操作---------------------------#


# sendKeys()：
driver.findElements(By.name("Name")).sendKeys("jack");



# pressKeyCode():
# appium扩展提供了pressKeyCode()方法。该方法Android特有。
driver.pressKeyCode(29); // 字母“a”,发送一个键码的操作
driver.pressKeyCode(AndroidKeyCode.HOME);  // Android的HOME键


'''
下面提供Android keycode参考表：

#-------------------------------------电话键:

KEYCODE_CALL 拨号键 5

KEYCODE_ENDCALL 挂机键 6

KEYCODE_HOME 按键Home 3

KEYCODE_MENU 菜单键 82

KEYCODE_BACK 返回键 4

KEYCODE_SEARCH 搜索键 84

KEYCODE_CAMERA 拍照键 27

KEYCODE_FOCUS 拍照对焦键 80

KEYCODE_POWER 电源键 26

KEYCODE_NOTIFICATION 通知键 83

KEYCODE_MUTE 话筒静音键 91

KEYCODE_VOLUME_MUTE 扬声器静音键 164

KEYCODE_VOLUME_UP 音量增加键 24

KEYCODE_VOLUME_DOWN 音量减小键 25

#-------------------------------------控制键:

KEYCODE_ENTER 回车键 66

KEYCODE_ESCAPE ESC键 111

KEYCODE_DPAD_CENTER 导航键 确定键 23

KEYCODE_DPAD_UP 导航键 向上 19

KEYCODE_DPAD_DOWN 导航键 向下 20

KEYCODE_DPAD_LEFT 导航键 向左 21

KEYCODE_DPAD_RIGHT 导航键 向右 22

KEYCODE_MOVE_HOME 光标移动到开始键 122

KEYCODE_MOVE_END 光标移动到末尾键 123

KEYCODE_PAGE_UP 向上翻页键 92

KEYCODE_PAGE_DOWN 向下翻页键 93

KEYCODE_DEL 退格键 67

KEYCODE_FORWARD_DEL 删除键 112

KEYCODE_INSERT 插入键 124

KEYCODE_TAB Tab键 61

KEYCODE_NUM_LOCK 小键盘锁 143

KEYCODE_CAPS_LOCK 大写锁定键 115

KEYCODE_BREAK Break/Pause键 121

KEYCODE_SCROLL_LOCK 滚动锁定键 116

KEYCODE_ZOOM_IN 放大键 168

KEYCODE_ZOOM_OUT 缩小键 169

#-------------------------------------组合键:

KEYCODE_ALT_LEFT Alt+Left

KEYCODE_ALT_RIGHT Alt+Right

KEYCODE_CTRL_LEFT Control+Left

KEYCODE_CTRL_RIGHT Control+Right

KEYCODE_SHIFT_LEFT Shift+Left

KEYCODE_SHIFT_RIGHT Shift+Right

#-------------------------------------基本:

KEYCODE_0 按键’0’ 7

KEYCODE_1 按键’1’ 8

KEYCODE_2 按键’2’ 9

KEYCODE_3 按键’3’ 10

KEYCODE_4 按键’4’ 11

KEYCODE_5 按键’5’ 12

KEYCODE_6 按键’6’ 13

KEYCODE_7 按键’7’ 14

KEYCODE_8 按键’8’ 15

KEYCODE_9 按键’9’ 16

KEYCODE_A 按键’A’ 29

KEYCODE_B 按键’B’ 30

KEYCODE_C 按键’C’ 31

KEYCODE_D 按键’D’ 32

KEYCODE_E 按键’E’ 33

KEYCODE_F 按键’F’ 34

KEYCODE_G 按键’G’ 35

KEYCODE_H 按键’H’ 36

KEYCODE_I 按键’I’ 37

KEYCODE_J 按键’J’ 38

KEYCODE_K 按键’K’ 39

KEYCODE_L 按键’L’ 40

KEYCODE_M 按键’M’ 41

KEYCODE_N 按键’N’ 42

KEYCODE_O 按键’O’ 43

KEYCODE_P 按键’P’ 44

KEYCODE_Q 按键’Q’ 45

KEYCODE_R 按键’R’ 46

KEYCODE_S 按键’S’ 47

KEYCODE_T 按键’T’ 48

KEYCODE_U 按键’U’ 49

KEYCODE_V 按键’V’ 50

KEYCODE_W 按键’W’ 51

KEYCODE_X 按键’X’ 52

KEYCODE_Y 按键’Y’ 53

KEYCODE_Z 按键’Z’ 54

'''


#---------------------------appium API 之 TouchAction 操作---------------------------#


# Appium的辅助类，主要针对手势操作，比如滑动、长按、拖动等。



# 1.按压控件:
# press(WebElement el, int x, int y)
# 开始按压一个元素或坐标点（x,y）。通过手指按压手机屏幕的某个位置。

TouchAction(driver).press(x=0,y=308).release().perform()

# release() 结束的行动取消屏幕上的指针。
# Perform() 执行的操作发送到服务器的命令操作。



# 2.长按控件:

longPress(WebElement el, int x, int y, Duration duration)
# duration以毫秒为单位。1000表示按一秒钟。其用法与press()方法相同。duration:按压时间，单位毫秒

TouchAction action = new TouchAction(driver);
action.longPress(names.get(1),1000).perform().release();
action.longPress(1 ,302,1000).perform().release();



# 3.点击控件：
tap(WebElement el, int x, int y)
# 用法参考press()

TouchAction action = new TouchAction(driver);
action.tap(names.get(1)).perform().release();
action.tap(1 ,302).perform().release();



# 4.移动:moveTo()
# 将指针（光标）从过去指向指定的元素或点。

movTo(WebElement el, int x, int y)

# 其用法参考press()方法。


TouchAction action = new TouchAction(driver);
action.moveTo(names.get(1)).perform().release();
action.moveTo(1 ,302).perform().release();



# 5.暂停
# 暂停脚本的执行，单位为毫秒。
action.wait(1000);



#---------------------------appium API 之其他操作---------------------------#

# 1、熄屏
.lockDevice()
# 在iOS设备可以设置熄屏一段时间。Android上面不带参数，所以熄屏之后就不会再点亮屏幕了。
driver.lockDevice(1000);  // iOS，可以带参数
driver.lockDriice();   //Android, 不带参数



# 2、当前Activity（Android only）
# 得到当前应用的activity。只适用于Android。 例（通讯录）：
currentActivity()

String ca = driver.currentActivity();
System.out.print(ca);
-------------输出结果为-------------
.activities.PeopleActivity




# 3、收起键盘
hideKeyboard()
# 收起键盘，这个方法很有用，当我们对一个输入框输入完成后，需要将键盘收起，再切换到一下输入框进行输入

driver.hideKeyboard();  //收起键盘



# 4、滑动

# 模拟用户滑动。将控件或元素从一个位置（x,y）拖动到另一个位置（x,y）。
swipe(int startx, int starty, int endx, int endy, int duration) 
# * start_x：开始滑动的x坐标。 * start_y：开始滑动的y坐标。 * end_x：结束滑动的x坐标。 * end_y：结束滑动的y坐标。
# * duration：持续时间。




# 5、拉出文件

pullFile()
# 从设备中拉出文件。
driver.pullFile('Library/AddressBook/AddressBook.sqlitedb')

# anr问题的log一般都在/data/anr/目录下，使用如下命令即可导出log
# adb pull /data/anr/traces.txt   d:/     =》意思是将手机上的traces.txt导出到电脑的d目录下


# adb pull <remote> <local>    Copies a specified file from an emulator/device instance to your development computer.    
# adb push <local> <remote>    Copies a specified file from your development computer to an emulator/device instance.  




# 6、推送文件

pushFile()
# 推送文件到设备中去。

pushFile(String remotePath, byte[] base64Data)


String content = "some data for the file";
byte[] data = Base64.encodeBase64(content.getBytes());
driver.pushFile("sdcard/test.txt", data);






#---------------------------appium client方法一览---------------------------#
'''
refer: 
http://www.testclass.net/appium/about_appium/

appium的技术架构
iOS: Apple’s UIAutomation
Android 4.2+: Google’s UiAutomator
Android 2.3+: Google’s Instrumentation. (Instrumentation support is provided by bundling a separate project, Selendroid)


appium client扩展了原生的webdriver client方法

下面以java代码为例，简单过一下appium client提供的适合移动端使用的新方法

refer: 
http://www.testclass.net/appium/methods/

'''


resetApp()
getAppString()
sendKeyEvent()
currentActivity()
pullFile()
pushFile()
pullFolder()
hideKeyboard()
runAppInBackground()
performTouchAction()
performMultiTouchAction()
tap()
swipe()
pinch()
zoom()
getNamedTextField()
isAppInstalled()
installApp()
removeApp()
launchApp()
closeApp()
endTestCoverage()
lockScreen()
shake()
complexFind()
scrollTo()
scrollToExact()
openNotifications()
Context Switching: .context(), .getContextHandles(), getContext()


新增的locator

findElementByAccessibilityId()
findElementsByAccessibilityId()
findElementByIosUIAutomation()
findElementsByIosUIAutomation()
findElementByAndroidUIAutomator()
findElementsByAndroidUIAutomator()


这些方法主要覆盖了3大类：

driver扩展：比如增加了resetApp等操作app的方法
action扩展：增加一些移动端的特有的action（怎么描述呢，相当于是移动端 特有的操作），比如swipe，shake(嗯，有了这个方法就可以让代码帮你摇一摇了)等；
locator扩展：增加了一些移动端专属的定位策略

