Hello viewer :)

I hope you are having a great day.

Thank you for allowing me to complete this assessment. It was a lot of fun taking on these tasks you supplied. I hope I have fulfilled them to your standards.

Installing the prerequisite

Python

    sudo apt install python3
Pip python package manager

    sudo apt install python3-pip
Pytest library

    sudo pip install pytest
Requests library

    sudo pip install requests
Docker

    sudo apt install docker.io
Vim as an editor

    sudo apt install vim
Tasks Handled: 1) Question 1

a )  The counter variable was not included in the scope of the function.
  Thus, I added the "global counter" to correct this error.
2) Question 2

a )  Running question2.py through pytest results in a failure message.
    Thus, I changed the value of inc() from 3 to 4 for the function to succeed and saved the file as answer2.

b )  *Images included as proof*
3) Question 3

a )  Created a python script named response_time.py

    vim response_time.py

b )  Imported the following python libraries: request, time, os

    import requests
    import time
    import os

c )  Define a function that takes an int(NUM) and an str(URL) variable

    def response_time(NUM, URL):

d )  Set a float variable called "time_lapse" in order to sum the total response time

    time_lapse = 0.0

e )  Included a time method from the time library to record the function time elapsed

    start = time.time()
    ***
    end = time.time()

f )  Created a for loop to iterate over the request object and assign it to web_object

    for i in range(int(NUM)):

        web_object = requests.get(str(URL))

g )  Assigned a compound assignment operator to the time_lapse variable to get the sum of the total seconds for the time elapsed

    time_lapse += web_object.elapsed.total_seconds()

 h ) Added a print function that prints the websites response time and formatted it to display to the 6th decimal

    print("Website response time: " + str("%.6f" % time_lapse) + " seconds")

 i ) Added a print function that prints the functions response time and formatted it to display to the 6th decimal

    print(f"Function response time: {end - start:0.6f} seconds")

 j ) Call the function with environment variables from the os library read from the dockerfile

    response_time(os.environ['NUM'], os.environ['URL'])
4) Question 4

a ) Created a docker file

    vim dockerfile

b ) Docker file content with the environment variables

    FROM python:latest

    LABEL Maintainer="etienne.henn@gmail.com"

    ENV NUM=10 \

        URL="https://al.co.za"

    WORKDIR /home

    RUN pip install requests

    COPY response_time.py ./

    CMD ["python","./response_time.py"]

c ) Build the docker image

    sudo docker image build -t pythonbuild:0.0.1 /home/"insert user name here"/autumleafassessment

d ) Run the docker image

    sudo docker run pythonbuild:0.0.1
5) Question 5

a ) Clone GitHub repository

    git clone https://github.com/EtienneHenn/Autum-Leaf-Assesment.git

b ) Add files to Git

    git add .

c ) Commit files to remote repository

    git commit -m "This is my final commit"

d ) Pushed the files to GitHub

    git push origin main
