import numpy as np
from message import Message
from thespian.actors import *


class Agent(Actor):
    def __init__(self):
        self.wealth = np.random.randint(1, 10)

    def get_wealth(self):
        return self.wealth

    def receiveMessage(self, message, sender):
        if isinstance(message, Message):
            if message.recipients == "Agents":
                if message.directive == "get_wealth":
                    self.send(sender, self.wealth)
