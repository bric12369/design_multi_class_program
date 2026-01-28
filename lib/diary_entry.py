import re

class DiaryEntry:
    def __init__(self, entry):
        self.entry = entry

    def extract_mobile_numbers(self):
        mobile_numbers = re.findall(r'07\d{9}', self.entry)
        return mobile_numbers