def decodeVersion(f):
    nums = []
    for i in range(4):
        nums.append(readUShort(f))
    return nums

def getTreeType(byte):
    if byte == 0:
        return None
    elif byte == 1:
        return "Bool"
    elif byte == 2:
        return "double"
    elif byte == 3:
        return "string"
    elif byte == 4:
        return "list"
    elif byte == 5:
        return "dict"
    
def readBool(f):
    return True if f.read(1) == b"\x01" else False

def readByte(f):
    return int.from_bytes(f.read(1),"little",signed=True)

def readUByte(f):
    val = f.read(1)
    return int.from_bytes(val,"little",signed=False)

def readShort(f):
    return int.from_bytes(f.read(2),"little",signed=True)

def readUShort(f):
    val = f.read(2)
    return int.from_bytes(val,"little",signed=False)

def readInt(f):
    return int.from_bytes(f.read(4),"little",signed=True)

def readUInt(f):
    return int.from_bytes(f.read(4),"little",signed=False)

def readLong(f):
    return int.from_bytes(f.read(8),"little",signed=True)

def readULong(f):
    return int.from_bytes(f.read(8),"little",signed=False)

def readFloat(f):
    return np.frombuffer(f.read(4),dtype=np.float32)[0]

def readDouble(f):
    return np.frombuffer(f.read(8),dtype=np.float64)[0]

def readString(f):
    boo = readBool(f)
    if boo:
        return None
    length = readUByte(f)
    return f.read(length).decode("utf-8")

def readDict(f : BinaryIO):
    dic = dict()
    # print(f.tell())
    numElements = readUInt(f)
    # print(f.tell())
    for i in range(numElements):
        key = readString(f)
        value = readPropTree(f)
        dic[key] = value
    return dic

def readList(f):
    numElements = readUInt(f)
    list = []
    for i in range(numElements):
        list.append(readPropTree(f))
    return list

def readPropTree(f):
    treeType = readUByte(f)
    readBool(f)
    if treeType == 0:
        return None
    elif treeType == 1:
        return readBool(f)
    elif treeType == 2:
        return readDouble(f)
    elif treeType == 3:
        return readString(f)
    elif treeType == 4:
        return readList(f)
    elif treeType == 5:
        return readDict(f)