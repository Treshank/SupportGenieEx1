from Data_generators.helper_fns import s2t
import json


def obj_dict(obj):
    return obj.__dict__


class Issue:
    _issues = []  # Stores the objects of class

    def __init__(self, arrival_t, result=None, response_t='00:00:00', completion_t='00:00:00', abandoned_t='00:00:00'):
        self.arrival_time = arrival_t
        self.result = result
        self.response_time = response_t
        self.completion_time = completion_t
        self.abandoned_time = abandoned_t
        self.__class__._issues.append(self)

    @classmethod
    def get_intances(cls):
        return cls._issues

    @classmethod
    def avg_response_time(cls):
        total_res_time = 0
        no_of_res = 0
        for obj in cls._issues:
            if obj.result == 'r':
                no_of_res += 1
                res_time = (s2t(obj.response_time) - s2t(obj.arrival_time)).total_seconds()
                total_res_time += res_time
        avg_res_time = total_res_time // no_of_res
        return avg_res_time

    @classmethod
    def avg_abandonment_time(cls):
        total_abandonment_time = 0
        no_of_aban = 0
        for obj in cls._issues:
            if obj.result == 'a':
                no_of_aban += 1
                aban_time = (s2t(obj.abandoned_time) - s2t(obj.arrival_time)).total_seconds()
                total_abandonment_time += aban_time
        if no_of_aban == 0:
            return 0
        else:
            avg_abandonment_time = total_abandonment_time // no_of_aban
            return avg_abandonment_time

    @classmethod
    def clear_objs(cls):
        for obj in cls._issues:
            del obj
        cls._issues = []

    @classmethod
    def push_to_json(cls, file):
        string = json.dumps(cls._issues, default=obj_dict)
        loaded = json.loads(string)
        formatted = json.dumps(loaded, indent=4)
        json.dump(formatted, file)
        # print(formatted) #Uncomment to print formatted json in console
