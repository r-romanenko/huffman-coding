from typing import Dict, Tuple
from huffman_node import HuffmanNode
from pri_queue import PriorityQueue

class HuffmanCoding:
   
    # encodes a string and returns the huffman tree and the resulting binary sequence
    # as a string
    @staticmethod
    def encode(string)->Tuple[HuffmanNode, str]:
        root = HuffmanCoding._generate_huffman_tree(HuffmanCoding._generate_priority_queue(string))
        final = ""
        codes = HuffmanCoding._get_char_codes(root, True)

        for n in string:
            final += codes[n]
        return root, final
    
    # takes the huffman tree root and the encoded string and decodes the message
    @staticmethod
    def decode(huffman_tree:HuffmanNode, encoding:str):
        codes = HuffmanCoding._get_char_codes(huffman_tree)
        final = ""
        temp_code = ""
        for n in encoding:
            temp_code += n
            if temp_code in codes:
                final += codes[temp_code]
                temp_code = ""

        return final
        
        

    
    # Builds a priority queue from the characters in the input_string, where the priority is
    # based on how many times a character appears. Smaller counts should come off the pqueue first.
    @staticmethod
    def _generate_priority_queue(input_string:str)->PriorityQueue:
        frequencies = PriorityQueue()
        letter_frequencies = dict()

        for char in input_string:
            if char not in letter_frequencies:
                letter_frequencies[char] = 1
            else:
                letter_frequencies[char] += 1

        for key in letter_frequencies.keys():
            frequencies.enqueue(letter_frequencies[key], HuffmanNode(key, letter_frequencies[key]))

        return frequencies


    # Builds a Huffman tree based on a priority queue using the Huffman Algorithm.
    # Dequeue 2 items at a time from the pqueue, put them under a new node, then enqueue the new node.
    # Repeat until you have only 1 node. 
    @staticmethod
    def _generate_huffman_tree(pqueue:PriorityQueue)->HuffmanNode:
        while pqueue.size() > 1:
            child_one = pqueue.dequeue()
            child_two = pqueue.dequeue()
            sum = child_one.weight + child_two.weight
            node = HuffmanNode(None, sum, child_one, child_two)
            pqueue.enqueue(node.weight, node)
        return pqueue.dequeue()

    # Traverses the Huffman tree to find the binary codes for each character and returns
    # a dictionary of codes for each character
    @staticmethod
    def _get_char_codes(huffman_tree_root:HuffmanNode, swapped:bool = False)->Dict:
        HuffmanCoding.codes = dict()
        HuffmanCoding._get_char_codes_recursive(huffman_tree_root, "", swapped)
        return HuffmanCoding.codes
        
    @staticmethod
    def _get_char_codes_recursive(node:HuffmanNode, code:str, swapped:bool) -> str:
        # BASE CASE
        if not node:
            return
        if node.value:
            if swapped:
                HuffmanCoding.codes[node.value] = code
            else:
                HuffmanCoding.codes[code] = node.value
        else:
            HuffmanCoding._get_char_codes_recursive(node.left, f"{code}0", swapped)
            HuffmanCoding._get_char_codes_recursive(node.right, f"{code}1", swapped)
        
