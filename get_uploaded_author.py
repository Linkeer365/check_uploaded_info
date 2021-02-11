import os

book_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"
author_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_authors.txt"
missing_author_path=r"D:\checkifuploaded\missing_authors.txt"  
authors=[]
missing_lines=[]

with open(book_path,"r",encoding="utf-8") as f:
    lines=[each for each in f.readlines() if each!="\n"]

for idx,line in enumerate(lines):
    if line.startswith("|"):
        author=line.split(" | ")[1]
        # print(author)
        if author!="作者" and author!="----":
            authors.append(author)
        if "NIL" in author:
            missing_line=f"{idx}===>{line}"
            missing_lines.append(missing_line)

authors_s="\n".join(authors)
missing_lines_s="\n".join(missing_lines)

with open(author_path,"w",encoding="utf-8") as f:
    f.write(authors_s)

with open(missing_author_path,"w",encoding="utf-8") as f:
    f.write(missing_lines_s)

print("done.")