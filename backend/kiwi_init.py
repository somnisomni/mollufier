from kiwipiepy import Kiwi
import sys
import os

def addWord(kiwi: Kiwi, word: str, tag: str, score: float = 0):
  result = kiwi.add_user_word(word, tag, score)

  if not result:
    sys.stderr.write("Word '{}' not added to Kiwi model".format(word))
    sys.stderr.write(os.linesep)


def initKiwi():
  kiwi = Kiwi()

  addWord(kiwi, "몰루", "NNP")
  addWord(kiwi, "아루", "NNP")
  addWord(kiwi, "네루", "NNP")
  addWord(kiwi, "코하루", "NNP")
  addWord(kiwi, "아카이브", "NNG")

  return kiwi
