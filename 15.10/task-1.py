class Buyer:
    def __init__(self, surname, name, patronymic, address, credit_card, bank_account):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.credit_card = credit_card
        self.bank_account = bank_account

    # Методы установки значений
    def set_surname(self, surname):
        self.surname = surname

    def set_name(self, name):
        self.name = name

    def set_patronymic(self, patronymic):
        self.patronymic = patronymic

    def set_address(self, address):
        self.address = address

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

    def set_bank_account(self, bank_account):
        self.bank_account = bank_account

    def get_surname(self):
        return self.surname

    def get_name(self):
        return self.name

    def get_patronymic(self):
        return self.patronymic

    def get_address(self):
        return self.address

    def get_credit_card(self):
        return self.credit_card

    def get_bank_account(self):
        return self.bank_account

    def display_info(self):
        print(f"{self.surname} {self.name} {self.patronymic}, "
              f"Адрес: {self.address}, "
              f"Карта: {self.credit_card}, "
              f"Счёт: {self.bank_account}")


buyers = [
    Buyer("Иванов", "Иван", "Иванович", "Москва", 4000123411112222, "1234567890"),
    Buyer("Петров", "Петр", "Петрович", "Санкт-Петербург", 4000567811113333, "2234567890"),
    Buyer("Сидоров", "Сидор", "Сидорович", "Казань", 4000999911114444, "3234567890"),
    Buyer("Алексеев", "Алексей", "Алексеевич", "Новосибирск", 4000000011115555, "4234567890"),
]

print("Покупатели в алфавитном порядке:")
for b in sorted(buyers, key=lambda x: x.surname):
    b.display_info()

low = 4000500000000000
high = 4001000000000000

print(f"\nПокупатели с номером карты в диапазоне {low} - {high}:")
for b in buyers:
    if low <= b.credit_card <= high:
        b.display_info()
