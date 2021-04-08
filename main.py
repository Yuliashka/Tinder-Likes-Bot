
# THE TINDER PAGE: https://tinder.com/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrom_driver_path = "C:\Development\chromedriver.exe"


# SHOWING A PATH TO OUR DRIVER:
driver = webdriver.Chrome(executable_path=chrom_driver_path)

# GETTING FORM PAGE:
driver.get("https://tinder.com/")

time.sleep(4)
# ENTER:
enter_button = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
enter_button.click()

time.sleep(5)
# ENTER WITH FACEBOOK:
facebook_enter_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_enter_button.click()

# OUR BASE WINDOW:
base_window = driver.window_handles[0]

# TO SWITCH TO FB NEW WINDOW:
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# LOGIN FORM:
mail = driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys("your facebook mail")

time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('your facebook password')

time.sleep(3)
button = driver.find_element_by_name('login')
button.click()

time.sleep(5)
# TURNING BACK TO BASE WINDOW:
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
# PERMISSION BUTTON:
allow_location_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[1]')
time.sleep(5)
allow_location_button.click()

time.sleep(5)
# CANCEL BUTTON:
cancel_notification_button = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[2]')
cancel_notification_button.click()

time.sleep(5)
# COOKIES:
cookies = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[2]/div/div/div[1]/button')
time.sleep(5)
cookies.click()

# PLACE:
time.sleep(5)
place = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/button')
time.sleep(5)
place.click()

# CLICKING PEOPLE:
time.sleep(5)

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):
    # Add a 1 second delay between likes.
    time.sleep(3)

    try:
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        time.sleep(5)
        like_button.click()

    # Sometimes, as you are swiping, you'll get a match which is a pop-up on the same page.
    # But this will mean that your Like button will be hidden behind the pop up and you'll
    # get a ElementClickInterceptedException. e.g.

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 3 seconds before retrying.
        except NoSuchElementException:
            time.sleep(3)

driver.quit()