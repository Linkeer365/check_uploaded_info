import hashlib
import os

md5_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_md5s.txt"
newbooks_path=r"D:\AllDowns\newbooks"

def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()

with open(md5_path,"r",encoding="utf-8") as f:
    md5s=set([each.strip("\n") for each in f.readlines() if each!='\n'])

for each in os.listdir(newbooks_path):
    if each.endswith(".pdf"):
        filepath=newbooks_path+os.sep+each
        md5=get_file_md5(filepath)
        print(md5)
        if md5 in md5s:
            print("already!")
            os.remove(filepath)
print("done.")