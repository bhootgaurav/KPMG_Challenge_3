import json
def get_value(obj, key):
    keys = key.split(".")
    for k in keys:
        obj = obj.get(k)
    return obj

object = {
    "a" : {
        "b" : {"c" : "d"}
    }
}

print(get_value(object, "a.b"))

with open(r'C:\Python\data.json') as json_file:
    data = json.load(json_file)
    

    print(get_value(data, "hardware_profile.vm_size"))