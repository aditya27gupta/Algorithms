"""
Huffman Coding:
    Count how often each piece of data occurs.
    Build a binary tree, starting with the nodes with the lowest count. The new parent node has the combined count of its child nodes.
    The edge from a parent gets '0' for the left child, and '1' for the edge to the right child.
    In the finished binary tree, follow the edges from the root node, adding '0' or '1' for each branch, to find the new Huffman code for each piece of data.
    Create the Huffman code by converting the data, piece-by-piece, into a binary code using the binary tree.
"""


class Node:
    def __init__(self, char: str | None = None, freq: int = 0):
        self.char = char
        self.freq = freq
        self.left: Node | None = None
        self.right: Node | None = None


def generate_codes(
    node: Node | None, codes: dict[str, str], current_code: str = ""
) -> None:
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_codes(node.left, codes, current_code + "0")
    generate_codes(node.right, codes, current_code + "1")


def huffman_encoder(input_string: str) -> tuple[str, dict[str, str]]:
    nodes: list[Node] = []
    added_node: set[str] = set()
    for letter in input_string:
        if letter not in added_node:
            added_node.add(letter)
            num_count = input_string.count(letter)
            nodes.append(Node(char=letter, freq=num_count))

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        nodes.append(merged)

    codes: dict[str, str] = {}
    generate_codes(nodes[0], codes)

    huffman_code = ""
    for letter in input_string:
        huffman_code += codes[letter]

    return huffman_code, codes


def huffman_decoder(huffman_code: str, codes: dict[str, str]) -> str:
    original_string = ""
    start_idx, end_idx = 0, 1
    reverse_codes = {val: key for key, val in codes.items()}
    while end_idx < len(huffman_code) + 1:
        curr_substr = huffman_code[start_idx:end_idx]
        if curr_substr in reverse_codes:
            original_string += reverse_codes[curr_substr]
            start_idx = end_idx
            end_idx = start_idx
        end_idx += 1

    return original_string
