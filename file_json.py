
# working with JSON files in Python

import json

bio_data = {
        "name": "Goodnews",
        "age": 18,
        "job": "visionary",
        "loves Pizza": True
        }

bio_dat = "bio_data.json"
with open(bio_dat, "w") as file:
    json.dump(bio_data, file, indent=2)

