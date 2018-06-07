
import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import NetworkPage
class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        self.network_page.click_2g()

    def test_mobile_network_3g(self):
        self.network_page.click_3g()

    def teardown(self):
        self.driver.quit()










# self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()



# self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
#         self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
