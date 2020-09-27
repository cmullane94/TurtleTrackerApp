#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Claire Mullaney (claire.mullaney@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './Data/Raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Creating empty dictionary for dates
date_dict = {}

#Creating empty dictionary for location coordinates
coord_dict = {}

#Iterate through all lines in the lineList
for lineString in line_list:
    if lineString[0] in ('#', 'u'): continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara using an f-string
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    
    #Add the observation date to an empty dictionary
    date_dict[record_id] = obs_date
    
    #Add the observation coordinates to an empty dictionary
    coord_dict[record_id] = (obs_lat, obs_lon)
    
    