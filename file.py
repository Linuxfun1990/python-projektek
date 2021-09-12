import time,random, threading, queue 
from utilities.file_utils import get_files

MAX_THREADS = 6

job_list = queue.Queue()
[

    job_list.put(i) for i in get_files('/home/mike/Képek', ext='.jpg')
]



def worker():
    while not job_list.empty():

        next_file = job_list.get()
        print(f'Working on:{next_file}')
        time.sleep(random.randint(1, 10))
        print('Worker finished')

        job_list.task_done()


for _ in range(MAX_THREADS):
       t = threading.Thread(target=worker)
       t.start()