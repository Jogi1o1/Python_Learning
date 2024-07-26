#Encryption file
#from alphabets import alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word,shift):
    word_list = list(word)
    indexes = []
    encoded_word = ""
    for i in word_list:
        indexes.append((alphabet.index(i)+shift)%26)
    print(shift)
    print(indexes)
    for i in indexes:
            encoded_word += alphabet[i]
    print(f"Here's the encoded result : {encoded_word}")

print(100%26)
encrypt("hello",100)

