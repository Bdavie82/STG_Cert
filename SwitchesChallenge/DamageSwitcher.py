class DamageSwitcher():

    # def __init__(self): #, damage=None):

    # self.damage_type_to_count(damage)

    def damage_type_to_count(self, damage):
        # damage_count = 'damage_' + str(damage_idx)
        # method = getattr(self, damage_count, lambda: "MISC")
        # string = damage

        # damage = str(damage)
        #         # str.lower(damage)
        #         # print(str.replace(" ", "_"))

        # print (len(damage))
        damage_count = 'damage_' + str(damage)

        method = getattr(self, damage_count, lambda: "MISC")
        # print(damage_count)
        return method()

    def switchdamage(self, damage):
        print(damage)
        damage_type = {
            "REAR END": self.REAREND(),
            "FRONT END": self.FRONTEND(),
            "MINOR DENT/SCRATCHES": self.MINORDENT_SCRATCHES(),
            "UNDERCARRIAGE": self.UNDERCARRIAGE(),
        }

        return damage_type.get(damage, self.MISC())

    def REAREND(self):
        return "REAR_END"

    def FRONTEND(self):
        return "FRONT_END"

    def MINORDENT_SCRATCHES(self):
        return "MINOR_DENT/SCRATCHES"

    def UNDERCARRIAGE(self):
        return "UNDERCARRIAGE"

    def MISC(self):
        return "MISC"
