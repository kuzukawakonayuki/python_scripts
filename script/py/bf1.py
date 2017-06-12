# -*- coding: utf-8 -*-

from sys import stdout,stdin,argv
import re

cells = [0 for x in xrange(0,30000)] # 30,000 Cells

dict = {"久城！": "+",
        "はぁ～また退屈になってしまった。どうせならもう少し歯ごたえのある事件をもってきてほしいものだな": "++",
        "よく来たな。春来たる黒い死神": "+++++",
        "カオスの欠片を再構成してやろう": "-",
        "読書の邪魔だ！帰れったら帰れ！": "--",
        "ヴィクトリカのいばりんぼ！": "-----",
        "ヴィクトリカ～！": ".",
        "私の知恵の泉に不可能は無いのだよ": "[",
        "この灰色狼め！": "]",
        "あ～退屈で死にそうだ": ">",
        "この屁こきイモリめ": "<",
     }

def brainfuck(code):
    cPtr = ptr = 0
    while cPtr < len(code):
        matching = 0
        c = code[cPtr]
        if c == ">": ptr += 1
        if c == "<": ptr -= 1
        if c == "+": cells[ptr] = cells[ptr] + 1
        if c == "-": cells[ptr] = cells[ptr] - 1
        if c == ".": stdout.write(chr(cells[ptr]))
        if c == ",": cells[ptr] = ord(stdin.read(1))
        if c == "[" and cells[ptr] == 0:
            for x in xrange(cPtr,len(code)):
                if code[x] == '[': matching += 1
                if code[x] == ']':
                    if matching > 0: matching -= 1
                    if matching == 0: cPtr = x; break
        if c == "]" and cells[ptr] != 0:
            for x in xrange(cPtr,-1,-1):
                if code[x] == ']': matching += 1
                if code[x] == '[':
                    if matching > 0: matching -= 1
                    if matching == 0: cPtr = x; break
        cPtr += 1

def openfile():
    text = open(argv[1],"r")
    text = text.readlines()
    text = "".join(text)
    line = re.sub("\n", "", text)
    for i in dict.keys():
        line = re.sub(i, dict[i], line)
    return line

def main():
    line = openfile()
    brainfuck(line)

if __name__ == "__main__":
    main()

