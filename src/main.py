from textnode import TextNode

def main():
    # Create a TextNode instance
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()