"""Generate Markov text from text files."""

from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #filename = open(argv[1]).read()
    opened_file = open(file_path).read()

    combined = opened_file

    #print (combined)
    return combined


def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    lst = text_string.split()
    n = 0
    k=0
    key_list = []
    for i in range(len(lst)- n_gram):
        k = i
        while n < n_gram:
            key_list.append(lst[k])
            n += 1
            k += 1
        n = 0
        k = 0
        dict_key = tuple(key_list)
        key_list=[]
        if dict_key in chains:
            chains[dict_key].append(lst[i + n_gram])
        else:
            chains[dict_key] = [lst[i + n_gram]]

    print (chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    current_key = choice(list(chains))
    words.extend([current_key[0],current_key[1]])
    while current_key in chains:
    	chosen_word = choice(chains[current_key])
    	words.append(chosen_word)
    	current_key = (current_key[1],chosen_word)

    print (" ".join(words))

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
combined = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(combined,3)

# Produce random text
random_text = make_text(chains)

#print random_text
