from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    pname = ''
    url = ''
    dname = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, pname, url, dname):
        Spider.pname = pname
        Spider.url = url
        Spider.dname = dname
        Spider.queue_file = pname + "/queue.txt"
        Spider.crawled_file = pname + "/crawled.txt"
        self.boot()
        self.crawl_page("First spider", Spider.url)

    @staticmethod
    def boot():
        create_pdir(Spider.pname)
        create_dfiles(Spider.pname, Spider.url)
        Spider.queue = fileToset(Spider.queue_file)
        Spider.crawled = fileToset(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, url):
        if url not in Spider.crawled:
            print(thread_name + " now crawling " + url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(len(Spider.crawled)))
            Spider.append_links(Spider.gather_links(url))
            Spider.queue.remove(url)
            Spider.crawled.add(url)
            Spider.update_records()

    @staticmethod
    def gather_links(url):
        html = ''
        try:
            response = urlopen(url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.url,url)
            finder.feed(html)
        except:
            print("Error: Can't crawl page")
            return set()
        return finder.page_links()

    @staticmethod
    def append_links(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.dname not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_records():
        setTofile(Spider.queue,Spider.queue_file)
        setTofile(Spider.crawled,Spider.crawled_file)