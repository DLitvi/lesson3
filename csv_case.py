import csv

answers = {'Привет':'И тебе привет!', 'как дела':'Лучше всех', 'Пока':'Увидимся'}
new = []
for el in answers:
	new_dict = {}
	new_dict ['Ключ'] = el
	new_dict['Значение'] = answers[el]
	new.append(new_dict)
print(new)

with open ('export.csv', 'w', encoding = 'utf-8') as file:
	keys = ['Ключ', 'Значение']
	writer = csv.DictWriter(file, keys, delimiter=';')
	writer.writeheader()
	for tandem in new:
		writer.writerow(tandem)




