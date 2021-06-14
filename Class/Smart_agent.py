from mesa import Agent

class Natural_agent(Agent):
    """
    An agent on Social Media.
    """

    def __init__(self, unique_id, model, status = 0):
        super().__init__(unique_id, model)
        self.status = status

    def step(self):
        # The agent's step will go here.
        pass
