#!/user/bin/env python3
import sys
import re
from urllib.request import urlopen

def urlGetFile():
    """
    Get the file from a url (web) location
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as error:
        error_file = []                     # set an empty array
        #for lines in error:                 # iterate over file
         #   lines_errors = lines.split()    # split file into a list
          #  for logs in lines_errors:        # iterate over errors in list
           #     error_file.append(logs.decode("utf-8")) # decode file

            #    print(logs.decode("utf-8"))

        for logs in error:        # iterate over errors in list
            file_out =  error_file.append(logs.decode("utf-8")) # decode file
            find_something = file_out.find(".ico")
            print(find_something.decode("utf-8"))

def main():
    """
	Main function
    """
    # call url get function
    urlGetFile()

    # call definition and call fetch words parameteri
#    fetch_words(error_file)

    pass

if __name__ == "__main__":
    #call main fuction
    main()

    exit(0)

