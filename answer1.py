counter = 3

def tester():
    # global counter was added in order to include the variable "counter" in the function scope
    global counter
    counter += 1
    print(counter)

tester()