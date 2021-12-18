import json

class DataRead:
    # singleton
    __instance = None

    @staticmethod
    def get_instance():
        if DataRead.__instance is None:
            with DataRead.Lock():
                if DataRead.__instance is None:
                    DataRead()
        return DataRead.__instance

    def __init__(self):
        if DataRead.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            DataRead.__instance = self
        with open('user_data.json', 'r') as openfile:
            # Reading from json file
            self.json_object = json.load(openfile)

    def print_user(self,user):
        print(self.json_object["employee"][user])

    def check_user_exist(self,user):
        if user in self.json_object["employee"]:
            reply = True
        else:
            reply = False
        return reply

    def get_name(self,empno):
        name = (self.json_object["employee"][empno]["name"])
        return name

    def get_current_salary(self,empno):
        current_salary = (self.json_object["employee"][empno]["currentBaseSalary"])
        return current_salary

    def get_current_leave(self,empno):
        current_annual_leave = (self.json_object["employee"][empno]["annualLeave"])
        return current_annual_leave

    def get_salary_year(self,empno,year):
         basic_salary= (self.json_object["employee"][empno]["year"][year]["basicPay"])
         overtime = (self.json_object["employee"][empno]["year"][year]["overTime"])
         return basic_salary, overtime

    def get_year_annual(self,empno,year):
        an_leave = (self.json_object["employee"][empno]["year"][year]["leave"])
        return an_leave