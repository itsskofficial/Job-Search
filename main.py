from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By


service=Service(executable_path="D:\Skills\Python\Projects\Google Meet Bot\ChromeDrivers\win32\chromedriver.exe")
driver=webdriver.Chrome(service=service)

#The constants
URL="https://www.linkedin.com/jobs/search?keywords=Web%20Development&location=India&locationId=&geoId=102713980&f_TPR=&f_E=1&f_JT=I&f_WT=2&position=1&pageNum=0"
driver.get(URL)
sleep(3)
signin=driver.find_element_by_link_text('Sign in')
signin.click()
sleep(3)
username=driver.find_element_by_id('username')
username.send_keys('sarthakkarandikar03@gmail.com')
password=driver.find_element_by_id('password')
password.send_keys('Billionairelife@03')
signinbtn=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signinbtn.click()
sleep(10)
allis=driver.find_elements_by_css_selector('.scaffold-layout__list-item')
print(allis)
for li in allis:
    li.click()
    savebtn=driver.find_element_by_css_selector('.artdeco-button--3, .artdeco-button--4')
    savebtn.click()
    sleep(2)
driver.quit()
