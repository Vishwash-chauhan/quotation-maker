from pathlib import Path
s=Path(r'c:\Users\vishw\Documents\Little Jalabies\quotation-maker\form.html').read_text(encoding='utf-8')
start = s.find('@media (min-width: 600px)')
print('start at',start)
# find first '{' after start
idx = s.find('{', start)
print('first brace at', idx)
# find matching close
i=idx+1
depth=1
n=len(s)
while i<n and depth>0:
    c=s[i]
    if c=='"' or c=="'" or c=='`':
        q=c; i+=1
        while i<n:
            if s[i]=='\\': i+=2; continue
            if s[i]==q: i+=1; break
            i+=1
        continue
    if s[i:i+2]=='/*':
        i+=2
        while i<n and s[i:i+2] != '*/': i+=1
        i+=2
        continue
    if s[i]=='{': depth+=1
    elif s[i]=='}': depth-=1
    i+=1
print('depth after scan',depth,'pos',i)
print('\n---SNIPPET---\n')
print(s[idx-80: i+80])
