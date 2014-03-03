def get_price(ID):
    ID = str(ID) + '.TW'
    start_date = date(2011,1,1)
    current_date = date(2014,1,1)
    return ystockquote.get_historical_prices(ID, start_date.isoformat(), current_date.isoformat())



ID = 1307
price = get_price(ID)
info = stockinfo(ID)
keys = list(price.keys())
keys.sort()
print(keys[0])
print(price[keys[0]]['Close'])
x = float(price[keys[0]]['Close'])
x = float(35.3)
print(keys[-1])
print(price[keys[-1]]['Close'])
y = float(price[keys[-1]]['Close'])
y = float(31)
print(info.data['2013'])

m = {}
n = {}

for index, element in enumerate(['2011','2012','2013']):
    m[index+1] = float(info.data[element]['現金股利：合計'])
    n[index+1] = float(info.data[element]['股票股利：合計'])

print(m)
print(n)

result = ((y * (1 + n[1]/10) * (1 + n[2]/10) * (1 + n[3]/10)) + (m[1] + m[2] * (1 + n[1]/10) + m[3] * (1 + n[1]/10) * (1 + n[2]/10))) / x
print(result)
