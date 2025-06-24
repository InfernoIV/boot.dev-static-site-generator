from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text (plain)"
    BOLD = "**Bold text**" 
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "Links, in this format: [anchor text](url)"
    IMAGE = "Images, in this format: ![alt text](url)"

class TextNode:
    #init
    def __init__(self, text = "", text_type = TextType.TEXT, url = None):
        #The text content of the node
        self.text = text
        #The type of text this node contains, which is a member of the TextType enum.
        self.text_type = text_type
        #The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        self.url = url
    
    def __repr__(self): 
        #method that returns a string representation of the TextNode object. It should look like this:
        #TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __eq__(self, other_textNode):
        
        if self.text != other_textNode.text:
            #print(f"text not equal!: '{self.text}', '{other_textNode.text}'")
            return False
        
        if self.text_type != other_textNode.text_type:
            #print(f"text_type not equal!: '{self.text_type}', '{other_textNode.text_type}'")
            return False
        
        if self.url != other_textNode.url:
            #print(f"url not equal!: '{self.url}', '{other_textNode.url}'")
            return False     
           
        #all checks passed, return true
        return True

def text_node_to_html_node(text_node: TextNode):
    #LeafNode(tag, value, props = None)  
   
    #It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception. Otherwise, it should return a new LeafNode object.
    match text_node.text_type:
        #TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        
        #TextType.BOLD: This should return a LeafNode with a "b" tag and the text
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        #TextType.ITALIC: "i" tag, text
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)

        #TextType.CODE: "code" tag, text
        case TextType.CODE:
            return LeafNode("code", text_node.text)

        #TextType.LINK: "a" tag, anchor text, and "href" prop
        case TextType.LINK:
            #TODO
            return LeafNode("a", text_node.text, {"href": ""})
        
        #TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": "", "alt": ""})
        
        case _:
            raise ValueError(f"Unknown text type! '{text_node.text_type}'")    
    