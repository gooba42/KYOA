#!/usr/bin/python3


class Challenge:
    """This represents the generic challenge object. It takes a level/die
    a type (which skill it should use) and a text description. """
    Level = 0
    Type = "Cook some beans"
    Description = ""

    def __init__(self, level, action_name, flavor_text):
        self.Level = level
        self.Type = action_name
        self.Description = {'Description': flavor_text,
                            'Success': "You've pulled it off and succeeded at " + self.Type + "!",
                            'Failure': "You've failed at " + action_name + ".",
                            'Declined': "You've refused to perform " + action_name + "."}

    def __call__(self):
        return self.Description["Description"]

    def success(self):
        return self.Description["Success"]

    def failure(self):
        return self.Description["Failure"]

    def accepted(self, roll):
        if roll > self.Level:
            return self.success()
        else:
            return self.failure()

    def declined(self):
        return self.Description["Declined"]
