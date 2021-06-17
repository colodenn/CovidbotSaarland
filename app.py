from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from playsound import playsound

# Input an existing mp3 filename
mp3File = "sound.mp3"
# Play the mp3 file


driver = webdriver.Firefox()
driver.set_window_size(500, 800)
driver.get("https://www.impfen-saarland.de/service/waitlist_entries")


test = True
while(test):
    elem = driver.find_element_by_xpath('//button[text()="Saarbrücken"]')
    # elem = driver.find_element_by_xpath('//button[text()="Impfzentrum Lebach - Nacht-Termine"]')
    elem.click()
    # driver.implicitly_wait(0.9)

    nextbutton = driver.find_element_by_xpath('//button[text()="Weiter"]')
    nextbutton.click()

    while(True):
        try:
            appointmentList = driver.find_elements_by_xpath(
                "//div[starts-with(@class,'TimeSelectorButton__SplitWrapper-')]")
            if not appointmentList:
                raise NameError("no appointments")
            print(appointmentList)
            print("found appointments")
            last = len(appointmentList) - 1
            ActionChains(driver).move_to_element(
                appointmentList[last]).click().perform()
            print("appointment clicked")
            nextbutton = driver.find_element_by_xpath(
                '//button[text()="Weiter"]')
            nextbutton.click()
            print("next clicked")
            try:
                nextbutton = driver.find_element_by_xpath(
                    '//h5[text()="Keine Termine verfügbar. "]')
                backbutton = driver.find_element_by_xpath(
                    '//button[text()="Zurück"]')
                backbutton.click()
                continue
            except Exception as e:
                print(e)
                pass
            test = False
            playsound(mp3File)
            break
        except Exception as e:
            print(e)
            pass

        try:
            nextbutton = driver.find_element_by_xpath(
                '//h5[text()="Keine Termine verfügbar. "]')
            backbutton = driver.find_element_by_xpath(
                '//button[text()="Zurück"]')
            backbutton.click()
            break
        except Exception as e:
            print(e)
            continue
