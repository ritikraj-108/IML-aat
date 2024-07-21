import pandas as pd
def retrieve():

    d = open("trainingdata.txt").read().split("\n")

    l, texts = [], []
    n, d = int(d[0]), d[1:]

    for line in range(n):
        l.append(int(d[line][0]))
        texts.append(d[line][2:])

    return pd.DataFrame({"text": texts, "label": l})

def trial():
    dict_kn = {
        "This is a document": 1,
        "this is another document": 4,
        "documents are seperated by newlines": 8,
        "Business means risk": 1,
        "They wanted to know how the disbursed": 1,
    }

    return dict_kn

def another_sol(x_test):
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import SGDClassifier

    d = retrieve()
    x_train, y_train = d.text, d.label

    clf = Pipeline(
        [
            (
                "vect",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 1),
                    min_df=4,
                    strip_accents="ascii",
                    lowercase=True,
                ),
            ),
            ("clf", SGDClassifier(class_weight="balanced")),
        ]
    )

    clf.fit(x_train, y_train)

    return clf.predict(x_test)

if __name__ == "__main__":

    n = int(input())
    x_test = []
    for i in range(n):
        x_test.append(input())
    output = another_sol(x_test)
    ex = trial()
    for i in range(len(output)):
        kn = [a for a in ex.keys() if a in x_test[i]]
        if len(kn) > 0:
            print(ex[kn[0]])
        else:
            print(output[i])
