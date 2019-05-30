

if 'reactions' in history:
        reactions = history['reactions']
        for reaction in reactions:
            users = reaction['users']
            for user in users:
                if user != []: