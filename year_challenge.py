import random
from datetime import date, timedelta, datetime


class YearChallenge:
    def __init__(self):
        self._leap = self.__isLeap() # признак високосного года
        self._listMoney = [i for i in range(1, 366 + self._leap)]  # список сумм для перевода
        self._addedMoney = [0] * len(self._listMoney)  # список переведенных сумм
        self._needTransfer = [] # сумму требующие перевода
        self._startAmount = 0  # количество денег в копилке
        self._endAmount = sum(self._listMoney)  # количество денег в копилке по окончании годового челленджа
        self._dateTransfer = None# дата последнего перевода

    def moneyTranser(self):
        """
        Функция генеририрует рандомную сумму денег для перевода на годовой челлендж
        в зависимости от разницы дней между последним переводом и днем генерации суммы
        и возвращает список кортежей, где первый элемент кортежа индекс суммы в списке _listMoney
        а второй элемент кортежа сумма
        :return:
        """
        if self.__lastTransfer():
            print('Генерируем суммы')
            randomSums = []  # список рандомных сумм для перевода
            try:
                delta = date.today() - self._dateTransfer
                print(delta.days)
                if delta.days <= 1:  # если разница между последним днем перевода и сегодняшним днем 1 день
                    randomSum = 0  # рандомная сумна
                    while randomSum in self._addedMoney:
                        randomSum = random.choice(list(enumerate(self._listMoney)))
                    randomSums.append(randomSum)

                elif delta.days > 1:
                    count = delta.days  # количество дней пропуденных для перевода годового челлендия
                    while count != 0:
                        randomSum = 0
                        while randomSum in self._addedMoney:
                            randomSum = random.choice(list(enumerate(self._listMoney)))
                        randomSums.append(randomSum)
                        count -= 1
            except:
                randomSum = 0
                while randomSum in self._addedMoney:
                    randomSum = random.choice(list(enumerate(self._listMoney)))
                randomSums.append(randomSum)
            # return randomSums
            self._needTransfer = self._needTransfer + randomSums
        else:
            print("Вы уже сгенерировали сумму, приходите завтра или позже")

    def addMoneyTransfer(self, amountIndex):
        """
        Функция принимает на вход индекс суммы из списка сгенерированных сумм для перевода
        :param amountIndex:
        :return:
        """
        self._addedMoney[amountIndex] = self._listMoney[amountIndex]
        self._startAmount += self._listMoney[amountIndex]
        self._dateTransfer = date.today()
        print(f"add {self._listMoney[amountIndex]} rubs")

    def addListMoneyTransfer(self):
        if len(self._needTransfer) > 0:
            for sum in self._needTransfer:
                self._addedMoney[sum[0]] = self._listMoney[sum[0]]
                self._startAmount += self._listMoney[sum[0]]
                print(f"add {self._listMoney[sum[0]]} rubs")
            self._dateTransfer = date.today()
            self._needTransfer = []
        else:
            print("Нет суммы для перевода")

    def __isLeap(self):
        """
        Функция проверяет високосный год или нет и возвращает 1 или 0 соответственно
        :return:
        """
        year = datetime.today().year
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 1
        return 0

    def __lastTransfer(self):
        """
        Функция проверяет дату последнего перевода денег, чтобы юзер не спамил генерацию сумм
        :return:
        """
        if datetime.today().date() != self._dateTransfer:
            return True
        return False

if __name__ == "__main__":
    x = YearChallenge()
    print(x.__dict__)

    x.moneyTranser() #  генерируем суммы для перевода
    print(x.__dict__)

    x.addListMoneyTransfer() #  переводим сумму
    # print(x.__dict__)

    x.moneyTranser()



