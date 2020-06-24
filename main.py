from Data_generators import stats_generator
import Objects.Issue as Issue


def controller(no_of_agents, add_requests):
    art, aat, awt = stats_generator.generate_data(no_of_agents)
    # print(art, aat, awt)
    with open('Data/Gen_Data.json', 'w') as gen_data:
        Issue.Issue.push_to_json(gen_data)
    print('Data Generated')
    Issue.Issue.clear_objs()
    art, aat, awt = stats_generator.generate_data(no_of_agents, add_requests, art, aat)
    # print(art, aat, awt)
    return awt
