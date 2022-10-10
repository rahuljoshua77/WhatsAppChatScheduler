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
from datetime import date, datetime
from apscheduler.schedulers.background import BlockingScheduler
import tzlocal
# Creates a default Background Scheduler
sched = BlockingScheduler(timezone=str(tzlocal.get_localzone()))
 
from time import sleep
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
# opts.add_argument("--window-size=500,300")
def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date

def login(data):
    opts.add_argument(r"--user-data-dir=C:\Users\rahul\AppData\Local\Google\Chrome\User Data\Default")
    opts.add_argument(f'--profile-directory=Profile 1')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=opts, desired_capabilities=dc)
    browser.get("https://web.whatsapp.com/")
    try:
        print(f"[+] {date()} Waiting for whatsapp Connected!")
        wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//header[@data-testid="chatlist-header"]')))
        print(f"[+] {date()} Whatsapp Connected!")
        number_list = data
        number_list = open(f"{cwd}/{number_list}","r",encoding='utf-8')
        number_list = number_list.read()
       
        pesan = open(f"{cwd}/pesan.txt","r")
        pesan = pesan.read()
        list_number = number_list.split("\n")
        for  number in list_number:
            print(f"[+] {date()} {number} Checking!")
            browser.get("https://web.whatsapp.com/send?phone=$"+ str(number) + "&text&app_absent=0")
            try:
                time.sleep(5)
                #Phone number shared via url is invalid.
                check = wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//*[@data-testid="msg-notification-container" or @data-testid="popup-controls-ok" or @data-testid="conversation-header"]'))).get_attribute('data-testid')
                if check == "msg-notification-container" or check == "conversation-header":
                    print(f"[+] {date()} {number} Exist, sending your message!")
                    with open('success.txt','a') as f:
                        f.write('{0}\n'.format(number))
                    wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="conversation-compose-box-input"]'))).send_keys(pesan)
                    sleep(2)
                    wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="conversation-compose-box-input"]'))).send_keys(Keys.ENTER)
                else:
                    print(f"[+] {date()} {number} Not Exist!")
                    with open('failed.txt','a') as f:
                        f.write('{0}\n'.format(number))
                sleep(10000)
            except Exception as e:
                try:
                    check = wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="msg-notification-container" or @data-testid="popup-controls-ok"'))).get_attribute('data-testid')
                    if check == "msg-notification-container":
                        print(f"[+] {date()} {number} Exist, sending your message!")
                        with open('success.txt','a') as f:
                            f.write('{0}\n'.format(number))
                        
                    else:
                        print(f"[+] {date()} {number} Not Exist!")
                        with open('failed.txt','a') as f:
                            f.write('{0}\n'.format(number))
                except Exception as e:
                    print(f"[+] {date()} {number} Unkown Error: {e}!")
                    
    except Exception as e:
        print(e)
        print(f"[+] {date()} Whatsapp not connected, Please your phone network or re-login your whatsapp!")
        browser.quit()
        
days = open(f"{cwd}/jadwal.txt","r")
days = days.read()
days = days.split("\n")
for day in days:
    hari = day.split("|")[0]
    data = day.split("|")[1]
    hours = day.split("|")[2].split(":")[0]
    min = day.split("|")[2].split(":")[1]
    print(f"[+] {date()} Waiting for schedule {hari} {hours}:{min}!")
    sched.add_job(login, 'cron', args=[data], day_of_week=day, hour=hours,minute=min)

sched.start()