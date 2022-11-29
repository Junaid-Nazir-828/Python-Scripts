#import multiprocessing
import time
import concurrent.futures


def do(sec):
    print(f'Sleeping for {sec} sec..')
    time.sleep(sec)
    print('Done Sleeping')

if __name__ == '__main__':

    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do,1) for _ in range(10)]

    finish = time.perf_counter()


    # start = time.perf_counter()
    
    # p1 = multiprocessing.Process(target=do)
    # p2 = multiprocessing.Process(target=do)

    # p1.start()
    # p2.start()

    # p1.join()
    # p1.join()

    # finish = time.perf_counter()

    
    # start = time.perf_counter()
    
    # proccesses = []

    # for i in range(10):
    #     p1 = multiprocessing.Process(target=do,args=[1.5])
    #     p1.start()
    #     proccesses.append(p1)

    # for process in proccesses:
    #     process.join()    

    # finish = time.perf_counter()        

    # start = time.perf_counter()
    # do()
    # do()
    # do()
    # do()
    # do()
    # do()
    # do()
    # do()
    # do()
    # do()
    # finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} sec...')