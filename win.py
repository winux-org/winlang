

keyWords = ["import"]


class Import:
    moduleName = ""

    def __init__(self, other_data):
        self.other_data = other_data

with open("./Examples/hello_world.win") as file:
    for line in file.readlines():
        print(line)