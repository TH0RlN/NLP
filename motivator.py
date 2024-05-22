from sys import argv
from nltk import CFG
from nltk.parse.generate import generate
from random import choice

def main():
    depth = 0
    if len(argv) == 2:
        depth = int(argv[1])
    elif len(argv) == 1:
        depth = 5
    else:
        print("Usage: python motivator.py [depth]")
        exit(1)

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
    
    parser = generate(grammar, depth=depth)
    phrases = []
    for sentence in parser:
        phrases.append(' '.join(sentence))
    print(choice(phrases))
    exit(0)

if __name__ == "__main__":
    main()