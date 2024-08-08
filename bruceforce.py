import urllib.request as urllib_req
import threading
import queue
import urllib.parse as urllib_parse

threads = 50
target_url = "http://testphp.vulnweb.com/login.php"
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


def dir_bruter(word_queue, extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append(f"/{attempt}/")
        else:
            attempt_list.append(f"/{attempt}")
        
        # If we want to bruteforce extensions
        if extensions:
            for extension in extensions:
                attempt_list.append(f"/{attempt}{extension}")
        
        # Iterate over our list of attempts
        for brute in attempt_list:
            url = f"{target_url}{urllib_parse.quote(brute)}"
            try:
                headers = {"User-Agent": user_agent}
                req = urllib_req.Request(url, headers=headers)
                
                with urllib_req.urlopen(req) as response:
                    content = response.read()
                    if len(content):
                        print(f"[{response.code}] => {url}")
            except urllib_req.URLError as e:
                if hasattr(e, 'code') and e.code != 404:
                    print(f"!!! {e.code} => {url}")





listword=build_wordlist(wordlist_file)
while not listword.empty() :
    data=listword.get()
    print(data)

# Exampl
if __name__ == "__main__":
    words_queue = build_wordlist(wordlist_file)
    extensions = [".php", ".html", ".asp"]  # Example extensions

    threads_list = []
    for i in range(threads):
        t = threading.Thread(target=dir_bruter, args=(words_queue, extensions))
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()
