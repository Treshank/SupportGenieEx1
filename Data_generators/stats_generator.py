import Classes.Issue as Issue
import Classes.Agent as Agent
from Data_generators.helper_fns import time_gen_regulator, make_time, s2t, fill_up_object
from Data_generators.object_fns import agent_queue_handler


def create_agents(no_of_agents):
    for i in range(0, no_of_agents):
        Agent.Agent(i)


def generate_data(no_of_agents, no_of_req=None, avg_res_time=None, avg_aban_time=None):
    h = 9
    m = 0
    s = 5
    create_agents(no_of_agents)
    agents_avail = Agent.Agent.get_instances()
    queue = []
    req_no = 0
    for agent in agents_avail:
        if agent.issue_assigned is None:
            h, m, s = make_time(h, m, s, no_of_agents)
            arrival_time = str(f'{h}:{m}:{s}')
            req_no += 1
            generated_issue = Issue.Issue(arrival_t=arrival_time)
            agent.issue_assigned = generated_issue
            fill_up_object(agent)
    while h < 17:
        h, m, s = make_time(h, m, s, no_of_agents)
        arrival_time = str(f'{h}:{m}:{s}')
        generated_issue = Issue.Issue(arrival_t=arrival_time)
        agent_queue_handler(agents_avail, queue, generated_issue)
        queue.append(generated_issue)
        req_no += 1
        if no_of_req is not None and no_of_req == req_no:
            break
    avg_response_time = Issue.Issue.avg_response_time()
    avg_abandonment_time = Issue.Issue.avg_abandonment_time()
    if no_of_req == req_no:
        ele_in_queue = len(queue)-1
        avg_response_time = (avg_response_time + avg_res_time) // 2
        multiplier = ele_in_queue // no_of_agents + 1
        waiting_time = avg_response_time*multiplier
    else:
        waiting_time = 0
    return avg_response_time, avg_abandonment_time, waiting_time



