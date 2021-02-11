import os
import re
target_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"

modify_path=r"D:\checkifuploaded\mm.txt"

with open(target_path,"r",encoding="utf-8") as f:
    lines=[each for each in f.readlines() if each!="\n"]

with open(modify_path,"r",encoding="utf-8") as f:
    modifys=[each for each in f.readlines() if each!="\n"]

newlines=lines
print(lines)

for modify in modifys:
    link,author_str=modify.split("\t")
    print(link)
    author=re.findall("\"(.*?)\"",author_str)[0]
    print("author",author)
    for idx,line in enumerate(newlines):
        if link in line:
            print("gg")
            newline=line.replace("NIL",author)
            print("newline:",newline)
            newlines[idx]=newline
            break

newlines_s="".join(newlines)

with open(target_path,"w",encoding="utf-8") as f:
    f.write(newlines_s)

print("done.")