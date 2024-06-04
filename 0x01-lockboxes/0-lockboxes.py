#!/usr/bin/python3
'''
determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to
    the other boxes.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    un_boxes = set(boxes[0]).difference(set([0]))
    while len(un_boxes) > 0:
        boxIdx = un_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            un_boxes = un_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
