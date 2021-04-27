# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Gullit'
scorer_1 = 'Van Basten'

goal_0 = 32
goal_1 = 54

scorers = (f'{scorer_0} {goal_0} {scorer_1} {goal_1}')
print (scorers)

report = (f'{scorer_0} scored in the {goal_0}nd minute \n{scorer_1} scored in the {goal_1}th minute')
print(report)

player = 'Ronald Koeman'

first_name = player[0:6]
last_name = player[7:]
print (first_name + ' ' + last_name)

print (player)
print (last_name)
name_short = (first_name[0] + ' ' +last_name[0:])
print (name_short)

last_name_len = len(last_name)
print (last_name_len)

g = 3
laatste = '!'
chant = (g * (first_name + '!' + ' '))
print (chant)
n = 2
good_chant = (n * (first_name + '! ') + (first_name + laatste))
print (good_chant)

x = 10
y = 10
z = 20

print(f'x is not equal to y = {x!=y}')

flag = x != z
print(f'x is not equal to z = {flag}')

# python is strongly typed language
s = '10'
print(f'x is not equal to s = {x!=s}')