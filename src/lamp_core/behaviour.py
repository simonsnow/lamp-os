class Behaviour:
    def __init__(self, lamp):
        self.lamp = lamp

    def __str__(self):
        return self.__class__.__name__

    async def run(self):
        pass

class BackgroundBehaviour(Behaviour):
    def __init__(self, lamp):
        super().__init__(lamp)
        self.type = "pipeline"

class BlockingBehaviour(Behaviour):
    def __init__(self, lamp):
        super().__init__(lamp)
        self.type = "glitch"

class StartupBehaviour(Behaviour):
    def __init__(self, lamp):
        super().__init__(lamp)
        self.type = "startup"
