from abydos.phonetic import RussellIndex

transcription_list = ["bio tech", "every youth", "holli via"]
brands_list = ["biotique", "everyuth", "olivia"]


class Phonetic_Similarity:
    # make a function that outputs updated list of transcriptions + confidence scores between 0-1

    # function below takes in 2 lists and tries to match words from the corresponding 
    # index values in both lists
    def matchCase(spokenList, brandsList):
        algo = RussellIndex()
        word_encode = lambda i : algo.encode(i)
        counter = 0
        for a in spokenList:
            print(spokenList)
            if word_encode(a) == word_encode(brandsList[counter]):
                spokenList[spokenList.index(a)] = brandsList[counter]
            counter += 1
        return spokenList

    # function replaces a word in a list with a new word
    def replace(sequence, old, new):
        return (new if x == old else x for x in sequence)

    # needs to be worked on
    def confidence_score():
        pass

pe = Phonetic_Similarity
print(pe.matchCase(transcription_list, brands_list))

# Next Steps
# delete counter and eliminate dependency on brand order by using dictionary, use keys somehow
# figure out best method to have confidence score
# also include try loops to caputre exceptions

#output, there is a print statement in matchCase that prints spokenList repeatedly
"""
['bio tech', 'every youth', 'holli via']
['biotique', 'every youth', 'holli via']
['biotique', 'everyuth', 'holli via']
['biotique', 'everyuth', 'olivia']
"""