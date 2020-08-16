# VAC
Project submission for HFA 2020
# Code Structure
AnalogClass.py defines GUI and user intractions with the platfrom. RemoteTeaching.py is where the functional methods are defined. 
Two class are defined:
### RemoteTeaching
RemoteTeaching is where the Book list in JSON format is recived. For each Book entry in the list the approrpiate READ method is called to read book and broadcats it.  3 different READ methods are defined: readTextBook, convertImgBook and playAudio
### LibraryManagment
This class is a simple Library management system to check the availability, and perform check-in, check-out. The main methods are checkAvailability, and checkOut 
### Input file format
The expected input file is in JSON format. The required fields are:
 "TxtBookDir": "Path to the directorie where ONLY books are stored",
 "BookType":"audio, txt or img",
 "What is AIDs": "Book name without format, e.g: Book_01"
