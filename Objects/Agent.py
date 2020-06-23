
class Agent:
    _agents = []

    def __init__(self, agent_no):
        self.agent_no = agent_no
        self.issue_assigned = None
        self.__class__._agents.append(self)

    @classmethod
    def get_instances(cls):
        return cls._agents
