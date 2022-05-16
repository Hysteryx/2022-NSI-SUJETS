def moyenne(notes):
    note_t = 0 
    coef_t = 0 
    for i in notes:
        note_t += i[0] * i[1]
        coef_t += i[1]
    return note_t / coef_t

#print(moyenne([(15,2),(9,1),(12,3)]))

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

#print(pascal(4))