# coding: utf-8
import sys
print u"-LiSA言語-" +\
      u"Ver0.01"
class LiSA():
    class LiSAError(StandardError): pass

    def __init__(self, src):
        self._tokens = src
        self._jumps = self._analyze_jumps(self._tokens)

    def run(self):
        tape = []
        pc = 0
        cur = 0

        while pc < len(self._tokens):
            if cur >= len(tape):
                tape.append(0)
            if self._tokens[pc] == u"サ":#bf = +
                tape[cur] += 1
            elif self._tokens[pc] == "-":#bf = -
                tape[cur] -= 1
            elif self._tokens[pc] == u"リ":#bf = >
                cur += 1
            elif self._tokens[pc] == u"ア":#bf = <
                cur -= 1
                if cur < 0: raise self.LiSAError(u'開始地点より左には移動できないんだよなぁ(呆れ')
            elif self._tokens[pc] == u"ぬ":#bf = .
                print chr(tape[cur]),
            elif self._tokens[pc] == ",":#bf = ,
                tape[cur] = ord(raw_input().strip())
            elif self._tokens[pc] == "[":#bf = [
                if tape[cur] == 0:
                    pc = self._jumps[pc]
            elif self._tokens[pc] == "]":#bf = ]
                if tape[cur] != 0:
                    pc = self._jumps[pc]
            pc += 1

    def _analyze_jumps(self, tokens):
        jumps = {}
        starts = []

        for i, c in enumerate(tokens):
            if c == "[":
                starts.append(i)
            elif c == "]":
                if not starts: raise self.LiSAError(u"「]」多スギィ！！")
                frm = starts.pop()
                to = i

                jumps[frm] = to
                jumps[to] = frm
        if starts: raise LiSAError(u"「[」多スギィ！！")

        return jumps

try:
    src = open(sys.argv[1]).read()
except IOError:
    src = sys.argv[1]
except IndexError:
    src = raw_input()

try:
    LiSA(src).run()
except LiSA.LiSAError:
    print u'実行失敗してんだよサルゥ！！'
stop = raw_input()
