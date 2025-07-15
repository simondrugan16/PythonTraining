from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.co.uk/dp/B0F3XZ2C79/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B0F3XZ2C79&pd_rd_w=gpJCa&content-id=amzn1.sym.7c2bff8e-4ce3-4cc7-b3f6-35ac6c74cf9b&pf_rd_p=7c2bff8e-4ce3-4cc7-b3f6-35ac6c74cf9b&pf_rd_r=VBZN3V5BWR6VRA82E6Q7&pd_rd_wg=WDoPH&pd_rd_r=c5b9afdb-173a-4cf1-9868-a6e7735c2fba&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw")

price_pound = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"£{price_pound}.{price_pence}")
driver.quit()

options2 = webdriver.ChromeOptions()
options2.add_experimental_option("detach", True)

driver2 = webdriver.Chrome(options=options2)
driver2.get("https://www.python.org/")

search_bar = driver2.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

submit_size = driver2.find_element(By.ID, value="submit").size
print(submit_size)

documentation_link = driver2.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

anything_by_xpath = driver2.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[4]/p[2]/a[2]')
print(anything_by_xpath.text)

driver2.quit()
