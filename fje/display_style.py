from abc import ABC, abstractmethod

class DisplayStyle(ABC):
    @abstractmethod
    def display(self, node, icon_family):
        pass

class TreeDisplayStyle(DisplayStyle):
    def display(self, node, icon_family):
        result = []
        self._display_helper(node, icon_family, result, "")
        return "\n".join(result)

    def _display_helper(self, node, icon_family, result, indent):
        icon = icon_family.get_icon(is_leaf=(len(node.children) == 0))
        result.append(f"{indent}{icon}{node.name}")
        for i in range(len(node.children)):
            child=node.children[i]
            inde=indent
            for j in range(len(inde)):
                if(inde[j]=="├"):
                    inde=inde[:j]+"│ "+inde[j+2:]
                elif (inde[j]=="└"):
                    inde=inde[:j]+"  "+inde[j+2:]
                    
            if(i==len(node.children)-1):
                self._display_helper(child, icon_family, result, inde + "└─ ")
            else:
                self._display_helper(child, icon_family, result, inde + "├─ ")
                
            

class RectangleDisplayStyle(DisplayStyle):
    def display(self, node, icon_family):
        result = []
        self._display_helper(node, icon_family, result, "", True)
        max_length = max(len(line) for line in result)
        for i in range(len(result)):
            resu=result[i]
            for j in range(max_length-len(result[i])):
                resu=resu[:-2]+"─"+resu[-2:]
            result[i]=resu
        return "\n".join(result)

    def _display_helper(self, node, icon_family, result, indent, is_root):
        icon = icon_family.get_icon(is_leaf=(len(node.children) == 0))
        if is_root:
            result.append(f"┌─ {icon}{node.name} ───────────────────────────────┐")
        else:
            result.append(f"{indent}├─ {icon}{node.name} ───────────────────────────┤")
        for child in node.children:
            self._display_helper(child, icon_family, result, indent + "│ ", False)
        if is_root:
            result.append(f"└───────────────────────────────────────────────┘")