

class Proof(object):

    def __init__(self):
        super().__init__()
        self.steps = []
        self.conditions = []

    def __len__(self):
        return len(self.steps)

    def __getitem__(self, key):
        return self.steps[key-1]

    def condition(self, prop):
        """Add a proposition as a step and a condition"""
        self.steps.append(prop)
        self.conditions.append(prop)
    
    def therefore(self, prop):
        """Add a proposition as a step"""
        self.steps.append(prop)

    @property
    def last(self) -> "Prop":
        """Returns the last proposition added"""
        return self.steps[-1]
