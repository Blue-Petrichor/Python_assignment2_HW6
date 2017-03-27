#!/user/bin/env python3
import sys
import re
import argparse
from urllib.request import urlopen
        

def help_function():
    """
    Help fucntion:
        Usage for file mihael_shaw_HW6.py <RunFile>
    """

def urlGetFile():
    """
    Get the file from a url (web) location
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as error:
        error_file  = []                     # set an empty array
        urls_d = {}                          # instanciate the dictionary

        # Compile the regex and put it into the variable regex for user later
        regex = re.compile(".*/.*")
        for logs in error:
            error_file.append(logs.decode("utf-8"))

        for line in error_file:
            line_words = line.split()
            for words in line_words:
                var = regex.match(words)
                if var:
                    if var.group() in urls_d:
                        urls_d[var.group()] += 1
                    else:
                        urls_d[var.group()] = 1
                    break
        print ("*** Top 25 page errors ***")
        sorted_urls_d = sorted(urls_d, key=urls_d.get, reverse=True)

        # Create a count to list only the first 25 from the count list
        count = 0
        for i in sorted_urls_d:
            count +=1
            # break when count of 25 has been reached
            if (count > 25):
                break
            else:
                # Print dictionary count and position
                print ("Count: ", urls_d[i], " Page: ", i)

def main():
    """
	Main function
    """
    # call url get function that prints the file parsed into the array
    urlGetFile()    
    

    pass

if __name__ == "__main__":
    #call main fuction

    parser = argparse.ArgumentParser()
    parser.add_argument("RunFile", help="Help")
    args = parser.parse_args()

    if args.RunFile == "RunFile":
        main()
    else:
        help_function()

    exit(0)

