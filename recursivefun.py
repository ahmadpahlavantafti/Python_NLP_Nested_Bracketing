import nltk

def recfun(tree):
    for node in tree:
        if (type(node) is nltk.Tree):
            if node.height() != 2:
                print("["),
            recfun(node)
            if node.height() != 2:
                print("]"),
            print(node.label()),

def parseTreeFromString(str):
    return nltk.Tree.fromstring(str)


tree = parseTreeFromString("""
( (S
    (NP-SBJ
      (NP (NNP Pierre) (NNP Vinken) )
      (, ,)
      (ADJP
        (NP (CD 61) (NNS years) )
        (JJ old) )
      (, ,) )
    (VP (MD will)
      (VP (VB join)
        (NP (DT the) (NN board) )
        (PP-CLR (IN as)
          (NP (DT a) (JJ nonexecutive) (NN director) ))
        (NP-TMP (NNP Nov.) (CD 29) )))
    (. .) ))
""")
recfun(tree)