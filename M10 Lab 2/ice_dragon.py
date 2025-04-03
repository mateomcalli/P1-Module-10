from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image)
        self.image = image
    def can_breath_fire(self):
        return False
