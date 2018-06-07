import os, sys
sys.path.append(os.getcwd())
from base.base_action import BaseAction
from selenium.webdriver.common.by import By

class DisplayPage(BaseAction):
    display_button = By.XPATH,"//*[contains(@text,'显示')]"
    search_button = By.ID,"com.android.settings:id/search"
    input_button = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.driver = driver

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element(By.ID,"com.android.settings:id/search").click()
        # self.driver.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_text(self,text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("text")
        # self.driver.fidnd_element(By.ID,"android:id/search_src_text").send_keys(text)
        # self.driver.find_element(self.input_button).send_keys(text)
        self.input(self.input_button,text)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element_by(By.CLASS_NAME,"android.widget.ImageButton").click()
        # self.driver.find_element(self.back_button).click()
        self.click(self.back_button)


