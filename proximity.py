"""
Author: fedebyes
Date: 26/10/19

Theory base: https://marcobonzanini.com/2015/02/09/phrase-match-and-proximity-search-in-elasticsearch/

proximity(text, query_string):
 return a value between 0 and 1 and a Boolean

Output:
- proximity value high-> high proximity -> boolean True
- proximity value low-> low proximity -> boolean False

Proximity value is calculated:
- 98% Proximity Search
- 1% Occurrency of the words
- 1% lenght of the text

I decided to give a lot of weight to proximity because it is "less restrictive than a pure phrase match,
 but still stronger than a general purpose query" and less to the occurrency or the length of the text so repeating words
and long text don't have a high score

Proximity Search use a window or slop (n times the length of the query) to find terms of the query that are similar at
least 80% without repetition inside the window

Some parameters can be changed to tune the search.

Improvement points:
- Context Search, currently there is no distinction if a word is part of another phrase, we could use punctuation probably
- Cluster of words, continental could be an adjective or a brand, it depends from the cluster of words around and from
the Language
- We can improve the query avoiding the search of common english words like (in, at, this, and) focusing on more important words

As core modules of Python I took this list https://docs.python.org/3.7/py-modindex.html



"""

import difflib

debug = False

"""
proximity(text, query_string)
Input:
-text a string with the text to analyze
-query a string of words to find proximity within the text

Output:
- proximity value high-> high proximity -> boolean True
- proximity value low-> low proximity -> boolean False
"""
def proximity(text, query_string):
    if(query_string is "" ) or len(query_string)<2: return False,0
    #Parameters
    desired_proximity= 0.6
    desired_similarity=0.9
    proximity_weight=0.98
    occurrency_weight=0.01
    text_length_weight=0.01

    #Variables
    max_proximity = 0
    curr_proximity = 0
    window = 0
    dict_proximity={}
    dict_occurrency={}
    occurrency=0

    #Word normalization
    query_list = query_string.lower().replace(".","").replace(",","").replace("ü","u").split()
    #Text normalization
    text = text.lower().replace(".", "").replace(",", "").replace("ü", "u")

    #weight of one word depends from the query
    word_weight=1/len(query_list)

    #slop dimension depends from query
    slop=len(query_list)*3


    # Proximity Search #
    #
    # Time O(n^2 * m^2) (m=len query list, n=len text) <- O(n*m) double cycle * O(n*m) difflib.SequenceMatcher
    #
    for word in text.split():
        for q in query_list:
            #Find if query and word are at least 80% similar
            word_similarity_percentage=difflib.SequenceMatcher(None, q, word).ratio()
            if ((word_similarity_percentage>=desired_similarity )):
                #inizialize window
                if (window is 0):
                    window = slop

                #there is no repetition in the slop
                if(q not in dict_proximity):
                    curr_proximity+= word_weight * ((window)/(slop))
                dict_proximity[q]=0

                #occurrency
                if(q in  dict_occurrency):dict_occurrency[q]+=1
                else: dict_occurrency[q]=1

        #decrease window each pass
        if (window > 0):
            window -= 1

        #find max between this proximity and previously found
        max_proximity = max(curr_proximity, max_proximity)

        #close window, reset parameters
        if(window is 0):
            curr_proximity=0
            dict_proximity={}

    # Occurrency Search #
    for q in dict_occurrency:

        occurrency+=(dict_occurrency[q])*word_weight
        if(occurrency>1): occurrency=1


    # Length #
    #both the length of text and length of the query impact the proximity value
    len_text=len(query_list)/len(text.split())

    # Total Proximity #
    proximity=max_proximity*proximity_weight
    proximity+=occurrency*occurrency_weight
    proximity+= len_text*text_length_weight

    # Boolean Value #
    if proximity>=desired_proximity:
        ret=True
    else:
        ret=False


    return ret, float(proximity)


