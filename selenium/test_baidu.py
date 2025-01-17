from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

test_time = 10
start_time = time.time()

driver = webdriver.Chrome()
try:

    for i in range(test_time):
        # 访问百度
        driver.get("https://www.baidu.com")
        time.sleep(1)
        # 搜索功能测试
        search_box = driver.find_element(By.ID, "kw")
        search_box.send_keys("testing")
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)

        # 验证搜索成功
        assert "testing" in driver.title
        print("搜索成功")

        time.sleep(2)

finally:
    driver.quit()
    print("平均测试时间： %s s" % ((time.time() - start_time) / test_time))



