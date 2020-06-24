import random
import datetime


def time_gen_regulator(no_of_agents):
    req_per_min = ((random.randrange(30, 50) * no_of_agents) // 8) // 60
    if req_per_min < 1:
        req_per_min = 1
    time_int = 60 // req_per_min
    return time_int


def make_time(h, m, s, no_of_agents):
    s += time_gen_regulator(no_of_agents)
    if s > 59:
        m += 1
        s %= 60
        if m > 59:
            h += 1
            m %= 60
    return h, m, s


def s2t(str_time):
    return datetime.datetime.strptime(str_time, '%H:%M:%S')


def t2s(time):
    return str(time.time())


def t2sec(time):
    return (time.hour * 60 + time.minute) * 60 + time.second


def fill_up_object(agent):
    arrival_time = s2t(agent.issue_assigned.arrival_time)
    response_time = arrival_time + datetime.timedelta(seconds=random.randint(10, 50))
    completion_time = response_time + datetime.timedelta(seconds=random.randint(900, 1800))
    agent.issue_assigned.result = 'r'
    agent.issue_assigned.response_time = str(response_time.time())
    agent.issue_assigned.completion_time = str(completion_time.time())
