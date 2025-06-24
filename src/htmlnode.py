class HTMLNode:
     #init
    def __init__(self, tag = None, value = None, children = None, props = None):
        #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value
        #A list of HTMLNode objects representing the children of this node
        self.children = children
        #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    #Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.
    def to_html(self):
        raise NotImplementedError
    
    #Add a props_to_html(self) method. It should return a string that represents the HTML attributes of the node. 
    def props_to_html(self):
        #string to fill
        properties = ""

        # if not set
        if self.props == None:
            return properties
    
        #if string input
        if isinstance(self.props, str):
            #for each line (except the first and last)
            for line in self.props.splitlines()[1:-1]:
                #print(f"Line: '{line}'")
                #trim the spaces
                line_trimmed = line.strip()
                #if it has a variable (starts with quote)
                if line_trimmed.startswith('"'):
                    words = line_trimmed.replace(",","").split(" ")
                    #print(f"words: {words}")
                    variable = words[0].replace('"',"").replace(":","=")
                    value = words[1].strip()
                    
                    property = f"{variable}{value}"
                    #if we already have properties
                    if properties != "":
                        #add a space inbetween
                        properties += " " 
                    #add the property
                    properties += property
                    #print(f"variable: '{variable}', value: '{value}'")

            #print(f"properties: '{properties}'")
        
        #if dict
        elif isinstance(self.props, dict):
            for k, v in self.props.items():
                property = f"{k}=\"{v}\""
                #if we already have properties
                if properties != "":
                    #add a space inbetween
                    properties += " " 
                #add the property
                properties += property

        #return the string
        return properties
    #For example, if self.props is:
    #{
    #"href": "https://www.google.com",
    #"target": "_blank",
    #}

    #Then self.props_to_html() should return:
    #href="https://www.google.com" target="_blank"
    #Notice the leading space character before href and before target. This is important. HTML attributes are always separated by spaces.

    #Add a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
    def __repr__(self):
        return f"HTMLNode - tag: '{self.tag}', value: '{self.value}', children: '{self.children}', props: '{self.props}'"
 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):      
        #Use the super() function to call the constructor of the HTMLNode class.
        super().__init__(tag, value, None, props)

    #Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).
    def to_html(self):
        #If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
        if self.value == None:
            raise ValueError("Missing value")

        #If there is no tag (e.g. it's None), the value should be returned as raw text.
        if self.tag == None:
            return self.value
        
        #Otherwise, it should render an HTML tag. For example, these leaf nodes:
        #LeafNode("p", "This is a paragraph of text.").to_html()
        #"<p>This is a paragraph of text.</p>"
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        #otherwise use the props_to_html
        #LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        #"<a href="https://www.google.com">Click me!</a>"
        
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"      


#Create another child class of HTMLNode called ParentNode. 
class ParentNode(HTMLNode):
    #Its constructor should differ from HTMLNode in that:
    #The tag and children arguments are not optional
    #It doesn't take a value argument
    #props is optional
    #(It's the exact opposite of the LeafNode class)
    def __init__(self, tag, children, props = None):      
        #Use the super() function to call the constructor of the HTMLNode class.
        super().__init__(tag, None, children, props)

    #Add a .to_html method. 
    def to_html(self):
        #If the object doesn't have a tag, raise a ValueError.
        if self.tag == None:
            raise ValueError("Missing tag")
        #If children is a missing value, raise a ValueError with a different message.
        if self.children == None:
            raise ValueError("Missing children")

        #Otherwise, return a string representing the HTML tag of the node and its children. 
        #This should be a recursive method (each recursion being called on a nested child node).
        return_string = f"<{self.tag}>"
        #print(f"self.tag: '{self.tag}'")
        #print(f"children: '{self.children}'")
        for child in self.children:    
            #print(f"child: '{child}'")
            #print(f"child.to_html(): {child.to_html()}")
            return_string += f"{child.to_html()}"

        #add closing tag
        return_string += f"</{self.tag}>"
        #return the string
        return return_string

