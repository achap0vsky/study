from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
  x = x_element.text
  print(x)
  y = calc(x)
  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)
  button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
  button1.click()
finally:
    time.sleep(5)
    browser.quit()