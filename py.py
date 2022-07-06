import os
import json
cargo = {}

'''
os.chdir('Fonts')
for i in os.listdir():
    print(i)
    cargo = {}
    try:
        f = open(i, 'r')
        cargo[str(i)] = f.read()
        f.close()
        f = open('../FontsJson/' + i.split('.')[0]+'.json', 'x')
        f.close()
        with open('../FontsJson/' + i.split('.')[0]+'.json', "w") as outfile:
            json.dump([{i.split('.')[0]: cargo[i]}], outfile)
    except:
        pass
'''
    