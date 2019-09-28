
brackets= {'{':'}','[':']','(':')'}

expression = "][(]}})("
expression = "(]"

open = []
#print(expression)

no = 0

if len(expression) % 2 != 0:
    no=1
else:
    for br in expression:
        if br in brackets:
            open.append(br)
        else:
            if open==[] or brackets[open.pop()]!=br:
                no=1
                break

if open!=[] or no == 1:
    print("false")
else:
    print("true")