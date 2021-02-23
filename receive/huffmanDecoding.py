from Node import Node
from array import array


class Decoding:

    def __init__(self, key_path, file_path):
        self.key_path = key_path
        self.file_path = file_path
        self.inv_code_dict = {}

    def read_code_dict(self):
        s = open(self.key_path, 'rb').read()
        code_dict = eval(s)
        self.inv_code_dict = {v: k for k, v in code_dict.items()}
        
    def read_byte_file(self):
        imput_file = open(self.file_path, 'rb')
        hex_text = imput_file.read()
        text = ""
        for i in range(len(hex_text)):
           text += (bin(hex_text[i]))[2:].rjust(8, '0')
           
       
        return text

    def decompress(self):
        text = self.read_byte_file()
        self.read_code_dict()
        #print(self.inv_code_dict)
        #print(text)
        output_text = ""
        char = ""
        for i in range(len(text)):
            char += text[i]
            #print(char)
            if char in self.inv_code_dict:
                output_text += self.inv_code_dict[char]
                char = ""
        #print(output_text)
        output_path = './received.txt'
        output_file = open(output_path, 'w')
        output_file.write(output_text)
        output_file.close()
        

       


################################################################

