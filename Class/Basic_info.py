import random
from enum import Enum

class State(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RESISTANT = 2

def number_state(model, state):
    return sum([1 for a in model.grid.get_all_cell_contents() if a.state is state])


def number_infected(model):
    return number_state(model, State.INFECTED)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_resistant(model):
    return number_state(model, State.RESISTANT)



class Information(object):

    """
        create_platform: 信息生成平台
        spread_platform: 信息传播平台
        confidence: 信息可信度
        create_time: 信息生成时间
    """

    def __init__(
            self,
            create_platform,
            spread_platform,
            confidence,
            create_time
    ):
        self.create_platform = create_platform
        self.spread_platform = spread_platform
        self.confidence = confidence
        self.create_time = create_time