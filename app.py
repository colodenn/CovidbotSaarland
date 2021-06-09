from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from playsound import playsound
from playsound import playsound

# Input an existing mp3 filename
mp3File = "faceit-accept-sound-epic.mp3"
# Play the mp3 file


driver = webdriver.Firefox()
driver.get("https://www.impfen-saarland.de/service/waitlist_entries")

instances = 10


test = True
while(test):
    elem = driver.find_element_by_xpath(
        '//button[text()="Saarbrücken"]')
    elem.click()
    # driver.implicitly_wait(0.9)

    nextbutton = driver.find_element_by_xpath('//button[text()="Weiter"]')
    nextbutton.click()
    try:

        nextbutton = driver.find_element_by_xpath(
            '//h5[text()="Keine Termine verfügbar. "]')
        backbutton = driver.find_element_by_xpath(
            '//button[text()="Zurück"]')
        backbutton.click()

    except Exception as e:
        found = driver.find_element_by_class_name(
            'TimeSelectorButton__SplitWrapper-sc-1rvgnx8-1 fleLrs')
        found.click()
        nextbutton = driver.find_element_by_xpath('//button[text()="Weiter"]')
        nextbutton.click()
        print(e)
        print(mp3File)
        playsound(mp3File)
        test = False
