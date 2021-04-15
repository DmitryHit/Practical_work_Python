import json
profit = [{}, {}]
with open("text_5_7.txt", encoding="utf-8") as txt_profit:
    lines = txt_profit.readlines()

    for line in lines:
        name, _, proceeds, expenses = line.split()
        profit[0][name] = int(proceeds) - int(expenses)

    profit[1]['average profit'] = round(
        sum(profit for _, profit in profit[0].items() if profit > 0) / len(profit[0]))

    with open("text_5_7.json", "w", encoding="utf-8") as con_json:
        json.dump(profit, con_json)

        json_mode = json.dumps(profit)
    print(f"Отображаем заработок/убыток: ", {json_mode})
