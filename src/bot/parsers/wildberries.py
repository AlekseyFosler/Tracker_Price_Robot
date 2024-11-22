import logging
from pathlib import Path
from uuid import uuid4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class WildberriesParser:
    def __init__(self) -> None:
        # Настройки
        self.options = Options()
        # self.options.add_argument("--headless")  # TODO: в фоне нет цен, разобраться
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Firefox(options=self.options)

        self.save_path: Path = Path('var/wildberries')  # TODO: создать в env значение

    def parse_product(self, url) -> dict | None:
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            # Ожидание появления элементов
            wait = WebDriverWait(self.driver, 50)
            # logger.info(self.driver.page_source)

            try:
                price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'price-block__final-price'))).text
                price_old = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'price-block__old-price'))).text
                product_nm_id = wait.until(EC.presence_of_element_located((By.ID, 'productNmId'))).text
            except Exception as e:
                logger.error(f'Ошибка при парсинге: {e}')
                return None

            logger.info(f'Price: {price}')
            logger.info(f'Old Price: {price_old}')
            logger.info(f'ProductNmId: {product_nm_id}')

            file_name = f'{uuid4()}.png'
            self.driver.save_screenshot(file_name)
            return {'price': price, 'price_old': price_old, 'productNmId': product_nm_id, 'file_name': file_name}
        except Exception as e:
            logger.error(f'Ошибка при парсинге: {e}')
            return None
