from timberkat.timberkat import TimberKat

def test_timberkat():
    '''
    This function is recognized as a test function that will be execuited
    by pytest since the name starts with "test_". The code is executed
    and if the two values in the assert line do not match an exception
    will be raised.
    '''

    test_str = 'hello_world'

    timberifier = TimberKat()
    assert timberifier.base_text == None

    timberifier = TimberKat(test_str)
    assert timberifier.base_text == test_str

    timberified = timberifier.timberify()
    assert timberified == f"{test_str}_timber"
    assert timberifier.base_text == f"{test_str}_timber"

    timberified = timberifier.untimberify()
    assert timberified == test_str
    assert timberifier.base_text == test_str
