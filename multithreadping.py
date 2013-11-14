from urllib.request import urlopen
from threading import Thread
import time

urlsz = ['google', 'amazon', 'ebay', 'reddit', 'facebook']
def urlwrapper(urls):
    newur = []
    for x in urls:
        f = 'http://www.' + x + '.com'
        newur.append(f)
    return newur

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urlopen(self.url)
        print(self.url, resp.getcode())

def get_responses():
    start = time.time()
    threads = []
    for url in newur:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('elapsed time: %s' % (time.time()-start))

newur = urlwrapper(urlsz)
get_responses()
