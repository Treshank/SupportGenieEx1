### ```agent_empty()```
This function is used to extract agents that have completed their issue and are now free. It is primarily used by ```agent_queue_handler()``` it returns a list of empty agents.

### ```agent_queue_handler()```
The function is used to see if queued issues can be assigned to agents. ``agent_empty()`` is called to determine the free agents. The queue is iterated through having 2 possibilities. 

If they have waited too long then they are removed from queue and marked as abandoned (3 to 5 min). Otherwise if there are free agents, the element is assigned to the agent, and the agent is removed from list of free agents. 
