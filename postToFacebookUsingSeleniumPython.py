import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re


class PostToFacebook(webdriver.Chrome):
    def __init__(self, driver_path=r";C:/SeleniumDriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(PostToFacebook, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def login(self, fb_mail, fb_pass):
        url = 'https://www.facebook.com/'
        self.get(url)

        email = self.find_element(By.ID, 'email')
        email.send_keys(fb_mail)

        password = self.find_element(By.ID, 'pass')
        password.send_keys(fb_pass)

        login = self.find_element(By.NAME, 'login')
        login.click()

    def openFacebookGroup(self, group_id):
        new_url = f'https://www.facebook.com/groups/{group_id}'

        self.execute_script("window.open('');")

        self.switch_to.window(self.window_handles[1])
        self.get(new_url)

    def sendPost(self, post_text):
        write_something = self.find_element(By.CSS_SELECTOR, "span[class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1']")
        write_something.click()

        create_post = self.find_element(By.CSS_SELECTOR, "div[class='_1mf _1mj']")
        create_post.send_keys(post_text)

        soup = BeautifulSoup(self.page_source, 'html.parser')
        all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
        id_ = str(all_pc[0].get('id'))
        xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div'
        post = self.find_element(By.XPATH, xpath)
        post.click()


if __name__ == '__main__':
    inst = PostToFacebook()
    inst.login('YOUR_EMAIL','YOUR_PASSWORD')
    inst.openFacebookGroup('GROUP_ID_WHERE_YOU_WANT_TO_POST')
    inst.sendPost('TEXT_YOU_WANT_TO_POST')