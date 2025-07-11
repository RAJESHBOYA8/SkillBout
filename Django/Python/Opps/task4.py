class User:
    def login(self):
        print("Login")
class BussinessUser(User):
    def run_add(self):
        print("run add")
b=BussinessUser()
b.login()
b.run_add()