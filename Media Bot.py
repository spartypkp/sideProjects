#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:54:10 2020

@author: willdiamond
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

# Actual password and username removed for obvious reasons
username = "#####"
password = "##"


class MediaBot():
    def __init__(self):
        self.speed = int(input("Input a speed: (0: no limit), (1: randomized wait time)"))
        self.driver = webdriver.Chrome()
        self.swipes = 0
        self.dislikes = 0
        self.likes = 0

    # The xpath elements change constantly. I haven't updated this in forever, therefore the
    # elements will probably no longer be findable through their respective XPaths
    def login(self):
        # Possible recruiter, if you've gotten this far and read my code, I promise you I'm not that weird.
        # I only made this out of pure boredom during the height of quarantine. Please don't judge me.
        # Makes for a good story and an even better side project! Ask me about it for a good story
        self.driver.get('https://tinder.com')
        # Could be updated to any website, but this program has been tailored to work on the above website

        sleep(2)
        try:

            fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
            #fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button/span[2]')
            fb_btn.click()
        except Exception:
            print("Couldnt find original")
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
        #//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        base_window = self.driver.window_handles[0]
        print("####################################")
        print("### Base: ", base_window)

        self.driver.switch_to_window(base_window)

        sleep(5)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        popup_1.click()

        sleep(5)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        popup_2.click()

        try:
            accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/div/button')
            accept.click()
            print("Closed Accept Button")
        except Exception:
            print("Failed to close accept button")

    def like(self):
        print("Liking...")
        if self.speed == 1:
            wait = random.randint(3, 10)
            sleep(wait)
        self.likes += 1
        window = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body')
        window.send_keys(Keys.ARROW_RIGHT)


    def dislike(self):
        print("Disliking...")
        if self.speed == 1:
            wait = random.randint(3, 10)
            sleep(wait)
        self.dislikes += 1
        window = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body')
        window.send_keys(Keys.ARROW_LEFT)


    def auto_swipe(self):
        while(True):
            if self.swipes >= 2000:
                break
            print("Swipe Count: ", self.swipes)
            sleep(1)
            swipe_prob = random.randint(0,100)
            if swipe_prob >= 25:
                swipe_bool = True
            else:
                swipe_bool = False

            try:
                self.close_popup()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    try:
                        if swipe_bool:
                            self.like()
                        else:
                            self.dislike()
                        self.swipes += 1
                    except Exception:
                        break



    def close_popup(self):

        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()
        print("Closing popup")

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        print("Closing match")

bot = MediaBot()
bot.login()
bot.auto_swipe()
