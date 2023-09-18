import random

def initialize_room():
    return random.choice([True, False])

def prisoner_strategy():
    return random.choice([1, 2, 3])

def simulate_game(num_prisoners):
    room_state = initialize_room()
    visited_count = 0
    prisoners_visited = [False] * num_prisoners

    while visited_count < num_prisoners:
        prisoner_id = random.randint(0, num_prisoners - 1)

        if not prisoners_visited[prisoner_id]:
            prisoners_visited[prisoner_id] = True
            visited_count += 1

            action = prisoner_strategy()
            if action == 1:
                room_state = not room_state

    return room_state

def main(num_simulations, num_prisoners):
    final_room_state = simulate_game(num_prisoners)
    print(f"Final Room State: {'On' if final_room_state else 'Off'}")

if __name__ == "__main__":
    num_simulations = 1
    num_prisoners = 100
    main(num_simulations, num_prisoners)
