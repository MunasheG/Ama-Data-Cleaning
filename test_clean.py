import re
import pytest
from data_cleaning_project import fill_year

class TestFillYear:

    def test1(self):
        assert fill_year('1947') == '1947'

    def test2(self):
        assert fill_year('49') == '1949'

    def test3(self):
        assert fill_year('92') == '1892'

    def test4(self):
        assert fill_year('81') == '1981'

    def test5(self):
        assert fill_year('82') == '1882'

    def test6(self):
        assert fill_year('48  AD ASTR') == '1948'

    def test7(self):
        assert fill_year('unknown') is None

    def test8(self):
        assert fill_year('') is None



