
# Przykład logowania w Pythonie
import logging

log_format="%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
logging.basicConfig(
    format=log_format,
    handlers= [
        logging.StreamHandler(),
        logging.FileHandler("app1.log")
    ],
    level=logging.DEBUG,
    #filename="app.log",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.fatal("fatal message")

try:
    y = 1/0
except Exception as exc:
    logging.critical(exc, exc_info=True)