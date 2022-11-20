from string import ascii_uppercase #из модуля взяли переменную (список английских букв)
class Alphabet():
    def __init__(self, lang, letters): #self - сам объект остальное - его свойства
        self.lang  = lang #присвоить динамическое свойство, определяющее, какой это язык (строка)
        self.letters = letters #список букв
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters) #обращаемся к свойству в объекте, применяем к нему len и возвращаем

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__("Eng",list(ascii_uppercase)) #вызвали родительский метод (обозначение языка и строка из букв алфавита)
        __letters_num = 26 #передали готовое значение, тк это приватное статическое свойство
    def is_en_letter(self, let): #let - введенная буква
        if let.upper() in self.letters: #перевели букву в верхний регистр
            return True
        else:
            return False
    def get_letter_num(self):
        return EngAlphabet.__letters_num
    @staticmethod
    def get_text():
        return "Any text in English"

le = EngAlphabet()
print(le.lang) #обращаемся к свойству
print(le.letters) ##обращаемся к свойству
print(le.get_letter_num()) #обращаемся к методу
print(le.is_en_letter())
print(EngAlphabet.get_text) #обращаемся к статическиму методу