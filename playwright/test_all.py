from playwright.sync_api import sync_playwright
import time

# 从终端中获取用户名和密码
username = input("Enter your GitHub username: ")
password = input("Enter your GitHub password: ")

start_time = time.time()    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 访问 GitHub 登录页
    page.goto("https://github.com/login")

    # 输入用户名和密码
    page.fill("#login_field", username)
    page.fill("#password", password)
    page.click("[name='commit']")

    # 验证登录成功
    page.wait_for_timeout(2000)
    assert "GitHub" in page.title()
    print("登录成功")

    # 搜索功能测试
    page.fill("input[name='q']", "testing")
    page.press("input[name='q']", "Enter")
    page.wait_for_timeout(2000)

    # 验证搜索成功
    assert "testing" in page.title()
    print("搜索成功")

    # 表单提交 创建仓库
    page.goto("https://github.com/new")
    page.fill("input[name='repository[name]']", "test-playwright-repo")
    page.fill("input[name='repository[description]']", "This is a test repository")
    page.click("button[type='submit']")
    page.wait_for_timeout(2000)

    # 验证仓库创建成功
    page.goto("https://github.com/"+username+"/test-playwright-repo")
    page.wait_for_timeout(2000)
    assert "test-playwright-repo" in page.title()
    print("仓库创建成功")
    browser.close()

print("测试时间： %s s" % (time.time() - start_time))