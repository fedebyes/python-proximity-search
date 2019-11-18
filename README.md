# Proximity Search Algorithm in Python

## Description

In text processing, a proximity search looks for documents where two or more separately matching term occurrences are within a specified distance, where distance is the number of intermediate words or characters. In addition to proximity, some implementations may also impose a constraint on the word order, in that the order in the searched text must be identical to the order of the search query. Proximity searching goes beyond the simple matching of words by adding the constraint of proximity and is generally regarded as a form of advanced search.

For example, a search could be used to find "red brick house", and match phrases such as "red house of brick" or "house made of red brick". By limiting the proximity, these phrases can be matched while avoiding documents where the words are scattered or spread across a page or in unrelated articles in an anthology.

[source](https://en.wikipedia.org/wiki/Proximity_search_(text))


## Content

- proximity.py function implementation
- test.py unit test
- output.txt unit test sample output
- challenge.txt challenge text
