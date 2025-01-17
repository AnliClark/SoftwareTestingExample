from playwright.sync_api import sync_playwright
import time

# 从终端中获取用户名和密码
username = input("Enter your GitHub username: ")

start_time = time.time()    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 访问 GitHub 
    page.goto("https://github.com")

    for i in range(10):
      # 搜索功能测试
      page.fill("input[name='q']", "testing")
      page.press("input[name='q']", "Enter")
      page.wait_for_timeout(2000)

      # 验证搜索成功
      assert "testing" in page.title()
      print("搜索成功")

      # 清空搜索框
      page.fill("input[name='q']", "")
      page.wait_for_timeout(4000)

    browser.close()

print("测试时间： %s s" % (time.time() - start_time))