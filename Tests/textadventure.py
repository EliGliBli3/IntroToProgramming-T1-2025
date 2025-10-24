import os, random
from enum import Enum

'''
Encounters list:
    - Octopus attack
    - Steal food
    - Find treasure
    - Eat (challenged)
    - Eat (unchallenged)
    - Explore (Wait encounter)
    - Rest



'''


end_buffer = False
def restart():
    global fih, end_buffer
    fih = Fih(
        luck=random.randrange(10, 200)/100 # 0.1 -> 2
    )
    end_buffer = False
    
    prompt_encounter(encounter_handler.start_life)
    

class Encounter:
        def __init__(self, prompt: str, options: list):
            self.prompt = prompt
            self.options = options

class Location(Enum):
    HOME = "home"
    WATER_SURFACE = "the ocean waters"
    REEF = "the reef"
    CAVE = "the cave"

class Fih:
    def __init__(self, luck):
        # Birth variables
        self.luck = luck
        
        # Active variables
        self.hunger = 1
        self.food_types = ["plankton"]
        self.health = 0.5
        self.energy = 0.5
        self.age = 0    # Years, 0 to 5
        self.location = Location.HOME
        self.depth = 0
        
        # Legacy variables
        self.boldness = 0
        self.sociability = 0
    
    def update(self):
        global end_buffer
        
        self.hunger -= 0.05
        self.energy -= 0.025
        self.age += 0.1
        
        self.luck = max(0.1, self.luck)
        self.boldness = max(0.1, self.boldness)
        self.sociability = max(0.1, self.sociability)
        
        if self.hunger <= 0 or self.energy <= 0:
            end_buffer = True
            prompt_encounter(exit_prompt)
            
fih = Fih(
    luck=random.randrange(10, 200)/100 # 0.1 -> 2
)

exit_prompt = Encounter(
        "-- GAME OVER --",
        [
            ("Restart", restart),
            ("Quit", quit)
        ]
    )

#region Encounter functions

class RandomEncounters:
    def __init__(self):
        self.encounters = dict()
        
        self.register_encounter(self.octopus_attack, 0)
        self.register_encounter(self.steal_food, 0.5)
        self.register_encounter(self.find_treasure, 1)
    
    def register_encounter(self, enc, positivity:float):
        self.encounters.update({
            positivity: enc
        })
    
    def get_encounter(self, value):
        encounter_list = [(e, self.encounters.get(e)) for e in self.encounters]
        dist = [abs(value-v[0]) for v in encounter_list]
        
        return encounter_list[dist.index(min(dist))][1]
    
    def octopus_attack(self):
        global fih
        fih.energy -= 0.4
        prompt_encounter(encounter_handler.confirmation("A camouflaged octopus jumps out, attacking you.\nYou have less energy."))
    def steal_food(self):
        global fih
        fih.energy -= 0.2
        fih.hunger = 1
        prompt_encounter(encounter_handler.confirmation("While gorging a stash of food you found, you see its owner approaching.\nYou run with the food, tired, but satiated."))
        
    def find_treasure(self):
        global fih
        fih.energy += 0.3
        prompt_encounter(encounter_handler.confirmation("While exploring, you find treasure!\nYou are ecstatic, and feel a burst of energy through your fishy veins."))
random_encounters = RandomEncounters()

def explore():
    fih.depth = min(5, fih.depth+1)
    if fih.depth == 1:
        fih.location = getattr(Location, random.choice(list([l for l in Location if l != Location.HOME])).name)
    prompt_encounter(encounter_handler.get_wait_encounter())
def turn_back():
    fih.depth = max(0, fih.depth-1)
    if fih.depth == 0:
        fih.location = Location.HOME
    prompt_encounter(encounter_handler.get_wait_encounter())

def eat_challenge(fighting: bool):
    if fighting:
        chance_lose = 0.5 / (fih.luck+1) / (fih.energy+1)
        if random.random() <= chance_lose:
            fih.energy -= 0.2
            prompt_encounter(encounter_handler.confirmation("You lose the fight and the food. You are still hungry, and you have less energy."))
        else:
            fih.hunger = 1
            fih.energy -= 0.15
            prompt_encounter(encounter_handler.confirmation("You win the fight and the food. You are satiated, but you have less energy."))
    else:
        prompt_encounter(encounter_handler.confirmation("You surrender the food. Nothing changes."))

def eat():
    global fih
    chance_sick = (0.25 / fih.luck) / fih.health
    chance_fight = (0.1 / fih.luck) / fih.sociability
    
    match fih.age:
        case n if n <= 0.5:
            fih.food_types = ["plankton", "fleas", "copepods"]
        case n if 0.5 < n <= 1.5:
            fih.food_types = ["worms", "larvae", "nymphs"]
        case n if 1.5 < n <= 3:
            fih.food_types = ["sowbugs", "worms", "snail"]
        case _:
            fih.food_types = ["minnow", "sunfish", "crayfish"]
            
    
    if random.random() <= chance_sick:
        fih.hunger = 1
        fih.energy -= 0.2
        prompt_encounter(encounter_handler.confirmation(f"The {random.choice(fih.food_types)} you ate makes you feel ill.\nYou are satiated, but have less energy."))
    elif random.random() <= chance_fight:
        prompt_encounter(encounter_handler.eat_fight)
    else:
        fih.hunger = 1
        prompt_encounter(encounter_handler.confirmation(f"You eat the {random.choice(fih.food_types)}. You are satiated"))

def rest():
    fih.energy = 1
    prompt_encounter(encounter_handler.confirmation("You feel rested."))
    
#endregion
    
    
class Encounters:
    def __init__(self):
        self.start_life = Encounter(
            "You are born in a nest of pebbles.",
            [
                ("Explore around", explore),
                ("Eat", eat),
                ("Rest", rest)
            ])
        self.eat_fight = Encounter(
            f"You go for the {random.choice(fih.food_types)}, but are challenged.",
            [
                ("Fight", lambda: eat_challenge(True)),
                ("Surrender", lambda: eat_challenge(False))
            ]
        )
        
    def get_wait_encounter(self):
        options = [
            ("Eat", eat),
        ]
        turn_back_msg = "Go home" if fih.depth == 1 else "Turn back"
        if fih.depth > 0: options.append((turn_back_msg, turn_back)) 
        if fih.depth < 5: options.insert(0, ("Explore", explore))
        
        match fih.location:
            case Location.HOME:
                options.extend([
                    ("Rest", rest),
                ])
            case Location.REEF:
                if fih.depth == 5:
                    options.extend([
                        ("Rest", rest),
                    ])
            case Location.CAVE:
                if fih.depth == 5:
                    options.extend([
                        ("Rest", rest),
                    ])
        
        print(options)
        return Encounter(
            f"You are {"alone at" if fih.depth < 5 else "deep in"} {fih.location.value}",
            options
        )
        
    def confirmation(self, msg):
        return Encounter(
            msg,
            [
                ("Continue", lambda: prompt_encounter(self.get_wait_encounter()))
            ]
        )
        
encounter_handler = Encounters()

def prompt_encounter(encounter:Encounter):
    global fih
    if not end_buffer: fih.update()
    
    if random.randint(0, 100) <= 20:    # 20% chance. Might need tweaking.
        encounter_luck = (0.5 * fih.luck) + (float(random.randint(-25, 25))/100)
        rand_encounter = random_encounters.get_encounter(encounter_luck)
        rand_encounter()
        
    else:
        def get_response():
            os.system('cls')
            
            print(f"-- Stats --\n\
    Food   {(chr(9608) + " ") * int(fih.hunger//0.1)}\n\
    Energy {(chr(9608) + " ") * int(fih.energy//0.1)}\n\
    Age    {(chr(9608) + " ") * int(fih.age//0.5)}\n\n\
            ")
            
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
        encounter.options[response-1][1]()

prompt_encounter(encounter_handler.start_life)

while True:
    prompt_encounter(exit_prompt)