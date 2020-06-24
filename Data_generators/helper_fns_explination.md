#### ```time_gen_regualor()```
  This function dictates how long before another request comes in. 
  On an average in a 8 hour shift an agent would take 30-50 request in a day. 
  
  Let ```x``` be the requests taken in a day by an agent. ``x * no_of_agents`` would be the total number of calls in a day. 
  
  ```(x * no_of_agents) / 8 ``` would be the number of calls per hour. 
    ```((x * no_of_agents) / 8 ) / 60 ``` would be the number of calls per minute. 
    
   Then we divide a minute by the obtained number to see how many seconds before a call must be made making sure that the time interval stays within limit. 
   Then a random number within 5 seconds of generated number is sent keeping the random nature of requests. 
   
   **Note: It is probably far from what happens in reality, but good enough to work with**
   
#### ```fill_up_object()```
Since this function only fills up inital objects, the response time is considered as a random number between 10 and 50 seconds. The completion time is set as a random number between 15min and 30min. 
These values are then set to the agent passed as parameter after setting result is ``'r'``, meaning responded. 


#### ```make_time()```
Use to make vaild hours, min, and sec from given time range incriment.

#### ```s2t()```
converts a stirng to a datetime object.

#### ```t2s()```
converts a datetime object to string

#### ```t2sec()```
converts datetime object to int in seconds. 
