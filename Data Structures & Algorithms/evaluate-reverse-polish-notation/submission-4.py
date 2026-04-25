class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i=="+":
                a = s.pop()
                b = s.pop()
                s.append(int(a)+int(b))
            elif i=="-":
                a = s.pop()
                b = s.pop()
                s.append(int(b)-int(a))
            elif i=="*":
                a = s.pop()
                b = s.pop()
                s.append(int(a)*int(b))
            elif i=="/":
                a = s.pop()
                b = s.pop()
                s.append(int(int(b)/int(a)))
            else:
                print(i)
                s.append(int(i))
        return s[-1]