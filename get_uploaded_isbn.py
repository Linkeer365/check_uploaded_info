import os

book_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"
isbn_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_isbns.txt"   
isbns=[]

with open(book_path,"r",encoding="utf-8") as f:
    lines=[each for each in f.readlines() if each!="\n"]

for line in lines:
    if line.startswith("|"):
        isbn=line.split(" | ")[2]
        # print(isbn)
        if isbn!="ISBN号" and isbn!="----":
            isbns.append(isbn)
        if "NIL" in isbn:
            print(f"No ISBN:{line}")

isbns_s="\n".join(isbns)

with open(isbn_path,"w",encoding="utf-8") as f:
    f.write(isbns_s)

print("done.")