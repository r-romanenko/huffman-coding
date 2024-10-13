import json
from unittest import TestCase

from huffman import HuffmanCoding
from huffman_node import HuffmanNode

class HuffmanTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def assert_huffman_node(self, huffman_tree_node:HuffmanNode):
        children = 0
        if huffman_tree_node.left is not None:
            self.assertGreaterEqual(huffman_tree_node.weight, huffman_tree_node.left.weight)
            self.assert_huffman_node(huffman_tree_node.left)
            children += 1
        if huffman_tree_node.right is not None:
            self.assertGreaterEqual(huffman_tree_node.weight, huffman_tree_node.right.weight)
            self.assert_huffman_node(huffman_tree_node.right)
            children += 1
        if children == 2:
            self.assertGreaterEqual(huffman_tree_node.right.weight, huffman_tree_node.left.weight)
            self.assertIsNone(huffman_tree_node.value)
        else:
            self.assertIsNotNone(huffman_tree_node.value)    
    

    def test_smallest_encoding(self):
        input = "happy"
        map, encoding = HuffmanCoding.encode(input)
        self.assertEqual(10, len(encoding))
        self.assert_huffman_node(map)
        self.assertEqual(input, HuffmanCoding.decode(map, encoding))

    def test_small_encoding(self):
        input = "she sells sea shells"
        map, encoding = HuffmanCoding.encode(input)
        self.assertEqual(49, len(encoding))
        self.assert_huffman_node(map)
        self.assertEqual(input, HuffmanCoding.decode(map, encoding))

    def test_medium_encoding(self):
        input = "Many of the truths that we cling to depend on our viewpoint."
        
        map, encoding = HuffmanCoding.encode(input)
        self.assertEqual(243,
                         len(encoding))
        self.assert_huffman_node(map)
        self.assertEqual(input, HuffmanCoding.decode(map, encoding))

    def test_larger_encoding(self):
        input = self._load_string_from_file(f"./tests/data/encoding_data.txt")
        map, encoding = HuffmanCoding.encode(input)
        print(input)
        self.assertEqual(8661, len(encoding))
        self.assert_huffman_node(map)
        self.assertEqual(input, HuffmanCoding.decode(map, encoding))

    def _load_string_from_file(self, file_name):
        with open(file_name, "r") as results:
            return  results.read()

