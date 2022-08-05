from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


s=Service('driver\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.implicitly_wait(100)
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
driver.find_element(By.NAME,"firstname").send_keys("Istiak Hassan")
driver.find_element(By.NAME,"lastname").send_keys("Emon")
driver.find_element(By.NAME,"reg_email__").send_keys("emon@nexisltd.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("emon@nexisltd.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("sde54g!24324@@#@#$")
day=Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
day.select_by_visible_text("8")
month=Select(driver.find_element(By.NAME,'birthday_month'))
month.select_by_visible_text("Oct")
year=Select(driver.find_element(By.NAME,'birthday_year'))
year.select_by_visible_text("1992")
driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()