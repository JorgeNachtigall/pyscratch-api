import json


class Analyscratch:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        self.data_targets = json_data['targets']

    def listBlocks(self):
        for actor in self.data_targets:
            if(actor['blocks']):
                for blocks in actor['blocks']:
                    if type(actor['blocks'][blocks]) is dict:
                        block = actor['blocks'][blocks]
                        print(block['opcode'])
                    else:
                        block = actor['blocks'][blocks]
                        print('variable_' + block[1])


block_list = Analyscratch('project.json')
block_list.listBlocks()
