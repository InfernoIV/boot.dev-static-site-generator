from textnode import TextNode
from htmlnode import HTMLNode

def main():
    #node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    
    props = """{
    "href": "https://www.google.com",
    "target": "_blank",
}"""
    node = HTMLNode("p", "Lorem Ipsum", None, props)
    
    props_html = node.props_to_html()

    print(props_html)

main()