from Objects import Agent, Issue
from Data_generators.helper_fns import t2s, s2t
import datetime
import random


def fill_up_object(agent):
    arrival_time = s2t(agent.issue_assigned.arrival_time)
    response_time = arrival_time + datetime.timedelta(seconds=random.randint(10, 50))
    completion_time = response_time + datetime.timedelta(seconds=random.randint(540, 1500))
    agent.issue_assigned.result = 'r'
    agent.issue_assigned.response_time = str(response_time.time())
    agent.issue_assigned.completion_time = str(completion_time.time())



