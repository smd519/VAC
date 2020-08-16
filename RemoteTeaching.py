#
# Copyright (C) Sajjad M- HFA 2020
# All Rights Reserved.
#
import json
import os
import codecs
# text to speech conversion
from gtts import gTTS
from playsound import playsound
from datetime import datetime
#image to text string
import pytesseract
#image processing
from PIL import Image
curDir = os.path.dirname(os.path.abspath(__file__))
listDir='BookList'
inventoryDir='Inventory'
# Language to convert
language = 'en'

class RemoteTeaching:
    def __init__(self, toRead_list):
        with open(toRead_list, 'r') as json_file:
            self.dictOfCmds = json.loads(json_file.read())
        self.TxtBookDir = self.dictOfCmds ['TxtBookDir']
        self.bookType=self.dictOfCmds ['BookType']

    # Go through the list of the books one by one
    def readBookList(self):
        for i in self.dictOfCmds.keys():
            if i in ['TxtBookDir','BookType']:
                continue
            if self.bookType=='txt':
                # Build the path to each Txt Book
                txtBookFileName= self.dictOfCmds [i] + ".txt"
                self.txtBookFile = os.path.join(self.TxtBookDir,txtBookFileName)
                print("\n\n\n\n****** Reading: ",i, "***")
                self.readTextBook(self.txtBookFile)

            elif self.bookType=='img' :
                print("Selected Book is in image format")
                # Build the path to each Txt Book
                txtBookFileName= self.dictOfCmds [i] + ".png"
                self.txtBookFile = os.path.join(self.TxtBookDir,txtBookFileName)
                print("\n\n\n\n****** Reading: ",i, "***")
                tempTxtFile=self.convertImgBook()
                self.readTextBook(tempTxtFile)

            elif self.bookType=='audio' :
                print("Selected Book is in audio format")
                # Build the path to each Txt Book
                txtBookFileName= self.dictOfCmds [i] + ".mp3"
                self.txtBookFile = os.path.join(self.TxtBookDir,txtBookFileName)
                print("\n\n\n\n****** Reading: ",i, "***")
                self.playAudio(self.txtBookFile)


    # Open the txt file and read line by line
    def readTextBook(self,txtBookFile):
        #print("I am here",self.txtBookFile)
        try:
            file = open(txtBookFile, 'r')
            file.close()
        except:
            print("There was an error opening the text book file!")
            return

        with codecs.open(txtBookFile, "r", encoding='utf-8', errors='ignore') as txtFile:
            txtBookFileLines = txtFile.readlines()
            for line in txtBookFileLines:
                print(line)
                if line not in [""," ",'\r\n','\n']:
                    audioFile = gTTS(text=line, lang=language, slow=False)
                    # Saving the converted audio in a mp3 file
                    audioFile.save("line.mp3")
                    # play the audio file
                    playsound("line.mp3")


    def convertImgBook(self):
        try:
            # open image from the source path
            imgBook = Image.open(self.txtBookFile)
            print("I am processing imge\n",imgBook)
            convertedToTxt = pytesseract.image_to_string(imgBook)
            #save output to a txt file
            timestamp = datetime.now().strftime('%Y-%m-%d_%Hh-%Mm-%Ss')
            filepath = os.getcwd() + '/ScanBook_Convert/'
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            filename='tempTxt'+timestamp+'txt'
            tempTxtFile= os.path.join(filepath,filename)
            with open(tempTxtFile, mode='w') as file:
                file.write(convertedToTxt)
                print("Your SCAN is converted to text. \n", convertedToTxt)
                return tempTxtFile
        except:
            print("There was an error opening the text book file!")
            return -1


    def playAudio(self,txtBookFile):
        try:
            # play the audio file
            playsound(txtBookFile)
            return 1
        except:
            print("There was an issue playing the audio file!\n",txtBookFile)


    @classmethod
    def getBookListJson(cls,BookListName):
        try:
            toRead_list=os.path.join(curDir,listDir,BookListName)
            file = open(toRead_list, 'r')
            file.close()
        except:
            print('Invalid input! Please try again')

        return cls(toRead_list)

class LibraryManagment:

    def __init__(self, toRead_list):
        self.bookInventory = toRead_list


    def checkAvailability(self,txtBookName):
        try:
            with open(self.bookInventory, 'r') as json_inventory:
                self.dictOfCmds = json.loads(json_inventory.read())
            bookInfo = self.dictOfCmds[txtBookName]
            bookStatus = bookInfo['status']
            if bookStatus=='out':
                return [bookInfo['status'],bookInfo['borrower'], bookInfo['date']]
            else:
                return ['available','','']

        except:
            print("There was an issue finding the book information\n",txtBookName)


    def checkOut(self,txtBookName,bName):
        try:
            with open(self.bookInventory, 'r') as json_inventory:
                self.dictOfBooks = json.loads(json_inventory.read())
            bookInfo = self.dictOfBooks[txtBookName]
            bookStatus = bookInfo['status']
            if bookStatus=='out':
                if bName=='':
                    timestamp = datetime.now().strftime('%Y-%m-%d')
                    self.dictOfBooks[txtBookName]['status'] = 'available'
                    self.dictOfBooks[txtBookName]['borrower'] = ''
                    self.dictOfBooks[txtBookName]['date'] = ''
                    # save the updated information
                    with open(self.bookInventory, 'w') as json_inventory:
                        json.dump(self.dictOfBooks, json_inventory)

                    # verify staus changed
                    with open(self.bookInventory, 'r') as json_inventory:
                        self.dictOfBooks = json.loads(json_inventory.read())
                    bookInfo = self.dictOfBooks[txtBookName]
                    print([bookInfo['status'], bookInfo['borrower'], bookInfo['date']])
                    return [bookInfo['status'], bookInfo['borrower'], bookInfo['date']]

                else:
                    print ("This book is already checked out")
                return [bookInfo['status'],bookInfo['borrower'], bookInfo['date']]
            else:
                timestamp = datetime.now().strftime('%Y-%m-%d')
                self.dictOfBooks[txtBookName] ['status']='out'
                self.dictOfBooks[txtBookName]['borrower'] = bName
                self.dictOfBooks[txtBookName]['date'] = timestamp
                # save the updated information
                with open(self.bookInventory, 'w') as json_inventory:
                    json.dump(self.dictOfBooks, json_inventory)

                # verify staus changed
                with open(self.bookInventory, 'r') as json_inventory:
                    self.dictOfBooks = json.loads(json_inventory.read())
                bookInfo = self.dictOfBooks[txtBookName]
                return [bookInfo['status'], bookInfo['borrower'], bookInfo['date']]

        except:
            print("There was an issue finding the book information\n",txtBookName)


    @classmethod
    def getLibraryJson(cls,LibraryName):
        print("\n\n\n\n****** checking: ", LibraryName, " Library ***")
        try:
            LibraryName = LibraryName + ".json"
            toRead_list=os.path.join(curDir,inventoryDir,LibraryName)
            print (toRead_list)
            file = open(toRead_list, 'r')
            file.close()
        except:
            print('Invalid input! Please try again')

        return cls(toRead_list)

if __name__ == '__main__':
    #Remote_Teaching = RemoteTeaching.getBookListJson()
    #Remote_Teaching.readBookList()
    Remote_Library=LibraryManagment.getLibraryJson('kalkbay')
    #print(Remote_Library.checkAvailability("Computer Basics"))
    print(Remote_Library.checkOut("Hygiene Basics","Maryam"))