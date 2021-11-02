from employee import Employee


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang
