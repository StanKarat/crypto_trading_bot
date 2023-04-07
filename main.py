import tkinter as tk
import logging
from connectors.Binance_futures import BinanceFuturesClient


logger = logging.getLogger()
logger.setLevel(logging.INFO)


logger.debug("This message is important only when debugging the program")
logger.info("This message just show the basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debug error that occurred in the program")


stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)


logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient(True)
    print(binance.get_historical_candles("BTCUSDT", "1h"))

    root = tk.Tk()
    root.mainloop()
    
