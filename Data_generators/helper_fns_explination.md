#### [```time_gen_regualor()```](https://github.com/Treshank/SupportGenieEx1/blob/1afd08a15721b6c434d4bfc9abb13d17bc35e694/Data_generators/helper_fns.py#L5)
  This function dictates how long before another request comes in. 
  On an average in a 8 hour shift an agent would take 30-50 request in a day. 
  
  Let ```x``` be the requests taken in a day by an agent. ``x * no_of_agents`` would be the total number of calls in a day. 
  
  ```(x * no_of_agents) / 8 ``` would be the number of calls per hour. 
    ```((x * no_of_agents) / 8 ) / 60 ``` would be the number of calls per minute. 
    
   Then we divide a minute by the obtained number to see how many seconds before a call must be made making sure that the time interval stays within limit.
   **Note: It is probably far from what happens in reality, but good enough to work with**
   
#### [```fill_up_object()```](https://github.com/Treshank/SupportGenieEx1/blob/1afd08a15721b6c434d4bfc9abb13d17bc35e694/Data_generators/helper_fns.py#L36)
Since this function only fills up inital objects, the response time is considered as a random number between 10 and 50 seconds. The completion time is set as a random number between 15min and 30min. 
These values are then set to the agent passed as parameter after setting result is ``'r'``, meaning responded. 


#### ```make_time()```
Use to make vaild hours, min, and sec from given time returned by calling ``time_gen_regulator()`` to recive incremental value.

#### ```s2t()```
converts a stirng to a datetime object.

#### ```t2s()```
converts a datetime object to string

#### ```t2sec()```
converts datetime object to int in seconds. 
