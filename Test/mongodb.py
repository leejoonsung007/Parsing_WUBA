import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

path = '/Users/leejoonsung/Document/Python/Parsing/db/walden.txt'
with open(path, 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index':index,
            'line':line,
            'words':len(line.split())
        }
        sheet_tab.insert_one(data)

# $lt/$lte/$gt/$gte/$ne，stand for </<=/>/>=/!= l represents less g represents greater e represents equal n represents not  ）

# find words which is less than 5
for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)