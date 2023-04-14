import requests
import time
import threading

# Free API
def getURL():
    return "https://official-joke-api.appspot.com/random_joke"


def requestFunction(n):
    for i in range(n):
        response = requests.get(getURL())
        print(f"Thread Response Text : {response.text}")


if __name__ == "__main__":
    totalRequests = 20

    start = time.perf_counter()

    for i in range(totalRequests):
        response = requests.get(getURL())
        print(f"Sequential Response Text : {response.text}")

    # Sequential Requests took :  19.166 seconds
    print(f"Sequential Requests took :  {time.perf_counter() - start} seconds ")

    start = time.perf_counter()

    # Split 20 requests among 4 Threads
    threads = [threading.Thread(target=requestFunction, args=(5,)) for _ in range(4)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Thread Requests took :  4.629 seconds
    print(f"Thread Requests took :  {time.perf_counter() - start} seconds ")
