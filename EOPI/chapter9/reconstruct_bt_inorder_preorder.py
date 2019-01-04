# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:17:01 2018

@author: xuehua
"""

def reconstruct_bt_inorder_preorder0(inorder, preorder):
    if not preoder:
        return None
    root = BNode(preorder[0])
    index = 0
    for i, x in enumerate(inorder):
        if x == preoder[0]:
            index = i
            break
        
    root.left = reconstruct_inorder_preorder(inorder[:index], preorder[1:index+1])
    root.right = reconstruct_inorder_preorder(inorder[index+1:], preoder[index+1:])
    

def reconstruct_bt_inorder_preoder1(inorder, preoder):
    if len(preoder) == 0:
        return None
    
    inoder_dict = {x:i for i, x in enumerate(inoder)}
    def doit(inoder_start, inorder_end, preorder_start, preorder_end):
        if inoder_start >= inoder_end:
            return None
        
        root = BNode(preoder[preoder_start])
        index = inorder_dict[preorder[preoder_start]]
        preorder_left_end = preoder_start+1 + index - inoder_start
        root.left = doit(inoder_start, index, preoder_start+1, preoder_left_end)
        root.right = doit(index+1, inorder_end, preoder_left_end, preoder_end )
        return root
        
    return doit(0, len(inoder), 0 , len(preoder))
        