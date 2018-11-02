def second_index(text: str, symbol: str):
    """
        returns the second index of symbol in a given text
    """
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(second_index("sims", "s"))
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
