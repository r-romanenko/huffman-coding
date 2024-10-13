class HuffmanNode:
    def __init__(self, 
                 value:str, 
                 weight:int,
                 left:"HuffmanNode" =None, 
                 right: "HuffmanNode" =None) -> None:
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right
