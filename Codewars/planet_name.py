"""Use of a switch statement in python example."""
def get_planet_name(id):
    # This doesn't work; Fix it!
    switch = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
        }
    return switch.get(id)

results = get_planet_name(3)
print(results)