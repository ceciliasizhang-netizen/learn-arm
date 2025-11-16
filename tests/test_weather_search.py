import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc

@pytest.fixture
def browser():
    # 自动安装 ChromeDriver 并打开浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
    # options = uc.ChromeOptions()
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # # 显式设置为你的 Chrome 主版本号（138）
    # uc.TARGET_VERSION = 138
    # # 启动浏览器
    # driver = uc.Chrome(options=options)

def test_search_weather(browser):
    # 打开 Google 首页
    browser.get("https://www.google.com")

    # 接受 cookies（可能有）
    try:
        agree_button = browser.find_element(By.XPATH, "//button[contains(text(),'同意') or contains(text(),'Accept')]")
        agree_button.click()
    except:
        pass  # 没有弹窗也继续

    # 找到搜索框并输入“天气”
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("天气")
    # search_box.send_keys(Keys.RETURN)
    #
    # # 等待页面加载
    # time.sleep(2)
    #
    # # 检查是否显示了天气模块
    # weather_card = browser.find_element(By.ID, "wob_wc")
    # assert weather_card.is_displayed()
