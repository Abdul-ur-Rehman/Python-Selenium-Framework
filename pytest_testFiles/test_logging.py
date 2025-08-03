import logging


def test_logging():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler("logfile.log")
    formatting = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    filehandler.setFormatter(formatting)
    logger.addHandler(filehandler) #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed.")
    logger.info("Information statement")
    logger.warning("Warning mode")
    logger.error("fatal error")
    logger.critical("Critical issue")