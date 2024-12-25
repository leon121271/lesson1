team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
team1_name = '"Мастера кода"'
team2_name = '"Волшебники данных"'

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'



print('В команде Мастера кода участников:%d!' % team1_num)
print('Итого сегодня в командах участников:%(1)d и %(2)d!' % {'1':team1_num, '2':team2_num})
print('Команда {} решила задач: {}!'.format(team2_name, score_2))
print('{} решили задачи за {} c!'.format(team2_name, team1_time))
print(f'Команда: {team1_name} решила- {score_1} задач, а команда: {team2_name} решила- {score_2} задач')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')