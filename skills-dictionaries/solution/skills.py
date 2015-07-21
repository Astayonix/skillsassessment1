# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    d = {}
    for w in input_string.split():
        d[w] = d.get(w, 0) + 1
    return d

    # Alternate library-based answer
    #
    # from collections import Counter
    # return Counter(string1.split())


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    overlap = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                overlap.append(item1)
    return overlap


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    # Alternate, set-based answer:
    #
    # return set(list1) & set(list2)

    overlap = {}
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                overlap[item1] = item1
    return overlap.keys()


def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    # Straightforward excellent solution
    result = []
    s = set(input_list)
    for x in s:
        if x >= 0 and -x in s:
            result.append([-x, x])
    return result

    # As a comprehension
    #
    # s = set(input_list)
    # return [[-x, x] for x in s if x >=0 and -x in s]

    # Different style:
    #
    # seen = set()
    # sum_to_zero = set()
    #
    # for x in input_list:
    #     if -x in seen:
    #         # Add them in a predictable lower, higher value
    #         # (so we don't have to worry about both (-3, 3) and (3, -3)
    #         # being in the list.
    #         sum_to_zero.add((min(x, -x), max(x, -x)))
    #     else:
    #         seen.add(x)
    # return sum_to_zero


    # Set-math solution
    #
    # pos = set(input_list)
    # neg = set(-x for x in input_list if x >= 0)
    # return [(-x, x) for x in pos & neg]


    # Potentially more straightforward, double-loop version:
    #
    # found = {}
    # for x in input_list:
    #     for y in input_list:
    #         if x == -y and (y, x) not in found:
    #             found[(x, y)] = 1
    # return found.keys()


    # Or, same ideas as a set:
    #
    # found = set()
    # for x in input_list:
    #     for y in input_list:
    #         if x == -y and (y, x) not in found:
    #             found.add((x, y))
    # return list(found)


    # With an optimization to not walk the whole inner list:
    # found = set()
    # for pos, x in enumerate(input_list):
    #     for y in input_list[pos+1:]:
    #         if x == -y and (y, x) not in found:
    #             found.add((x, y))
    # return list(found)


    # Alternate functional-style answer:
    # (hold on to your seatbelts!)
    #
    # return list(set(tuple(sorted((x, y))) for x in input_list for y in input_list if x == -y))


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # Alternate, set-based answer:
    # return set(words)

    # Alternate, dict-comprehension answer:
    # return { w: 1 for w in words }.keys()

    d = {}
    for w in words:
        d[w] = 1
    return d.keys()


def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    code = {'e': 'p', 'a': 'd', 't': 'o', 'i': 'u'}
    coded_phrase = ""
    for char in phrase:
        if char in code:
            coded_phrase = coded_phrase + code[char]
        else:
            coded_phrase = coded_phrase + char
    return coded_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    d = {}
    for w in words:
        d.setdefault(len(w), []).append(w)
    return sorted(d.items())

    # Alternate, library-based answer:
    #
    # from collections import defaultdict
    # d = defaultdict(list)
    # for w in words:
    #     d[len(w)].append(w)
    # return sorted(d.items())


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    en_to_pirate = {
        'student': 'swabbie',
        'my': 'me',
        'is': 'be',
        'man': 'matey',
        'sir':  'matey',
        'hotel': 'fleabag inn',
        'boy': 'matey',
        'madam': 'proud beauty',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'lawyer': 'foul blaggart',
        'the': 'th',
        'restroom': 'head',
        'hello': 'avast',
    }

    return " ".join([en_to_pirate.get(w, w) for w in phrase.split()])


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    tallies = {}
    for letter in input_string:
        if letter == ' ':
            continue
        tallies[letter] = tallies.get(letter, 0) + 1

    tallies_reversed = {}
    for key, val in tallies.iteritems():
        tallies_reversed.setdefault(val, []).append(key)

    return sorted(tallies_reversed[max(tallies_reversed.keys())])

def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # Alternate, pre-sort method
    #
    # d = {}
    # for w in words:
    #   d.setdefault(len(w), []).append(w)
    # for v in d.values():
    #   v.sort()
    # return sorted(d.items())

    d = {}
    for w in words:
        d.setdefault(len(w), []).append(w)
    out = []
    for k, v in sorted(d.items()):
        out.append((k, sorted(v)))
    return out


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
