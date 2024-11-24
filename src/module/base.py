
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class crawler_spport():

    def __init__(self):
        self.options = Options()
        #options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        service =  Service()

        self.drive = webdriver.Chrome(options=self.options, service=service)
        self.wait = WebDriverWait(driver=self.drive, timeout=10)
        

    
    def click(self, by:By, id:str):
        def inner_func(func:callable):
            def wrapper(*args, **kwargs):
                result = self.wait.until(
                    EC.element_to_be_clickable((by, id))
                )
                result.click()
                return func(*args, **kwargs)
            return wrapper
        return inner_func

    def setParent(self, by:By, id:str):
        def inner_func(func:callable):
            result = self.wait.until(
                EC.presence_of_element_located((by, id))
            )
            return func(result)
        return inner_func
    
    def setIflame(self, id:str):
        def inner_func(func:callable):
            def wrapper(*args, **kwargs):
                iframe = self.wait.until(
                    EC.presence_of_element_located((By.ID, id))
                )
                self.drive.switch_to.frame(iframe)
                try:
                    return func(*args, **kwargs)
                finally:
                    self.drive.switch_to.default_content()
            return wrapper
        return inner_func