import json

class PyScratch:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        self.data_targets = json_data['targets']

    def listBlocks(self, actorName = None):
        for actor in self.data_targets:
            if(actorName):
                if(actor['name'] == actorName and actor['blocks']):
                    for blocks in actor['blocks']:
                        if type(actor['blocks'][blocks]) is dict:
                            block = actor['blocks'][blocks]
                            print(block['opcode'])
                        else:
                            block = actor['blocks'][blocks]
                            print('variable_' + block[1])
            else:
                if(actor['blocks']):
                    for blocks in actor['blocks']:
                        if type(actor['blocks'][blocks]) is dict:
                            block = actor['blocks'][blocks]
                            print(block['opcode'])
                        else:
                            block = actor['blocks'][blocks]
                            print('variable_' + block[1])

    def listActors(self):
        for actor in self.data_targets:
            print(actor['name'])
    
    def listCostumes(self, actorName = None):
        for actor in self.data_targets:
            if(actorName):
                if(actor['name'] == actorName):
                    for costumes in actor['costumes']:
                        print(costumes['name'])
            else:
                for costumes in actor['costumes']:
                    print(costumes['name'])