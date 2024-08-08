import queue as qu
import threading
import os
import urllib.request
import urllib.error

threads = 10 
target = "https://jsonplaceholder.typicode.com/posts/1" 
directory = "C:/Users/PC/Downloads/Joomla_5.1.2-Stable-Full_Package"
filters = [".jpg", ".gif", ".png", ".css"]
os.chdir(directory)

web_paths = qu.Queue() 

for r, d, f in os.walk("."): 
    for file in f:
        remote_path = "%s/%s" % (r, file)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(file)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():
    while not web_paths.empty(): 
        path = web_paths.get()
        url = "%s%s" % (target, path)
        request = urllib.request.Request(url) 

        try:
            response = urllib.request.urlopen(request)
            content = response.read()
            print("[%d] => %s" % (response.code, path)) 
            response.close()
        except urllib.error.HTTPError as error: 
            # Uncomment the following line to print error codes
            # print("Failed %s" % error.code)
            pass

for i in range(threads): 
    print("Spawning thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()
