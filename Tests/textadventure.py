import os, random
from enum import Enum

class Encounter:
        def __init__(self, prompt: str, options: list):
            self.prompt = prompt
            self.options = options

class Location(Enum):
    HOME = "home"
    WATER_SURFACE = "the surface"
    WATER_DEEP = "the bottom"
    REEF = "the reef"
    CAVE = "the cave"

class Fih:
    def __init__(self, luck):
        # Birth variables
        self.luck = luck
        
        # Active variables
        self.hunger = 0
        self.food_types = ["plankton"]
        self.health = 0.5
        self.energy = 0.5
        self.age = 0    # Years, 0 to 5
        self.location = Location.HOME
        
        # Legacy variables
        self.boldness = 0
        self.sociability = 0
    
    def update(self):
        self.hunger -= 0.2
        self.energy -= 0.1
        self.age += 0.1
        
        self.luck = max(0.1, self.luck)
        self.boldness = max(0.1, self.boldness)
        self.sociability = max(0.1, self.sociability)
        
fih = Fih(
    luck=random.randrange(10, 200)/100 # 0.1 -> 2
)

#region Encounter functions

def explore():
    print("Explored")
    
def go_home():
    print("You go home.")
    fih.location = Location.HOME

def eat_challenge(fighting: bool):
    if fighting:
        chance_lose = 0.5 / (fih.luck+1) / (fih.energy+1)
        if random.random() <= chance_lose:
            prompt_encounter(encounter_handler.confirmation("You lose the fight and the food. You are still hungry, and you have less energy."))
            fih.energy -= 0.2
        else:
            prompt_encounter(encounter_handler.confirmation("You win the fight and the food. You are satiated, but you have less energy."))
            fih.hunger = 0
            fih.energy -= 0.15
    else:
        prompt_encounter(encounter_handler.confirmation("You surrender the food. Nothing changes."))

def eat():
    chance_sick = (0.25 / fih.luck) / fih.health
    chance_fight = (0.1 / fih.luck) / fih.sociability
    
    match fih.age:
        case n if n <= 0.2:
            fih.food_types = ["plankton", "fleas", "copepods"]
        case n if 0.2 < n <= 0.5:
            fih.food_types = ["worms", "larvae", "nymphs"]
        case n if 0.5 < n <= 1.5:
            fih.food_types = ["sowbugs", "worms", "snail"]
        case _:
            fih.food_types = ["minnow", "sunfish", "crayfish"]
            
    
    if random.random() <= chance_sick:
        prompt_encounter(encounter_handler.confirmation(f"The {random.choice(fih.food_types)} you ate makes you feel ill.\nYou are satiated, but have less energy."))
        fih.hunger = 0
        fih.energy -= 0.75
    elif random.random() <= chance_fight:
        prompt_encounter(encounter_handler.eat_fight)
    else:
        prompt_encounter(encounter_handler.confirmation(f"You eat the {random.choice(fih.food_types)}. You are satiated"))
        fih.hunger = 0

def sleep():
    print("Slept")
    
#endregion
    
    
class Encounters:
    def __init__(self):
        self.start_life = Encounter(
            "You are born in a nest of pebbles.",
            [
                ("Explore around", explore),
                ("Eat", eat),
                ("Sleep", sleep)
            ])
        #self.wait  <- no longer needed, replaced by get_wait_encounter().
        
        self.eat_fight = Encounter(
            f"You go for the {random.choice(fih.food_types)}, but are challenged.",
            [
                ("Fight", lambda: eat_challenge(True)),
                ("Surrender", lambda: eat_challenge(False))
            ]
        )
        
    def get_wait_encounter(self):
        options = [
            ("Explore", explore),
            ("Eat", eat),
        ]
        match fih.location:
            case Location.HOME:
                options.extend([
                    ("Sleep", sleep),
                ])
            case Location.WATER_SURFACE:
                options.extend([
                    ("Go home", go_home),
                ])
            case Location.WATER_DEEP:
                options.extend([
                    ("Go home", go_home),
                ])
            case Location.REEF:
                options.extend([
                    ("Go home", go_home),
                ])
            case Location.CAVE:
                options.extend([
                    ("Go home", go_home),
                ])
        
        print(options)
        return Encounter(
            f"You are alone at {fih.location.value}",
            options
        )
        
    def confirmation(self, msg):
        return Encounter(
            msg,
            [
                ("Continue", self.get_wait_encounter)
            ]
        )
        
encounter_handler = Encounters()

def prompt_encounter(encounter:Encounter):
    def get_response():
        os.system('cls')
        print(encounter.prompt + "\n----------\n")
        for i, option in enumerate(encounter.options):
            print(f"{i+1}) {option[0]}")
            
        response = input("\n>")
        try:
            _result = int(response)
            if 0 < _result <= len(encounter.options):
                return _result
            raise IndexError
        except:
            return get_response()
    response = get_response()
    
    os.system('cls')
    fih.update()
    encounter.options[response-1][1]()

prompt_encounter(encounter_handler.start_life)
    