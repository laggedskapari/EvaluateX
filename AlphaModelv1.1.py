import streamlit as st
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt

# Load the model
model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')
model2 = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')
model3 = SentenceTransformer('paraphrase-mpnet-base-v2')

scoreArray = []


def similarity_score(embedding1, embedding2):


    
    return 1 - cosine(embedding1, embedding2)


def compare_strings_transformer(string1, string2, model):
    embeddings = model.encode([string1, string2])
    similarity = similarity_score(embeddings[0], embeddings[1])
    score = round(similarity * 10, 2)
    return score


st.title("Subjective Answer Evaluation - ")

st.title("What is DBMS ?")

# string1 = st.text_area(label='Base Answer - ', placeholder='Enter Base Answer...')
string1 = "A database management system (or DBMS) is essentially nothing more than a computerized data-keeping system. Users of the system are given facilities to perform several kinds of operations on such a system for either manipulation of the data in the database or the management of the database structure itself."
string2 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="1")

# if st.button("Compare", key="2"):
#     if string1 and string2:
#         score = compare_strings_transformer(string1, string2, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")

st.title("What is Data Structure ?")

# string1 = st.text_area(label='Base Answer - ', placeholder='Enter Base Answer...')
string3 = "a data structure is a data organization, management, and storage format that is usually chosen for efficient access to data. "
string4 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="3")

# if st.button("Compare", key="4"):
#     if string1 and string2:
#         score = compare_strings_transformer(string3, string4, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")

st.title("What is an Algorithm")

string5 = "An algorithm is a set of step-by-step procedures, or a set of rules to follow, for completing a specific task or solving a particular problem.Algorithmic programming is all about writing a set of rules with a finite number of steps that instruct the computer how to perform a task. A computer program is essentially an algorithm that tells the computer what specific steps to execute, in what specific order, in order to carry out a specific task. Algorithms are written using particular syntax, depending on the programming language being used."
string6 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="5")

# if st.button("Compare", key="6"):
#     if string1 and string2:
#         score = compare_strings_transformer(string5, string6, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("Explain Binary Tree ?")

string7 = "A binary tree is a hierarchal data structure in which each node has at most two children. The child nodes are called the left child and the right child."
string8 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="7")

# if st.button("Compare", key="8"):
#     if string1 and string2:
#         score = compare_strings_transformer(string7, string8, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("Explain Object Oriented Languages ?")

string9 = "Object-oriented language (OOL) is a high-level computer programming language that implements objects and their associated procedures within the programming context to create software programs. Object-oriented language uses an object-oriented programming technique that binds related data and functions into an object and encourages reuse of these objects within the same and other programs."
string10 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="9")

# if st.button("Compare", key="10"):
#     if string1 and string2:
#         score = compare_strings_transformer(string9, string10, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("What is Polymorphism?")

string11 = "Polymorphism is one of the core concepts of object-oriented programming (OOP) and describes situations in which something occurs in several different forms. In computer science, it describes the concept that you can access objects of different types through the same interface. Each type can provide its own independent implementation of this interface."
string12 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="11")

# if st.button("Compare", key="12"):
#     if string1 and string2:
#         score = compare_strings_transformer(string11, string12, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("What is Artificial Intelligence?")

string13 = "Artificial intelligence is intelligence—perceiving, synthesizing, and inferring information—demonstrated by machines, as opposed to intelligence displayed by humans or by other animals."
string14 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="13")

# if st.button("Compare", key="14"):
#     if string1 and string2:
#         score = compare_strings_transformer(string13, string14, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("What is a Transformer in AIML?")

string15 = "A transformer is a deep learning model. It is distinguished by its adoption of self-attention, differentially weighting the significance of each part of the input (which includes the recursive output) data. It is used primarily in the fields of natural language processing (NLP) and computer vision (CV)."
string16 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="15")

# if st.button("Compare", key="16"):
#     if string1 and string2:
#         score = compare_strings_transformer(string15, string16, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")
#
#
st.title("What is Cosine Similarity?")

string17 = "In data analysis, cosine similarity is a measure of similarity between two non-zero vectors defined in an inner product space. Cosine similarity is the cosine of the angle between the vectors; that is, it is the dot product of the vectors divided by the product of their lengths. "
string18 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="17")

# if st.button("Compare", key="18"):
#     if string1 and string2:
#         score = compare_strings_transformer(string17, string18, model)
#         score2 = compare_strings_transformer(string1, string2, model2)
#         score3 = compare_strings_transformer(string1, string2, model3)
#         finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
#         scoreArray.append(score)
#     else:
#         st.warning("Please enter both sentences to compare.")


st.title("What is Tokenization?")

string19 = "Tokenization, when applied to data security, is the process of substituting a sensitive data element with a non-sensitive equivalent, referred to as a token, that has no intrinsic or exploitable meaning or value. The token is a reference that maps back to the sensitive data through a tokenization system. "
string20 = st.text_area(label='User Answer - ', placeholder='Enter User Answer...', key="19")

if st.button("Get Scores", key="20"):
    score = compare_strings_transformer(string1, string2, model)
    scoreArray.append(score)
    score2 = compare_strings_transformer(string3, string4, model)
    scoreArray.append(score2)
    score3 = compare_strings_transformer(string5, string6, model)
    scoreArray.append(score3)
    score4 = compare_strings_transformer(string7, string8, model)
    scoreArray.append(score4 - 1)
    score5 = compare_strings_transformer(string9, string10, model)
    scoreArray.append(score5)
    score6 = compare_strings_transformer(string11, string12, model)
    scoreArray.append(score6)
    score7 = compare_strings_transformer(string13, string14, model)
    scoreArray.append(score7)
    score8 = compare_strings_transformer(string15, string16, model)
    scoreArray.append(score8)
    score9 = compare_strings_transformer(string17, string18, model)
    scoreArray.append(score9)
    score10 = compare_strings_transformer(string19, string20, model)
    scoreArray.append(score10)

    avgScore = sum(scoreArray) / 10
    st.title(str(avgScore) + " / 10")

    fig, ax = plt.subplots()

    ax.bar(range(1, len(scoreArray)+1), scoreArray)
    ax.set_title('Bar Graph')
    ax.set_xlabel('Question No.')
    ax.set_ylabel('Score / 10')
    st.pyplot(fig)



    # score2 = compare_strings_transformer(string1, string2, model2)
    # score3 = compare_strings_transformer(string1, string2, model3)
    # finalScore = (0.1 * score) + (0.2 * score2) + (0.7 * score3)
    # scoreArray.append(score)


