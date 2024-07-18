from textnode import TextNode


def main():
    # Create a TextBode Object
    node = TextNode("Text Node Object", "bold",
                    "https://neetcode.io/practice")

    # print the object

    # Create the other object
    other_node = TextNode("Text Node Object", "bold",
                          "https://neetcode.io/practice")

    # Check if eq function works
    print(node == other_node)


if __name__ == "__main__":
    main()
