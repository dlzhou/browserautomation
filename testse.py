# -*- coding: gb2312 -*-  
  
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException  
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0  
import time  
  
i = 0  
while i <= 10000:

    # Create a new instance of the Firefox driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-plugins")  
    driver = webdriver.Chrome(chrome_options=chrome_options)  
  
    # go to the google home page  
    driver.get("http://ent.sina.com.cn/v/m/2013-01-03/05183825681.shtml")  
  
    # find the element that's name attribute is q (the google search box)  
    inputElements = driver.find_elements_by_class_name("comment_ding_link")

    inputElement = None

    for inputEle in inputElements:
        act = inputEle.get_attribute("action-data")
        if act == "mid=50E4D189-76D4C1DB-0-821-92C":
            inputElement = inputEle
            break  
  
    # type in the search  
    #inputElement.send_keys("Cheese!")
    Wait = True
    while inputElement and Wait:
        try: 
            # submit the form. (although google automatically searches now without submitting)
            Wait = False  
            inputElement.click()
            print inputElement.text        
        except WebDriverException, excpt:
            print excpt
            msg = str(excpt)
            if msg.find("not clickable") != -1:
                time.sleep(10)
                Wait = True      
    
    i += 1
    print i
    driver.quit()
    time.sleep(30)
#try:  
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title  
    #WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))  
  
    # You should see "cheese! - Google Search"  
    #print driver.title  
  
#finally:  
    #driver.quit()  