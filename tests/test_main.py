#!/usr/bin/env python
# -*- coding: utf-8 -*-
from quantTradingAlgorithm.main import SimpleCalculator

from quantTradingAlgorithm.main import ClassifyBar
from quantTradingAlgorithm.main import RetrieveData
from quantTradingAlgorithm.main import FormatData
from quantTradingAlgorithm.main import ConsolidateBar

################################
# Unit Tests (ClassifyBar)
################################

def test_bar_is_green():
    bar = ClassifyBar()
    result = bar.polarity(4,5)
    assert result == True

def test_bar_is_wide_range():
    # definition of wide range based on large difference between open/close, relative to surrounding bars
    # technical definition TBD
    assert result == True

def test_bar_has_bottoming_tail():
    # check for bottoming tail 
    assert result == True

def test_bar_has_topping_tail():
    # check for topping tail 
    assert result == True

def test_bar_is_doji():
    # definition of doji, neither bullish or bearish, based on open and close being virtually the same,
    # technical definition TBD 
    assert result == True

def test_bar_has_volume_spike():
    bar = ClassifyBar()
    result = bar.volumeCompare(prevBar, currentBar)    
    assert result == True

def test_bar_is_igniting_move():
    # check for volume spike, wide range, and breaking through pivot (support/resistance) 
    assert result == True

def test_bar_is_ending_move():
    # check for volume spike, wide range, and failing at pivot (support/resistance)
    assert result == True

################################
# Unit Tests (RetrieveData)
################################

def test_input_start_date_is_valid():
    assert result == True

def test_input_end_date_is_valid():
    assert result == True

def test_read_data_from_yahoo():
    assert result == []

def test_output_to_csv():
    assert result == []

################################
# Unit Tests (FormatData)
################################

def test_map_dates():
    assert result == True

def test_drop_missing_values():
    assert result == True

def test_reset_index():
    assert result == True


################################
# Unit Tests (ConsolidateBar)
################################

def test_resample_bar_data():
    assert result == True

def test_oversample_bar_data():
    assert result == True

def test_combine_two_bars():
    assert result == True

################################
# Unit Tests (ClassifyTrend)
################################
################################
# Unit Tests (ClassifyMovingAverage)
################################
################################
# Unit Tests (ClassifyBullish)
################################
################################
# Unit Tests (ClassifyBearish)
################################
################################
# Unit Tests (ClassifyRetracement)
################################
################################
# Unit Tests (ClassifyMove)
################################
################################
# Unit Tests (FindGap)
################################
################################
# Unit Tests (FindResistance)
################################
################################
# Unit Tests (FindSupport)
################################
################################
# Unit Tests (DefinePattern)
################################
################################
# Unit Tests (FindPattern)
################################
################################
# Unit Tests (ClassifyBullish)
################################
################################

# Simple Calculator Tests (for reference to better understand TDD/BDD)

def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9

def test_subtract_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.subtract(4, 5)
    assert result == -1

def test_add_three_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5, 6)
    assert result == 15
   
def test_add_many_numbers():
    calculator = SimpleCalculator()
    numbers = range(100)
    
    result = calculator.add(*numbers)
    assert result == 4950

