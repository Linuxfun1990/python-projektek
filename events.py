import threading, time, random


downloadig = threading.Event()

def downloader_worker():
    print('Download started')
    time.sleep(random.randint(1,10))

    print('Download finished')
    downloadig.set()




def file_worker():
    downloadig.wait()
    print('File_worker started')  

t1 = threading.Thread(target=downloader_worker)
t2 = threading.Thread(target=file_worker)


t1.start()
t2.start()


#event commads
#print(downloadig.is_set())
#downloadig.set()
#print(downloadig.is_set())
#downloadig.clear
#print(downloadig.is_set())