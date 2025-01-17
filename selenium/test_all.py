from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 从终端中获取用户名和密码
username = input("Enter your GitHub username: ")
password = input("Enter your GitHub password: ")

start_time = time.time()

driver = webdriver.Chrome()
try:
    # 访问 GitHub 登录页
    driver.get("https://github.com/login")
    
    # 输入用户名和密码
    driver.find_element(By.ID, "login_field").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()

    # 验证登录成功
    time.sleep(2) 
    assert "GitHub" in driver.title
    print("登录成功")

    # 搜索功能测试
    driver.find_element(By.NAME, "q").send_keys("testing", Keys.RETURN)
    time.sleep(2)

    # 验证搜索成功
    assert "testing" in driver.title
    print("搜索成功")

    # 表单提交 创建仓库
    driver.get("https://github.com/new")
    driver.find_element(By.ID, "repository_name").send_keys("test-selenium-repo")
    driver.find_element(By.CSS_SELECTOR, "button.first-in-line").click()
    time.sleep(2)

    # 验证仓库创建成功
    driver.get("https://github.com/"+username+"/test-selenium-repo")
    time.sleep(2)
    assert "test-selenium-repo" in driver.title
    print("仓库创建成功")
finally:
    driver.quit()

print("测试时间： %s s" % (time.time() - start_time))

