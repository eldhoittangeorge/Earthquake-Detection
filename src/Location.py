import spacy


def get_location(tweet = None):
    nlp = spacy.load("en_core_web_sm")
    location = []
    if(not tweet):
        return 
    doc = nlp(tweet)
    if(doc.ents):
        # print(doc.ents)
        for ent in doc.ents:
            if(ent.label_ == "GPE"):
                location.append(ent.text)
        if(not location):
            print("No location found")
            return
        else:
            return ", ".join(location)
    else:
        print("Doesn't exist")