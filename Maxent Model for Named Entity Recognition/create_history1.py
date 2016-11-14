import nltk

def create_history(tags,tokens):
    """Method to create history tuples"""
    history = []
    tags_l=["PERSON","ORGANIZATION","GPE","MONEY","DATE","TIME","OTHER","FACILITY"]
    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            if((j-2)<0):
                u = '*'
            else:
                try:
                    u = tags[tokens[i][j-2]]
                except:
                    u = 'OTHER'
            if((j-1)<0):
                v = '*'
            else:
                try:
                    v = tags[tokens[i][j-1]]
                except:
                    v ='OTHER'
            try:
                kk = tags[tokens[i][j]]
            except:
                kk ='OTHER'
            if(u not in tags_l or not(u=='*')):
                u='OTHER'
            if(v not in tags_l or not(v=='*')):
                v='OTHER'
            if(kk not in tags_l or not(kk=='*')):
                kk='OTHER'
            x = (u,v,tuple(tokens[i]),j,kk)
            history.append(x)
    return history

with open('output.txt', 'r') as f:
    sample = f.read()
     
sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = []
for i in tagged_sentences:
    chunked_sentences.append(nltk.chunk.ne_chunk(i))

def extract_entity_names(t):
    for n in t:
        if isinstance(n, nltk.tree.Tree):
                tags[str(n).split("/")[0].split(" ")[1]] = n.label()

entity_names = []
tags = dict()
for tree in chunked_sentences:
    extract_entity_names(tree)
h = create_history(tags,tokenized_sentences)
f = open("history_5_tuple.txt","w")
f.write(str(h))
f.close()
