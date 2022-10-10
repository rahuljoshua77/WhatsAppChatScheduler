from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random,time,os,re
cwd = os.getcwd()
opts = Options()
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date
def login():
    opts.add_argument(r"--user-data-dir=C:\Users\rahul\AppData\Local\Google\Chrome\User Data\Default")
    opts.add_argument(f'--profile-directory=Profile 1')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=opts, desired_capabilities=dc)
    browser.get("https://web.whatsapp.com/")
    input(f"[+] {date()} PLEASE LOGIN FIRST, AFTER LOGIN, ENTER!")
    print(f"[+] {date()} Run bot.py!")
    browser.close()
login()