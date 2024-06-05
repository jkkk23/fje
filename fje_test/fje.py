import json
import argparse
from factories import DisplayStyleFactory, IconFamilyFactory
from json_node import build_json_tree


class FunnyJsonExplorer:
    def __init__(self, args):
        self.file = args.file
        self.style = args.style
        self.icon = args.icon

    def _load(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def show(self):
        data = self._load()
        
        root_node = build_json_tree(data)

        style_factory = DisplayStyleFactory()
        icon_factory = IconFamilyFactory()

        style = style_factory.create_display_style(self.style)
        icon_family = icon_factory.create_icon_family(self.icon)

        print(root_node.display(style, icon_family))

        
        
def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to JSON file')
    parser.add_argument('-s', '--style', required=True, help='Display style (tree, rectangle)')
    parser.add_argument('-i', '--icon', required=True, help='Icon family (poker-face, other)')
    args = parser.parse_args()

    explorer = FunnyJsonExplorer(args)
    explorer.show()
'''
    with open(args.file, 'r') as f:
        data = json.load(f)

    root_node = build_json_tree(data)

    style_factory = DisplayStyleFactory()
    icon_factory = IconFamilyFactory()

    style = style_factory.create_display_style(args.style)
    icon_family = icon_factory.create_icon_family(args.icon)

    print(root_node.display(style, icon_family))
'''
if __name__ == "__main__":
    main()