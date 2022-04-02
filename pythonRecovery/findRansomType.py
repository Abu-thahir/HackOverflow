from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import warnings

warnings.filterwarnings("ignore")

PATH = r"C:\Program Files\chromedriver.exe"

options = Options()
options.headless = True

options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(PATH, options=options)


def findRansomName(path):
    driver.get("https://id-ransomware.malwarehunterteam.com")
    search = driver.find_element_by_name("ransomnote_upload")
    search.send_keys(path)

    search = driver.find_element_by_id("upload_button")
    search.click()

    elements = driver.find_elements_by_xpath("//*[@class='panel-title']")

    # print("done")
    # driver.quit()
    return elements[0].text


# print(findRansomName(
#     r"C:\Users\daadreyaa\Desktop\HackOverFlow\pythonRecovery\ransom.micro.txt"))

print(findRansomName(r"C:\Users\daadreyaa\Desktop\HackOverFlow\pythonRecovery\sample.txt"))
