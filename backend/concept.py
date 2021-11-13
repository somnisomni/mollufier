from kiwipiepy import Kiwi, Token
kiwi = Kiwi()

sentence = input().strip()

analyzed = kiwi.analyze(sentence)
print(analyzed, end='\n\n')

for token in analyzed[0][0]:
  if token.tag.startswith("N") and len(token.form) == 2:
    print("{}?{}".format(token.form[0], token.form[1]), end='')
  else:
    print(token.form, end='')
