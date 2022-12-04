# Подготовить таблицу вероятностей каждого символа
final_result_code = {}
def findTheCharFrequency(text):
    result = dict()
    with open(text,'r') as f:
        result = dict()
        with open(text,'r') as f:
            lines = f.readlines()
            ver = [float(i) for i in list(lines[1].split())]
            result = dict(zip(lines[0], ver))
    return result


# Создать класс узла
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None

# Создать дерево Хаффмана
class HuffmanTree(object):
    # По идее дерева Хаффмана: на основе узла построить дерево Хаффмана в обратном порядке
    def __init__(self, char_Weights):
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    # Создавать коды с рекурсивным мышлением
    def Hu_generate(self, tree, length):
        node = tree
        k = []
        if (not node):
            return
        elif node.name:
            for i in range(length):
                k.append(self.Buffer[i])
            final_result_code.update({node.name: ''.join(map(str, k))}) 
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1)

    #Output кодировка Хаффмана
    def get_code(self):
        self.Hu_generate(self.root, 0)

if __name__=='__main__':
    text = r'code_hafmann_input.txt'
    result = findTheCharFrequency(text)
    tree = HuffmanTree(result)
    tree.get_code()
    print(final_result_code)