import json

def convert_json():
    json_string = '{"first_name": "Guido", "last_name": "Rossum"}'
    parsed_json = json.loads(json_string)
    print (parsed_json['last_name'])
    print "*&*"

convert_json()
