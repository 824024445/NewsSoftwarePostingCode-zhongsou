#!/usr/bin/env python
from begin import obtain_url
from multiprocessing import Process
from multiprocessing import Pool
from foo.send_url import send_url
from foo.send_email import send_email
map_lists = ["经济圈", "摄影圈", "男人圈", "社会百科", "内涵段子"]


def send_start(i):
    try:
        obtain_url(i)
    except:
        send_url(i)
    print(map_lists[i]+ "发帖完成")


if __name__ == "__main__":
    try:
        p = Pool(5)
        for i in range(5):
            p.apply_async(send_start, args=(i,))
        print('Waiting for all subproces'
              'ses done...')
        p.close()
        p.join()
    except:
        print("Error: 无法启动线程")









