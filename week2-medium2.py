## The Minion Game
## link: https://www.hackerrank.com/challenges/the-minion-game

s = input()

vowels = "AEIOU"

kevin = 0
stuart = 0

for i in range(len(s)):
    if s[i] in vowels:
        kevin += (len(s)-i)
    else:
        stuart += (len(s)-i)
      
if kevin > stuart:
    print("Kevin "+str(kevin))
elif kevin < stuart:
    print("Stuart "+str(stuart))
else:
    print("Draw")
