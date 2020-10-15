#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
import time 
import os
import datetime
from cryptography.fernet import Fernet
from os.path import basename
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect

####################### Definitions des fonctions ########################

def attendre(a):
	WebDriverWait(driver, 10, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, a)))

def remplchamp(a, b):
	driver.find_element_by_xpath(a).send_keys(b)

def clickbouton(path):
	driver.find_element_by_xpath(path).click()

def clickelement(path):
	element = driver.find_element_by_xpath(path)
	driver.execute_script("$(arguments[0]).click();", element)
driver = webdriver.Firefox()
def loginform(url,login,passwd):
    driver.get(url)
    print("connexion à {}...".format(url))

    #attendre("//button[@title='Accept All']")
    #clickbouton("//button[@title='Accept All']")
    attendre("//input[@name='email']")
    remplchamp("//input[@name='email']",login)
    print("Username entered...")
    attendre("//input[@name='pass']")
    remplchamp("//input[@name='pass']",passwd)
    print("Password entered...")
    clickbouton("//button[@type='submit']")
    print("login Successful")
    time.sleep(3)

def writemsg(login,passwd,friend,msg,url="https://www.messenger.com/login/"):
    loginform(url,login,passwd)
    attendre("//a[@aria-label='Nouveau message']")
    clickbouton("//a[@aria-label='Nouveau message']")
    attendre("//input[@aria-label='Recherche dans Messenger']")
    remplchamp("//input[@aria-label='Recherche dans Messenger']",friend)
    remplchamp("//div[contains(text(),'crivez un message...')]",msg)


writemsg('abdoul_gandega@yahoo.com','portable','estelle','yo')

