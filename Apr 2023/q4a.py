edmDict = {
    "Martin": 14,
    "Avicii": 8,
    "KSHMR": 6,
}
key = "Avicii"

if key in edmDict.keys():
    print(f"Key {key} exists in dictionary")
    edmDict.pop(key)
    edmDict["KRSNA"] = 4
else:
    print(f"Key {key} does not exist in dictionary")

print(f"New dictionary: {edmDict}")