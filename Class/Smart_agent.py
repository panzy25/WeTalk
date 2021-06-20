from mesa import Agent
from .Basic_info import State

class Natural_agent(Agent):
    """
    An agent on Social Media.
    """

    def __init__(
        self,
        unique_id,
        model,
        initial_state,
        info_spread_chance,
        info_check_frequency,
        recovery_chance,
        gain_resistance_chance,
    ):
        super().__init__(unique_id, model)

        self.state = initial_state

        self.info_spread_chance = info_spread_chance
        self.info_check_frequency = info_check_frequency
        self.recovery_chance = recovery_chance
        self.gain_resistance_chance = gain_resistance_chance

    def try_to_infect_neighbors(self):
        neighbors_nodes = self.model.grid.get_neighbors(self.pos, include_center=False)
        susceptible_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.SUSCEPTIBLE
        ]
        for a in susceptible_neighbors:
            if self.random.random() < self.info_spread_chance:
                a.state = State.INFECTED

    def try_gain_resistance(self):
        if self.random.random() < self.gain_resistance_chance:
            self.state = State.RESISTANT

    def try_remove_infection(self):
        # Try to remove
        if self.random.random() < self.recovery_chance:
            # Success
            self.state = State.SUSCEPTIBLE
            self.try_gain_resistance()
        else:
            # Failed
            self.state = State.INFECTED

    def try_check_situation(self):
        if self.random.random() < self.info_check_frequency:
            # Checking...
            if self.state is State.INFECTED:
                self.try_remove_infection()

    def step(self):
        if self.state is State.INFECTED:
            self.try_to_infect_neighbors()
        self.try_check_situation()