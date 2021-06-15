from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
search_product = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search_product.send_keys("lenovo laptop")
search_button = driver.find_element_by_id('nav-search-submit-button')
search_button.click()
product_item = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[6]/div/span/div/div/div[2]/div[2]/div/div[1]/h2/a/span')
product_item.click()
buying_options_button = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
buying_options_button.click()
driver.quit()

# add_to_cart_button.click()





