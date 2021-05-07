# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = (f'{scorer_0} {goal_0}, {scorer_1} {goal_1}')
print (scorers)

report = (f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute')
print(report)

player = 'Ronald Koeman'

first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]
print (first_name + ' ' + last_name)

name_short = (first_name[0] + '. ' +last_name[0:])
print (name_short)

first_name_len = len(first_name)
last_name_len = len(last_name)

# feedback eerste keer inleveren https://vimeo.com/546016577/437f33849f
# print (first_name_len)
# print (last_name_len)

g = (first_name_len - 1)
chant = (g * (first_name + '! ') + (first_name + '!'))
print (chant)
n = (first_name_len - 1)
good_chant1 = (n * (first_name + '! ') + (first_name + '!'))
print (good_chant1)

first_name1 = (first_name + '! ')
# print (first_name1)
m = (first_name_len -1)
good_chant_start = (m * (first_name + '! '))
good_chant_end = first_name1[:-1]
# print (good_chant_end)
good_chant = (good_chant_start) + (good_chant_end)
print (good_chant)