
import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.display_page import DisplayPage

class TestDisplay:
    def setup(self):
        # 从配置文件里调用具体流程和前置调用这两个函数在可以实现以下的功能
        # base和page相当于公共资源，调用才执行
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_display()
        self.display_page.click_search()
        self.display_page.input_text('hello')
        self.display_page.click_back()

    def teardown(self):
        self.driver.quit()

        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
