from mesa import Agent
from random import choice
import pyfiglet
from emoji import emojize


class Randao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Randao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
    


class Pedrao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Pedrao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = emojize("pedra :rock:")


class Papelao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Papelao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = emojize("papel :roll_of_paper:")


class Tesourao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Tesourao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = emojize("tesoura :scissors:")


class Arnaldo(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.previous_move = ""
        self.name = "Arnaldo"
        self.previous_result = None
        # self.status = True
        self.move = None

    def step(self):
        if not self.previous_move or self.previous_result == "ganhou":
            self.moves = {
                "ganhou": {
                    "pedra": ["papel", "spock"],
                    "papel": ["tesoura", "lagarto"],
                    "tesoura": ["spock", "pedra"],
                    "lagarto": ["pedra", "tesoura"],
                    "spock": ["lagarto", "papel"],
                },
                "perdeu": {
                    "pedra": ["lagarto", "tesoura"],
                    "papel": ["pedra", "spock"],
                    "tesoura": ["papel", "lagarto"],
                    "lagarto": ["spock", "papel"],
                    "spock": ["tesoura", "pedra"],
                },
            }        
        else:
            self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
    def step(self):
        if not self.previous_move or self.previous_result == "empate":
            self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
        else:
            self.move = choice(self.moves[self.previous_result[self.previous_move]])
            

class Ruanzão(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_move = ""
        self.previous_result = None
        self.move = None
        self.name = "Ruanzão"
        # self.status = True
        self.moves = {
            "ganhou": {
                "pedra": ["papel", "spock"],
                "papel": ["tesoura", "lagarto"],
                "tesoura": ["spock", "pedra"],
                "lagarto": ["pedra", "tesoura"],
                "spock": ["lagarto", "papel"],
            },
            "perdeu": {
                "pedra": ["lagarto", "tesoura"],
                "papel": ["pedra", "spock"],
                "tesoura": ["papel", "lagarto"],
                "lagarto": ["spock", "papel"],
                "spock": ["tesoura", "pedra"],
            },
        }
    def step(self):
        if not self.previous_move or self.previous_result == "empate":
            self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
        else:
            self.move = choice(self.moves[self.previous_result[self.previous_move]])
            
class Bomsao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_move = ""
        self.previous_result = None
        self.move = None
        self.name = "Bomsao"
        # self.status = True
        self.moves = {
            "ganhou": {
                "pedra": ["lagarto", "tesoura"],
                "papel": ["pedra", "spock"],
                "tesoura": ["papel", "lagarto"],
                "lagarto": ["spock", "papel"],
                "spock": ["tesoura", "pedra"],
            },
            "perdeu": {
                "pedra": ["papel", "spock"],
                "papel": ["tesoura", "lagarto"],
                "tesoura": ["spock", "pedra"],
                "lagarto": ["pedra", "tesoura"],
                "spock": ["lagarto", "papel"],
            },
        }

    def step(self):
        if not self.previous_move or self.previous_result == "empate":
            self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
        else:
            self.move = choice(self.moves[self.previous_result[self.previous_move]])

class Empatao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_move = ""
        self.previous_result = None
        self.move = None
        self.name = "Empatao"
        # self.status = True
        self.moves = {
            "ganhou": {
                "pedra": ["lagarto", "tesoura"],
                "papel": ["pedra", "spock"],
                "tesoura": ["papel", "lagarto"],
                "lagarto": ["spock", "papel"],
                "spock": ["tesoura", "pedra"],
            },
            "perdeu": {
                "pedra": ["papel", "spock"],
                "papel": ["tesoura", "lagarto"],
                "tesoura": ["spock", "pedra"],
                "lagarto": ["pedra", "tesoura"],
                "spock": ["lagarto", "papel"],
            }, 
            "empate": {
                "pedra": ["pedra"],
                "papel": ["papel"],
                "tesoura": ["tesoura"],
                "lagarto": ["lagarto"],
                "spock": ["spock"],
            }
        }

    def step(self):
        if not self.previous_move:
            self.move = choice([emojize("pedra :rock:"), 
                            emojize("papel :roll_of_paper:"), 
                            emojize("tesoura :scissors:"), 
                            emojize("lagarto :lizard:"), 
                            emojize("spock :alien:")])
        else:
            if self.previous_result == "perdeu":
                self.move = self.moves["perdeu"][self.previous_move][0]
            elif self.previous_result == "ganhou":
                self.move = self.moves["ganhou"][self.previous_move][0]
            else:
                self.move = choice(self.moves[self.previous_result[self.previous_move]])