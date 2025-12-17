def emoji_coverter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😔"
    }
    output = ""
    for word in words:
        emojis.get(word, word)
        output += emojis.get(word, word) + " "
        return output


message = input('> ')
print(emoji_coverter(message))