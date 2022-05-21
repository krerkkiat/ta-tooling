"""
Test the bbutils package.
"""
from bbutils import BbAPI


def test_parse_url_for_course_id():
    url = "https://blackboard.ohio.edu/ultra/courses/_067238_1/cl/outline"
    assert BbAPI.parse_url_for_course_id(url) == "_067238_1"

    url = "https://blackboard.ohio.edu/ultra/courses/_067238_1"
    assert BbAPI.parse_url_for_course_id(url) == "_067238_1"

    url = "https://blackboard.ohio.edu/"
    assert BbAPI.parse_url_for_course_id(url) is None

    # Detecting if the string passing to the function
    # is a url or not is not included.
    url = "_067238_1"
    assert BbAPI.parse_url_for_course_id(url) is None

    # The function does not check if the "url" is a valid one or not.
    url = "httpcs:/courses/_067238_1"
    assert BbAPI.parse_url_for_course_id(url) == "_067238_1"
