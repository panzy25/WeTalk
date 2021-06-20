import math
import networkx as nx
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import NetworkGrid

from .Basic_info import State
from .Basic_info import number_infected
from .Basic_info import number_susceptible
from .Basic_info import number_resistant
from .Basic_info import number_state
from .Smart_agent import Natural_agent

class Social_Network_Model(Model):
    """
        A virus model with some number of agents
    """

    def __init__(
            self,
            num_nodes=10,
            avg_node_degree=3,
            initial_outbreak_size=1,
            info_spread_chance=0.4,
            info_check_frequency=0.4,
            recovery_chance=0.3,
            gain_resistance_chance=0.5,
    ):

        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        self.initial_outbreak_size = (
            initial_outbreak_size if initial_outbreak_size <= num_nodes else num_nodes
        )
        self.info_spread_chance = info_spread_chance
        self.info_check_frequency = info_check_frequency
        self.recovery_chance = recovery_chance
        self.gain_resistance_chance = gain_resistance_chance

        self.datacollector = DataCollector(
            {
                "Infected": number_infected,
                "Susceptible": number_susceptible,
                "Resistant": number_resistant,
            }
        )

        # Create agents
        for i, node in enumerate(self.G.nodes()):
            a = Natural_agent(
                i,
                self,
                State.SUSCEPTIBLE,
                self.info_spread_chance,
                self.info_check_frequency,
                self.recovery_chance,
                self.gain_resistance_chance,
            )
            self.schedule.add(a)
            # Add the agent to the node
            self.grid.place_agent(a, node)

        # Infect some nodes
        infected_nodes = self.random.sample(self.G.nodes(), self.initial_outbreak_size)
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.state = State.INFECTED

        self.running = True
        self.datacollector.collect(self)

    def resistant_susceptible_ratio(self):
        try:
            return number_state(self, State.RESISTANT) / number_state(
                self, State.SUSCEPTIBLE
            )
        except ZeroDivisionError:
            return math.inf

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run_model(self, n):
        for i in range(n):
            self.step()