from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('username')     # usern

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('password')       #pw

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()     # login
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()   # save pass

driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()      # notification
driver.implicitly_wait(5)

profile = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a')
profile.click()

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
last_ht = 1
current_ht = 0

scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
while last_ht != current_ht:
    last_ht = current_ht
    time.sleep(1)
    current_ht = driver.execute_script("""
    arguments[0].scrollTo(0, arguments[0].scrollHeight);
    return arguments[0].scrollHeight;
    """, scroll_box)

followers = [name.text for name in scroll_box.find_elements_by_tag_name('a') if name.text != '']
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
last_ht, current_ht = 1, 0
scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

while last_ht != current_ht:
    last_ht = current_ht
    time.sleep(1)
    current_ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)

following = [name.text for name in scroll_box.find_elements_by_tag_name('a') if name.text != '']
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

print("People who don't follow you back are:")
for name in following:
    if name not in followers:
        print('    ' + name)