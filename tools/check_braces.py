from pathlib import Path
p=Path(r'c:\Users\vishw\Documents\Little Jalabies\quotation-maker\form.html')
s=p.read_text(encoding='utf-8')
# Simple lexer to ignore strings and comments and count braces
i=0
n=len(s)
stack=[]
errors=[]
while i<n:
    c=s[i]
    if c=='"' or c=="'" or c=='`':
        q=c
        i+=1
        while i<n:
            if s[i]=='\\': i+=2; continue
            if s[i]==q: i+=1; break
            i+=1
        continue
    if s[i:i+2]=='//':
        i+=2
        while i<n and s[i]!='\n': i+=1
        continue
    if s[i:i+2]=='/*':
        i+=2
        while i<n and s[i:i+2] != '*/': i+=1
        i+=2
        continue
    if c=='{' or c=='(' or c=='[':
        stack.append((c,i))
    elif c=='}' or c==')' or c==']':
        if not stack:
            errors.append((i,c,'closing without opening'))
        else:
            o,pos=stack.pop()
            pairs={'{':'}','(':')','[':']'}
            if pairs[o]!=c:
                errors.append((i,c,f'mismatched {o} vs {c} at pos {pos}'))
    i+=1
print('stack size:', len(stack))
for o,pos in stack[:50]:
    print('unclosed',o,'at',pos)
print('errors count:', len(errors))
for e in errors[:50]:
    print('err at', e)
