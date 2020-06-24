#### ```time_gen_regualor()```
  This function dictates how long before another request comes in. 
  On an average in a 8 hour shift an agent would take 30-50 request in a day. 
  
  Let ```x``` be the requests taken in a day by an agent. ``x * no_of_agents`` would be the total number of calls in a day. 
  
  ```(x * no_of_agents) / 8 ``` would be the number of calls per hour. 
    ```((x * no_of_agents) / 8 ) / 60 ``` would be the number of calls per minute. 
    
   Then we divide a minute by the obtained number to see how many seconds before a call must be made making sure that the time interval stays within limit. 
   Then a random number within 5 seconds of generated number is sent keeping the random nature of requests. 
   
   **Note: It is probably far from what happens in reality, but good enough to work with**
   
