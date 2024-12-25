
import os
import sys
import time
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject
from autogen.settings import url, import_paths

from server import backend
from logwindow import Log

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app_dir = Path(__file__).parent.parent

    engine.addImportPath(os.fspath(app_dir))
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    screenRoot = engine.rootObjects()[0]
    root = screenRoot.findChild(QObject, "SCREEN");

    log = Log(root, "logWindow")

    controlServer = backend(log)

    if not root:
        print("Root not initialized propely")
        sys.exit(-1)



    sys.exit(app.exec())

if __name__ == '__main__':
    main()
