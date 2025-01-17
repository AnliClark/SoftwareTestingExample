from playwright.sync_api import sync_playwright
import time

test_time = 10
start_time = time.time()    
with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()

    for i in range(test_time):
        # 访问 GitHub
        page.goto("https://github.com")
        page.wait_for_timeout(4000)
        # 搜索功能测试
        page.get_by_label("Search or jump to…").click()
        page.get_by_role("combobox", name="Search").fill("testing")
        page.wait_for_timeout(8000)
        page.get_by_role("combobox", name="Search").press("Enter")
        page.wait_for_timeout(8000)

        # 验证搜索成功
        assert "testing" in page.title()
        print("搜索成功")

        # 清空搜索框
        page.get_by_role("combobox", name="Search").fill("")
        page.wait_for_timeout(4000)

    browser.close()

print("测试时间： %s s" % (time.time() - start_time)/test_time)