from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ontario.ca/document/ontario-fishing-regulations-summary/fisheries-management-zone-18")

assert "Zone 18" in driver.title

sections = driver.find_elements(By.XPATH, "//div[@class='main-content']/div[@class='body-field']/div[@class='row']/div")
sections = sections[:2]


print('------------------------------------------')

for section in sections:
    child_elements = section.find_elements(By.XPATH, './*')
    
    for child_element in child_elements:
        text = child_element.text
        print(text)

    print('---------------------')


print('------------------------------------------')
driver.close()