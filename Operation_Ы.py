import tkinter as ttk
import pyperclip as pp


class UltraZashifr():
    def __init__(self):
        f = open("poslanie.txt", "r")
        self.txt = f.readline()
        f.close()
        self.dict = {"а": 1, "А": -1, "б": 2, "Б": -2, "в": 3, "В": -3,
                     "г": 4, "Г": -4, "д": 5, "Д": -5, "е": 6, "Е": -6,
                     "ё": 7, "Ё": -7, "ж": 8, "Ж": -8, "з": 9, "З": -9,
                     "и": 10, "И": -10, "й": 11, "Й": -11, "к": 12, "К": -12,
                     "л": 13, "Л": -13, "м": 14, "М": -14, "н": 15, "Н": -15,
                     "о": 16, "О": -16, "п": 17, "П": -17, "р": 18, "Р": -18,
                     "с": 19, "С": -19, "т": 20, "Т": -20, "у": 21, "У": -21,
                     "ф": 22, "Ф": -22, "х": 23, "Х": -23, "ц": 24, "Ц": -24,
                     "ч": 25, "Ч": -25, "ш": 26, "Ш": -26, "щ": 27, "Щ": -27,
                     "ъ": 28, "Ъ": -28, "ы": 29, "Ы": -29, "ь": 30, "Ь": -30,
                     "э": 31, "Э": -31, "ю": 32, "Ю": -32, "я": 33, "Я": -33,
                     " ": 34, 1: "а", -1: "А", 2: "б", -2: "Б", 3: "в", -3: "В",
                     4: "г", -4: "Г", 5: "д", -5: "Д", 6: "е", -6: "Е",
                     7: "ё", -7: "Ё", 8: "ж", -8: "Ж", 9: "з", -9: "З",
                     10: "и", -10: "И", 11: "й", -11: "Й", 12: "к", -12: "К",
                     13: "л", -13: "Л", 14: "м", -14: "М", 15: "н", -15: "Н",
                     16: "о", -16: "О", 17: "п", -17: "П", 18: "р", -18: "Р",
                     19: "с", -19: "С", 20: "т", -20: "Т", 21: "у", -21: "У",
                     22: "ф", -22: "Ф", 23: "х", -23: "Х", 24: "ц", -24: "Ц",
                     25: "ч", -25: "Ч", 26: "ш", -26: "Ш", 27: "щ", -27: "Щ",
                     28: "ъ", -28: "Ъ", 29: "ы", -29: "Ы", 30: "ь", -30: "Ь",
                     31: "э", -31: "Э", 32: "ю", -32: "Ю", 33: "я", -33: "Я",

                     34: " ", ",": 35, 35: ",", 36: ".", ".": 36, 37: "!", "!": 37,
                     38: "?", "?": 38, "\n": 39, 39: "\n", ":": 40, 40: ":", "-": 41, 41: "-",
                     "—": 42, 42: "—", 43: "(", "(": 43, 44: ")", ")": 44,

                     "a": 45, "A": -45, "b": 46, "B": -46, "c": 47, "C": -47,
                     "d": 48, "D": -48, "e": 49, "E": -49, "f": 50, "F": -50,
                     "g": 51, "G": -51, "h": 52, "H": -52, "i": 53, "I": -53,
                     "j": 54, "J": -54, "k": 55, "K": -55, "l": 56, "L": -56,
                     "m": 57, "M": -57, "n": 58, "N": -58, "o": 59, "O": -59,
                     "p": 60, "P": -60, "q": 61, "Q": -61, "r": 62, "R": -62,
                     "s": 63, "S": -63, "t": 64, "T": -64, "u": 65, "U": -65,
                     "v": 66, "V": -66, "w": 67, "W": -67, "x": 68, "X": -68,
                     "y": 69, "Y": -69, "z": 70, "Z": -70,
                     45: "a", -45: "A", 46: "b", -46: "B", 47: "c", -47: "C",
                     48: "d", -48: "D", 49: "e", -49: "E", 50: "f", -50: "F",
                     51: "g", -51: "G", 52: "h", -52: "H", 53: "i", -53: "I",
                     54: "j", -54: "J", 55: "k", -55: "K", 56: "l", -56: "L",
                     57: "m", -57: "M", 58: "n", -58: "N", 59: "o", -59: "O",
                     60: "p", -60: "P", 61: "q", -61: "Q", 62: "r", -62: "R",
                     63: "s", -63: "S", 64: "t", -64: "T", 65: "u", -65: "U",
                     66: "v", -66: "V", 67: "w", -67: "W", 68: "x", -68: "X",
                     69: "y", -69: "Y", 70: "z", -70: "Z", "'": 71, 71: "'", '"': -71, -71: '"'}
        self.save_to_file()

    def code(self):
        if len(self.txt) % 4 != 0:
            while len(self.txt) % 4 != 0:
                self.txt += " "
        bukvi = []
        for i in range(0, len(self.txt)):
            bukvi.append(self.txt[i])
        with_dict = []
        for k in bukvi:
            with_dict.append(self.dict[k])
        matr = []
        for i in range(0, len(with_dict), 2):
            matr.append(with_dict[i:i+4])
        matr_shifr = [10, 9, 11, 10]
        vivod = []
        del matr[1::2]
        for i in range(0, len(matr)):
            zashifr = [(matr[i][0] * int(matr_shifr[0])) + (matr[i][1] * matr_shifr[2]), (matr[i][0] * matr_shifr[1]) + (matr[i][1] * matr_shifr[3]),
                       (matr[i][2] * matr_shifr[0]) + (matr[i][3] * matr_shifr[2]), (matr[i][2] * matr_shifr[1]) + (matr[i][3] * matr_shifr[3])]
            vivod.append(zashifr)
        zashifr = []
        for i in vivod:
            zashifr += i
        return zashifr

    def save_to_file(self):
        f = open("zashifr.txt", "w")
        for i in self.code():
            f.write(str(i) + " ")
        f.close()


class UltraDeshifr():
    def __init__(self):
        self.txt = ""
        self.dict = {"а": 1, "А": -1, "б": 2, "Б": -2, "в": 3, "В": -3,
                     "г": 4, "Г": -4, "д": 5, "Д": -5, "е": 6, "Е": -6,
                     "ё": 7, "Ё": -7, "ж": 8, "Ж": -8, "з": 9, "З": -9,
                     "и": 10, "И": -10, "й": 11, "Й": -11, "к": 12, "К": -12,
                     "л": 13, "Л": -13, "м": 14, "М": -14, "н": 15, "Н": -15,
                     "о": 16, "О": -16, "п": 17, "П": -17, "р": 18, "Р": -18,
                     "с": 19, "С": -19, "т": 20, "Т": -20, "у": 21, "У": -21,
                     "ф": 22, "Ф": -22, "х": 23, "Х": -23, "ц": 24, "Ц": -24,
                     "ч": 25, "Ч": -25, "ш": 26, "Ш": -26, "щ": 27, "Щ": -27,
                     "ъ": 28, "Ъ": -28, "ы": 29, "Ы": -29, "ь": 30, "Ь": -30,
                     "э": 31, "Э": -31, "ю": 32, "Ю": -32, "я": 33, "Я": -33,
                     " ": 34, 1: "а", -1: "А", 2: "б", -2: "Б", 3: "в", -3: "В",
                     4: "г", -4: "Г", 5: "д", -5: "Д", 6: "е", -6: "Е",
                     7: "ё", -7: "Ё", 8: "ж", -8: "Ж", 9: "з", -9: "З",
                     10: "и", -10: "И", 11: "й", -11: "Й", 12: "к", -12: "К",
                     13: "л", -13: "Л", 14: "м", -14: "М", 15: "н", -15: "Н",
                     16: "о", -16: "О", 17: "п", -17: "П", 18: "р", -18: "Р",
                     19: "с", -19: "С", 20: "т", -20: "Т", 21: "у", -21: "У",
                     22: "ф", -22: "Ф", 23: "х", -23: "Х", 24: "ц", -24: "Ц",
                     25: "ч", -25: "Ч", 26: "ш", -26: "Ш", 27: "щ", -27: "Щ",
                     28: "ъ", -28: "Ъ", 29: "ы", -29: "Ы", 30: "ь", -30: "Ь",
                     31: "э", -31: "Э", 32: "ю", -32: "Ю", 33: "я", -33: "Я",

                     34: " ", ",": 35, 35: ",", 36: ".", ".": 36, 37: "!", "!": 37,
                     38: "?", "?": 38, "\n": 39, 39: "\n", ":": 40, 40: ":", "-": 41, 41: "-",
                     "—": 42, 42: "—", 43: "(", "(": 43, 44: ")", ")": 44,

                     "a": 45, "A": -45, "b": 46, "B": -46, "c": 47, "C": -47,
                     "d": 48, "D": -48, "e": 49, "E": -49, "f": 50, "F": -50,
                     "g": 51, "G": -51, "h": 52, "H": -52, "i": 53, "I": -53,
                     "j": 54, "J": -54, "k": 55, "K": -55, "m": 56, "M": -56,
                     "n": 57, "N": -57, "l": 58, "L": -58, "o": 59, "O": -59,
                     "p": 60, "P": -60, "q": 61, "Q": -61, "r": 62, "R": -62,
                     "s": 63, "S": -63, "t": 64, "T": -64, "u": 65, "U": -65,
                     "v": 66, "V": -66, "w": 67, "W": -67, "x": 68, "X": -68,
                     "y": 69, "Y": -69, "z": 70, "Z": -70,
                     45: "a", -45: "A", 46: "b", -46: "B", 47: "c", -47: "C",
                     48: "d", -48: "D", 49: "e", -49: "E", 50: "f", -50: "F",
                     51: "g", -51: "G", 52: "h", -52: "H", 53: "i", -53: "I",
                     54: "j", -54: "J", 55: "k", -55: "K", 56: "l", -56: "L",
                     57: "m", -57: "M", 58: "n", -58: "N", 59: "o", -59: "O",
                     60: "p", -60: "P", 61: "q", -61: "Q", 62: "r", -62: "R",
                     63: "s", -63: "S", 64: "t", -64: "T", 65: "u", -65: "U",
                     66: "v", -66: "V", 67: "w", -67: "W", 68: "x", -68: "X",
                     69: "y", -69: "Y", 70: "z", -70: "Z", "'": 71, 71: "'", '"': -71, -71: '"'}
        self.save_to_file()

    def load_from_file(self):
        f = open("zashifr.txt", "r")
        data = list(map(int, f.readline()[0:-1].split(" ")))
        f.close()
        return data

    def save_to_file(self):
        f = open("poslanie.txt", "w")
        for i in self.decode():
            f.write(i)
        f.close()

    def decode(self):
        decoded = []
        matr = []
        k_bukvam = []
        self.vivod = []
        matr_deshifr = [10, -9, -11, 10]
        for i in range(0, len(self.load_from_file()), 2):
            matr.append(self.load_from_file()[i:i+4])
        del matr[1::2]
        for i in range(0, len(matr)):
            deshifr = [(matr[i][0] * int(matr_deshifr[0])) + (matr[i][1] * matr_deshifr[2]), (matr[i][0] * matr_deshifr[1]) + (matr[i][1] * matr_deshifr[3]),
                       (matr[i][2] * matr_deshifr[0]) + (matr[i][3] * matr_deshifr[2]), (matr[i][2] * matr_deshifr[1]) + (matr[i][3] * matr_deshifr[3])]
            decoded.append(deshifr)
        for i in range(0, len(decoded)):
            for g in range(0, 4):
                k_bukvam.append(decoded[i][g])
        for i in k_bukvam:
            self.vivod.append(self.dict[i])
        return self.vivod


class UltraCode(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self)
        self.txtxt = ""
        try:
            f = open("poslanie.txt", "r")
        except:
            f = open("poslanie.txt", "w")
            f.write("Привет")
            c = open("poslanie.txt", "r")
            self.txtxt = c.readline()
            c.close()
            f.close()
        try:
            f = open("zashifr.txt", "r")
        except:
            f = open("zashifr.txt", "w")
            f.write("-35 -31 191 172 239 217 233 210 331 299 799 723 ")
            f.close()
        self.pack()
        self.master.title("Матричный Шифратор 3000")
        self.create_widgets()
        self.refresh()

    def paste(self):
        var = pp.paste()
        self.Text_for_zashifr.insert(1.0, var)

    def refresh(self):
        self.Label_for_zashifr.destroy()
        self.Label_for_zashifr = ttk.Label(self, text=UltraDeshifr().decode(), font="allegrian 20", width="50", bg="rosy brown")
        self.Label_for_zashifr.pack()
        self.Label_for_zashifr.after(2000, self.refresh)

    def create_widgets(self):
        self.Baton_for_paste = ttk.Button(text="Нажми, чтобы скопировать в поле ввода текст из буфера обмена", command=lambda: self.paste(), font="arial 20", width="50", bg="burlywood1")
        self.Label_for_zashifr = ttk.Label(self, font="allegrian 20", text=self.txtxt, width="50", bg="rosy brown")
        self.Baton_for_zashifr = ttk.Button(text="Нажми, чтобы зашифровать", command=lambda: self.zashifr(), font="arial 20", width="50", bg="wheat1")
        self.Text_for_zashifr = ttk.Text(self, font="arial 20", bg="cornsilk2", width="50", height="10")
        self.Baton_for_deshifr = ttk.Button(text="Нажми, чтобы дешифровать", command=lambda: self.deshifr(), font="arial 20", width="50", bg="gold1")
        self.Text_for_zashifr.pack()
        self.Label_for_zashifr.pack()
        self.Baton_for_deshifr.pack()
        self.Baton_for_zashifr.pack()
        self.Baton_for_paste.pack()

    def zashifr(self):
        f = open("poslanie.txt", "w")
        f.write(self.Text_for_zashifr.get("1.0", ttk.END))
        f.close()
        UltraZashifr()

    def deshifr(self):
        return UltraDeshifr().decode()


UltraCode().mainloop()
