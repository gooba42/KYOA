#!/usr/bin/python3


class challenge:
    """This represents the generic challenge object. It takes a level/die
    a type (which skill it should use) and a text description. """

    def __init__(self, level, type, flavorText):
        self.level = level
        self.type = type
        self.description = {'Description': flavorText,
                            'Success': "You've pulled it off and succeeded at " + self.type + "!",
                            'Failure': "You've failed at " + type + ".",
                            'Declined': "You've refused to perform " + type + "."}

    def __call__(self):
        return self.description["Description"]

    def success(self):
        return self.description["Success"]

    def failure(self):
        return self.description["Failure"]

    def accepted(self, roll):
        if roll > self.level:
            return self.success()
        else:
            return self.failure()

    def declined(self):
        return self.description["Declined"]
