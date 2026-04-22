import re
import pytest
from data_cleaning_project import fill_year, df
import pandas as pd


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

# test dataframe

class Test_Df:

    def test_105(self):
        assert df.loc['105', "Exit_Year"] == 1948

    def test_8620(self):
        assert df.loc['8620', "Exit_Year"] == 1981
class Test_DOB:
    
     def test_28_Aug_30(self):
         assert df.loc['2881', "Birth_Year"] == 1930

     def test_1928(self):
         assert df.loc['10268', "Birth_Year"] is None

     def test_na(self):
         assert df.loc['105', "Birth_Year"] is None

     def test_died(self):
         assert df.loc['12543', "Birth_Year"] is None        

     def test_born(self):
         assert df.loc['5769', "Birth_Year"] == 1873

