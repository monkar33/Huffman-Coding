from Node import Node
import heapq
from array import array
import json


class Coding:
    def __init__(self, file_path):
        self.path = file_path
        self.heap = []
        self.frequency_dic = {}
        self.code_dic = {}
    
    def fill_frequency_dic(self, text):
        for char in text:
            if char in self.frequency_dic:
                self.frequency_dic[char] += 1
            else:
                self.frequency_dic[char] = 1

    def push_nodes_on_heap(self):
        for key in self.frequency_dic:
            node = Node(key, self.frequency_dic[key])
            heapq.heappush(self.heap, node)

    def connect_nodes(self):
        while(len(self.heap) > 1):
            first_node = heapq.heappop(self.heap)
            second_node = heapq.heappop(self.heap)
            freq = first_node.char_freq + second_node.char_freq
            new_node = Node(None, freq)
            new_node.left_child = first_node
            new_node.right_child = second_node
            heapq.heappush(self.heap, new_node)

    def find_char_code(self, code, top):
        if(top == None):
            return
        if(top.char != None):
            self.code_dic[top.char] = code
        self.find_char_code((code + "0"),top.left_child)
        self.find_char_code((code + "1"),top.right_child)

        
    
    def fill_code_dic(self):
        top = heapq.heappop(self.heap)  
        code = ""
        self.find_char_code(code,top)
        

    def code_text(self, text):
        coded_text = ""
        
        for char in text:
            coded_text += self.code_dic[char]
            
        return coded_text
    
    def to_byte(self, text):
        fill = 8 - (len(text) % 8)
        filled_text = text
        for i in range(fill):
            filled_text += "0"
        Bytes = bytearray()
        for i in range(0, len(filled_text), 8):
            byte = text[i:i+8]
            Bytes.append(int(byte,2))
        return Bytes

    def compress_file(self):
        output_path = 'toSend.bin'
        key_path = 'key.txt'
        imput_file = open(self.path, 'r')
        output_key_file = open(key_path, 'w')
        output_file = open(output_path, 'wb')
        text = imput_file.read()
        self.fill_frequency_dic(text)
        
        self.push_nodes_on_heap()
        self.connect_nodes()
        self.fill_code_dic()
        output_text = self.code_text(text)

        output_byte_text = self.to_byte(output_text)
    
        
        output_key_file.write(json.dumps(self.code_dic))
        output_key_file.close()
        output_file.write(output_byte_text) #bytes(output_byte_text)
        output_file.close()
        imput_file.close()

    
        


##########################################################

 #path = 'path/to/.txt'
#  newHeap  = Coding(path)
#  newHeap.compress_file()
#  Last_node = heapq.heappop(newHeap.heap)
#  print(Last_node.char_freq)
#print(Last_node.left_child.char_freq)
#print(Last_node.right_child.char_freq)
#print(newHeap.frequency_dic)

#file = open(path, 'r')
#text = file.read()
#print(len(text))
#print(newHeap.code_dic)