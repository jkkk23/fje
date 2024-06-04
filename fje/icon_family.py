class IconFamily:
    def get_icon(self, is_leaf):
        pass

class PokerFaceIconFamily(IconFamily):
    def get_icon(self, is_leaf):
        return "♤" if is_leaf else "♢"

class OtherIconFamily(IconFamily):
    def get_icon(self, is_leaf):
        return "★" if is_leaf else "☆"