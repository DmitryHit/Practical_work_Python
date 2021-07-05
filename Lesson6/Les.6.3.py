class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


if __name__ == '__main__':
    position_data = (
        {
            'name': 'Иван',
            'surname': 'Иванов',
            'position': 'Менеджер.',
            'wage':  25000,
            'bonus': 30579
        },
        {
            'name': 'Петр',
            'surname': 'Петров',
            'position': 'Старший Инженер.',
            'wage':  70000,
            'bonus': 30000
        },
        {
            'name': 'Семён',
            'surname': 'Сидоров',
            'position': 'Начальник отдела контроля качества.',
            'wage':  80000,
            'bonus': 0
        },
        {
            'name': 'Изолай',
            'surname': 'Хариметинов',
            'position': 'Клининг менеджер.',
            'wage': 25000,
            'bonus': 3500
        }
    )

    for item in position_data:
        position = Position(**item)

        print('Полное имя: ', position.get_full_name())
        print('Занимаемая должность: ', position.position)
        print('Общий доход с учётом премии: ', position.get_total_income())
        print('\n')
