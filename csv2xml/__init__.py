import sys
import pandas as pd
from .csv2xml import to_xml

pd.DataFrame.to_xml = to_xml

def main():
    """Entry point for the application script"""
    if len(sys.argv) == 1:
        print(""" 
            Usage:
            $ csv2xml filein [fileout]

            Examples:
            $ csv2xml some_data.csv                  --> print xml to stdout
            $ csv2xml some_data.csv contert_data.xml --> write xml to file 
        """)
        sys.exit()
    elif len(sys.argv) == 2:
        df = pd.read_csv(sys.argv[1])
        print(df.to_xml())
    elif len(sys.argv) == 3:
        df = pd.read_csv(sys.argv[1])
        df.to_xml(sys.argv[2])
    else:
        print(""" 
            Usage:
            $ csv2xml filein [fileout]

            Examples:
            $ csv2xml some_data.csv                  --> print xml to stdout
            $ csv2xml some_data.csv contert_data.xml --> write xml to file 
        """)
        sys.exit()

if __name__ == "__main__":
    main()