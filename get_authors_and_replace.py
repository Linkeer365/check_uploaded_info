import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait

# 一出现就马上点，这个操作好啊！！！

# https://stackoverflow.com/questions/62868434/button-click-only-works-when-time-sleep-added-for-selenium-python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
from yals import open_one_link
import time

import re

firefox_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe"

options = Options()
options.headless = True
# options.headless=False

max_delay=15

# driver=webdriver.Firefox(options=options,executable_path=firefox_path)

missing_author_path=r"D:\check_uploaded_info\missing_authors.txt"
book_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"
needToModify_path=r"D:\check_uploaded_info\need_to_modify447.txt"

already_path=r"D:\check_uploaded_info\already_modify.txt"

missing_lines=[]
with open(missing_author_path,"r",encoding="utf-8") as f:
    missing_lines=[each.strip("\n") for each in f.readlines() if each!="\n"]

already_lines=[]
with open(already_path,"r",encoding="utf-8") as f:
    already_lines=[each.strip("\n") for each in f.readlines() if each!="\n"]

already_lines_set=set(already_lines)

delim="===>"

driver=webdriver.Firefox(options=options,executable_path=firefox_path)

book_lines=[]
with open(book_path,"r",encoding="utf-8") as f:
    book_lines=f.readlines()

for missing_line in missing_lines:
    if missing_line in already_lines:
        continue
    line_num,line_content=missing_line.split(delim)
    assert line_content.startswith("|")
    print("line content:",line_content)
    title,author,isbn,link=line_content.split(" | ")
    link_len=len("http://libgen.rs/book/index.php?md5=4725AF642D828FC90DF6E9703C65F212")
    link_head=len("[4725AF642D828FC90DF6E9703C65F212](")
    link=link[link_head:link_head+link_len]
    # print("isbn:",isbn)
    if "NIL" in isbn:
        print("no isbn:",line_num)
    elif "NIL" in author:
        if "," in isbn:
            head_idx=isbn.find("978")
            isbn=isbn[head_idx:head_idx+13]
        final_dict=open_one_link(driver,isbn)
        time.sleep(3)
        if 'authors' in final_dict.keys():
            author=final_dict['authors']
            if author!='':
                author=author.strip(" ")
                print("author:",author)
                line_content=line_content.replace("NIL",author)
                book_lines[int(line_num)]=line_content+"\n"
                needToModify=f"{link}\n[Author(s) -> \"{author}\"]\n\n"
                with open(needToModify_path,"a",encoding="utf-8") as f:
                    f.write(needToModify)
                book_lines_s="".join(book_lines)
                with open(book_path,"w",encoding="utf-8") as f:
                    f.write(book_lines_s)
    with open(already_path,"a",encoding="utf-8") as f:
        f.write(missing_line+"\n")


# needToModify_s="".join(needToModifys)

print("done.")
    
    
    