from dis import dis
import json
from tkinter.messagebox import NO
from urllib.parse import _NetlocResultMixinBytes

# Opening JSON file
f = open("data.json")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
ok = 0
nok = 0
avg_nok = 0
avg_ok = 0
dist_dict = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
for feature in data["features"]:
    dist = feature["properties"]["distance_overtaker"]
    if dist != None:
        dist = round(dist, 1)
        dist_dict[int(dist * 10)] += 1

        if dist > 1.5:
            avg_ok += dist
            ok += 1
        else:
            nok += 1
            avg_nok += dist

# Closing file
f.close()

print(ok)
print(nok)

print(avg_ok / ok)
print(avg_nok / nok)

print(dist_dict)
