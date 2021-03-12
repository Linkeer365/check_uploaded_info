import hashlib
import os

md5_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_md5s.txt"
isbn_path=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365BookReview\source\_posts\last_isbns.txt"
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

def get_file_isbn(file_path):
    assert file_path.endswith(".pdf")
    if os.sep in file_path:
        filename=file_path.rsplit(os.sep,maxsplit=1)[1]
    else:
        filename=file_path
    isbn=filename.split("isbnisbn")[1].replace(".pdf","")
    # isbn:str
    assert isbn.isdigit()
    return isbn

with open(md5_path,"r",encoding="utf-8") as f:
    md5s=set([each.strip("\n") for each in f.readlines() if each!='\n'])

with open(isbn_path,"r",encoding="utf-8") as f:
    isbns=[each.strip("\n") for each in f.readlines() if each!='\n' and each!="NIL\n"]

for idx,isbn in enumerate(isbns):
    if "," in isbn:
        startAt=isbn.find("9787")
        isbn=isbn[startAt:startAt+13]
        isbns[idx]=isbn

for each in os.listdir(newbooks_path):
    if each.endswith(".pdf"):
        filepath=newbooks_path+os.sep+each
        isbn=get_file_isbn(filepath)
        # print(md5)
        if isbn in isbns:
            print("already.")
            os.remove(filepath)
            continue
        md5=get_file_md5(filepath)
        if md5 in md5s:
            print("already.")
            os.remove(filepath)
        
print("done.")