from kiwipiepy import Kiwi

def initKiwi():
  kiwi = Kiwi()

  kiwi.add_user_word("몰루", "NNP")
  kiwi.add_user_word("아루", "NNP")
  kiwi.add_user_word("네루", "NNP")
  kiwi.add_user_word("코하루", "NNP")
  kiwi.add_user_word("아카이브", "NNG")

  return kiwi
