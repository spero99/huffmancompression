import heapq
import os


class heap_node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, heap_node):
            return False
        return self.freq == other.freq


class Compressing:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.code = {}
        self.remapping = {}

    # compression
    def freq_dict(self, file):
        frequency = {}
        for char in file:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def create_heap(self, frequency):
        for i in frequency:
            node = heap_node(i, frequency[i])
            heapq.heappush(self.heap, node)

    # taking 2 nodes ,sum it up,create  parent node an then add the 2 nodes as children
    def merge(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merging = heap_node(None, node1.frequency + node2.frequency)
            merging.left = node1
            merging.right = node2
            heapq.heappush(self.heap, merging)

    def code_function1(self, root, current_code):
        if root is None:
            return
        if root.character is not None:
            self.code[root.character] = current_code
            self.remapping[current_code] = root.character
            return
        self.code_function1(root.left, current_code + "0")
        self.code_function1(root.right, current_code + "1")

    def create_code(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.code_function1(root, current_code)

    def encode(self, file):
        encoded_file = ""
        for character in file:
            encoded_file += self.code[character]
        return encoded_file

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def byte_array(self, padded_encoded_file):
        if len(padded_encoded_file) % 8 !=0:
            print("paddin not done properly")
            exit(0)

        b= bytearray()
        for i in range(0, len(padded_encoded_file), 8):
            byte = padded_encoded_file[i:i+8]
            b.append(int(byte, 2))
        return b

    # compression of the file using the new codes for the characters
    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_file = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_file, 'wb') as output:
            file = file.read()
            file = file.rstrip()
            frequency = self.freq_dict(file)
            self.create_heap(frequency)
            self.merge()
            self.create_code()
            encoded_text = self.encode(file)
            padded_encoded_file = self.pad_encoded_text(encoded_text)
            b = self.byte_array(padded_encoded_file)
            output.write(bytes(b))
        print("Compression with huffman algoritmh complete")
        return output_file

    def unpad_encoded_text(selfself, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.remapping:
                char = self.remapping[current_code]
                decoded_text += char
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            string = ""
            byte = file.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                string += bits
                byte = file.read(1)

            encoded_text = self.unpad_encoded_text(string)
            decompressed_text = self.decode(encoded_text)
            output.write(decompressed_text)

        print("decompression complete")
        return output_path

