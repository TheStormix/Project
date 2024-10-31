# view.py

class View:
    @staticmethod
    def show_digit_count(digit_count_before, digit_count_after):
        print(f"Кількість цифр у файлі до змін: {digit_count_before}")
        print(f"Кількість цифр у файлі після змін: {digit_count_after}")

    @staticmethod
    def show_error(message):
        print(message)
