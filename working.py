from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

usertag = input("enter username of person to find: ")

browser = webdriver.Chrome(
    executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options=option)

page = browser.get("https://instagram.com/")

input("login and then press enter...")

page = browser.get("https://instagram.com/"+usertag)

time.sleep(5)

followingbox = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
followingbox.click()

input("scroll to bottom of following and then press enter...")

# Scraping for data
whole = browser.find_element_by_xpath('/html')
htmldata = whole.get_attribute("innerHTML")
html = str(htmldata)
soup = BeautifulSoup(html, "html.parser")
soup = soup.prettify()
followingstring = str(soup)

exit = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
exit.click()

followerbox = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followerbox.click()

input("scroll to bottom of followers and then press enter...")

whole = browser.find_element_by_xpath('/html')
htmldata = whole.get_attribute("innerHTML")
html = str(htmldata)
soup = BeautifulSoup(html, "html.parser")
soup = soup.prettify()
followerstring = str(soup)

exit = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
exit.click()

browser.close()

# Processing Data

test_str = followerstring
followers = list()
regex = r"<a class=\"FPmhX notranslate _0imsa\" href=\"\/(.+)\/"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        followers.append(match.group(groupNum))

test_str = followingstring
following = list()
regex = r"<a class=\"FPmhX notranslate _0imsa\" href=\"\/(.+)\/"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        following.append(match.group(groupNum))

# Display Output

print("List of People who don't follow you back: ")

for followed in following:
    if(followed not in followers):
        print(followed)

print("number of followers: " + str(len(followers)))
print("number following: " + str(len(following)))

quit()
