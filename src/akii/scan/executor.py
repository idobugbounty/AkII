from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Thread

q = Queue()


def ui_worker():
    while True:
        result = q.get()

        if result is None:
            break

        print(result)

        q.task_done()


def execute(tasks, worker, max_workers=10):
    ui = Thread(target=ui_worker)
    ui.start()

    def wrapped(task):
        result = worker(task)
        q.put(result)
        return result

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(wrapped, tasks))

    q.put(None)
    ui.join()

    return results