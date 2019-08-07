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

    def damage_REAR(self):
        return "REAR_END"

    def damage_FRONT(self):
        return "FRONT_END"

    def damage_MINOR(self):
        return "MINOR_DENT/SCRATCHES"

    def damage_UNDERCARRIAGE(self):
        return "UNDERCARRIAGE"

        # def switchdamage(self, damage):
        #     damage_type = {
        #         "REAR END": 0,
        #         "FRONT END": 0,
        #         "MINOR DENT/SCRATCHES": 0,
        #         "UNDERCARRIAGE": 0,
        #         "MISC": 0
        #     }
        #
        #     # damage_type[damage] = all_damages.count(damage)
        #
        #     func = damage_type.get(damage, lambda: "MISC")
        #     # print(damage_type.get(damage, "MISC"))
        #
        #     return func()
        # time.sleep(15)
