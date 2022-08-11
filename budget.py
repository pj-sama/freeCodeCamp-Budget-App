import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=None):
        if description == None:
            self.ledger.append({"amount": amount, "description": ''})
        else:
            self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == False:
            return False
        if description == None:
            self.ledger.append({"amount": -amount, "description": ''})
        else:
            self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        budget = 0
        for i in self.ledger:
            budget += i['amount']
        return budget

    def transfer(self, amount, budget):
        if self.withdraw(amount, "Transfer to " + budget.name) == False:
            return False
        budget.deposit(amount, "Transfer from " + self.name)
        return True

    def check_funds(self, amount):
        funds = 0
        for i in self.ledger:
            funds += i['amount']
        if funds < amount:
            return False
        return True

    def __repr__(self):
        pad = math.floor((30 - len(self.name))/2)
        res = pad * '*' + self.name + pad * '*' + '\n'
        total = 0
        for i in self.ledger:
            aux = i['description'][0:23] + str("{:.2f}".format(i['amount']))
            res += i['description'][0:23] + \
                (30-len(aux)) * ' ' + str("{:.2f}".format(i['amount'])) + '\n'
            total += i['amount']
        res += 'Total: ' + str(total)
        return res

def create_spend_chart(categories):
    total = 0
    values = []
    for i in categories:
        spent = 0
        for j in i.ledger:
            if j['amount'] < 0:
                spent -= j['amount']
        values.append(round(spent, 2))
    for i in values:
        total += i
    percents = []
    for i in range(len(categories)):
        percents.append(values[i]/total)
    title = "Percentage spent by category\n"
    hundred = '100|'
    ninety = ' 90|'
    eighty = ' 80|'
    seventy = ' 70|'
    sixty = ' 60|'
    fift = ' 50|'
    four = ' 40|'
    thirty = ' 30|'
    twenty = ' 20|'
    ten = ' 10|'
    zero = '  0|'
    line = '    ' + (len(categories)*3 + 1) * '-' + '\n'
    for i in percents:
        if i == 1:
            hundred += ' o '
        else:
            hundred += '   '
        if i >= 0.9:
            ninety += ' o '
        else:
            ninety += '   '
        if i >= 0.8:
            eighty += ' o '
        else:
            eighty += '   '
        if i >= 0.7:
            seventy += ' o '
        else:
            seventy += '   '
        if i >= 0.6:
            sixty += ' o '
        else:
            sixty += '   '
        if i >= 0.5:
            fift += ' o '
        else:
            fift += '   '
        if i >= 0.4:
            fourty += ' o '
        else:
            four += '   '
        if i >= 0.3:
            thirty += ' o '
        else:
            thirty += '   '
        if i >= 0.2:
            twenty += ' o '
        else:
            twenty += '   '
        if i >= 0.1:
            ten += ' o '
        else:
            ten += '   '
        zero += ' o '
    hundred += ' \n'
    ninety += ' \n'
    eighty += ' \n'
    seventy += ' \n'
    sixty += ' \n'
    fifty += ' \n'
    four += ' \n'
    thirty += ' \n'
    twenty += ' \n'
    ten += ' \n'
    zero += ' \n'
    greatest = 0
    for i in categories:
        if len(i.name) > greatest:
            greatest = len(i.name)
    names = ''
    toWrite = []
    for i in categories:
        toWrite.append(i.name)
    for i in range(len(toWrite)):
        while len(toWrite[i]) < greatest:
            toWrite[i] += ' '
    for i in range(greatest):
        names += 4 * ' '
        for j in toWrite:
            names += ' ' + j[i] + ' '
        names += ' \n'
    names = names[:-1]
    result = title + hundred + ninety + eighty + seventy + sixty + \
        fift + four + thirty + twenty + ten + zero + line + names
    return result

