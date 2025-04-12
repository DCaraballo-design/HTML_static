from textnode import TextNode

def main():
    # Create a TextNode instance
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


main()