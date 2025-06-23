from enum import Enum

class TextType(Enum):
    PLAIN = "text (plain)"
    BOLD = "**Bold text**" 
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "Links, in this format: [anchor text](url)"
    IMAGE = "Images, in this format: ![alt text](url)"

class TextNode:
    #init
    def __init__(self, text = "", text_type = TextType.PLAIN, url = None):
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
