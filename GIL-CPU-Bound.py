import time
import threading

sequentialVariable = 0
threadVariable = 0

def sequentialAddition(n):
    global sequentialVariable
    for _ in range(n):
        sequentialVariable += 1


def threadAddition(n, lock):
    global threadVariable
    for _ in range(n):
        lock.acquire()
        threadVariable += 1
        lock.release()


if __name__ == "__main__":

    times = 1000000
    start = time.perf_counter()

    sequentialAddition(times)

    # Sequential addition took :  0.08666570000059437 seconds
    print(f"Sequential addition took :  {time.perf_counter() - start} seconds ")

    start = time.perf_counter()
    threads = []

    # Lock object to protect the critical section
    lock = threading.Lock()

    # Split 1000000 additions task among 4 Threads
    for i in range(4):
        threads.append(threading.Thread(target=threadAddition, args=(times // 4, lock)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Thread addition took :  0.8813463000005868 seconds
    print(f"Thread addition took :  {time.perf_counter() - start} seconds ")
