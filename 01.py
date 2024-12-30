from secrets import choice as sc
o="?"
x=[0,1]
while o:
    if input(o+'\n') == o:
        if (v:=sc(x)) == 1:
            o += o[-1]
            x.append(0)
        else:
            x.remove(0)
            o = o[:-1]
    else:
        o = o[:-1]
exit()
