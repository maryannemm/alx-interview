#!/usr/bin/python3
'''UTF-* validation module
'''
def validUTF8(data):
    # Number of bytes remaining to complete the current UTF-8 character
    byte_count = 0
    
    # Masks to check leading bits
    first_byte_masks = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    valid_patterns = [0b00000000, 0b11000000, 0b11100000, 0b11110000]
    
    for num in data:
        # Only consider the least significant 8 bits
        byte = num & 0xFF
        
        if byte_count == 0:
            # Determine how many bytes should follow
            if byte >> 7 == 0:  # 1-byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:  # 2-byte character (110xxxxx)
                byte_count = 1
            elif byte >> 4 == 0b1110:  # 3-byte character (1110xxxx)
                byte_count = 2
            elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
                byte_count = 3
            else:
                return False
        else:
            # Subsequent byte must be of the form 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            byte_count -= 1
    
    # Ensure that we have consumed all bytes for any multi-byte character
    return byte_count == 0

