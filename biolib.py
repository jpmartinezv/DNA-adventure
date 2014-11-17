from Tkinter import *
import re

class BioLib():

    def __init__(self, list, parameters):
        self.list = []
        self.dist = parameters[0]
        self.radio = parameters[1]
        self.conservacion = parameters[2]
        self.len_seq = 0
    
        for item in list:
            self.list.append(item)

        self.fill()

    def fill(self):
        max_size = 0
        for item in self.list:
            max_size = max(max_size, len(item))

        self.len_seq = max_size

        i = 0
        for i in range(len(self.list)):
            tmp = '-' * abs(max_size - len(self.list[i]))
            self.list[i] = tmp + self.list[i]

    def f(self, x):
        return {
                'A': "A",  
                'G': "G",   
                'C': "C",   
                'T': "T",   
                'U': "U",   
                'R': "[A|G]",   
                'Y': "[C|T]",
                'N': "[A|G|C|T|U]",
                'W': "A|T",
                'S': "G|C",
                'M': "A|C",
                'K': "G|T",
                'B': "G|C|T",
                'H': "A|C|T",
                'D': "A|G|T",
                'V': "A|G|C"
        }[x]

    def mapMotif(self, motif):
        ret = ""
        for x in motif:
            ret += self.f(x)

        return ret

    def matchMotif(self, motif = ""):
        print motif
        motif = r"" + self.mapMotif(motif)
        self.matches = []
        
        for seq in self.list:
            it = re.finditer(motif, seq)
            tmp = []
            for match in it:
                tmp.append( ( match.start() , match.end() ) )
            self.matches.append(tmp)

    def showMatches(self):
        root = Tk()
        text = Text(root)
        line = 1
        for i in range(len(self.list)):
            text.insert(INSERT, "Secuencia " + str(i+1) + ":\n")
            line = line + 1
            text.insert(INSERT, self.list[i] + "\n\n")

            for item in self.matches[i]:
                text.tag_add("yellow", str(line) + "." + str(item[0]), str(line) + "." + str(item[1]))
            line = line + 2

        text.tag_config("yellow", background="yellow", foreground="black")
        text.pack(expand = YES, fill = BOTH)

        root.mainloop()
