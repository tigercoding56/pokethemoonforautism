cquests = []
class quest():
    def __init__(self):
        self.name = ""
        self.active = 0
    def complete(self):
        self.active =0
    def give(self):
        self.active = 1

class dialog():
    def __init__(self):
        self = self
    def lvl(self,level=0,ans=1):
        if ans == 1:
            return ["EXIT DIALOG ",["yes","no"]]
        else:
            return "EXIT"
