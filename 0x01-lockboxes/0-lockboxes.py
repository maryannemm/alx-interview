#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Checks if all the boxes can be unlocked.
    Returns:
        True: if every box can be unlocked
        False: if not all boxes can be unlocked
    '''
    total_boxes = len(boxes)
    keys = set()  # To store the collected keys
    unlocked_boxes = []  # Track which boxes are unlocked
    current_box = 0

    while current_box < total_boxes:
        previous_box = current_box
        unlocked_boxes.append(current_box)
        keys.update(boxes[current_box])  # Add keys found in the current box
        for key in keys:
            if key != 0 and key < total_boxes and key not in unlocked_boxes:
                current_box = key  # Move to the next box using a key
                break
        if previous_box != current_box:
            continue
        else:
            break

    # Check if all boxes (except the first one) have been unlocked
    for box_index in range(total_boxes):
        if box_index not in unlocked_boxes and box_index != 0:
            return False
    return True

