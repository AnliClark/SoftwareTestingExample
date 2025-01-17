from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 从终端中获取用户名和密码
username = input("Enter your GitHub username: ")

start_time = time.time()

driver = webdriver.Chrome()
try:
    # 访问 GitHub 
    driver.get("https://github.com")

    for i in range(1):
      # 搜索功能测试
      driver.find_element(By.NAME, "q").send_keys("testing", Keys.RETURN)
      time.sleep(2)

      # 验证搜索成功
      assert "testing" in driver.title
      print("搜索成功")

      # 清空搜索框
      driver.find_element(By.NAME, "q").clear()
      time.sleep(4)

finally:
    driver.quit()

print("测试时间： %s s" % (time.time() - start_time))

