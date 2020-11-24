from multiprocessing import RLock
from threading import Thread

"""
A thread pool to handle concurrency
"""


class LimitedThread:
    def __init__(self, limit):
        self.thread_pool = []
        self.limit = limit
        self.lock = RLock()

    def check_thread_pool(self) -> bool:
        if len(self.thread_pool) >= self.limit:
            for thread in self.thread_pool:
                thread.join()
            self.thread_pool.clear()
            return False
        return True

    def insert_thread(self, target, args):
        self.check_thread_pool()
        process = Thread(target=target, args=args + [self.lock])
        process.start()
        self.thread_pool.append(process)

    def wait_to_end(self):
        for thread in self.thread_pool:
            thread.join()
