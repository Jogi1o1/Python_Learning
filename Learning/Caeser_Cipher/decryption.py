#Decryption file

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(word,shift):
    word_list = list(word)
    indexes = []
    decoded_word = ""
    for i in word_list:
        indexes.append((alphabet.index(i)-shift)%26)
    print(shift)
    print(indexes)
    for i in indexes:
        decoded_word += alphabet[i]
    print(f"Here's the decoded result : {decoded_word}")

decrypt("hello",100)
