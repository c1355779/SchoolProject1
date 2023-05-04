#Program Name: Lab 6 - Dictionary
#Program Description: This program will create a dictionary and find the dictionary,
#then print out the found results from the dictionary

# write the program to do the following :
# 1: Course, name, and lab
# 2: Current time
# 3: create_my_contact()
# 4: save_json_file(fileName, contact_list)
# 5: find_my_contact_key(searchKey, my_contact)
# 6: test dricer code

#@Author: Kuan-Hua Fu  
#@Date : 2022/04/17

# Import Module
import json 
from datetime import datetime

# create_my_contact()
def create_my_contact(): 
    dic = {"01": {"firstname" : "John", \
                "lastname": "Smith", \
                "DOB" : "1/20/1991", \
                "phoneNum": { \
                    "home" : "5100-600-5400", \
                    "cell" : "510-873-2543" \
                }, \
                "address": { \
                "street" : "100 main street", \
                    "city": "Fremont", \
                    "state" : "CA", \
                    "zipcode" : "94536" \
                }, \
            }, \
            "02": {"firstname": "Ron", \
                    "lastname" : "Robertson", \
                    "DOB" : "5/23/1991", \
                    "phoneNum": { \
                        "home" : "510-600-8800", \
                        "cell" : "925-983-5487" \
                    }, \
                    "address": { \
                        "street" : "4600 Ohlone Way", \
                        "city": "Fremont", \
                        "state" : "CA", \
                        "zipcode" : "94539" \
                    }, \
            }, \
            "03": {"firstname": "Paul", \
                    "lastname": "Washington", \
                    "DOB" : "6/15/1995", \
                    "phoneNum": { \
                        "home" : "510-688-1241", \
                        "cell" : "408-489-8905" \
                    }, \
                    "address": { \
                        "street" : "8543 Ohlone Plaza", \
                        "city": "Fremont", \
                        "state" : "CA", \
                        "zipcode" : "94539" \
                    }, \
                }, \
            }
            
    return dic

# save_json_file(fileName, contact_list)    
def save_json_file(filename, data):
    with open( filename, "w") as outputfile:
        json.dump( data, outputfile)

def open_json_file( filename ):
 
    file = open( filename, 'r' ) 
    return file

# find_my_contact_key(searchKey, my_contact)
def find_my_contact_key( first_name, data ):
    Json = json.load( data )
    first_name_found = False
    print(f"*** Searching for {first_name}" )
    for id, nested_dict in Json.items(): 
        if nested_dict['firstname']==first_name:
            first_name_found = True
            print( f"*** {first_name} found ***" ) 
            print("Name:".ljust(9), f"{nested_dict['firstname']} {nested_dict['lastname']}" )
            print("Birthday:".ljust(9), f"{nested_dict['DOB']}" ) 
            print("cell:".ljust(9) ,f"{nested_dict['phoneNum']['home']}" ) 
            print("Address:".ljust(9) ,f"{nested_dict['address']['street']}\n\t {nested_dict['address']['city']} , {nested_dict['address']['state']} {nested_dict['address']['zipcode']}") 
            print("\n") 
            Json = None 
            return
    
    if not first_name_found:
        print(f"*** {first_name} not found **** ")

# test dricer code
if __name__ == '__main__':

    # Course, name, and lab    
    name = "Kuan-Hua Fu - CNET 142 - Lab 6 Dictionary"
    print ("{:16}".format("Name"), ':', name)
    
    lab = "dictionary.py" 
    print ("{:16}".format("Program"),':', lab)
    # Current time    
    currentTime = datetime.now()
    TimestampStr = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
    print("{:16}".format("Current Time"), ':', TimestampStr)
    
    contact_list = create_my_contact() 
    save_json_file("my_contact.json" , contact_list )

    json_data = open_json_file( "my_contact.json" )
    
    print("***BEGINING OF JSON List: \n", contact_list, \
        "\n***END OF JSON LIST\n\n")
        
    find_my_contact_key("Ron", json_data)
    
    json_data = open_json_file( "my_contact.json" )
    
    find_my_contact_key("Sha", json_data)