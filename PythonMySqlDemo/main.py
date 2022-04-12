import logging
import os
import sys
import datetime
import utils


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Program start.")
utils.print_all_options()
input_option = utils.take_option()
utils.do_operation(input_option)






