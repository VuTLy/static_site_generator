from textnode import *
from htmlnode import *

def main():

    test = TextNode('This is some anchor text', TextType.LINK , 'https://www.boot.dev')
    print(test)

    node = HTMLNode(props={"href": "https://example.com", "class": "link"})
    print(node.props_to_html())

if __name__ == "__main__":
    main()