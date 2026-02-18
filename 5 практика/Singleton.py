import json
import threading
from typing import Optional
from enum import Enum


class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3


class Logger:
    _instance: Optional['Logger'] = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._level = LogLevel.INFO
                    cls._instance._log_file = "app.log"
                    cls._instance._load_config()
        return cls._instance

    def _load_config(self, filename: str = "logger_config.json") -> None:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                config = json.load(f)
                self._level = LogLevel[config.get("level", "INFO")]
                self._log_file = config.get("file", "app.log")
        except:
            pass

    def set_log_level(self, level: LogLevel):
        self._level = level

    def log(self, message: str, level: LogLevel):
        if level.value >= self._level.value:
            with open(self._log_file, "a", encoding="utf-8") as f:
                f.write(f"[{level.name}] {message}\n")


class LogReader:
    def __init__(self, filename: str = "app.log"):
        self.filename = filename

    def read_errors(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return [line for line in f if "[ERROR]" in line]
        except:
            return []


if __name__ == "__main__":
    open("app.log", "w").close()  # This truncates the file to empty

    logger = Logger()
    logger.log("Info message", LogLevel.INFO)
    logger.log("Warning", LogLevel.WARNING)
    logger.log("Error", LogLevel.ERROR)

    logger.set_log_level(LogLevel.ERROR)
    logger.log("Info after change", LogLevel.INFO)


    def worker():
        log = Logger()
        log.log("From thread", LogLevel.ERROR)


    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    reader = LogReader()
    print("Errors from log:", reader.read_errors())