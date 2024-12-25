import socket

from PySide6.QtCore import QObject
from typing import Optional

from logwindow import Log

class backend:
    def __init__(self, logger: Log):
        self.log = logger
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        if not self.ip :
            logger.push("Can't retrieve your ip address, please make sure you are connected to the router")
        logger.push(f"Succesfully retrieved your ip address: {self.ip}")

