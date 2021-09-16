str = "nanda"
key = int(input())
temp = ''
for i in range(0,len(str)):
  if str[i]>='A' and str[i]<='Z':
    offset = ord(str[i])-65
    offset  = (offset+key)%26
    ch = chr(offset+ord('A'))
    temp += ch
  elif str[i]>='a' and str[i]<='z':
    offset = ord(str[i])-97
    offset = (offset+key)%26
    ch = chr(offset+ord('a'))
    temp+=ch
  else:
    temp += ' '
print(temp)




