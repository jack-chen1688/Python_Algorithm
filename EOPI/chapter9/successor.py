# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 22:59:48 2018

@author: xuehua
"""

def successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        while node.parent and node.parent.right is node:
            node = node.parent
            
        return node.parent
        
            
        