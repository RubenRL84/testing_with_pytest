"""
File for the exercise of chapter 1
Outside the folder use the cmd : pytest --tb=no ch1 
[--tb] will hide the traceback of the failed tests
"""
def test_wrong_number():
    # going to fail the assert
    assert 1 in [2,3,4]

def test_wrong_letters():
    # test will pass
    assert 'a' < 'b'

def test_not_in():
    #test will pass
    assert 'fizz' in 'fizzbuzz'