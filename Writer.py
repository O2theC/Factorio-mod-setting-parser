import numpy as np

from Settings import Settings





def encodeVersion(VersionAr):
    versionBytes = bytes()
    for i in range(4):
        versionBytes += encodeUShort(VersionAr[i])
    return versionBytes
        
def encodeBool(b):
    return bytes([b])

def encodeByte(b):
    return int.to_bytes(b,1,"little",signed=True)

def encodeUByte(b):
    return int.to_bytes(b,1,"little",signed=False)

def encodeShort(b):
    return int.to_bytes(b,2,"little",signed=True)

def encodeUShort(b):
    return int.to_bytes(b,2,"little",signed=False)

def encodeInt(b):
    return int.to_bytes(b,4,"little",signed=True)

def encodeUInt(b):
    return int.to_bytes(b,4,"little",signed=False)

def encodeLong(b):
    return int.to_bytes(b,8,"little",signed=True)

def encodeULong(b):
    return int.to_bytes(b,8,"little",signed=False)

def encodeFloat(b):
    return np.float32(b).tobytes()

def encodeDouble(b):
    return np.float64(b).tobytes()

def encodeString(b: str):
    stringBytes = bytes()
    stringBytes += encodeBool(False)
    stringBytes += encodeUByte(len(b.encode("utf-8")))
    stringBytes += b.encode("utf-8")
    return stringBytes

def encodeDict(b: dict):
    dictBytes = bytes()
    dictBytes += encodeUInt(len(b))
    for key in b:
        dictBytes += encodeString(key)
        dictBytes += encodePropTree(b[key])
    return dictBytes
    
def encodeList(b: list):
    listBytes = bytes()
    listBytes += encodeUInt(len(b))
    for item in b:
        listBytes += encodePropTree(item)
    return listBytes

def encodePropTree(b):
    varType = 0
    if type(b) == bool:
        varType = 1
    elif type(b) == float:
        varType = 2
    elif type(b) == str:
        varType = 3
    elif type(b) == list:
        varType = 4
    elif type(b) == dict:
        varType = 5
    else:
        raise Exception("Unknown type - " + str(type(b)))
    propTreeBytes = bytes()
    propTreeBytes += encodeUByte(varType)
    propTreeBytes += encodeBool(False)
    if varType == 1:
        propTreeBytes += encodeBool(b)
    elif varType == 2:
        propTreeBytes += encodeDouble(b)
    elif varType == 3:
        propTreeBytes += encodeString(b)
    elif varType == 4:
        propTreeBytes += encodeList(b)
    elif varType == 5:
        propTreeBytes += encodeDict(b)
    return propTreeBytes

def encodeSettings(settings: Settings):
    
    settingsBytes = bytes()
    settingsBytes += encodeVersion(settings.version)
    settingsBytes += encodeBool(False)
    settingsCopy = settings.settings.copy()
    settingsCopy.pop("version")
    settingsBytes += encodePropTree(settingsCopy)
    return settingsBytes
