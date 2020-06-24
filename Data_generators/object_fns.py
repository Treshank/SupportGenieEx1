from Data_generators.helper_fns import s2t, t2s
import random
import datetime


def agent_empty(agents, generated_issue):
    free_agents = []
    for agent in agents:
        if agent.issue_assigned is not None and s2t(agent.issue_assigned.completion_time) < s2t(generated_issue.arrival_time):
            agent.issue_assigned = None
            free_agents.append(agent)
        elif agent.issue_assigned is None:
            free_agents.append(agent)
    return free_agents


def agent_queue_handler(agents, queue, generated_issue):
    free_agents = agent_empty(agents, generated_issue)
    for ele in queue:
        leave = datetime.timedelta(seconds=random.randrange(180, 300))
        if (s2t(generated_issue.arrival_time) - s2t(ele.arrival_time)) > leave:
            ele.result = 'a'
            ele.abandoned_time = t2s(s2t(ele.arrival_time) + leave)
        else:
            free_agents[0].issue_assigned = ele
            free_agents = free_agents[1:]
