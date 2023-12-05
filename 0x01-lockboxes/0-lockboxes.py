#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes."""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    opened_boxes = [0]
    for box in opened_boxes:
        for key in boxes[box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.append(key)

    return len(opened_boxes) == len(boxes)
