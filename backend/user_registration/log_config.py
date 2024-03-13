import logging
import time


def get_logger():
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt="%Y-%m-%dT%H:%M:%SZ"
    )
    formatter.converter = time.gmtime

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename='app.log')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logging.basicConfig(
        handlers=(stream_handler, file_handler,),
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)
    return logger
