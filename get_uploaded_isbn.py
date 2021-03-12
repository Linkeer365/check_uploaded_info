import os

book_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"
isbn_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_isbns.txt"
missing_isbn_path=r"D:\check_uploaded_info\missing_isbns.txt"  
missing_lines=[]   
isbns=[]

with open(book_path,"r",encoding="utf-8") as f:
    lines=[each for each in f.readlines() if each!="\n"]

for idx,line in enumerate(lines):
    if line.startswith("|"):
        isbn=line.split(" | ")[2]
        # print(isbn)
        if isbn!="ISBN号" and isbn!="----":
            isbns.append(isbn)
        if "NIL" in isbn and not "统一书号" in line:
            print(f"No ISBN:{line}")
            missing_line=f"{idx}===>{line}"
            missing_lines.append(missing_line)

isbns_s="\n".join(isbns)

with open(isbn_path,"w",encoding="utf-8") as f:
    f.write(isbns_s)

missing_lines_s="\n".join(missing_lines)

with open(missing_isbn_path,"w",encoding="utf-8") as f:
    f.write(missing_lines_s)

print("done.")