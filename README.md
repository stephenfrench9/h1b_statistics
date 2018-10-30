# Run Instructions
Download H1-B data from this Google Drive Repo [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing), and place it in the '/input' directory in your repo. Execute run.sh from project root. Alternatively, visit [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension) to get raw data, and format a csv file in the same manner as the ones above.

The results can be round in `/output/top_10_occupations.txt` and `/output/top_10_states.txt`

# Problem
This repo calculates the percentage of successful H1-B applications by occupation and state, and returns the ten most frequent jobs and states for successful applications, as well as the total count and percentage of total. 

# Approach
Simple counting of the number of successful applications, number of successful applications by state, and number of successful applications by job was performed. It is important that the data be formatted as in the above .csv files in the google drive. If erroneous results are observed, it may be neccessary to add filters that examine each row of data to see if they conform to header guidelines. Results are first ordered by count and then by alphabet. Python's built-in `sorted()` method was used to order the results after they were accumulated in a python dictionary. The csv was parsed with the Python library called 'csv'.

# Additional testing
Additional tests may be placed alongside '/insight_testsuite/tests/corrected_test_1'. To test, run 'run_tests.sh' from the '/insight_testsuite' directory. The raw csv in '/insight_testsuite/tests/newtest/input' will be processed, and the results will be written to the '/insight_testsuite/temp/output' directory.  

