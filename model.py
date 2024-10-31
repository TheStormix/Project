# model.py
import random
import string

class TextProcessor:
    @staticmethod
    def replace_odd_digits_with_random_letter(text):
        result = []
        for c in text:
            if c.isdigit() and int(c) % 2 != 0:
                random_letter = random.choice(string.ascii_letters)
                result.append(random_letter)
            else:
                result.append(c)
        return ''.join(result)

    @staticmethod
    def count_digits(text):
        return sum(c.isdigit() for c in text)

    @staticmethod
    def count_digits_in_file_and_replace_odds(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            digit_count_before = TextProcessor.count_digits(text)
            modified_text = TextProcessor.replace_odd_digits_with_random_letter(text)
            digit_count_after = TextProcessor.count_digits(modified_text)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_text)
            
            return digit_count_before, digit_count_after
        except FileNotFoundError:
            return None
