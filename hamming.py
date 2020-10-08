import filecmp

path = 'uncompressedFile'
encrypted_file = "2encrypted1.bin"
decrypted_file = "4decrypted1.bin"


def parity_bits(bits):
    i = 0
    while 2 ** i <= bits + i:
        i += 1
    return i


def parity_bits_incode(bits):
    i = 0
    while 2 ** i <= bits:
        i += 1
    return i


def append_parity_bits(data):
    n = parity_bits(len(data))
    i = 0
    j = 0
    k = 0
    list1 = list()
    while i < n + len(data):
        if i == (2 ** j - 1):
            list1.insert(i, 0)
            j += 1
        else:

            list1.insert(i, data[k])
            k += 1
        i += 1
    return list1


def hamming_encode(path):
    with open(path, 'rb') as file:
        data = file.read()

    data = list(data)
    n = parity_bits(len(data))
    list1 = append_parity_bits(data)
    i = 0
    k = 1
    while i < n:
        k = 2 ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 < len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 < len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j * k) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)

            j += 2

        if total % 2 > 0:
            list1[int(k) - 1] = 1
        i += 1

    with open(encrypted_file, 'w') as output:
        for bit in list1:
            try:
                x = list1[bit]
                output.write(str(x))
            except IndexError:
                print('list index out of range')
    return list1


def hamming_correct(path):
    with open(path, 'rb') as file:
        file = file.read()
    data = list(file)
    n = parity_bits_incode(len(data))
    i = 0
    list1 = list(data)

    errorbit = 0
    while i < n:
        k = 2 ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = (j * k) - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j * 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)

            j += 2
        if total % 2 > 0:
            errorbit += k
        i += 1

    if errorbit >= 1:
        print("error in", errorbit, "bit ")
        print(list1[int(errorbit)])
        if list1[int(errorbit - 1)] == '0' or list1[int(errorbit - 1)] == 0:
            list1[int(errorbit - 1)] = 1
        else:
            list1[int(errorbit - 1)] = 0
    else:
        print("no error")

    list2 = list()
    i = 0
    j = 0
    k = 0
    while i < len(list1):
        if i != ((2 ** k) - 1):
            temp = list1[int(i)]
            list2.append(temp)
            j += 1
        else:
            k += 1
        i += 1

    list3 =list()
    with open(decrypted_file, 'wb') as output:
        for i in list2:
            output.write(bytes(list2[i]))




#hamming_encode(path)
#hamming_correct('2encrypted1.bin')
#print(filecmp.cmp(path, decrypted_file))

