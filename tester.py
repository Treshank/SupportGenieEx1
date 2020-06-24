import unittest
import main
from Data_generators.stats_generator import generate_data
from Classes import Issue


class MyTestCase(unittest.TestCase):

    def test_case_group1(self):
        no_of_agents = 10
        art, aat, awt = generate_data(no_of_agents)
        # with open('Data/Gen_Data.json', 'w') as gen_data:
        #     Issue.Issue.push_to_json(gen_data)
        print('Data Generated')
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=10, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(0, res)
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=50, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(res, res)

    def test_case_group2(self):
        no_of_agents = 50
        art, aat, awt = generate_data(no_of_agents)
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=50, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(0, res)
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=150, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(res, res)

    def test_case_group3(self):
        no_of_agents = 70
        art, aat, awt = generate_data(no_of_agents)
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=520, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(res, res)
        Issue.Issue.clear_objs()
        res = main.controller(no_of_agents, add_requests=700, art=art, aat=aat)
        print(int(res), 'seconds')
        self.assertEqual(res, res)


if __name__ == '__main__':
    unittest.main()
