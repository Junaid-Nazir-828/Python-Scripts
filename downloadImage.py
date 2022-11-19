import requests
from selenium.webdriver import Chrome

def download(imgurl,filename):

    driver = Chrome()
    # imgurl = 'https://instagram.fisb5-1.fna.fbcdn.net/v/t51.2885-15/315927217_842885536855202_2341585826765014712_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.fisb5-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=EARblI5M_8gAX90Jy_2&edm=AFoqvFcBAAAA&ccb=7-5&ig_cache_key=Mjk3MzU0OTk2MTk5NjIyMzUxMg%3D%3D.2-ccb7-5&oh=00_AfCjCwpFjqn0GqjmTOG3KFDYc3AKa_Jt-p5O8Ozmo88z7A&oe=637CD56A&_nc_sid=c3f888'
    # filename = 'folder//abcd'

    headers = {
    "User-Agent":
        "Chrome/107.0.5304.107"
    }
    s = requests.session()
    s.headers.update(headers)

    for cookie in driver.get_cookies():
        c = {cookie['name']: cookie['value']}
        s.cookies.update(c)

    r = s.get(imgurl, allow_redirects=True)
    open(filename + '.jpeg', 'wb').write(r.content)