class Warrior(object):

    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
             "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    experience = 100
    achievements = []

    def __init__(self):
        super(Warrior, self).__init__()

    @property
    def rank(self):
        return self.ranks[int(self.level / 10)]

    @property
    def level(self):
        return min(int(self.experience / 100), 100)

    def training(self, training):
        if training[2] > self.level:
            return "Not strong enough"

        self.achievements.append(training[0])
        self.experience += training[1]
        self.experience = min(10000, self.experience)
        return training[0]

    def battle(self, level):
        if level < 1 or level > 100:
            return "Invalid level"
        elif level - self.level >= 5 and int(level / 10) - int(self.level / 10) >= 1:
            return "You've been defeated"

        diff = self.level - level
        if diff == 0:
            self.experience += 10
        elif diff > 0:
            if diff == 1:
              self.experience += 5
        else:
            self.experience += diff * diff * 20
        self.experience = min(10000, self.experience)
        
        if diff >= 2:
            return "Easy fight"
        elif diff == 1 or diff == 0:
            return "A good fight"
        else:
            return "An intense fight"