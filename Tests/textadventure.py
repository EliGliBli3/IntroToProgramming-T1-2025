import os, random, time
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
    - Welcome (Inner reef)
    - Welcome (Inner cave)
    

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
    INNER_REEF = "the inner reef"
    CAVE = "the cave"
    INNER_CAVE = "the inner cave"

invalid_random_locs = [
    Location.HOME,
    Location.INNER_REEF,
    Location.INNER_CAVE
]

def get_inner_location(loc: Location):
    match loc:
        case Location.CAVE: return Location.INNER_CAVE
        case Location.REEF: return Location.INNER_REEF
        case _: return loc
def get_outer_location(inner: Location):
    match inner:
        case Location.INNER_CAVE: return Location.CAVE
        case Location.INNER_REEF: return Location.REEF
        case _: return inner


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
        self.visited_locations = set()
        
        # Legacy variables
        self.boldness = 0
        self.sociability = 0
    
    def update(self):
        global end_buffer, iterations_since_last_random
        
        iterations_since_last_random += 1
        
        self.hunger -= 0.05
        self.energy -= 0.02
        self.energy += (
            (pow(-24.5*self.hunger,2)+(9.8*self.hunger)-0.98) if self.hunger <= 0.2     # y = -24.5x^2 + 9.8x - 0.98
            else pow(-0.125*self.hunger,2)+(0.275*self.hunger)-0.05                     # y = -0.125x^2 + 0.275x - 0.05
        )
        
        self.age += 0.1
        
        self.luck = max(0.1, self.luck)
        self.boldness = max(0.1, self.boldness)
        self.sociability = max(0.1, self.sociability)
        
        if self.energy <= 0:
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

struggle_count = 0
struggle_start_time = 0
iterations_since_last_random = 0

class RandomEncounters:
    def __init__(self):
        self.encounters = dict()
        
        self.register_encounter(self.octopus_attack, 0)
        self.register_encounter(self.steal_food, 0.75)
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
        global fih, struggle_count, struggle_start_time
        if struggle_start_time != 0:
            struggle_count += 1
        else:
            struggle_start_time = time.time()
        
        if struggle_count <= 10:    
            prompt_encounter(
                encounter_handler.octupus_fight
                , update=False
                )
        else:
            if time.time() - struggle_start_time < 5:
                prompt_encounter(encounter_handler.confirmation(
                    "You won against the octopus. You are tired, but alive.",
                ), update=False)
            else:
                prompt_encounter(encounter_handler.confirmation(
                    "You got away, but barely. You are very tired."
                ), update=False)
            struggle_count = 0
        
    def steal_food(self):
        global fih
        fih.energy -= 0.1
        fih.hunger = 1
        prompt_encounter(
            encounter_handler.confirmation(
                "While gorging a stash of food you found, you see its owner approaching.\nYou run with the food, tired, but satiated."
                ), update=False)
        
    def find_treasure(self):
        global fih
        fih.energy += 0.3
        prompt_encounter(
            encounter_handler.confirmation
            ("While exploring, you find treasure!\nYou are ecstatic, and feel a burst of energy through your fishy veins."
            ), update=False)
random_encounters = RandomEncounters()

def explore():
    fih.depth = min(6, fih.depth+1)
    if fih.depth == 1:
        fih.location = getattr(Location, random.choice(list([l for l in Location if l not in invalid_random_locs])).name)
    elif fih.depth > 5:
        fih.location = get_inner_location(fih.location)
        
        if fih.location not in fih.visited_locations:
            prompt_encounter(encounter_handler.get_welcome_encounter(fih.location))
        
    fih.visited_locations.add(fih.location)
    prompt_encounter(encounter_handler.get_wait_encounter())
def turn_back(wait: bool = True):
    fih.depth = max(0, fih.depth-1)
    if fih.depth == 0:
        fih.location = Location.HOME
    elif fih.depth == 5:
        fih.location = get_outer_location(fih.location)
    if wait: prompt_encounter(encounter_handler.get_wait_encounter())   # ONLY SET TO FALSE IF YOU'RE PROMPTING A DIFFERENT ENCOUNTER IN PLACE OF 'WAIT'

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
    fih.energy = max(1, fih.energy)
    prompt_encounter(encounter_handler.confirmation("You feel rested."))
    
def quick_time(wait_msg, attack_msg, time_limit):
    start_time = time.time()
    os.system('cls')
    print(wait_msg)
    
    while (start_time < random.randrange(2,5)):
        pass
    prompt_encounter(Encounter(
        prompt=attack_msg,
        options=[
            ("Attack", lambda: (time.time() - start_time) < time_limit)
        ]
    ), False)
    
#endregion
    
    
class Encounters:
    def __init__(self):
        global struggle_count
        
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
            ])
        self.octupus_fight = Encounter(
            f"Quick! Fight back!\nAn octopus took hold of you ({struggle_count}/10)",
            [
                ("Struggle", random_encounters.octopus_attack)
            ]
        )
        
    def get_wait_encounter(self, additional_msg: str = ""):
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
                        ("Travel to Inner Reef", explore)
                    ])
                elif fih.depth == 6:
                    options.extend([
                    ])
            case Location.CAVE:
                if fih.depth == 5:
                    options.extend([
                        ("Rest", rest),
                        ("Travel to Inner Cave", explore)
                    ])
                elif fih.depth == 6:
                    options.extend([
                    ])
        
        return Encounter(
            f"{additional_msg}{"\n\n" if additional_msg != "" else ""}You are {"alone at" if fih.depth != 5 else "deep in"} {fih.location.value}",
            options
        )
        
    def confirmation(self, msg, wait:bool=True):    # ONLY SET WAIT TO FALSE IF YOU'RE PROMPTING A DIFFERENT ENCOUNTER IN PLACE OF 'WAIT'
        return Encounter(
            msg,
            [
                ("Continue", (lambda: prompt_encounter(self.get_wait_encounter())) if wait else lambda: True)
            ]
        )
    
    def dialogue(self, name: str, msg: str, options: list, last_response:str=""):
        enc = Encounter(
            f'"{last_response}{"\n\n" if last_response != "" else ""}"{name}:\n    {msg}',
            options
        )
        return enc
    
    def get_welcome_encounter(self, loc: Location):
        
        def fall_back():
            turn_back(False)
            add_msg = ""
            match loc:
                case Location.INNER_CAVE: add_msg = "You leave the inner cave, choosing not to confront Ivan."
                case Location.INNER_REEF: add_msg = "You leave the inner reef, off-put by Bubbles's energy."
                case _: None
            prompt_encounter(encounter_handler.get_wait_encounter(add_msg))
            
        def fight_ivan():
            win_count = 0
            for i in range(4):
                if quick_time("Ivan gets ready to charge you...", "Ivan charges!", 2/(i+1)):    # 2/(i+1) means the first attack will require 2 seconds, and the last will require 0.5.
                    win_count += 1
                    prompt_encounter(encounter_handler.confirmation("Ivan charges, but you dodge and land a hit.", False), False)
                else:
                    prompt_encounter(encounter_handler.confirmation("You try to fight back, but Ivan lands a hit before you can make a move.", False), False)
            if win_count >= 3:
                prompt_encounter()
        
        def follow_bubbles():
            pass
        
        match loc:
            case Location.INNER_CAVE:
                greeting = "Ivan"
                return self.dialogue(
                    name=greeting,
                    msg="Hey, I don't recognize you. You looking for trouble..?",
                    options=[
                        ("Confirm (fight)", lambda: self.dialogue(
                            name=greeting,
                            last_response="Yeah. matter'a fact, I am.",
                            msg="You don't wanna do this pal.",
                            options=[
                                ("Double down (fight)", fight_ivan),
                                ("Fall back", fall_back)
                            ]
                        )),
                        ("Deny"),
                        ("Run")])
            case Location.INNER_REEF:
                greeting = "Bubbles"
                return self.dialogue(
                    name=greeting,
                    msg="Hey there! My name's Bubbles! I don't believe we've met! Where'd you come from? What's your name? Do you want to meet my friends?",
                    options=[
                        ("Confirm (meet friends)", lambda: self.dialogue(
                            name=greeting,
                            last_response="Oh- Okay, sure.",
                            msg="Yippie!! Come on, come on!!.",
                            options=[
                                ("Follow (meet friends)", follow_bubbles),
                                ("Stay behind (stay in inner reef)", lambda: prompt_encounter(encounter_handler.get_wait_encounter())),
                                ("Leave inner reef", fall_back)
                            ]
                        )),
                        ("Deny"),
                        ("Run")])
            case _: None    # Already happens by default; Just for clarity.
        
encounter_handler = Encounters()

def prompt_encounter(encounter:Encounter, update:bool=True):
    global fih, iterations_since_last_random
    if not end_buffer and update: fih.update()
    
    if random.randint(0, 100) <= 20*(fih.age/2) * (iterations_since_last_random-1)/3:
        encounter_luck = (0.5 * fih.luck) + (float(random.randint(-40, 40))/100)
        rand_encounter = random_encounters.get_encounter(encounter_luck)
        iterations_since_last_random = 0
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