import threading

safeVariable = 0

def threadSafe(lock):
    global safeVariable
    for _ in range(100):
        # Acquire the lock
        lock.acquire()
        safeVariable += 1
        # Release the lock
        lock.release()


if __name__ == "__main__":

    lock = threading.Lock()

    # Creation of two competing Threads
    threads = []
    threads.append(threading.Thread(target=threadSafe, args=(lock,)))
    threads.append(threading.Thread(target=threadSafe, args=(lock,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Guaranteed to print 200 as the code is thread safe
    print(safeVariable)
