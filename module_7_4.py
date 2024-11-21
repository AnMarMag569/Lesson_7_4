team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
challenge_result1 = 'Победа команды Мастера кода!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = '‘Ничья!'
# %s
print('В команде Мастера кода участников: %s !' % str(team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (str(team1_num), str(team2_num)))
# format
print('Команда Волшебники данных решила задач: {} !'.format(str(score_2)))
print('Волшебники данных решили задачи за {} с !'.format(str(team1_time)))
# f- строка
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result1}')

print(result)