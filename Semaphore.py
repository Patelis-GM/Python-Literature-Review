import threading


def threadFunction(semaphore, otherSemaphore, i):
    semaphore.acquire()
    for _ in range(2):
        otherSemaphore.acquire()
        print(f'Hello from Thread - {i}')
        otherSemaphore.release()

    print()
    semaphore.release()


if __name__ == "__main__":
    threads = []

    # Semaphore object to allow only 2 Threads
    # to enter the for - loop critical section at a time
    semaphore = threading.Semaphore(2)

    # Semaphore object to allow only 1 Thread
    # to enter the print critical section at a time
    otherSemaphore = threading.Semaphore(1)
    for i in range(4):
        threads.append(threading.Thread(target=threadFunction, args=(semaphore, otherSemaphore, i)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
