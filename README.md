import random

def initialize_room():
    return random.choice([True, False])

def main(num_prisoners):
    room_state = initialize_room()
    print(f"Initial Room State: {'On' if room_state else 'Off'}")

if __name__ == "__main__":
    num_prisoners = 100
    main(num_prisoners)

  
