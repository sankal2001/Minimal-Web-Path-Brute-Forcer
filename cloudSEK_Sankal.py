import requests
import sys
import threading
import time


sucess_code = []
urls = []

def create_new_url(webApp_url,word):
    return webApp_url + "/" + word
    

def algo(webApp_url):
    
    response = requests.get(webApp_url)
    codee[webApp_url] = int(response.status_code)
        


if __name__ == '__main__':

    s = time.perf_counter()

    global paths_file

    t = 1

    while(str(sys.argv[t][-4:]) != '.txt'):
        urls.append(str(sys.argv[t]))
        t = t+1

    paths_file = sys.argv[t]

    with open(paths_file, "r") as f:
        webApp_paths = f.read().splitlines()
        f.close()
    
    #sucess_code = json.loads(sys.argv[3])
    for x in range(t+1,len(sys.argv)):
        sucess_code.append(int(sys.argv[x]))
    
    for url in urls:
        sss = []
        codee = dict()
        webApp_urls = []

        for web in webApp_paths:
            webApp_urls.append(create_new_url(url,web))

        for ul in webApp_urls:
            sss.append(threading.Thread(target=algo,args=(ul,)))
               
        for x in range(len(sss)):
            sss[x].start()
        
        for x in range(len(sss)):
            sss[x].join()
        
        for web,cod in codee.items():
            if cod in sucess_code:
                print(web + ' [Status code ' + str(cod) + ']')

        elapsed = time.perf_counter() - s
        s = time.perf_counter()
        print(f"{__file__} executed in {elapsed:0.4f} seconds.")
        print("\n\n")