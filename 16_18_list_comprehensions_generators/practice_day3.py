NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites',
         'bob belderbos', 'julian sequeira', 'al pacino', 'brad pitt',
         'matt damon', 'brad pitt']

bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}

exclude_bites = (6, 10, 16, 18, 21)


def dedup_and_title_case_names(names):
    """
    Should return a list of names, each name appears only once.
    """
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """
    Returns name list sorted desc by surname.
    """
    names = dedup_and_title_case_names(names)
    names = sorted(names,
                   key=lambda x: x.split()[-1],
                   reverse=True)
    return names


def shortest_first_name(names):
    """
    Returns the shortest first name (str).
    """
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=str)


names = shortest_first_name(NAMES)
print(names)


def filter_bites(bites=bites, bites_done=exclude_bites):
    """
    return the bites dict with the exclude_bites filtered out.
    """
    return {key: value for key, value in bites.items()
            if key not in exclude_bites}
