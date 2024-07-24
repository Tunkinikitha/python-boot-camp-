def check(s):
    stack=[]
    openings=['(','[','{']
    brackets={
        '(':')',
        '[':']',
        '{':'}'
    }
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack:
                top=stack.pop()
                if brackets[top]!=i:
                    return 'no'
                else:
                    return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'
s='{} [] () {}'
print(check(s))    