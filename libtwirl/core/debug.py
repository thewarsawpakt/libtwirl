import datetime
import logging

logging.basicConfig(
                    level=logging.INFO, 
                    filename="twirl.log", 
                    filemode="a+",
                    format=f"({datetime.datetime.now()}) %(levelname)s: %(message)s")
