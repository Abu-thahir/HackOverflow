from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings
import sys

warnings.filterwarnings("ignore")

PATH = r"C:\Program Files\chromedriver.exe"

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)


def findRansomKey(ransomName):

    driver.get("https://www.nomoreransom.org/en/decryption-tools.html")
    search = driver.find_element_by_id("ransomSearch")
    search.send_keys(ransomName)


ransomName = sys.argv[1]
findRansomKey(ransomName)
