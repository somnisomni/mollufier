from kiwi_init import initKiwi
kiwi = initKiwi()

def mollufy(sentence, noLenLimit=False):
  analyzed = kiwi.analyze(sentence)
  mollufiedSentence = ""

  offset = 0

  for token in analyzed[0][0]:
    if token.tag.startswith("N") and ((noLenLimit and token.len >= 2) or token.len == 2):
      if offset < token.start:
        mollufiedSentence += sentence[offset:token.start]

      startOffset = token.start
      leftEndOffset = startOffset + (token.len - 1)
      rightEndOffset = leftEndOffset + 1

      mollufiedSentence += "{}?{}".format(sentence[startOffset:leftEndOffset], sentence[leftEndOffset:rightEndOffset])

      offset = token.start + token.len
  
  if offset < len(sentence):
    mollufiedSentence += sentence[offset:]

  return mollufiedSentence
