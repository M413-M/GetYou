#!/usr/bin/python
from time import sleep
from selenium import webdriver

act = webdriver.Firefox()
act.get('https://google.com')
search_abc = act.find_element_by_name('q')
dork = raw_input("Enter Dork : ")
search_abc.send_keys(dork)
index = 0
links = []
urls = act.find_element_by_css_selector('h3.r a')
for mct in urls:
	links.append(mct.get_attribute('href'))
	mct.get_attribute('href ')

while index <= 10:
	next_page = act.find_element_by_css_selector('#pnnext')
	next_page.click()
	sleep(5)
	urls = act.find_element_by_css_selector('h3.r a')
	for mct in urls:
		links.append(mct.get_attribute('href'))
		mct.get_attribute('href')
	index = index + 1
	sleep(2)
	