# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
# from appium import TouchAction
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformVersion"] = "10.3.2"
caps["platformName"] = "iOS"
caps["deviceName"] = "PG-0130"
caps["automationName"] = "XCUITest"
caps["bundleId"] = "com.vstudio.camera360"
caps["udid"] = "b1c8e924eb629f79a34ca4a3b2b638ec70cdb7c0"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# TouchAction action = new TouchAction(driver)
TouchAction(driver).tap(x=70, y=514).perform()
TouchAction(driver).tap(x=235, y=543).perform()
TouchAction(driver).tap(x=79, y=112).perform()
TouchAction(driver).tap(x=38, y=136).perform()
TouchAction(driver).tap(x=158, y=538).perform()
TouchAction(driver).tap(x=37, y=509).perform()
TouchAction(driver).tap(x=167, y=458).perform()
TouchAction(driver).tap(x=289, y=546).perform()
TouchAction(driver).tap(x=286, y=18).perform()

driver.quit()