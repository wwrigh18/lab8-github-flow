from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[i][gray3]You stand still,[/gray3] unsure what to do. [dark_green]The forest swallows you.[/dark_green][/i]"

def left_path(event):
    return "[red3][i]You walk left.[/red3] " + event

def right_path(event):
    return "[blue3][i]You walk right.[/blue3] " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[gold3 i]You wake up in a dark forest.[/gold3 i] [b i]You can go left or right.[/b i]")
    while True:
        choice = console.input("[gray69]Which direction do you choose?[/gray69] ([red3]left[/red3]/[blue3]right[/blue3]/[grey37]exit[/grey37]): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
