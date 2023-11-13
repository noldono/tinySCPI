import time

import tinyscpi
from tinyscpi import tinySCPI

'''
    Example of scanraw command showcasing data collection along with how data will be saved for later uses
'''
def main():

    #sets the min start frequency for low input mode 
    low_start_freq = 0
    #sets the max stop frequency for low input mode
    low_stop_freq = 350000000
    #sets the min start frequency for high input mode
    high_start_freq = 240000000
    #sets the max stop frequency for high input mode
    high_stop_freq = 959000000
    #sets the number of points the scanraw command will collect from tinySA 
    points = 200
    
    #sets the tinySA to Low input mode 
    tinySCPI.user_input("SYST:MODE:LOW:IN")
    #runs the scanraw command and will save data collected as "Low.csv"
    Low_Data = tinySCPI.scan_raw_points(True, low_start_freq, low_stop_freq, points, 'Low')
   
    #outputs gathered data from low input mode in terminal 
    print(Low_Data)
    
    time.sleep(2)
    
    #sets the tinySA to High input mode 
    tinySCPI.user_input("SYST:MODE:HIGH:IN")
    #runs the scanraw command and will save data collected as "High.csv"
    High_Data = tinySCPI.scan_raw_points(True, high_start_freq, high_stop_freq, points, 'High')
    
    #outputs gathered data from high input mode in terminal 
    print(High_Data)


if __name__ == "__main__":
    main()