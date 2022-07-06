import requests
import time
import os

def response_time(NUM,URL):

    time_elapsed = 0.0
    start = time.time()
    
    for i in range(int(NUM)):
        web_object = requests.get(str(URL))
        time_elapsed += web_object.elapsed.total_seconds()

    end = time.time()
    print("Website response time: " + str("%.6f" % time_elapsed) + " seconds")
    print(f"Function response time: {end - start:0.6f} seconds")


response_time(os.environ['NUM'], os.environ['URL'])
