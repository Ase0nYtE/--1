import json
import threading
from typing import Dict, Optional


class ConfigurationManager:
    _instance: Optional['ConfigurationManager'] = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._settings = {}
                    cls._instance._load_from_file()
        return cls._instance

    def _load_from_file(self, filename: str = "config.json") -> None:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self._settings = json.load(f)
        except FileNotFoundError:
            pass
        except Exception:
            pass

    def save_to_file(self, filename: str = "config.json") -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self._settings, f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def get(self, key: str, default: str = None) -> Optional[str]:
        return self._settings.get(key, default)

    def set(self, key: str, value: str) -> None:
        self._settings[key] = value


if __name__ == "__main__":
    config1 = ConfigurationManager()
    config1.set("theme", "dark")
    config1.save_to_file()

    config2 = ConfigurationManager()
    print(config1 is config2)  # True


    def worker():
        cfg = ConfigurationManager()
        cfg.set("worker_set", "yes")


    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()