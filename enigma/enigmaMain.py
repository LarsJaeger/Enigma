# allgemeines
import datetime
import pickle
global alphabet
alphabet = []
reverseLookup_alphabet = []
for i in range(32, 126, 1):
    alphabet.append(i)
for i in range(161, 328, 1):
    if i != 173:
        alphabet.append(i)


def loadPlugboard(day, month):
    with open("plugboards/" + str(month) + '/' + str(day) + '.pkl', "rb") as f:
        return pickle.load(f)


def encode_decode_char(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3, b):
    out = chr(alphabet[reverseLookup_plugboard[reverseLookup_roll1[(reverseLookup_roll2[(reverseLookup_roll3[(reverseRoll[roll3[(roll2[(roll1[(plugboard[reverseLookup_alphabet[b]] + wp1) % len(roll1)] + wp1) % len(roll2)] + wp1) % len(roll3)]] - wp3) % len(roll3)] - wp2) % len(roll2)] - wp1) % len(roll1)]]])
    return out


def encode_decode_text(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3, text):
    out = ""
    for char in text:
        if alphabet.count(char) != 0:
            out += encode_decode_char(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3, char)
            if wp1 == len(roll1) - 1:
                wp1 = 0
                if wp2 == len(roll2) - 1:
                    wp2 = 0
                    if wp3 == len(roll3) - 1:
                        wp3 = 0
                    else:
                        wp3 += 1
                else:
                    wp2 += 1
            else:
                wp1 += 1
    return out


def encode_decode_file(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3):
    dateiIn = open("enigmaInput.txt", "r", encoding='utf-8')
    dateiOut = open("enigmaOutput.txt", "w", encoding='utf-8')
    for line in dateiIn:
            dateiOut.write(encode_decode_text(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3, line.rstrip()))
    dateiIn.close()
    dateiOut.close()


def generateReverseLookupTables():
    for i in range(len(roll1)):
        reverseLookup_roll1.append(roll1.index(i))
    for i in range(len(roll2)):
        reverseLookup_roll2.append(roll2.index(i))
    for i in range(len(roll3)):
        reverseLookup_roll2.append(roll3.index(i))
    for i in range(len(plugboard)):
        reverseLookup_plugboard.append(plugboard.index(i))
    for i in range(len(alphabet)):
        reverseLookup_alphabet.append(alphabet.index(i))

# einstellung
plugboard = []
reverseLookup_plugboard = []
roll1 = [152, 252, 2, 58, 173, 38, 82, 1, 128, 181, 157, 85, 75, 68, 39, 137, 47, 20, 257, 125, 120, 150, 146, 8, 197, 218, 170, 81, 153, 101, 224, 217, 221, 42, 35, 49, 174, 206, 235, 245, 177, 98, 187, 61, 10, 95, 138, 176, 208, 67, 195, 219, 11, 46, 244, 254, 33, 93, 63, 123, 3, 209, 97, 109, 230, 216, 188, 135, 115, 23, 160, 140, 238, 74, 84, 105, 233, 57, 129, 205, 193, 92, 26, 253, 249, 169, 89, 28, 41, 242, 211, 83, 154, 121, 259, 232, 40, 162, 94, 52, 130, 201, 27, 179, 199, 136, 72, 21, 111, 220, 234, 183, 56, 43, 78, 241, 9, 126, 139, 80, 12, 184, 185, 71, 62, 24, 194, 53, 99, 163, 116, 48, 127, 141, 222, 159, 103, 112, 247, 70, 59, 106, 4, 142, 25, 5, 243, 133, 6, 134, 55, 214, 180, 203, 66, 77, 37, 207, 148, 118, 165, 104, 144, 100, 73, 215, 196, 132, 237, 88, 13, 0, 213, 90, 102, 45, 190, 96, 161, 210, 155, 251, 64, 149, 255, 202, 110, 69, 166, 7, 200, 158, 189, 164, 34, 175, 236, 114, 172, 31, 186, 19, 122, 86, 226, 192, 51, 14, 231, 258, 60, 171, 113, 15, 16, 32, 36, 227, 22, 250, 87, 119, 117, 108, 30, 191, 76, 145, 198, 143, 17, 124, 18, 131, 178, 223, 50, 256, 182, 79, 229, 212, 239, 156, 168, 107, 228, 91, 225, 240, 44, 29, 65, 147, 151, 246, 167, 248, 54, 204]
roll2 = [14, 121, 203, 190, 248, 240, 169, 86, 99, 231, 135, 186, 35, 138, 229, 199, 53, 122, 244, 177, 187, 172, 44, 47, 140, 152, 51, 49, 82, 226, 232, 155, 180, 79, 15, 219, 201, 25, 59, 197, 224, 143, 245, 133, 4, 88, 213, 147, 75, 249, 84, 102, 256, 39, 54, 12, 5, 72, 181, 243, 145, 234, 124, 116, 48, 183, 141, 117, 66, 30, 218, 206, 179, 171, 9, 158, 131, 0, 212, 71, 235, 228, 107, 96, 64, 112, 90, 2, 26, 207, 74, 194, 6, 185, 109, 3, 27, 178, 100, 157, 110, 237, 258, 136, 104, 105, 77, 98, 154, 150, 192, 214, 175, 227, 97, 43, 41, 132, 126, 42, 144, 161, 156, 139, 94, 62, 19, 255, 55, 29, 108, 200, 209, 151, 111, 18, 148, 40, 170, 101, 142, 123, 196, 210, 233, 115, 28, 78, 164, 45, 220, 114, 216, 46, 189, 32, 254, 58, 81, 11, 13, 50, 8, 80, 215, 223, 166, 198, 217, 253, 246, 236, 174, 118, 119, 221, 257, 173, 162, 22, 168, 61, 211, 193, 95, 103, 23, 83, 36, 241, 129, 93, 21, 130, 57, 24, 52, 250, 184, 1, 159, 149, 65, 17, 191, 85, 67, 73, 16, 10, 239, 60, 92, 167, 76, 106, 31, 204, 91, 146, 238, 128, 69, 127, 33, 222, 160, 259, 120, 153, 251, 137, 34, 38, 134, 202, 70, 56, 163, 125, 176, 208, 37, 188, 225, 7, 87, 252, 63, 195, 247, 113, 89, 205, 242, 68, 230, 165, 182, 20]
roll3 = [113, 12, 230, 195, 43, 254, 209, 78, 6, 114, 155, 149, 103, 141, 95, 18, 192, 160, 106, 91, 87, 150, 40, 188, 200, 258, 211, 17, 239, 58, 109, 190, 186, 5, 77, 169, 247, 44, 64, 220, 14, 119, 235, 144, 154, 259, 22, 104, 153, 171, 218, 250, 172, 13, 136, 31, 123, 10, 107, 183, 108, 246, 231, 70, 74, 232, 1, 19, 83, 84, 196, 45, 234, 3, 198, 137, 251, 161, 163, 177, 191, 210, 249, 248, 99, 80, 139, 8, 36, 181, 140, 89, 217, 15, 127, 48, 57, 197, 86, 105, 85, 225, 174, 167, 21, 151, 2, 165, 116, 124, 24, 46, 245, 60, 187, 33, 158, 49, 216, 213, 23, 241, 255, 134, 39, 88, 212, 236, 32, 52, 75, 176, 125, 156, 97, 26, 145, 110, 101, 184, 131, 118, 142, 199, 115, 244, 129, 20, 233, 16, 203, 252, 59, 215, 130, 256, 9, 61, 53, 202, 201, 221, 222, 208, 162, 4, 166, 71, 135, 214, 67, 121, 229, 27, 193, 207, 189, 66, 72, 146, 92, 170, 180, 257, 128, 223, 37, 168, 30, 224, 63, 100, 240, 126, 28, 38, 50, 96, 102, 25, 205, 226, 228, 111, 82, 237, 7, 73, 204, 164, 54, 185, 65, 76, 0, 179, 29, 42, 79, 62, 51, 138, 148, 219, 93, 175, 182, 94, 133, 147, 11, 159, 41, 206, 242, 122, 35, 238, 81, 47, 178, 68, 112, 120, 117, 227, 132, 69, 194, 243, 56, 98, 55, 157, 143, 90, 34, 253, 152, 173]
reverseLookup_roll1=[]
reverseLookup_roll2=[]
reverseLookup_roll3=[]
reverseRoll = [5, 157, 30, 258, 12, 0, 194, 215, 146, 112, 98, 133, 4, 137, 251, 199, 185, 53, 19, 18, 214, 160, 127, 223, 54, 93, 77, 28, 27, 190, 2, 159, 149, 246, 101, 41, 64, 188, 79, 224, 141, 35, 169, 92, 147, 248, 83, 238, 142, 177, 210, 100, 222, 17, 24, 175, 154, 219, 61, 95, 62, 58, 60, 220, 36, 242, 207, 250, 115, 125, 103, 153, 236, 217, 257, 135, 232, 26, 208, 38, 119, 241, 164, 46, 132, 111, 253, 247, 117, 206, 129, 176, 43, 25, 163, 59, 243, 168, 10, 182, 51, 34, 226, 70, 121, 108, 172, 144, 105, 209, 150, 85, 9, 170, 205, 68, 148, 88, 202, 80, 227, 104, 228, 231, 151, 69, 155, 22, 200, 90, 201, 218, 84, 11, 237, 75, 186, 13, 183, 233, 245, 40, 48, 158, 107, 171, 8, 44, 116, 32, 110, 124, 179, 71, 56, 126, 195, 1, 143, 31, 21, 161, 191, 94, 82, 189, 180, 187, 97, 42, 113, 145, 106, 211, 181, 55, 91, 49, 254, 152, 166, 174, 99, 138, 212, 16, 136, 167, 37, 165, 29, 162, 234, 204, 6, 156, 244, 213, 249, 15, 128, 130, 118, 240, 193, 114, 89, 66, 78, 109, 50, 173, 184, 197, 20, 7, 221, 73, 131, 57, 63, 216, 52, 23, 39, 255, 102, 120, 122, 252, 256, 123, 76, 139, 192, 239, 72, 134, 47, 235, 203, 81, 65, 96, 196, 140, 33, 87, 45, 198, 67, 14, 229, 86, 178, 225, 230, 74, 3]
wp1 = int(input("position of roll 1: "))
wp2 = int(input("position of roll 2: "))
wp3 = int(input("position of roll 3: "))
global datumVerwenden
datumVerwenden = input("use current date to choose plugboard? (y / n)")
global day
global month
if datumVerwenden == "n" or datumVerwenden == "N":
    plugboard = loadPlugboard(input("Day: "), input("Month: "))
else:
    plugboard = (datetime.date.today().day, datetime.date.today().month)
# ausführung
generateReverseLookupTables()
dateiOderText = input("en- / decrypt text or file? (t / f)")
if dateiOderText == "t" or dateiOderText == "T":
    print(encode_decode_text(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3, input("insert text: ")))
else:
    encode_decode_file(roll1, roll2, roll3, reverseRoll, wp1, wp2, wp3)
a = input("Beenden")