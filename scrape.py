
"""
MUST USE PYTHON 3!!!!!!!!!!!!!!!!!!!!!!!!!!!
IF YOU WANT TO DOWNLOAD FROM URL!!!!!!!!!!!

Run this script on the command line and enter 
a argument that represents a .html file
of a vocabulary.com list that you want to scrape.
An example could be, the html file found at 
https://www.vocabulary.com/lists/1259884

If no argument is found it will automatically
scrape the cet4.html file.
"""

import sys
req_version = (3, 4)
cur_version = sys.version_info

if cur_version >= req_version:
    print(cur_version)
    import urllib.request
    print("Python 3!\n\n" * 3)
    python3 = True
else:
    print("Your Python Interpreter is too old. Python 3 is required")
    python3 = False

class MakeVocabClass(object):

    def __init__(self, filename=None):
        """
        If a filename parameter is passed
        then that will be used for the filename
        string that will be opened.
        If not then they will check
        if a sys.argv was provided
        if so then index 1 of args will 
        be used as filename.
        if not then the default
        "cet4.html" will be used.
        """
        argv_num = len(sys.argv)

        if __name__ == "__main__":
            if filename:
                self.filename = filename
            elif argv_num >= 2:
                self.filename = sys.argv[1]
            else:
                self.filename = "cet4.html"  
        else:
            if filename:
                self.filename = filename
            else:
                self.filename = "cet4.html"




    def get_file_text(self):
        """
        Returns string 
        of html textfile.
        Takes an optional parameter 
        of an .html filename    
        """

        filename = self.filename


        
        if filename[-4:] == "html":
            print("Opening text file\n\n" * 2)
            file = open(filename, "r")
            text = file.read()
            file.close()
        else:
            print("searching url\n\n" * 2)
            if python3:
                url = filename
                response = urllib.request.urlopen(url)
                print("page loaded" * 2)
                text = response.read()    
                
                #convert text from byes to utf-8 string
                text = text.decode('utf-8')
            else:
                raise Exception("Your Python Interpreter is too old. Python 3 is required")
            
            
        return text


    def make_vocab_dict(self, text):
        """
        Takes as input a string
        representing the html contents
        of a vocabulary.com
        vocab list.
        Returns as output a dict of all the 
        words and definitions. 
        """
        word_index = 0


        index = text.find('entry' + str(word_index))


        my_dict = {}



        while index != -1:    
            start_word_index = text.find('word', index) + 6
            end_word_index = text.find('"', start_word_index + 2)
            word = text[start_word_index: end_word_index]

            start_def_index = text.find('definition">', end_word_index + 1) 
            start_def_index = text.find('">', start_def_index) + 2
            end_def_index = text.find('</div>', start_def_index) 
            definition = text[start_def_index:end_def_index]

            my_dict[word] = definition

            word_index += 1
            index = text.find('entry' + str(word_index), index)



        return my_dict

    def get_dict(self):


        return self.make_vocab_dict(self.get_file_text())

a = MakeVocabClass()
my_dict = a.get_dict()
print(my_dict)


found_word_dict = {}

text2 = "I want to defend every person until the age of twenty four if it isn't too demanding."

for word in my_dict:
    if word in text2:
        found_word_dict[word] = my_dict[word]