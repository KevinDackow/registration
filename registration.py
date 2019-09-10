#!/usr/bin/env python3
""" registration checks if the course has open seats and sends me
a text if so"""

import argparse
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# the course to check. must exactly match CAB
COURSE = "BIOL 0030"
# path to chromedriver
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no_headless", help="Disable headless browsing for debugging.", action="store_true")
    args = parser.parse_args()
    # the time to wait between checks
    min_to_wait = 1
    duration = .1  # seconds
    repeats = 20
    freq = 440  # Hz
    options = Options()
    # enable this option to see the web automation. Recommended for debugging
    if not args.no_headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    while True:
        try:
            driver = webdriver.chrome.webdriver.WebDriver(CHROMEDRIVER_PATH, chrome_options=options)
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
                for i in range(0, repeats):
                    os.system('sox -nq -t alsa synth {} sine {}'.format(duration, freq))
                return
            else:
                print("...")
            driver.quit()
        except Exception:
            print("Error.")
        time.sleep(60*min_to_wait) # wait

if __name__ == "__main__":
    main()
