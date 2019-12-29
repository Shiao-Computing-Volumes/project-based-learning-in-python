from googletrans import Translator
from gtts import gTTS


if __name__ == '__main__':
    # read the file
    text = open("./words.txt", 'r')
    words = [] 
    translated = []
 
    # parsing a word list
    for word in text:
        words.append(word.strip())

    # translating from English to Hindi
    translator = Translator()
    for word in words:
        word = translator.translate(word, dest='hi')
        translated.append(word.text)
        tts = gTTS(word.text)
        tts.save(str(word) + ".mp3")
    print(translated)
