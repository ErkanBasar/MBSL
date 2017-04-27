from pynlpl.formats import folia

def getFoliaTokens(sentenceId):
    corpus = []
    filepath = "data/EIFD-FlatData/" + sentenceId.split('.')[0] + ".folia.xml"
    doc = folia.Document(file=filepath)
    sentence = doc[sentenceId]
    for word in sentence.words():
        corpus.append(word.text())             
    return corpus
