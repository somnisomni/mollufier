import unittest
from mollufy import mollufy

class MollufyTestSimple(unittest.TestCase):
  def test_mollufy_word_2chars(self):
    # TEST 1: Mollufy simple 2-characters noun word
    self.assertEqual(mollufy.mollufy("블루"), "블?루")
    self.assertEqual(mollufy.mollufy("하루"), "하?루")
    self.assertEqual(mollufy.mollufy("감정"), "감?정")

  def test_mollufy_word_manychars_without_param(self):
    # TEST 2: Ensure 3-characters-or-above noun word not to be mollufied without parameter
    self.assertEqual(mollufy.mollufy("마술사"), "마술사")
    self.assertEqual(mollufy.mollufy("모니터"), "모니터")
    self.assertEqual(mollufy.mollufy("아이스크림"), "아이스크림")

  def test_mollufy_word_manychars(self):
    # TEST 3: Mollufy 3-characters-or-above noun word with parameter
    self.assertEqual(mollufy.mollufy("슬리퍼", True), "슬리?퍼")
    self.assertEqual(mollufy.mollufy("이구동성", True), "이구동?성")
    self.assertEqual(mollufy.mollufy("아메리카노", True), "아메리카?노")

  def test_mollufy_non_noun_word(self):
    # TEST 4: Ensure non-noun words not to be mollufied
    self.assertEqual(mollufy.mollufy("좋아"), "좋아")
    self.assertEqual(mollufy.mollufy("그만해", True), "그만해")
    self.assertEqual(mollufy.mollufy("냠냠쩝쩝", True), "냠냠쩝쩝")

class MollufyTestSentence(unittest.TestCase):
  def test_mollufy_sentence_with_one_2chars_word(self):
    # TEST 5: Mollufy sentence with one 2-characters noun word
    self.assertEqual(mollufy.mollufy("귀가하세요"), "귀?가하세요")
    self.assertEqual(mollufy.mollufy("바다에 갑시다"), "바?다에 갑시다")
    self.assertEqual(mollufy.mollufy("재미있는 게임인데"), "재미있는 게?임인데")

  def test_mollufy_sentence_with_one_manychar_word(self):
    # TEST 6: Mollufy sentence with one 3-characters-or-above noun word
    self.assertEqual(mollufy.mollufy("참관인이세요?", True), "참관?인이세요?")
    self.assertEqual(mollufy.mollufy("보드카 너무 써", True), "보드?카 너무 써")
    self.assertEqual(mollufy.mollufy("필라멘트가 타버렸네", True), "필라멘?트가 타버렸네")

  def test_mollufy_sentence_with_many_2chars_words(self):
    # TEST 7: Mollufy sentence with many 2-characters noun words
    self.assertEqual(mollufy.mollufy("내가 재미있는 게임을 하나 알아냈는데, 나중에 검색해봐"), "내가 재미있는 게?임을 하나 알아냈는데, 나?중에 검?색해봐")
    self.assertEqual(mollufy.mollufy("그야말로 연애재판 너는 나에게 얼마만큼의 죄를 물을 거니?"), "그야말로 연?애재?판 너는 나에게 얼?마만큼의 죄를 물을 거니?")
    self.assertEqual(mollufy.mollufy("두 글자 명사가 다수 존재하는 문장을 생각하기는 곤란하다"), "두 글?자 명?사가 다?수 존?재하는 문?장을 생?각하기는 곤?란하다")

  def test_mollufy_sentence_with_many_words(self):
    # TEST 8: Mollufy sentence with many noun words (without no length limit)
    self.assertEqual(mollufy.mollufy("대한민국의 영토는 한반도와 그 부속도서로 한다.", True), "대한민?국의 영?토는 한반?도와 그 부?속도?서로 한다.")
    self.assertEqual(mollufy.mollufy("대한민국은 통일을 지향하며, 자유민주적 기본질서에 입각한 평화적 통일 정책을 수립하고 이를 추진한다.", True), "대한민?국은 통?일을 지?향하며, 자?유민?주적 기?본질?서에 입?각한 평?화적 통?일 정?책을 수?립하고 이를 추?진한다.")
    self.assertEqual(mollufy.mollufy("블루 아카이브 정말 건전하고 건강하고 밝은 게임인데...", True), "블?루 아카이?브 정말 건?전하고 건?강하고 밝은 게?임인데...")

  def test_mollufy_sentence_with_many_words_without_param(self):
    # TEST 9: Mollufy 2-characters noun words in sentence, not 3-characters-or-above noun words
    self.assertEqual(mollufy.mollufy("그래픽 디자인은 특정 메시지 (혹은 콘텐츠)와 이를 전달하려는 대상자에게 걸맞은 매체 (인쇄물, 웹사이트, 동영상 등)를 선택하여 표현 또는 제작하는 창의적인 과정이다."),
                                     "그래픽 디자인은 특?정 메시지 (혹은 콘텐츠)와 이를 전?달하려는 대상자에게 걸맞은 매?체 (인쇄물, 웹사이트, 동영상 등)를 선?택하여 표?현 또는 제?작하는 창?의적인 과?정이다.")

class MollufyTestMeme(unittest.TestCase):
  def test_mollufy_meme_words(self):
    # TEST 10: Meme words
    self.assertEqual(mollufy.mollufy("몰루"), "몰?루")
    self.assertEqual(mollufy.mollufy("코하루"), "코하?루")
    self.assertEqual(mollufy.mollufy("아루"), "아?루")
    self.assertEqual(mollufy.mollufy("네루"), "네?루")

  def test_mollufy_meme_sentences(self):
    # TEST 11: Meme sentences
    self.assertEqual(mollufy.mollufy("몰루는건가..."), "몰?루는건가...")
    self.assertEqual(mollufy.mollufy("내가 몰루가 될께..."), "내가 몰?루가 될께...")

class MollufyTestAltmark(unittest.TestCase):
  def test_mollufy_altmark(self):
    # TEST 12: Mollufy with alternative mark: [!]
    self.assertEqual(mollufy.mollufy("바람", alternativeMark=True), "바!람")
    self.assertEqual(mollufy.mollufy("아루", alternativeMark=True), "아!루")
    self.assertEqual(mollufy.mollufy("스튜디오", True, True), "스튜디!오")
    self.assertEqual(mollufy.mollufy("각설탕을 커피에 타먹으면 달게요 안 달게요~", True, True), "각설!탕을 커!피에 타먹으면 달게요 안 달게요~")

if __name__ == "__main__":
  unittest.main()
