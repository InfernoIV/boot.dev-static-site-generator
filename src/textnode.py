from enum import Enum

class TextType(Enum):
    Plain_text = "text (plain)"
    Bold_text = "**Bold text**" 
    Italic_text = "_Italic text_"
    Code_text = "`Code text`"
    Links = "Links, in this format: [anchor text](url)"
    Images = "Images, in this format: ![alt text](url)"

class TextNode:
    #The text content of the node
    text = ""
    #The type of text this node contains, which is a member of the TextType enum.
    text_type = TextType.Plain_text
    #The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    url = ""
    #init
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_textNode):
        #use represent for a quick check if both are equal
        return self.__repr__ == other_textNode.__repr__

        return False

    def __repr__(self): 
        #method that returns a string representation of the TextNode object. It should look like this:
        #TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


