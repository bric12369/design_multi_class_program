from lib.diary import *
from lib.diary_entry import *

def test_add_entry():
    entry_1 = DiaryEntry('Entry 1')
    my_diary = Diary()
    my_diary.add_entry(entry_1)
    assert my_diary.diary_entries == [entry_1]

    entry_2 = DiaryEntry('Entry 2')
    entry_3 = DiaryEntry('Entry 3')
    my_diary.add_entry(entry_2)
    my_diary.add_entry(entry_3)
    assert my_diary.diary_entries == [entry_1, entry_2, entry_3]

def test_list_entries():
    my_diary = Diary()
    assert my_diary.list_entries() == []
    entry_1 = DiaryEntry('Entry 1')
    entry_2 = DiaryEntry('Entry 2')
    entry_3 = DiaryEntry('Entry 3')
    my_diary.add_entry(entry_1)
    my_diary.add_entry(entry_2)
    my_diary.add_entry(entry_3)
    assert my_diary.list_entries() == [entry_1, entry_2, entry_3]

def test_select_best_entry_for_time_simple():
    entry_1 = DiaryEntry('One two three four five')
    entry_2 = DiaryEntry('One two three four five six seven eight nine ten')
    my_diary = Diary()
    my_diary.add_entry(entry_1)
    my_diary.add_entry(entry_2)
    assert my_diary.select_best_entry_for_time(5, 1) == entry_1  

def test_select_best_entry_for_time_complex():
    content = 'content '
    entry_400_words = DiaryEntry(content * 400)
    entry_500_words = DiaryEntry(content * 500)
    entry_999_words = DiaryEntry(content * 999)
    entry_1050_words = DiaryEntry(content * 1050)
    my_diary = Diary()
    my_diary.add_entry(entry_400_words)
    my_diary.add_entry(entry_500_words)
    my_diary.add_entry(entry_999_words)
    my_diary.add_entry(entry_1050_words)
    assert my_diary.select_best_entry_for_time(110, 4) == entry_400_words
    assert my_diary.select_best_entry_for_time(200, 5) == entry_999_words
    assert my_diary.select_best_entry_for_time(360, 3) == entry_1050_words

def test_best_entry_feedback_for_not_enough_time():
    content = 'content '
    entry_201_words = DiaryEntry(content * 201)
    entry_205_words = DiaryEntry(content * 205)
    my_diary = Diary()
    my_diary.add_entry(entry_201_words)
    my_diary.add_entry(entry_205_words)
    assert my_diary.select_best_entry_for_time(100, 2) == "You don't currently have enough time to start and finish any of your diary entries."

def test_list_all_mobile_numbers_simple():
    entry_1 = DiaryEntry('This is a mobile number: 07123456789')
    my_diary = Diary()
    my_diary.add_entry(entry_1)
    assert my_diary.list_all_mobile_numbers() == ['07123456789']

def test_list_all_mobile_numbers_complex():
    entry_1 = DiaryEntry('This is a mobile number: 07123456789')
    entry_2 = DiaryEntry('This is a mobile number: 07123556789 and so is this: 07985746352')
    entry_3 = DiaryEntry('Another mobile number here: 07493826506')
    my_diary = Diary()
    my_diary.add_entry(entry_1)  
    my_diary.add_entry(entry_2)  
    my_diary.add_entry(entry_3)  
    assert my_diary.list_all_mobile_numbers() == ['07123456789', '07123556789', '07985746352', '07493826506']

def test_feedback_if_no_mobile_numbers_found():
    entry_1 = DiaryEntry('No mobile numbers here...')
    my_diary = Diary()
    my_diary.add_entry(entry_1)
    assert my_diary.list_all_mobile_numbers() == 'No mobile numbers found.'