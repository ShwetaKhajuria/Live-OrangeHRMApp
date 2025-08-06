# OLD CODE
# import logging
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#
#         fh = logging.FileHandler("Logs/Automation.log", mode='a')
#         formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
#                                       datefmt='%m/%d/%y %I:%M:%S')
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)
#
#         return logger

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
