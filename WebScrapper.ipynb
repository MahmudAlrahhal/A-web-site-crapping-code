# A-web-site-crapping-code
A python code that scraps a web site to gather the users' comments and stor them in a csv file


import sys
import csv
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# default path to file to store data
path_to_file = "Page.csv"

# default number of scraped pages
num_page = 10

url = "Example.html"
#url = "Example.html"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

# import the webdriver
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
wait = WebDriverWait(driver,60)
time.sleep(10)
button = driver.find_elements_by_tag_name('button')
for m in button:
    if(m.text == "I Accept"):
        print(m.text)
        m.click()
# change the value inside the range to save more or less reviews
for i in range(0, num_page):
    # expand the review 
    time.sleep(2)
    #ele = driver.find_element_by_xpath("*//div[contains(@data-test-target, 'expand-review')]")
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2000000).until(EC.element_to_be_clickable((By.XPATH, "*//div[contains(@data-test-target, 'expand-review')]"))))
    #ele.click()
    container = driver.find_elements_by_xpath("//div[@data-reviewid]")
    dates = driver.find_elements_by_xpath(".//div[@class='_2fxQ4TOx']");
    for j in range(len(container)):
        time.sleep(3)
        
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        title = container[j].find_element_by_xpath("//*[@id='component_14']/div/div[3]/div["+str(3+j)+"]/div[1]/div/div[2]/span/a").text
        
        driver.implicitly_wait(10)
        a = container[j].find_element_by_xpath(".//span[@class='Ignyf _S Z']")
        print(a.text)
        if(a.text == "Read more"):
            a.click()
        review = container[j].find_element_by_xpath(".//div[@class='fIrGe _T']").text.replace("\n", "  ")
        date = container[j].find_element_by_xpath(".//span[@class='teHYY _R Me S4 H3']").text
        print(date)
        #date = " ".join(dates[j].text.split(" ")[-2:])
        csvWriter.writerow([date, title, rating, review]) 
        
    # change the page
    time.sleep(3) 
    
    #driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, './/a[@class="ui_button nav next primary "]'))))
    if(i>0):
        url = "Example.html"
        driver.get(url)


driver.quit()
csvFile.close()
print('Finished')
