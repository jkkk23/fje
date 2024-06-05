from abc import ABC, abstractmethod
from display_style import DisplayStyle
from icon_family import IconFamily

class AbstractFactory(ABC):
    @abstractmethod
    def create_display_style(self) -> DisplayStyle:
        pass

    @abstractmethod
    def create_icon_family(self) -> IconFamily:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_display_style(self) -> DisplayStyle:
        from display_style import TreeDisplayStyle
        return TreeDisplayStyle()

    def create_icon_family(self) -> IconFamily:
        from icon_family import PokerFaceIconFamily
        return PokerFaceIconFamily()

class ConcreteFactory2(AbstractFactory):
    def create_display_style(self) -> DisplayStyle:
        from display_style import RectangleDisplayStyle
        return RectangleDisplayStyle()

    def create_icon_family(self) -> IconFamily:
        from icon_family import StarIconFamily
        return StarIconFamily()