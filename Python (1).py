import urllib.request as res
import urllib.parse as par
import urllib.error as err
import queue
#https://pythonprogramming.net/search/?q=basicpython
import threading
target_url = "http://testphp.vulnweb.com"
linkpath=r"C:\Users\PC\OneDrive\Máy tính\Python (1).txt"
resume=None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101Firefox/19.0"


def build_word_list(linkpath):
    with open(linkpath,"r") as read:
         drawword=read.readlines()
    
    words=queue.Queue()
    resume_check=False
    for word in drawword:
        word=word.strip()
        if resume is not None:
            if resume_check:
                words.put(word)
            else:
                if resume==word:
                    resume_check=True
                    print(f"bat dau tu day {resume}")
        else:
            words.put(word)
    return words



def bruce_force(words,extensions):
    while not words.empty():
        listurl=[]
        word = words.get()
        if "." not in word:
            listurl.append(f"/{word}/")
        else:
            listurl.append(f"/{word}")
        for extension in extensions :
            listurl.append(f"/{word}{extension}")

        for url in listurl:
            headers={"User-Agent": user_agent}
            resq=f"{target_url}{par.quote(url)}"
            print(resq)
            resqest=res.Request(resq,headers=headers)
            try:
                 with res.urlopen(resqest) as respond:
                      if respond.read() != 0:
                           print(f"")
            except err.URLError as e:
                 if hasattr(e,"code") and e.code != 404:
                      print (f"!!!!!! {e.code()}  =>  {resqest} ")

     



words_queue = build_word_list(linkpath)
extensions = [".php", ".html", ".asp"]  # Example extensions

threads_list = []
for i in range(50):
        t = threading.Thread(target=bruce_force, args=(words_queue, extensions))
        t.start()
        threads_list.append(t)

for t in threads_list:
        t.join()


        