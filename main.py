from faker import Faker
from Password_gen import password_gen
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

faker = Faker()
# i=0
# j=int(input("How many fake profiles do you want?\n"))
# while i<=j:
#     print(faker.simple_profile(sex=None))
#     i=i+1
name =faker.name()
FirstName = name.split()[0]
LastName = name.split()[1]
email = faker.email()
password = password_gen()
birth_day = str(random.randint(1,28))
month_list=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec']
birth_month = random.choice(month_list)
birth_year=str(random.randint(1970,2000))
gender_list=['Male','Female']
gender=random.choice(gender_list)

s=Service('driver\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.implicitly_wait(100)
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
driver.find_element(By.NAME,"firstname").send_keys(FirstName)
driver.find_element(By.NAME,"lastname").send_keys(LastName)
driver.find_element(By.NAME,"reg_email__").send_keys(email)
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys(email)
driver.find_element(By.NAME,"reg_passwd__").send_keys(password)
day=Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
day.select_by_visible_text(birth_day)
month=Select(driver.find_element(By.NAME,'birthday_month'))
month.select_by_visible_text(birth_month)
year=Select(driver.find_element(By.NAME,'birthday_year'))
year.select_by_visible_text(birth_year)
driver.find_element(By.XPATH,f"//label[text()='{gender}']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()


