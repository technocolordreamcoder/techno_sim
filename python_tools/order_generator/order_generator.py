import random
import yaml
import os

REPO_ROOT = os.environ['PWD']

def read_locations() -> dict:
    """Read locations of avilable vertiports from YAML file"""
    yml_locations = os.path.join(REPO_ROOT, 'data/vertiport_locations.yaml')

    with open(yml_locations, 'r') as f:
        return yaml.safe_load(f)

def generate_orders(num_orders) -> dict:
    """Function to generate random orders"""
    vertiports = read_locations()
    orders = []
    for i in range(num_orders):
        # Randomly choose start and end vertiports
        start_port = random.choice(vertiports)
        end_port = random.choice(vertiports)
        # Ensure start and end ports are different
        while start_port == end_port:
            end_port = random.choice(vertiports)
        # Randomly choose number of passengers and departure time
        num_passengers = random.randint(1, 4)
        departure_time = random.randint(0, 3599)
        # Construct order dictionary
        order = {
            'start_port': start_port['name'],
            'end_port': end_port['name'],
            'num_passengers': num_passengers,
            'departure_time': departure_time
        }
        orders.append(order)
    return orders

# Example usage: generate 10 random orders
orders = generate_orders(10)
print(orders)
