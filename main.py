#creating a node
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return "{}".format(self.value)

#creating the tree
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value), type(cur_node.left_child))
            self._print_tree(cur_node.right_child)

    def remove(self):
        pass

    def search(self, value):
        if self.root != None:
            if value == self.root.value:
                return print("the value {} in tree".format(value))
            else:
                self._search(value, self.root)
        else:
            return print("tree has no values")

    def _search(self, value, cur_node):
        # print(cur_node.value)
        if value < cur_node.value:
            if value == cur_node.left_child:
                print("the value {} in tree".format(value))
                return
            else:
                self._search(value, cur_node.left_child)
        elif value > cur_node.value:
            print("hi")
            print(type(cur_node.right_child))
            print(type(value))

            if value == cur_node.right_child:
                print("the value {} in tree".format(value))
                return
            else:
                self._search(value, cur_node.right_child)
        # else:
        #     print("value {} not in tree".format(value))
        #     return



def fill_tree(tree, num_elements =100, max_int=1000):
    for i in range(num_elements):
        element = random.randint(0, max_int)
        tree.insert(element)
    return tree


tree = BST()
print(tree)
fill_tree(tree, 100)
tree.insert(10)
tree.insert(12)
tree.print_tree()

tree.search(12)



class Class:

    def __init__(self, att):
        self.att =  att


test = Class(10)
print(type(test.att))
a= 10

if a == test.att:
    print("equal!")

print(type(test))
print(type(tree))
print(type(Node.left_child))