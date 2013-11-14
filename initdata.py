#initialize data to be stored in files, pickles, shelves

#records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 35, 'pay': 45000, 'job': 'hdw'}
dex = {'name': 'Dex Caff', 'age': 24, 'pay': 20000, 'job': None}

#database
db = {}
db['dex'] = dex
db['sue'] = sue
db['bob'] = bob

if __name__ == '__main__':#when run as a script
    for key in db:
        print(key, '=>\n  ', db[key])

