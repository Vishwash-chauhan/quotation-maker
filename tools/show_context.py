from pathlib import Path
s=Path(r'c:\Users\vishw\Documents\Little Jalabies\quotation-maker\form.html').read_text(encoding='utf-8')
for pos in [9395,119908]:
    line = s.count('\n',0,pos)+1
    col = pos - s.rfind('\n',0,pos)
    start = max(0,pos-120)
    end = min(len(s),pos+120)
    print('--- position',pos,'line',line,'col',col,'---')
    print(s[start:end])
    print('\n')
