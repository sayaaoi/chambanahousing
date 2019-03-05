from selenium import webdriver
import os
import time
links = open('apartmentfinder_link.txt','r')
address_1 = []
# address_2 = []
for link in links:
    time.sleep(2)
    link_init = link
    driver = webdriver.Chrome('/Users/paulliu/Desktop/chromedriver')  # Optional argument, if not specified will search path.
    try:
        driver.get(link_init)
        time.sleep(5)
    except:
        raise Exception('The link is invalid. The initial link was {}'.format(link_init))
    try:
        target_element = 'location'
        target_element_extra = 'placardTitle'
        searches = driver.find_elements_by_class_name(target_element)
        searches_extra = driver.find_elements_by_class_name(target_element_extra)
    except:
        raise Exception('The required element does not exist({})'.format(target_element))
    for search in searches:
        address_1.append(search.text)
    # for search_extra in searches_extra:
        # address_2.append(search_extra.text)
    # try:
    #     next_page = driver.find_element_by_class_name('off')
    #     # print(next_page)
    # except:
    #     nextpage = 0
    #     raise Exception('No next page to scrape')
    driver.close()

print(address_1)
with open("address_apartmentsfinder.txt", "w") as output:
    for i in range(len(address_1)-1):
        output.write(str(address_1[i]) + '\n')