#!/usr/bin/env python3
""" registration checks if the course has open seats and sends me
a text if so"""

import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

COURSE = "BIOL 0030"
MIN_TO_WAIT = 1

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    while True:
        try:
            driver = webdriver.chrome.webdriver.WebDriver(chrome_options=options)
            driver.get("https://cab.brown.edu")
            # input it to search box
            search_box = driver.find_element_by_id("crit-keyword")
            search_box.click()
            search_box.send_keys(COURSE)
            # search for it
            driver.find_element_by_id("search-button").click()
            # now do stuff with it
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/main/div[2]/div/div[3]/div[1]/a").click()
            time.sleep(1)
            seats = int(driver.find_element_by_class_name("seats_avail").text)
            if seats > 0:
                print("%d Slot(s)! GO NOW!!!! GOGOGOGOOGOGOG" % seats)
                duration = .1  # seconds
                repeats = 20
                freq = 440  # Hz
                for i in range(0, repeats):
                    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                return
            else:
                print("...")
            driver.quit()
        except Exception:
            print("Error.")
        time.sleep(60*MIN_TO_WAIT) # wait 5 min

if __name__ == "__main__":
    main()
