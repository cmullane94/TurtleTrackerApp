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

#Ask the user for a date, specifying the format
user_date = input('Enter a date (M/D/YYYY):')

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
    
    #Print the location of sara using an f-string if lc is 1, 2, or 3
    if obs_lc in ('1', '2', '3'):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        #Add the observation date to empty dictionary
        date_dict[record_id] = obs_date
        #Add the observation coordinates to empty dictionary
        coord_dict[record_id] = (obs_lat, obs_lon)
        
#Create an empty key list
matching_keys = []

#Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():   
#See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
    