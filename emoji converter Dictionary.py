message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😃",
    ":(" : "😔"
}
output = ""
for word in words:
    emojis.get(word, word)
    output += emojis.get(word, word) + " "
print(output)