

class BaseMarket(object):
    pass

class VirtualMarket(Market):
    def __init__(self, agent, database="db/finance.db"):
        # account register
        # load asset data
        self.database = database
        self.agent = agent

    def __load_assets(self):
        pass

    def run_by_step(self):
        pass

    


