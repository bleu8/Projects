from selenium import webdriver

import time
class Instagram():
    def tar_ac(self):
        
        driver=webdriver.Firefox()
        return driver
        
    def giris(self,us,passs,browser):
        url="https://instagram.com"
        browser.get(url)
        time.sleep(1)
        uss=browser.find_element_by_name("username")
        pasw=browser.find_element_by_name("password")
        uss.send_keys(us)
        pasw.send_keys(passs)
        login=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        login.click()
        

 
    def foll():
        url="https://www.instagram.com/crashjj62478/"
        browser.get(url)
        tkpc=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        tkpc.click()
        time.sleep(2)
        
        takip=browser.find_element_by_css_selector("div[role=dialog] ul").find_elemens_by_css_selector("li")
        time.sleep(2)
        
        for ki in takip:
            link=find_elements_by_css_selector("a").getattribute("href")
            print(link)
    
    