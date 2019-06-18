from io import StringIO
from re import match

def extractNextPair(stream):
    buffer = ''
    lvl = 0
    char = stream.read(1)
    while True:
        if lvl == 0 and char == ',' or not char:
            break

        if char == '{':
            lvl += 1
        elif char == '}':
            lvl -= 1

        if char != ' ':
            buffer += char

        char = stream.read(1)

    return buffer

def deserializeValue(value):
    if match('^{.*}$', value):
        return deserializeObject(value)
    elif value == 'None':
        return None

    return int(value)

def deserializeObject(text):
    if not match('^{.*}$', text):
        raise Exception('Invalid formatted object: {0}'.format(text))

    stream = StringIO(text[1:-1])

    result = {}
    while True:
        pair = extractNextPair(stream)
        if not pair:
            break

        key, value = pair.split(':', 1)
        result[key[1:-1]] = deserializeValue(value)

    return result

def denormalizeObject(normalized):
    denormalizeChild = lambda x: denormalizeObject(x) if x else None
    
    return Node(
        value = normalized['value'],
        left = denormalizeChild(normalized['left']),
        right = denormalizeChild(normalized['right']),
    )

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def serialize(self):
        serializeChild = lambda x: x.serialize() if x else 'None'

        return "{{'value': {0}, 'left': {1}, 'right': {2}}}".format(
            self.value,
            serializeChild(self.left),
            serializeChild(self.right),
        )
    @staticmethod
    def deserialize(serialized):
        normalized = deserializeObject(serialized)

        return denormalizeObject(normalized)

__all__ = ['Node']
