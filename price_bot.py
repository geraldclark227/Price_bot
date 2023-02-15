#from requests import HTMLSession
#from bs4 import BeautifulSoup
from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.common.by import By

year = input("enter year: ")
year = str(year)

card_set = input("card_set: ")
card_set = str(card_set)

character = input("Choose Character: ")
character = str(character)
my_search = year+" "+card_set+" "+character
print(my_search)


wd = wd.Chrome()

wd.implicitly_wait(10)

wd.get("http://www.amazon.com")

#locality for order
wd.find_element(By.ID,"nav-global-location-popover-link").click()
postcode_field = wd.find_element(By.ID,"GLUXZipUpdateInput")
postcode_field.send_keys("91423")
wd.find_element(By.ID,"GLUXZipUpdate").click() 
close_element = wd.find_element(By.CSS_SELECTOR, "button.a-button-text")
close_element.click()

wd.implicitly_wait(10)

search_field = wd.find_element(By.NAME, "field-keywords").send_keys(my_search)
search_button_click = wd.find_element(By.ID, "nav-search-submit-button")
search_button_click.click()

wd.implicitly_wait(10)

#wd.get("https://www.amazon.com/s?k={year}+{card_set}+{character}&crid=2XB82YGA8S9LV&sprefix={year}+{card_set}+{character}%2Caps%2C163&ref=nb_sb_noss")

#beatiful soup
from bs4 import BeautifulSoup
import re
#regular expression

soup = BeautifulSoup(wd.page_source, 'html.parser')

web_page = soup.findAll("div",{"data-component-type": "s-search-result"})
#print(results)
for result in web_page:
    title = result.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
    wolverine = result.find("span", text = re.compile(character))
    print(title.text)
    print(wolverine)







