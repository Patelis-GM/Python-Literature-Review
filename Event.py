import threading

sharedVariable = 0


def adderThread(event):
    global sharedVariable
    for i in range(10):
        sharedVariable += 1
    print("Adder thread finished")
    # Notify the printerThread
    event.set()


def printerThread(event):
    global sharedVariable
    # Wait for adderThread to finish
    event.wait()
    print(f"Shared variable is {sharedVariable}")
    print("Printer thread finished")


if __name__ == "__main__":
    threads = []
    event = threading.Event()
    threads.append(threading.Thread(target=printerThread, args=(event,)))
    threads.append(threading.Thread(target=adderThread, args=(event,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
