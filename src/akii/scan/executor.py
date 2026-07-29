from concurrent.futures import ThreadPoolExecutor, as_completed

from akii.scan.scanner import scan


def execute(tasks, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(scan, task)
            for task in tasks
        ]

        for future in as_completed(futures):
            yield future.result()
