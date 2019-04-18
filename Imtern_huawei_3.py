s="3(2(sd)3(ert)A)6(BCV)"
def fun (s):
    s_dict={'(':')','[':']','{':'}'}

    start=[]
    end=[]
    for i,c in enumerate(s):
        if c=='(' or c=='[' or c=='{':
            start.append(i)
        if c==')' or c==']' or c=='}':
            end.append(i)
    e_i=0
    tmp=''

    for s_i in range(len(start)-1,-1,-1):
        for e_i in range(len(end)):
            if end[e_i]>start[s_i]:
                tmp=s[start[s_i]+1:end[e_i]]*int(s[start[s_i]-1])
                old=s[start[s_i]-1:end[e_i]+1]
                s=s.replace(old,tmp)
                mo=len(tmp)-(end[e_i]-start[s_i]+2)
                if mo!=0:
                    for i in range(e_i+1,len(end)):
                        end[i]+=mo
                del end[e_i]
                break
    out=s[0:start[0]-1]+tmp
    lst=list(out)
    lst.reverse()
    l="".join(lst)
    print(l)
fun(s)