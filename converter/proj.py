a = [1,2,3,4,5,1,1,1,2,3,4,4,5,6,4,5]

elem = a.index(4)
# print(elem)
# print(a.count(4))
amount = sum(1 for i in a if i == 4)
# print(amount)


wallets = {}
exchange_rate = {}
trans_log = []

def create_wallet(currency, balance):
    if currency in wallets:
        print(f'{currency} in wallet already')
    else:
        wallets[currency] = balance
        print(f'wallet {currency} has been created with {balance} units')


def set_exchange_rate(from_curr, to_curr, rate):
    exchange_rate[(from_curr, to_curr)] = rate
    print(f'from {from_curr} to {to_curr} = {rate}')


def convert(from_curr, to_curr, amount):
    if from_curr not in wallets or to_curr not in wallets:
        print('one or both wallets are not exist')
        return
    if wallets[from_curr] < amount:
        print('not enough money on your balance')
        return
    if (from_curr, to_curr)  not in exchange_rate:
        print('this transaction are not avaliable')

    rate = exchange_rate[(from_curr, to_curr)]
    converted_amount = amount * rate


    wallets[from_curr] -= amount
    wallets[to_curr] += converted_amount

    trans_log.append(f'convertation was succesfull. u transfered {from_curr} units')

    print(f'convertation was succesfull. u transfered {from_curr} units')


def show_wallets():
    print('balance: ')

    for curr, amount in wallets.items():
        print(f'{curr}: {amount}')
        print()

def show_logs():
    print('transaction story: ')

    for i in trans_log:
        print(i)
    print()


def reset_wallets():
    wallets.clear()
    trans_log.clear()
    print('all cleared')


create_wallet('USD', 765)
create_wallet('UAH', 36000)

set_exchange_rate('UAH', 'USD', .42)
set_exchange_rate('USD', 'UAH', 42)

convert('USD', 'UAH', 10)
convert('UAH', 'USD', 4200)

show_wallets()
show_logs()

reset_wallets()

show_wallets()

