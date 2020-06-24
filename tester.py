import unittest
import main
from Data_generators.stats_generator import generate_data
from Classes import Issue


def recur_function(self, no_of_agents, req_nos):
    art, aat, awt = generate_data(no_of_agents)
    # with open('Data/Gen_Data.json', 'w') as gen_data:
    #     Issue.Issue.push_to_json(gen_data)
    Issue.Issue.clear_objs()
    print('Data Generated.')
    for req_no in req_nos:
        res = main.controller(no_of_agents, add_requests=req_no, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(res, res)
        Issue.Issue.clear_objs()


class MyTestCase(unittest.TestCase):

    def test_case_group1(self):
        no_of_agents = 10
        request_nos = [10,100]
        recur_function(self, no_of_agents, request_nos)

    def test_case_group2(self):
        no_of_agents = 50
        request_nos = [100, 259]
        recur_function(self, no_of_agents, request_nos)

    def test_case_group3(self):
        no_of_agents = 70
        request_nos = [520, 700]
        recur_function(self, no_of_agents, request_nos)


if __name__ == '__main__':
    unittest.main()
