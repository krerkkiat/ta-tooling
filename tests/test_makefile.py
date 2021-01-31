"""
Test Makefile.
"""
import os

import pytest
from makefile import Makefile, Target


@pytest.fixture
def sample_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Makefile")


def test_reading_parsing(sample_file_path):
    m = Makefile(sample_file_path)
    assert len(m.targets) == 8

    t = Target.from_lines(["build: clean all archive"])
    assert len(t.dependencies) == 3
    assert t.name == "build"
