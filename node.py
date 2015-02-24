# CSCI 3202: Assignment 4
# Node.py
# Kara James, Joshua Weaver

# File for defining the node object

# Node for storing information in Bayes Net
class node(object):
    # Store list of parent nodes
    parents = list()
    # Store dictionary of probabilities
    probabilities = dict()

    def __init__(self, parents, probabilities):
        for parent in parents:
            self.parents = parents
        self.probabilities = probabilities

def make_node(parents, probabilities):
    node1 = node(parents, probabilities)
    return node1
    


