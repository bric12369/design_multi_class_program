class Diary:
    def __init__(self):
        self.diary_entries = []

    def add_entry(self, diary_entry):
        self.diary_entries.append(diary_entry)

    def list_entries(self):
        return self.diary_entries
    
    def select_best_entry_for_time(self, wpm, mins):
        words_to_read = wpm * mins
        closest_word_count = 0
        closest_entry = {}
        for entry in self.diary_entries:
            length = len(entry.entry.split())
            if length > closest_word_count and length <= words_to_read:
                closest_word_count = length
                closest_entry = entry
        return closest_entry if closest_word_count else "You don't currently have enough time to start and finish any of your diary entries."
    
    def list_all_mobile_numbers(self):
        mobile_nums_3d_list = [entry.extract_mobile_numbers() for entry in self.diary_entries]
        mobile_nums = sum(mobile_nums_3d_list, [])
        return mobile_nums if len(mobile_nums) else 'No mobile numbers found.'
