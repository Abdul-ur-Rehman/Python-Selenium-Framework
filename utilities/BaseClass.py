import inspect
import logging

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler("../pytest_testFiles/logfile.log")
        formatting = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatting)
        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.INFO)

        return logger