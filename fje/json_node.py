class container:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def accept(self, visitor, icon_family):
        visitor.visit(self, icon_family)

class JSONObjectNode(container):
    def __init__(self, name):
        super().__init__(name)

class JSONLeafNode(container):
    def __init__(self, name, value):
        super().__init__(name, value)

    def accept(self, visitor, icon_family):
        visitor.visit_leaf(self, icon_family)

def build_json_tree(data, name="root"):
    if isinstance(data, dict):
        node = JSONObjectNode(name)
        for key, value in data.items():
            node.add_child(build_json_tree(value, key))
        return node
    else:
        return JSONLeafNode(name, data)