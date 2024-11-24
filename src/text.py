from module.base import crawler_spport as CS


class text(CS):
    def __init__(self):
        super().__init__()

    @CS.click()
    def getShort():
        return '11'