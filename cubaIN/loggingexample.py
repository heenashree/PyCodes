# there are 5 types of logging
#https://www.linkedin.com/learning/advanced-python/custom-logging?u=2113185
import logging
logging.basicConfig(filename='testlog.log', level=logging.DEBUG, filemode='w')
#logging.info('Session Start')
def loggerFunc():
    logging.error("Couldnt find item")
    logging.warning("this is warning")
    logging.info("this is info")
    logging.debug("this is debug"
                  )
    logging.critical("this is critical")
if __name__ == "__main__":
    loggerFunc()