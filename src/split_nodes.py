from textnode import TextType, TextNode

#It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. 
# For example, given the following input:
#node = TextNode("This is text with a `code block` word", TextType.TEXT)
#new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#new_nodes becomes:
#[
    #TextNode("This is text with a ", TextType.TEXT),
    #TextNode("code block", TextType.CODE),
    #TextNode(" word", TextType.TEXT),
#]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #guard clauses
    if old_nodes == None or len(old_nodes) == 0:
        raise SyntaxError(f"old_nodes not correct: '{old_nodes}'")
    
    if delimiter == None or len(delimiter) == 0:
        raise SyntaxError(f"delimiter not correct: '{delimiter}'")
    
    if text_type not in TextType:
        raise SyntaxError(f"text_type not known: '{text_type}'")
    
    #list to fill, to return
    node_list = []
    
    for node in old_nodes:
        #we only handle text nodes
        if node.text_type != TextType.TEXT:
            #just add the node
            node_list.append(node)
        else:
            #check if we have an even amount of delimiters
            delimiter_amount = node.text.count(delimiter)
            if delimiter_amount % 2 != 0:
                raise ValueError(f"Delimiter '{delimiter}' is not correctly set, found '{delimiter_amount}' times")
           
            #split the text according to the delimiter
            text_blocks = node.text.split(delimiter)
            #print(f"text_blocks: '{text_blocks}'")
            #if no split has happened
            if len(text_blocks) == 1:
                #just add the node
                node_list.append(node)
            #check for even split
            #elif len(text_blocks) != 3:
                #raise ValueError(f"Split has '{delimiter}' is not correctly set, found '{delimiter_amount}' times")
            #split has happened, should be 3?
            else:
                #set counter to keep track of position (before, delimited, after)
                count = 0
                for text_block in text_blocks:
                    #first index
                    if count == 0:
                        node_list.append(TextNode(text_block, node.text_type))
                        #set to middle index
                        count = 1
                    #middle index
                    elif count == 1:
                        #add to the list
                        node_list.append(TextNode(text_block, text_type))
                        #set to last index
                        count = 2
                    #final index
                    elif count == 2:
                        node_list.append(TextNode(text_block, node.text_type))
                        #reset to first index
                        count = 0
        
    #return the list
    return node_list
