# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:41:20 2020

@author: Ahmed's Computer
"""


import webbrowser
import time

my_Websites = ["https://accessuh.uh.edu/login.php","https://gmail.com","https://google.com"]
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def open_website(website_list):
    for website in website_list:
        webbrowser.open_new_tab(website)

def main():
    webbrowser.get(chrome_path).open("youtube.com", new=0, autoraise=False)
    time.sleep(2)
    open_website(my_Websites)


main()
