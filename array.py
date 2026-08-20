
import array


# 1. append() - add a single element to the end of the array
def demo_append():
    arr = array.array('i', [1, 2, 3])
    arr.append(4)
    return arr


# 2. buffer_info() - returns memory address and length (in elements)
def demo_buffer_info():
    arr = array.array('i', [1, 2, 3])
    return arr.buffer_info()


# 3. byteswap() - swap byte order of each element (for endianness conversion)
def demo_byteswap():
    arr = array.array('i', [1, 2, 3])
    arr.byteswap()
    return arr


# 4. count() - count occurrences of a value in the array
def demo_count():
    arr = array.array('i', [1, 2, 2, 3, 2])
    return arr.count(2)


# 5. extend() - add elements from an iterable to the end of the array
def demo_extend():
    arr = array.array('i', [1, 2, 3])
    arr.extend([4, 5, 6])
    return arr


# 6. frombytes() - append items from a bytes-like object
def demo_frombytes():
    arr = array.array('i', [1, 2, 3])
    data = array.array('i', [4, 5, 6]).tobytes()
    arr.frombytes(data)
    return arr


# 7. fromfile() - read n items from a file object and append them
def demo_fromfile(filepath, n):
    arr = array.array('i')
    with open(filepath, 'rb') as f:
        arr.fromfile(f, n)
    return arr


# 8. fromlist() - append items from a list
def demo_fromlist():
    arr = array.array('i', [1, 2, 3])
    arr.fromlist([4, 5, 6])
    return arr


# 9. fromunicode() - extend array (unicode type 'u') from a string
def demo_fromunicode():
    arr = array.array('u', 'hello')
    arr.fromunicode(' world')
    return arr


# 10. index() - return the index of the first occurrence of a value
def demo_index():
    arr = array.array('i', [10, 20, 30, 20])
    return arr.index(20)


# 11. insert() - insert a value at a given index
def demo_insert():
    arr = array.array('i', [1, 2, 4])
    arr.insert(2, 3)
    return arr


# 12. pop() - remove and return the item at the given index (default last)
def demo_pop():
    arr = array.array('i', [1, 2, 3, 4])
    popped = arr.pop()
    return popped, arr


# 13. remove() - remove the first occurrence of a value
def demo_remove():
    arr = array.array('i', [1, 2, 3, 2])
    arr.remove(2)
    return arr


# 14. reverse() - reverse the order of elements in place
def demo_reverse():
    arr = array.array('i', [1, 2, 3, 4])
    arr.reverse()
    return arr


# 15. tobytes() - convert array to a bytes representation
def demo_tobytes():
    arr = array.array('i', [1, 2, 3])
    return arr.tobytes()


# 16. tofile() - write all elements to a file object (binary mode)
def demo_tofile(filepath):
    arr = array.array('i', [1, 2, 3, 4])
    with open(filepath, 'wb') as f:
        arr.tofile(f)
    return f"Array written to {filepath}"


# 17. tolist() - convert array to an ordinary Python list
def demo_tolist():
    arr = array.array('i', [1, 2, 3])
    return arr.tolist()


# 18. tounicode() - convert a unicode type array to a string
def demo_tounicode():
    arr = array.array('u', 'hello')
    return arr.tounicode()
