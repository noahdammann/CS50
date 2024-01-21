import nltk
nltk.download("punkt")
import sys
import re

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# Sentence -> Noun Phrase + Verb Phrase | Sentence + Conjunction + Sentence | Sentence + Conjunction + Clause
# Noun Phrase -> Noun | Determiner + Noun Phrase | Preposition + Noun Phrase | Adjective + Noun Phrase | Preposition + Determiner + Noun Phrase | Noun Phrase + Noun Phrase | Adverb + Noun Phrase | Noun Phrase + Adverb
# Verb Phrase -> Verb | Verb + Noun Phrase | Adverb + Verb Phrase | Verb Phrase + Adverb
# Clause -> Verb + Noun Phrase

NONTERMINALS = """
S -> NP VP | S Conj S | S Conj C
NP -> N | Det NP | P NP | Adj NP | P Det NP | NP NP | Adv NP | NP Adv
VP -> V | V NP | Adv VP | VP Adv
C -> V NP

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    tokenized = nltk.word_tokenize(sentence)

    list = []
    for token in tokenized.copy():
        for char in token:
            if char.isalpha():
                list.append(token.lower())
                break

    return list

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    return tree.subtrees(
        lambda t: t.label() == "NP"
        and not list(t.subtrees(lambda st: t != st and st.label() == "NP"))
    )

if __name__ == "__main__":
    main()
