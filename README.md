# SupportGenieEx1
  This program was made as an assignment to submit for an internship as a test. The code will be explained as detailed as possible. Any issues in the code or its explination are welcome in the Issues section. 
  
### Disclaimer
  The program works on the basis of generated data. In order to achieve this, a random data generator is made such that the data generated is close to what is expected from a good call service provider. Due to this data generation takes time and I would highly recommend that in order to not use parameters that are too large as it would take alot of time to generate it's data.
  
**The accuracy of the program is always questionable. I guess we'll never know until real world data is used and verified.**

# Introduction
  This program is used to predict the time a caller would have to wait before the request would be answered. It follows a simple set of steps in order to do so.
  1. [Generate data](https://github.com/Treshank/SupportGenieEx1/blob/master/README.md#generating-data).
  2. Calculate the waiting and abandonment times. 
  3. Create data based on number of requests. 
  4. Correct the calculated times.
  5. Predict the time to wait.
  
**Note: It would help to have the code open in another window**
  
  If you are looking for a machine learning solution to this problem, you may stop reading this if you feel my justification for not using it is not convincing. If you aren't you can just skip ahead. 
  
 
 ### Why not machine learning? 
  I have not used machine learning partly as I don't know any (Do mind its not that I don't want to learn) but mostly because of the following reasons:
  1. The mammoth ammout of data required and the 1000 new parameters I will have to create to train a model that would give me probably no proper conclusions due to the highly random nature of human beings. 
  2. I am using pseduo random numbers so the model would just find the pattern that generates these random numbers which would be a waste of effort.
  3. The number ranges of random numbers generated are based on statistics of good waiting times thus apart from correction of the phases that take too long out of the blue this should be able to give resonably good predictions
  4. For good predictiont the model would have to be very complicated. 
  5. This isn't enough time for me to master machine learning and I dont want to just slap in some statistical model without knowing what it is, and all that I think I know about machine learning is wrong and this would have been much simpler had I used it.  
  
  Maybe for another time this could be possible provided the resources from real world to work on it. 
  
  Now if you aren't convinced you may leave. 
  
 # The Classes
  The classes are fairly straight forward. 
  ## Agent
   #### Attributes: 
 ```_agents ``` is used to store the refernce to the objects created of Agent class.
  
 ```agent_no``` Stores what is equivalent to and id number given to an agent 
 
 ```issue_assigned``` Stores ```None```, when no issue is assigned to it and stores refernce to and object of type  ```Issue``` if an issue is assigned to an agent.
 Agent.
   #### Functions:
 ```get_intances(cls)``` is a class method that is used to retive ```_agents```
  ## Issue
   #### Attributes:
   ``` _issues ``` is used to store the refernce to the objects created of Issue class.
   
   ```arrival_time``` Time at which the issue arrives.
   
   ```result``` Stores 'r' or 'a' indicating responded or abandoned. If issue is responded to ```response_time``` and ```completion_time``` are set. If issue was abandoned ```abandoned_time``` is set.
   
   ```response_time``` Time at which the issue was request was accepted by an agent.
   
   ```completion_time``` Time at which the issue was closed by agent.
   
   ```abandoned_time``` Time at which Issue was abandoned. 
   #### Functions:
   ```avg_response_time(cls)``` Class method used to generate the average time taken to respond by all the objects created. 
   
   ```avg_abandonment_time(cls)``` Class method used to generate the average time before which a user would leave the request as it was not responded to. 
   
  ```clear_objs(cls)``` Class method that is used to delete all instances of class. 
  
  ```push_to_json(cls, file)``` Class method used to move all current class methods onto a json file. Used to debug the program and also see the data generated. **Note: The json dumped into file is not getting formated for some reason. Uncomment the print statement to print formatted json on the console or if you know the mistake let me know in the Issues section.**

# The Code
 ** Click on the heading to take yourself to the file containting the code being explained.
 ## Generating Data
 Most of the Data is generated using ```Data_generators.stats_generator.generate_data()```. It works as a control unit calling other functions of ```Data_generators```. The data generated is for a maximum of 7hrs or in the case of determining waiting time the number of requests.
 
 #### [``generate_data()``](https://github.com/Treshank/SupportGenieEx1/blob/master/Data_generators/stats_generator.py#L14)
  This function is used for 2 operations, to generate the data upon which perdictions are made and to generate the data before the request whoose waiting time is to be predicted. 
  The variables ```h = 9, m = 0, s = 5``` are indicating the service starts at 09:00:05. This would not be required really in the real world its just to generate the data. The agents are created using ```create_agents()``` in bulk. ```queue``` is used to hold all the objects that have arrived but not been assigned to an Agent. [```time_gen_regualor()```](https://github.com/Treshank/SupportGenieEx1/blob/master/Data_generators/helper_fns.py#L5)([read_more_here](https://github.com/Treshank/SupportGenieEx1/blob/master/Data_generators/helper_fns_explination.md#time_gen_regualor)) is used to generate time in incrementals specific to the workload ment for given number of agents. An Issue object is then created using the arrival time generated.
  ```
  for agent in agents_avail:
            if agent.issue_assigned is None:
                agent.issue_assigned = generated_issue
                fill_up_object(agent)
                fl = 1
                break
  ```
  
  The above snippet is used to check if any agents are free if they are then the issue is assigend to them and then the rest of the data is filled by ``[fill_up_object()](https://github.com/Treshank/SupportGenieEx1/blob/master/Data_generators/helper_fns.py#L39)`` ([more_here](https://github.com/Treshank/SupportGenieEx1/blob/master/Data_generators/helper_fns_explination.md#fill_up_object)). 
  
  The agents are then checked for possible completions to assign queue elements to the agents using ``[agent_queue_handler()](https://github.com/Treshank/SupportGenieEx1/blob/52e66e59445ed2bcc44b3c9badcec951e92cc491/Data_generators/object_fns.py#L12)``
  
  If the data was not assigned to an agent in the above snippet, the generated issue is queued.
  
  ```
  if no_of_req is not None and no_of_req == req_no:
            break
  ```
  The above snipped is used when a finite number of data must be generated .ie. no_of_req is passed to function call. This is done when the function is used in prediction phase.
  
  The average response time and the average abandonment time is then calculated for the dataset using the respective class functions.
  
  The rest of the function belongs to predictive side of this function and shall be explained below.  

 
         
  
  
  
    
  
  
