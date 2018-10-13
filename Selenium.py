from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path=r"c:\webdrivers\chromedriver.exe")
driver.get('https://web.whatsapp.com/')
name=input('Enter the name of the user(s) or group(s):').split(',')
msg=input('Enter the message:')
count=input('Enter the count:').split()
n_c={}
if len(name)==len(count):
    for i in zip(name,count):
        n_c[i[0]]=i[1]
input('ENTER AFTER SCANNING QR CODE')
for key in n_c.keys():
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(key))
    user.click()
    text_box=driver.find_element_by_class_name('_2S1VP')
    button = driver.find_element_by_class_name('weEq5')
    for i in range(int(n_c[key])):
        text_box.send_keys(msg)
        send=button.find_element_by_xpath('//button[@class="_35EW6"]')
        send.click()
driver.implicitly_wait(60)
driver.close()
