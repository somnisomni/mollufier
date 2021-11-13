from kiwi_init import initKiwi
kiwi = initKiwi()

def mollufy(sentence):
  analyzed = kiwi.analyze(sentence)
  mollufiedSentence = ""

  offset = 0

  for token in analyzed[0][0]:
    if token.tag.startswith("N") and token.len == 2:
      if offset < token.start:
        mollufiedSentence += sentence[offset:token.start]

      mollufiedSentence += "{}?{}".format(sentence[token.start:token.start + 1], sentence[token.start + 1:token.start + 2])

      offset = token.start + token.len
  
  if offset < len(sentence):
    mollufiedSentence += sentence[offset:]

  return mollufiedSentence
