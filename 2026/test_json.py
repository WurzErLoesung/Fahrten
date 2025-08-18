import ujson as json

# Example data
data = {"speed": 100, "direction": "forward"}

# Write JSON to a file
with open("config.json", "w") as f:
    json.dump(data, f)

# Read JSON back
with open("config.json", "r") as f:
    loaded = json.load(f)

print(loaded)  # {'speed': 100, 'direction': 'forward'}
