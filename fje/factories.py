from display_style import TreeDisplayStyle, RectangleDisplayStyle
from icon_family import PokerFaceIconFamily, OtherIconFamily

class DisplayStyleFactory:
    def create_display_style(self, style_type):
        if style_type == "tree":
            return TreeDisplayStyle()
        elif style_type == "rectangle":
            return RectangleDisplayStyle()
        else:
            raise ValueError(f"Unknown style type: {style_type}")

class IconFamilyFactory:
    def create_icon_family(self, icon_type):
        if icon_type == "poker-face":
            return PokerFaceIconFamily()
        elif icon_type == "other":
            return OtherIconFamily()
        else:
            raise ValueError(f"Unknown icon type: {icon_type}")