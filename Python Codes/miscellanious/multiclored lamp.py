class Lamp:
    count = -1
    fires = ['Green', 'Red','Blue','Yellow']
    def light(self):
        self.count = self.count + 1
        if self.count < len(self.fires):
            return self.fires[self.count]
        else:
            self.count  = self.count%4
            return self.fires[self.count]
        '''
        self.count = self.count+1
        return (self.fires[self.count%4])
        '''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")