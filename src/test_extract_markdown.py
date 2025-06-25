import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class testExtract_markdown_images(unittest.TestCase):
    def test_0_images(self):
        text = "This is text with no images "
        images = extract_markdown_images(text)
        self.assertEqual(images, [])
    
    def test_1_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_2_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ])
        
    def test_mixed_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),  
        ])
    
    def test_mixed_links(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ])

    def test_2_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [
            ("to boot dev", "https://www.boot.dev"), 
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])
            

if __name__ == "__main__":
    unittest.main()
