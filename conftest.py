import logging
import undetected_chromedriver as uc
import pytest

# def pytest_configure(config):
#     logging.basicConfig(
#         level=logging.INFO,
#         filename='test.log',  # 指定日志文件名
#         filemode='w',
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )

@pytest.fixture
def driver():
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()