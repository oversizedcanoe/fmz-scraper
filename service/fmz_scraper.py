from selenium import webdriver
from selenium.webdriver.common.by import By

def get_text_sections(zone_number: int) -> list[str]:
    driver = webdriver.Chrome()
    driver.get("https://www.ontario.ca/document/ontario-fishing-regulations-summary/fisheries-management-zone-" + str(zone_number))

    sections = driver.find_elements(By.XPATH, "//div[@class='main-content']/div[@class='body-field']/div[@class='row']/div")
    sections = sections[:2]

    text_sections: list[str] = []

    for section in sections:
        child_elements = section.find_elements(By.XPATH, './*')

        for child_element in child_elements:
            element_text = child_element.text
            # for some reason some of the lines come back together, but with a line break
            text_sections.extend(t for t in element_text.split('\n'))

    driver.close()

    return text_sections