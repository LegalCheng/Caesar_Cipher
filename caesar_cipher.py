def CaesarCipher(Plaintext,offset,Side):
    textlist=list(Plaintext)
    if Side==1:
        for i in range(0,len(textlist)):
            after=ord(textlist[i])+offset
            if (after>90 and after<97) or (after>122):
                textlist[i]=chr(ord(textlist[i])+offset-26)
            else:
                textlist[i]=chr(ord(textlist[i])+offset)
    else:
        for i in range(0,len(textlist)):
            after=ord(textlist[i])-offset
            if (after<65) or (after>90 and after<97):
                textlist[i]=chr(ord(textlist[i])-offset+26)
            else:
                textlist[i]=chr(ord(textlist[i])-offset)
    Ciphertext=''.join(textlist)
    print(Ciphertext)

Plaintext=input("Plaintext:")
offset=input("offset:")
rightANDleft=input("Offset (1) Right and (2) Left ?")
CaesarCipher(Plaintext,int(offset),int(rightANDleft))
