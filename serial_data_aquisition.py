# mjdt 22.03.2023
# code to acquite data from a serial port (i.e anemometer)


# Import necessary packages
import serial
from datetime import datetime

20
# define inputs 
com ='COM6' # USB serial port
baud = 19200 # Transmission rate in serial channel
filename_root = "anemometer.csv" # create filnename root
F = 32 # (Hz) sampling frequency 
print_data = "y" # command to display live data
duration = 60 # (s) measurement duration 


# function that opens the serial port
def createSerial(com, baud):
    ser = serial.Serial(port=com, baudrate=baud, bytesize=serial.EIGHTBITS, timeout=2)
    return ser


# function that acquires and saves measurements
def acquire_data(fs_acq, duration,print_data):
    # initialise variables
    i = 0 
    data = []

    anemometer = createSerial(com, baud) # call createSerial, function that opens the serial port
    print(anemometer.is_open) # print whether the anemometer is open (True) or not (False)

    while i< fs_acq*duration: # for every sample in the given duration
        data.append(anemometer.readline()) # read line of data
        if print_data == "y": # If the print data is set to yes 
            print(data[-1]) # Print last line of data 
        i += 1 # update counter
    
    anemometer.close()
    return data  # return the measured data 


def save_data(data, filename_root):
    # filename
    now = datetime.now() # get current date and time
    dt_string = now.strftime("%Y%m%d-%H%M%S") # transform it into string
    filename = (dt_string + filename_root) # add date to filename

    with open(filename, 'wb') as file: # open the file in binary format for writing
        for line in data: 
            file.write(line) # write every line 
    

data = acquire_data( F, duration,print_data) # call function to acquire data
save_data(data, filename_root) # call function to save data as .csv

