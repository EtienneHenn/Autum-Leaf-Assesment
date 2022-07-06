# Autum-Leaf-Assesment

Hello viewer :)

I hope you are having a great day.

Thank you for allowing me to complete this assessment.
It was a lot of fun taking on these tasks you supplied.
I hope I have fulfilled them to your standards. 

**Tasks Handled:**
1)  **Question 1**

    a)  The counter variable was not included in the scope of the function.
      Thus, I added the "global counter" to correct this error.

2)  **Question 2**

    a)  Running question2 through pytest results in a failure message.
        Thus, I changed the value of inc() from 3 to 4 in order for the function to succeed and saved the file as answer2.
        
    b)  *Images included as proof*

3)  **Question 3**

    a)  Created a python script named response_time.py
    
    b)  Imported the following python libraries: request, time, os
        
        import requests
        import time
        import os
        
    c)  Define a function that takes a int(num) and a str(link) variable
    
        def response_time(num, link):
    
    d)  Created a float variable called "time_lapse" in order to sum the response time
    
        time_lapse = 0.0
    
    e)  Included a time method from the time library to record the functions time elapsed
        
        start = time.time()
        ***
        end = time.time()
    
    f)  Created a for loop to iterrate over the request object and assign it to web_object
        
        for i in range(int(num)):

            web_object = requests.get(str(link))
    
    g)  Assigned a compound assignment operator to the time_lapse variable in order to get the sum of the total seconds for the time elapsed
    
        time_lapse += web_object.elapsed.total_seconds()
        
     h) Added a print function that prints the websites response time
        
        print("Website response time: " + str(time_lapse) + " seconds")
        
     i) Added a print function that prints the functions response time
        
        print(f"Function response time: {end - start:0.6f} seconds")
        
     j) Call tthe funtion with environment variables from the os library
        
        
        

4)  **Question 4**


5)  
