class Text():
    def write(self):
        with open('file', 'a') as a:
            a.write(Text)
    def set_font(self):


    def show(self):

    def restore(self, SavedText.get_version(number)):


class SavedText():
    def save_text(self, Text):



    def get_version(self, number):
        return number+1

if __name__ == "__main__":
    text = Text()
    saver = SavedText()
    text.write("At the beginning")
    saver.save_text(text)
