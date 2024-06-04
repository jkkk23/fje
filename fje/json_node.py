class JSONNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def display(self, style, icon_family):
        return style.display(self, icon_family)

class JSONObjectNode(JSONNode):
    def __init__(self, name):
        super().__init__(name)

class JSONLeafNode(JSONNode):
    def __init__(self, name, value):
        super().__init__(name, value)

def build_json_tree(data, name="root"):
    if isinstance(data, dict):
        node = JSONObjectNode(name)
        for key, value in data.items():
            node.add_child(build_json_tree(value, key))
        return node
    else:
        return JSONLeafNode(name, data)