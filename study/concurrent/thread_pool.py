import threadpool
import time
import Queue


class SharedVariables:
    def __init__(self):
        self.global_mark = False


def thread_function(my_int):
    print type(my_int)
    time.sleep(1)
    return my_int


def callback_function(request, result):
    print "the result is %s %r\n" % (request.requestID, result)


def init_my_list():
    q = Queue.Queue()
    for i in range(100):
        q.put(i)
    return [q.get() for i in range(q.qsize())]


def run_demo():
    argument_list = init_my_list()
    # master/boss thread creates forked threads or workers
    pool = threadpool.ThreadPool(20)
    # initialize task queues
    requests = threadpool.makeRequests(thread_function, argument_list, callback_function)
    for req in requests:
        pool.putRequest(req)
    pool.wait()


if __name__ == '__main__':
    run_demo()
