#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Start with the first box (index 0)
    stack = [0]
    
    while stack:
        # Get the current box index
        current_box = stack.pop()
        # Mark the current box as visited
        if current_box not in visited:
            visited.add(current_box)
            # Add all keys found in the current box to the stack
            for key in boxes[current_box]:
                if key not in visited and key < len(boxes):
                    stack.append(key)
    
    # Return True if all boxes are visited
    return len(visited) == len(boxes)

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

