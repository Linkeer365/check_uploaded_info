import os

book_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\【长期更新】每日传书计划.md"
md5_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_md5s.txt"   
md5s=[]

with open(book_path,"r",encoding="utf-8") as f:
    lines=[each for each in f.readlines() if each!="\n"]

for line in lines:
    if line.startswith("|"):
        md5=line.rsplit(" | ",maxsplit=1)[1]
        md5=md5[1:33]
        if not "书链接" in md5 and not "---" in md5:
            print(md5)
            md5s.append(md5) 

md5s_s="\n".join(md5s)

with open(md5_path,"w",encoding="utf-8") as f:
    f.write(md5s_s)

print("done.")
