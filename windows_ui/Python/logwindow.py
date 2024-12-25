from PySide6.QtCore import QObject
from utility.qthelper import findObject
from typing import List

class Log:
    def __init__(self, root: QObject, objectName: str):
        elem = findObject(objectName, root)
        if elem is None :
            print("Could not find logger element")
            return

        print("Logger found")
        self.qtElem = elem
        self.logs: List[str] = []

    def push(self, text: str):
        if not self.qtElem:
            print("Logger not initialized")
            return

        self.logs.append(text)
        self.qtElem.setProperty("model", self.logs)