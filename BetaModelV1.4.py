from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')


def similarity_score(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)


def compare_strings_transformer(string1, string2, model):
    embeddings = model.encode([string1, string2])
    similarity = similarity_score(embeddings[0], embeddings[1])
    score = round(similarity * 10, 2)
    return score


string1 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."
string2 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."

score = compare_strings_transformer(string1, string2, model)
print(f"Similarity score: {score}/10")

from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')


def similarity_score(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)


def compare_strings_transformer(string1, string2, model):
    embeddings = model.encode([string1, string2])
    similarity = similarity_score(embeddings[0], embeddings[1])
    score = round(similarity * 10, 2)
    return score

string1 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."
string2 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."


score = compare_strings_transformer(string1, string2, model)
print(f"Similarity score: {score}/10")

from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')


def similarity_score(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)


def compare_strings_transformer(string1, string2, model):
    embeddings = model.encode([string1, string2])
    similarity = similarity_score(embeddings[0], embeddings[1])
    score = round(similarity * 10, 2)
    return score


string1 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."
string2 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."


score = compare_strings_transformer(string1, string2, model)
print(f"Similarity score: {score}/10")

from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('paraphrase-mpnet-base-v2')


def similarity_score(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)


def compare_strings_transformer(string1, string2, model):
    embeddings = model.encode([string1, string2])
    similarity = similarity_score(embeddings[0], embeddings[1])
    score = round(similarity * 10, 2)
    return score


string1 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."
string2 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."


score = compare_strings_transformer(string1, string2, model)
print(f"Similarity score: {score}/10")
# %%
