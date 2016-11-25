import os


def create_pdir(direc):
    if not os.path.exists(direc):
        print("Creating project " + direc)
        os.makedirs(direc)


def create_dfiles(pname, url):
    queue = os.path.join(pname, "queue.txt")
    crawled = os.path.join(pname, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
    f.close()


def appendf(path,data):
    with open(path,'a') as f:
        f.write(data + '\n')
    f.close()


def flushFile(path):
    open(path, 'w').close()


def fileToset(fname):
    results = set()
    with open(fname, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def setTofile(setData, file):
    with open(file, 'w') as f:
        for link in sorted(setData):
            f.write(link+'\n')