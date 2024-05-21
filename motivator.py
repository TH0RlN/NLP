from nltk import CFG
from nltk.parse.generate import generate
from random import choice

def main():
    grammar = CFG.fromstring("""
        S -> NP VP

        NP -> D A N | D N | N
        D -> "The" | "Your" | "A"
        A -> "incredible" | "amazing" | "remarkable" | "unstoppable" | "brilliant" | "extraordinary"
        N -> "potential" | "journey" | "strength" | "talent" | "vision" | "effort"

        VP -> V V2 | V PP | V
        V -> "will" | "can" | "shall" | "must"
        V2 -> "shine" | "succeed" | "grow" | "flourish" | "prevail"
        PP -> P NP
        P -> "in" | "through" | "with"
    """)

    parser = generate(grammar, depth=4)
    phrases = []
    for sentence in parser:
        phrases.append(' '.join(sentence))
    print(choice(phrases))

if __name__ == "__main__":
    main()