from PySide6.QtCore import QObject
from typing import Optional

def findObject(objectName: str, obj: QObject) -> Optional[QObject] :

    if obj.objectName() == objectName :
        return obj

    children = obj.children()
    for child in children :
        result = findObject(objectName, child)
        if result:
            return result

    return None
