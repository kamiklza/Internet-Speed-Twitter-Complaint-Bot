from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException, NoSuchElementException, ElementNotInteractableException

import time
desktop_driver_path = "C:/Users/user/PycharmProjects/chromedriver.exe"
dl_speed = None
ul_speed = None

class InternetSpeedTwitterBot:

    def __init__(self, downspeed, upspeed):
        self.driver = webdriver.Chrome(executable_path=desktop_driver_path)
        self.down = downspeed
        self.up = upspeed

    def get_internet_speed(self):
        global dl_speed, ul_speed
        self.driver.get("https://www.speedtest.net/")
        go_tap = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
        go_tap.click()
        time.sleep(60)
        try:
            back_to_result = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            back_to_result.click()
        except ElementNotSelectableException:
            time.sleep(5)
        except ElementNotInteractableException:
            time.sleep(5)
        else:
            down_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            dl_speed = down_speed.text
            print(dl_speed)
            up_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            ul_speed = up_speed.text
            print(ul_speed)



    def tweet_at_provider(self, TWITTER_EMAIL, TWITTER_PASSWORD):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        login_tap = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span')
        login_tap.click()
        time.sleep(3)
        login_with_email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
        login_with_email.click()
        email_input = self.driver.find_element_by_name("session[username_or_email]")
        email_input.send_keys(TWITTER_EMAIL)
        password_input = self.driver.find_element_by_name("session[password]")
        password_input.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_button.click()
        time.sleep(3)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_btn.click()
        time.sleep(2)
        message_box = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div')
        message_box.click()
        time.sleep(1)
        message_box.send_keys(f"Hey Internet Provider, why is my internet speed {dl_speed}down / {ul_speed}up when i pay for 1000down / 1000up? ")
        time.sleep(3)
        tweet_message = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        tweet_message.click()
        time.sleep(5)