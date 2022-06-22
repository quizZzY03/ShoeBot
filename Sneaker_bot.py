from selenium import webdriver
import csv
import time
from itertools import zip_longest
import sys
from selenium.webdriver.support.ui import Select

url = input("Enter your product URL: ")
input_size = input("Enter your product size: ")
print("Your Product size is: ", input_size)
input_size = str(input_size)

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")  # Chrome web driver along with path
driver.maximize_window()
# Here You can pass the urls
driver.get(url)

try:
    driver.find_element_by_xpath("//div[@id='select-size']").click()
    size = driver.find_elements_by_xpath("//div[@class='option enabled']")
    for al in size:
        res = al.get_attribute("data-eu-size")
        if input_size == res:
            driver.execute_script("arguments[0].click();", al)
        else:
            pass

    add_to_bag = driver.find_element_by_xpath("//div[@id='add-to']").click()
    time.sleep(5)
    check_out_btn = driver.find_element_by_xpath("//div[@class='goto-checkout button']")
    driver.execute_script("arguments[0].click();", check_out_btn)
    time.sleep(3)
    driver.implicitly_wait(15)

    ########################## Billing Information #########################################3

    # You can put actual info inside send_keys, like dummy data is abc, you put your first name

    first_name = driver.find_element_by_xpath("//input[@id='billing_first_name']").send_keys("abc")
    last_name = driver.find_element_by_xpath("//input[@id='billing_last_name']").send_keys("a")
    country = driver.find_element_by_xpath("//select[@id='billing_country']")
    drp = Select(country)
    drp.select_by_visible_text("Israel")
    street_address = driver.find_element_by_xpath('//input[@id="billing_address_1"]').send_keys("a")
    post_code = driver.find_element_by_xpath('//input[@id="billing_postcode"]').send_keys("a")
    city = driver.find_element_by_xpath('//input[@id="billing_city"]').send_keys("a")
    phone = driver.find_element_by_xpath('//input[@id="billing_phone"]').send_keys("a")
    email = driver.find_element_by_xpath('//input[@id="billing_email"]').send_keys("a")

    ################################### End ##################################################3

    terms = driver.find_element_by_xpath('//*[@id="payment"]/div[2]/div/p[1]/label')
    driver.execute_script("arguments[0].click();", terms)
    try:
        standard_shipping = driver.find_element_by_xpath('//*[@id="shipping_method"]/li[2]/label')
        driver.execute_script("arguments[0].click();", standard_shipping)
    except:
        standard_shipping = driver.find_element_by_xpath('//*[@id="shipping_method_0_free_shipping1"]')
        driver.execute_script("arguments[0].click();", standard_shipping)

    place_order_btn = driver.find_element_by_xpath('//button[@id="place_order"]')
    driver.execute_script("arguments[0].click();", place_order_btn)

except: pass
