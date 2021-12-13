import json

class Data_read:
    # singleton
    __instance = None

    @staticmethod
    def get_instance():
        if Data_read.__instance is None:
            with Data_read.Lock():
                if Data_read.__instance is None:
                    Data_read()
        return Data_read.__instance

    def __init__(self):
        if Data_read.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            Data_read.__instance = self
        with open('user_data.json', 'r') as openfile:
            # Reading from json file
            self.json_object = json.load(openfile)

    def print_user(self,user):
        print(self.json_object["employee"][user])

    def check_user_exist(self,user):
        if (user in self.json_object["employee"]):
            reply = True
        else:
            reply = False
        return reply

