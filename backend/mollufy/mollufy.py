from mollufy.kiwi_init import initKiwi

kiwi = initKiwi()

def mollufy(sentence, noLenLimit=False, alternativeMark=False):
  analyzed = kiwi.analyze(sentence)[0][0]
  mollufiedSentence = sentence

  mark = "!" if alternativeMark else "?"

  for token in reversed(analyzed):
    if token.tag.startswith("N") and ((noLenLimit and token.len >= 2) or token.len == 2):
      leftEndPos = token.start + (token.len - 1)

      mollufiedSentence = "{}{}{}".format(mollufiedSentence[:leftEndPos], mark, mollufiedSentence[leftEndPos:])

  return mollufiedSentence
