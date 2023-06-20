voted = {}

def check_voter(name):
    if voted.get(name):
        print(f'Kick {name} out!')
    else:
        voted[name]= True
        print(f'Let {name} vote!')

people = input()
check_voter(people)
