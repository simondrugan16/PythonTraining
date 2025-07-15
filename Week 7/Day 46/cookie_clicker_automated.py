from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)

language_english = wait.until(EC.visibility_of_element_located((By.ID, "langSelect-EN")))

language_english.click()

products = driver.find_elements(By.CLASS_NAME, value="product unlocked enabled")

def safe_get_text(element, selector, default="0"):
    try:
        number = element.find_element(By.CSS_SELECTOR, selector).text
        if number == "":
            return default
        else:
            return number 
    except:
        return default
    

while True:
    current_cookies: str = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cookies"]'))).text.split(" ")[0].replace(",", "")
    current_cookies_int = int(current_cookies)
    products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    item_and_price_list = [
        (
            web_element,
            safe_get_text(web_element, ".title.owned")
            # ,
            # safe_get_text(web_element, ".price").replace('"', "").replace(",", "")
        )
        for web_element in products
    ]
    print(item_and_price_list)
    filtered_items = [elem for (elem, num) in item_and_price_list if int(num) < 30]

    upgrades = driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")

    purchasable_elems = filtered_items + upgrades 

    if len(purchasable_elems) > 0:
        purchasable_elems[0].click()
    # if current_cookies_int > 100:
    #     cursor = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="product0"]')))
    #     cursor.click()

    cookie = driver.find_element(By.ID, value="bigCookie")
    cookie.click()

