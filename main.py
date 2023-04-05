import tkinter as tk
import logging
from BitMEX_futures import get_contracts

# Create a logger 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Different types of messages for program events
logger.debug("This message is important only when debugging the program")
logger.info("This message just show the basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debug error that occurred in the program")

# Create handlers for the logger object to log messages to the console and to a file
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Add the handlers to the logger object
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    # Getting list of BitMEX futures contracts using a function from the BitMEX_futures
    bitmex_contracts = get_contracts()

    # Create the main window of the GUI using Tkinter
    root = tk.Tk()
    root.configure(bg='snow3')

    # Set up row and column counters for displaying the contract labels in a grid
    i = 0
    j = 0

    # Define a font to be used for the contract labels
    montserrat_font = ("montserrat", 11, "normal")

    # Iterate over each contract in the list of BitMEX futures contracts
    for contract in bitmex_contracts:
        # Create a label widget with the contract name and add it to the GUI using the grid method
        label_widget = tk.Label(root, text=contract, bg='snow3', fg='Steelblue4', width=13, font=montserrat_font)
        label_widget.grid(row=i, column=j, sticky='ew')

        # Increment the column counter and reset the row counter after displaying 5 contracts in a row
        if i == 4:
            j += 1
            i = 0
        else:
            i += 1

    # Start the Tkinter event loop to display the GUI
    root.mainloop()
