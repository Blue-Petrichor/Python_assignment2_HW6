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
        for lines in error:                 # iterate over file
            lines_errors = lines.split()    # split file into a list
            for logs in lines_errors:        # iterate over errors in list
                error_file.append(logs.decode("utf-8")) # decode file

                #print(logs.decode("utf-8"))
                file_out = logs.decode("utf-8")
                f = (re.match("<span> &.ico </span>", file_out))
                print(f)


def main():
    """
	Main function
    """
    # call url get function that prints the file parsed into the array
    urlGetFile()

    pass

if __name__ == "__main__":
    #call main fuction
    main()

    exit(0)

