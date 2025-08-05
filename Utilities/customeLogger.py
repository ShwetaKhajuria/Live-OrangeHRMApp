import logging

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler("Logs/Automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%y %I:%M:%S')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger

