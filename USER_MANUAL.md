This file only shows how the project can be used. I would highly recommned reading the README file to better understand how program works. 

#### Before you start using this you must understand a few things. 

* This data prediction will show you many different values for the same test cases as the data generated is random in nature.
* The model will probably need some changes in in logic before it can be put into use.
* Prepare to see lots of zeros. 

#### Running it
Inorder to run it you can simply run ``tester.py``. 

The first parameter dictates the number of agents and the 2nd dictates number of requests. The program always predicts the waiting time for last request. 

The file has 6 test cases. Under all circumstances, the fisrt 3 given test cases shall give 0sec as answer. Any test case which has less or equal number of requests than its number of agents results in 0sec 

Apart from having 0 as an answer in such situations, the answer will be 0 if in the situation the queue is empty and probably the answer will vary from run to run as the data generated is random much real life. 

If you want to access the functions directly call ``contoller()`` from ``main.py``. 
