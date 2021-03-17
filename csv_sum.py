import pandas as pd
from nltk.tokenize import sent_tokenize as st
from gensim.summarization import summarize
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

# given path loads data as dataframe
def loadDataAsDataFrame(f_path):
    df = pd.read_csv(f_path, encoding="ISO-8859-1")
    # encoding allows system to properly consume special characters
    return df

# saves all headers from dataframe in a list
def header():
    title = data['title']
    score = data['score']
    ids = data['id']
    url = data['url']
    comms_num = data['comms_num']
    created = data['created']
    body = data['body']
    timestamp = data['timestamp']
    h = [title, score, ids, url, comms_num, created, body, timestamp]
    return h

# gtech summarize function
def NLP_summarize(description: str):

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(description, abstractable_doc)
    '''commented out print statement in gtech's original function
    print(result_dict)
    print()
    '''
    # Output result. Find sentence with the maximum score value
    maxi = [0, 0]
    for result in result_dict["scoring_data"]:
        if maxi[1] < result[1]:
            maxi = result

    if maxi[0] < len(result_dict["summarize_result"]):
        return result_dict["summarize_result"][maxi[0]]
    else:
        return None

# file path
f_path = './reddit_wsb.csv'
# calls loadDateAsDataFrame function as data
data = loadDataAsDataFrame(f_path)
# calls header function as head
head = header()
# calls body header from the header function
body = head[6]
# initialize new list for summaries
summarizedList = []
# loops through the items in body list
for line in body:
    # checks if the items being looped through exist
    if pd.notna(line):
        # checks the number of sentences of the currenct item in loop as num_sent
        num_sent = len(st(line))
        # checks to see if there is more than one sentence in the 
        # current item of loop to selectively summary and append to new list
        if num_sent > 1:
            summarizedList.append(NLP_summarize(line))
            
