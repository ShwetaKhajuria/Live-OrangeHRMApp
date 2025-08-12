

import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)
        logger.propagate = False  # ✅ Prevents duplicate logging via root logger

        log_file_path = "Logs/automation.log"
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

        if not logger.handlers:
            fh = logging.FileHandler(log_file_path, mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
