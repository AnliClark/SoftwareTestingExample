from playwright.sync_api import sync_playwright
import time

test_time = 10
start_time = time.time()    
with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()

    for i in range(test_time):
        # 访问百度
        page.goto("https://www.baidu.com")
        page.wait_for_timeout(1000)
        # 搜索功能测试
        page.locator("#kw").click()
        page.locator("#kw").fill("testing")
        page.wait_for_timeout(2000)
        page.locator("#kw").press("Enter")
        page.wait_for_timeout(1000)

        # 验证搜索成功
        assert "testing" in page.title()
        print("搜索成功")

        page.wait_for_timeout(2000)

    browser.close()
    print("测试时间： %s s" % ((time.time() - start_time)/test_time))