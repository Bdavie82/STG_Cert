class DamageSwitcher():

    def switchdamage(self, damage):
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
