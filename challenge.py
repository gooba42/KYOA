#!/usr/bin/python3


class challenge:
    """This represents the generic challenge object. It takes a level/die
    a type (which skill it should use) and a text description. """

    def __init__(self, level, type, description):
        self.level = level
        self.type = type
        self.description = description

    def __call__(self):
        return self.description["Description"]

    def success(self):
        return self.description["Success"]

    def failure(self):
        return self.description["Failure"]

    def accepted(self, roll):
        if(roll > 2):
            self.success()
        else:
            self.failure()

    def declined(self):
        return self.description["Declined"]
