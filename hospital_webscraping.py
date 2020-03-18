from selenium import webdriver
import csv

hospital_wait_time ={}
url = 'https://goodsamsanjose.com/about/er-wait-times.dot'
driver = webdriver.Chrome()
driver.get(url)
table =  driver.find_element_by_xpath("//table[@class='table table-striped']")
for row in table.find_elements_by_xpath(".//tr"):
    hospital_wait_time[[td.text for td in row.find_elements_by_xpath(".//td")][0]] = 
[td.text for td in row.find_elements_by_xpath(".//td")][1]

with open('test.csv', 'w') as f:
    for key in hospital_wait_time.keys():
        f.write("%s,%s\n"%(key,hospital_wait_time[key]))
