from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

test_time = 10
start_time = time.time()

driver = webdriver.Chrome()
try:

    for i in range(test_time):
        # 访问 GitHub 
        driver.get("https://github.com")
        time.sleep(4)
        # 搜索功能测试
        driver.find_element(By.CSS_SELECTOR, ".mr-2 > .octicon").click()
        driver.find_element(By.ID, "query-builder-test").send_keys("testing")
        time.sleep(8)
        driver.find_element(By.ID, "query-builder-test").send_keys(Keys.RETURN)
        time.sleep(8)

        # 验证搜索成功
        assert "testing" in driver.title
        print("搜索成功")

        # 清空搜索框
        driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search or jump to…']").send_keys("testing")
        time.sleep(4)

finally:
    driver.quit()

print("平均测试时间： %s s" % (time.time() - start_time)/test_time)

