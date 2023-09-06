"""
# boggle-search-python

Includes generating boards, loading existing boards, and searching for words
"""

from prefix_trie import PrefixTrie

def run():
    print('loading dictionary!')
    dictionary = PrefixTrie.from_file("words")

    print('loaded dictionary!')

    print('is_word tests')

    print(dictionary.is_word("aardvark"))
    print(dictionary.is_word("nothing"))
    print(dictionary.is_word("jsdlfjslkdjls"))
    print(dictionary.is_word("Abencerrages"))

    print('is_prefix tests')

    print(dictionary.is_prefix("A"))
    print(dictionary.is_prefix("Z"))
    print(dictionary.is_prefix("Abelian"))
    print(dictionary.is_prefix("Abel"))
    print(dictionary.is_prefix("nonsensenotaword"))



if __name__ == '__main__':
    run()