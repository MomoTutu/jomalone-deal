'''
This is for testing purpose
author: fanfan
'''

from selenium import webdriver
import time
import sys
import codecs
import random

if __name__ == '__main__':

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    cnt = 5

    while True:
        driver = webdriver.Chrome(chrome_options = chrome_options)
        driver.get('http://www.jomalone.com/pick-and-spritz')

        play_button = driver.find_element_by_id('play-button')
        time.sleep(10)
        play_button.click()
        time.sleep(5)
        
        win_msg = driver.find_element_by_id('win-box')
        cnt = 1
        while win_msg.text == '':
            cnt += 1
            if win_msg.text.find("100ml") > 0:
                raw_input()
                time.sleep(10000)
            play_button.click()
            time.sleep(random.randint(5,10))

        print "%d\t\t"%cnt,
        print win_msg.text

        driver.quit()
        #cnt -= 1

    
    
