# controller.py
from model import TextProcessor
from view import View

class Controller:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_file(self):
        result = TextProcessor.count_digits_in_file_and_replace_odds(self.file_path)
        if result is None:
            View.show_error(f"Файл {self.file_path} не знайдено.")
        else:
            digit_count_before, digit_count_after = result
            View.show_digit_count(digit_count_before, digit_count_after)
