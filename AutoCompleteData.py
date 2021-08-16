class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def __init__(self, completed_sentence, offset, score, source_text):
        self.completed_sentence = completed_sentence
        self.score = score
        self.source_text = source_text
        self.offset = offset
