import os, random

class Fih:
    def __init__(self, luck):
        self.luck = luck
fih = Fih(
    luck=random.randrange(0.1, 2)
)

def explore():
    print("Explored")

def eat():
    chance_sick = 0.25 / fih.luck
    if random.random() <= chance_sick:
        pass # Sick
    else:
        pass # Not sick

def sleep():
    print("Slept")


class Encounter:
        def __init__(self, prompt: str, options: list):
            self.prompt = prompt
            self.options = options

class Encounters:
    def __init__(self):
        self.start_life = Encounter(
            "You are born in a nest of pebbles.",
            [
                ("Explore around", explore),
                ("Eat", eat),
                ("Sleep", sleep)
            ])
        self.home_
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
            get_response()
    response = get_response()
    
    os.system('cls')
    encounter.options[response-1][1]()

prompt_encounter(encounter_handler.start_life)