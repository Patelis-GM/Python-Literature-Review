import asyncio
import time

import httpx as httpx
import requests


# Free API
def getURL():
    return "https://official-joke-api.appspot.com/random_joke"


# Coroutine to send a GET request in an asynchronous manner
async def sendAsynchronousRequest(client):
    response = await client.get(getURL())
    if response.status_code == 200:
        print(response.json())
    else:
        print("Request failed")


async def asynchronousMain(n):
    client = httpx.AsyncClient()

    # Create a set of Task objects
    tasks = [sendAsynchronousRequest(client) for _ in range(n)]

    # Schedule and execute the set of Task objects within the Event Loop
    await asyncio.gather(*tasks)
    await client.aclose()


# Function to send a GET request in a synchronous manner
def sendSynchronousRequest():
    response = requests.get(getURL())
    return response


def synchronousMain(n):
    for i in range(n):
        response = sendSynchronousRequest()
        if response.status_code == 200:
            print(response.json())
        else:
            print("Request failed")


if __name__ == "__main__":
    totalRequests = 20

    start = time.perf_counter()
    synchronousMain(totalRequests)

    # Synchrounous requests took : 21.034seconds
    print(f"Synchrounous requests took : {time.perf_counter() - start} seconds")

    start = time.perf_counter()
    asyncio.run(asynchronousMain(totalRequests))

    # Asynchrounous requests took : 1.386 seconds
    print(f"Asynchrounous requests took : {time.perf_counter() - start} seconds")
