import pandas as pd
from nltk.tokenize import sent_tokenize as st
from gensim.summarization import summarize
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


def loadDataAsDataFrame(f_path):
    df = pd.read_csv(f_path)
    return df

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
    
    print(result_dict)
    print()

    # Output result. Find sentence with the maximum score value
    maxi = [0, 0]
    for result in result_dict["scoring_data"]:
        if maxi[1] < result[1]:
            maxi = result

    if maxi[0] < len(result_dict["summarize_result"]):
        return result_dict["summarize_result"][maxi[0]]
    else:
        return None


f_path = './reddit_wsb.csv'
data = loadDataAsDataFrame(f_path)
head = header()
title = head[0]
body = head[6]

blah = []
count = 0
# testing
for line in body:
    if pd.notna(line):
        num_sent = len(st(line))
        count+=1
        if num_sent > 1:
            # use NLP summarizer from gtech teams code to store the summary in a new list
            # NLP_summarize(line)
            print('yay')
        else:
            print('boo!')
            break
                        
NLP_summarize(line)
