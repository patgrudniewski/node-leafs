#! /usr/bin/env python

from node_leafs import Node

a = Node(value=1)
b = Node(value=2, left=a)
c = Node(value=3, right=b)
d = Node(value=4)
final_node = Node(value=6, left=d, right=c)

assert final_node.serialize() == '''{'value': 6, 'left': {'value': 4, 'left': None, 'right': None}, 'right': {'value': 3, 'left': None, 'right': {'value': 2, 'left': {'value': 1, 'left': None, 'right': None}, 'right': None}}}'''
