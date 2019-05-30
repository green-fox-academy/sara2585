import json

def read_json(file):
    with open (file, 'r') as f:
        histories = json.load(f)
        return histories
histories = read_json('gfa-team-thanks.json')
for history in histories: 
    if 'reactions' in history:
        reactions = history['reactions']

        for reaction in reactions:
            users = reaction['users']
            for user in users:
                if user == []:
                    print(reaction)