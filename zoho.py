def isupper(ch):
    if ch >= 'A' and ch <= 'Z':
        return True
    return False
  
# to check for LOWERCASE
def islower(ch):
    if ch >= 'a' and ch <= 'z':
        return True
    return False
  
# To print reciprocal string
def reciprocalString(word):
    ch = ''
    for i in range(len(word)):
  
        
        if isupper(word[i]):
            ch = chr(ord('Z') - 
                     ord(word[i]) + ord('A'))
            print(ch, end = "")
  
        
        elif islower(word[i]):
            ch = chr(ord('z') - 
                     ord(word[i]) + ord('a'))
            print(ch, end = "")
        else:
            print(word[i], end = "")
  
# Driver Code
if __name__ == "__main__":
    s = input('string:')
    print("The reciprocal of", s, "is - ")
    reciprocalString(s)
  
