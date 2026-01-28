from lib.diary_entry import *

def test_sets_entry_on_initialisation():
    entry_1 = DiaryEntry('This is entry 1')
    assert entry_1.entry == 'This is entry 1'

def test_extracts_single_mobile_number_simple():
    entry_1 = DiaryEntry('07123456789')
    assert entry_1.extract_mobile_numbers() == ['07123456789']

def test_extracts_single_mobile_number_complex():
    entry_1 = DiaryEntry('Only extract this number: 07123456789')
    assert entry_1.extract_mobile_numbers() == ['07123456789']

def test_extracts_multiple_mobile_numbers():
    entry_1 = DiaryEntry('Extract this number: 07123456789; and this one: 07987654321; and this one: 07981254764')
    assert entry_1.extract_mobile_numbers() == ['07123456789', '07987654321', '07981254764']