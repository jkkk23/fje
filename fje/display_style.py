from abc import ABC, abstractmethod

class DisplayStyle(ABC):
    @abstractmethod
    def visit(self, node, icon_family):
        pass

    @abstractmethod
    def visit_leaf(self, node, icon_family):
        pass

class TreeDisplayStyle(DisplayStyle):
    def __init__(self):
        self.result = []

    def visit(self, node, icon_family):
        self._display_helper(node, icon_family, "")

    def visit_leaf(self, node, icon_family):
        self._display_helper(node, icon_family, "")

    def _display_helper(self, node, icon_family, indent):
        icon = icon_family.get_icon(is_leaf=(len(node.children) == 0))
        self.result.append(f"{indent}{icon}{node.name}")
        for i, child in enumerate(node):
            new_indent = indent
            for j, char in enumerate(new_indent):
                if char == "├":
                    new_indent = new_indent[:j] + "│ " + new_indent[j+2:]
                elif char == "└":
                    new_indent = new_indent[:j] + "  " + new_indent[j+2:]

            if i == len(node.children) - 1:
                self._display_helper(child, icon_family, new_indent + "└─ ")
            else:
                self._display_helper(child, icon_family, new_indent + "├─ ")

    def get_result(self):
        return "\n".join(self.result)

class RectangleDisplayStyle(DisplayStyle):
    def __init__(self):
        self.result = []

    def visit(self, node, icon_family):
        self._display_helper(node, icon_family, "", True)

    def visit_leaf(self, node, icon_family):
        self._display_helper(node, icon_family, "", True)

    def _display_helper(self, node, icon_family, indent, is_root):
        icon = icon_family.get_icon(is_leaf=(len(node.children) == 0))
        if is_root:
            self.result.append(f"┌─ {icon}{node.name} ───────────────────────────────┐")
        else:
            self.result.append(f"{indent}├─ {icon}{node.name} ───────────────────────────┤")
        for child in node.children:
            self._display_helper(child, icon_family, indent + "│ ", False)
        if is_root:
            self.result.append(f"└───────────────────────────────────────────────┘")

    def get_result(self):
        max_length = max(len(line) for line in self.result)
        for i in range(len(self.result)):
            line = self.result[i]
            self.result[i] = line + "─" * (max_length - len(line))
        return "\n".join(self.result)