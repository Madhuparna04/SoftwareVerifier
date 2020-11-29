# SoftwareVerifier

This projects contains code for the Software Verification Tool.

## Project Description:

The projects uses Software Requirements specified in the form of state diagrams to automatically verify the correctness of a software.
It uses a set of independent state diagrams and the software verification algorithm designed for this project to identify if the runtime
behaviour of the software is anomalous or not.

## Quick Start

1. Prepare the individual state diagrams in .dot file format. (For e.g see Fine.dot file)

2. Modify the combinemodel.py file by adding the names of the files in the list of files.

3. Run the combinemodel.py program to which will save the processed information in save.p file.
 
   `python3 combinemodel.py`

4. Run the flask app

   `python3 tool.py`

5. Open it in browser

    http://127.0.0.1:2020/

6. Upload a python program and click upload.

7. List of functions extracted from the python file will appear on the left, click on a function to see its definition. List of events extracted from the .dot files will appear on the right. Fill the form to select lines in the python code where extra log statements will be added. For example, the event "Book submitted" should be added just after the user's book submission request is approved, in case of a Library Management System.

8. After adding all the log statements click submit. The tool will run the code and store the log statements in log.txt file. And check if there are any violations of the expected behaviour specified using the state diagrams and report it.
