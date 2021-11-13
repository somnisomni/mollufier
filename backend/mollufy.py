from kiwi_init import initKiwi
kiwi = initKiwi()

def mollufy(sentence):
  analyzed = kiwi.analyze(sentence, 10)
  mollufiedSentence = ""

  offset = 0

  for token in analyzed[0][0]:
    if offset < token.start:
      mollufiedSentence += sentence[offset:token.start]
    
    if token.tag.startswith("N") and token.len == 2:
      mollufiedSentence += "{}?{}".format(sentence[token.start:token.start + 1], sentence[token.start + 1:token.start + 2])
    else:
      mollufiedSentence += sentence[token.start:token.start + token.len]
    
    offset = token.start + token.len
  
  if offset < len(sentence):
    mollufiedSentence += sentence[offset:]

  return mollufiedSentence
