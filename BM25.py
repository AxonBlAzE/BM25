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
    print(query_freq)

    # get input for occurence of each word in all the documents
    word_doc_occur = {}
    for word in query_freq:
        word_doc_occur[word] = {}
        word_doc_occur[word] = int(input("Enter Frequency of Occurence of " + word + " in All Documents" + ": "))
    print(word_doc_occur)

    # calcualting value of k
    k = calculate_k(k1, b, 1, ratio_of_doc_len)
    print("k = ", k)

    # BM25 formula
    score = 0
    for word in query_freq:
        score += math.log(((r+0.5)/(R-r+0.5))/((word_doc_occur[word]-r+0.5)/(N-word_doc_occur[word]-R+r+0.5)))*(((k1+1)*query_freq[word])/(k+query_freq[word]))* (((k2+1)*query_freq[word])/(k2+query_freq[word]))
    
    return score

if __name__ == "__main__":

    # query string
    query = "Cat Dog Cat Dog Cat"

    # number of documents
    N = 1000
    
    # free parameters
    k1 = 1.2
    k2 = 100
    b = 0.75
    # document length/average document length
    ratio_of_doc_len = 0.90

    # calculate score
    score = BM25(query, N, k1, k2, b, ratio_of_doc_len, 0, 0)
    print("Score = ", score)