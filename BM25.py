import math

def calculate_k(k1,b, avg_doc_len, doc_len):
    return k1 * ((1-b) + b * (doc_len/avg_doc_len))

def BM25(query, N, k1, k2, b, ratio_of_doc_len, r, R):

    # identify unique words in query separated by space
    query = query.split()
    unique_words = set(query)

    # count frequency of each word in query and create a dictionary
    query_freq = {}
    for word in query:
        query_freq[word] = query.count(word)
    print(f"Query Frequencies are as follows: {query_freq}\n")

    # get input for occurence of each word in all the documents (document frequency)
    doc_frequency = {}
    for word in query_freq:
        doc_frequency[word] = int(input("Enter Frequency of Occurence of " + word + " in All Documents (Document Frequency)" + ": "))
    print(f"\nDocument Frequencies are as follows: {doc_frequency}\n")


    # get input for occurence of each word in the document (term frequency)
    term_frequency = {}
    for word in query_freq:
        term_frequency[word] = int(input("Enter Frequency of Occurence of " + word + " in the Document (Term Frequency)" + ": "))
    print(f"\nTerm Frequencies are as follows: {term_frequency}\n")

    # calcualting value of k
    k = calculate_k(k1, b, 1, ratio_of_doc_len)
    # print("k = ", k)

    # To Find
    bm1_score = 0
    bm11_score = 0
    bm15_score = 0
    bm25_score = 0

    for word in query_freq:
        n = doc_frequency[word]
        f = term_frequency[word]
        qf = query_freq[word]

        # BM1 formula
        bm1_score += math.log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))

        # BM11 formula
        bm11_score += math.log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))*(((k1+1)*f)/(k*ratio_of_doc_len+f))

        # BM15 formula
        bm15_score += math.log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))*(((k1+1)*f)/(k+f))

        # BM25 formula
        bm25_score += math.log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))*(((k1+1)*f)/(k+f))* (((k2+1)*qf)/(k2+qf))
    

    score = {
        "BM1": bm1_score,
        "BM11": bm11_score,
        "BM15": bm15_score,
        "BM25": bm25_score
    }

    # display scores in tabular format
    print('-'*47, '\n| {:<20} | {:<20} |'.format('Algorithm', 'Score'))
    print('-'*47)
    for k, v in score.items():
        print('| {:<20} | {:<20} |'.format(k, v))
    print('-'*47)
    
    return score

if __name__ == "__main__":

    # query string
    query = "Cat Dog Cat Dog Cat"

    # number of documents
    N = 1000
    
    # free parameters
    k1 = 1.2
    k2 = 100
    b = 0.50
    # document length/average document length
    ratio_of_doc_len = 0.80

    # calculate score
    score = BM25(query, N, k1, k2, b, ratio_of_doc_len, 0, 0)
    # print("Score = ", score)