class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def __str__(self):
        star_count = (30 - len(self.name)) // 2
        display = star_count * '*' + self.name + star_count * '*' + '\n'
        for i in self.ledger:
            line = i['description'][:min(len(i['description']),23)]
            line = line + ' '*(23-len(line))
            amount = f"{float(i['amount']):.2f}"
            if len(amount)  >= 7:
                line += amount[-7:]
            else:
                line += (7 - len(amount)) * ' ' + amount
            display += line + '\n'
        display += f"Total: {self.get_balance()}"
        return display
            
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -1*amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([i['amount'] for i in self.ledger])

    def transfer(self,amount,transfer_to):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {transfer_to.name}')
            transfer_to.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    bar_chart = 'Percentage spent by category\n'
    percaentage_by_category = []

    for category in categories:
        percaentage_by_category.append({'name':category.name, 'withdraw': sum([i['amount'] for i in category.ledger if i['amount'] < 0])})

    withdraws = sum([i['withdraw'] for i in percaentage_by_category])

    for per in percaentage_by_category:
        per['percentage'] = per['withdraw'] * 100 // withdraws
    for i in range(100,-1,-10):
        bar_chart += (3-len(str(i))) * ' ' + str(i) + '| '
        for category in percaentage_by_category:
            if category['percentage'] >= i :
                bar_chart += 'o  '
            else:
                bar_chart += '   '
        bar_chart += '\n'
    bar_chart += ' '*4 + '-'*3*len(percaentage_by_category) + '-'
    for i in range(max([len(cat['name']) for cat in percaentage_by_category])):
        bar_chart += '\n     '
        for category in percaentage_by_category:
            if len(category['name']) > i:
                bar_chart += category['name'][i] + ' '*2
            else: 
                bar_chart += ' '*3

    return bar_chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(30)
print(clothing)
print(create_spend_chart([food, clothing]))
