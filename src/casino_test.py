from casino import word_search, doc_contains_term

# This is the first test we write, but it's the last that will pass

def test_full_flow():
    test_data = ["The Learn Python Challenge Casino.", "they bought a car", "Casinoville"]

    assert word_search(test_data, "casino") == [0]

# The basic happy path logic - these are easy matches to implement

def test_match_for_exact_match():
    assert doc_contains_term("bar", "bar") == True

def test_match_for_exact_match_within_sentence():
    assert doc_contains_term("bar", "the bar is high") == True

def test_should_not_match_if_words_are_different():
    assert doc_contains_term("bar", "food") == False

def test_ignore_space_split_matches():
    assert doc_contains_term("bar", "b a r") == False

# Adding the requirements to ignore partial words

def test_ignore_partial_word_matches():
    assert doc_contains_term("bar", "baritone") == False

# Adding case-insensitivity rule

def test_should_be_case_insensitive():
    assert doc_contains_term("casino", "CaSInO") == True

def test_search_term_should_be_case_insensitive():
    assert doc_contains_term("Casino", "CaSInO") == True

# Adding the requirement that periods and commas shouldn't matter

def test_ignore_commas_when_determining_matches():
    assert doc_contains_term("really", "but, really,") == True

def test_ignore_periods_when_determining_matches():
    assert doc_contains_term("closed", "it is closed.") == True

def test_ignore_periods_and_commas_together():
    assert doc_contains_term("closed", "it is ,,.,.closed,.") == True
