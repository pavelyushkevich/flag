import argparse

def flag(n):
	if not isinstance(n, int):
		raise argparse.ArgumentTypeError(str(n) +' not integer number.')
	elif n < 0:
		raise argparse.ArgumentTypeError(str(n) + ' must be positive number.')
	elif n % 2 != 0:
		raise argparse.ArgumentTypeError(str(n) + ' is odd number')
	else:
		first_str = (n * 3) + 2
		result = '#' * first_str + '\n'

		second_str = n * 3
		clear_str = n/2

		for i in range(int(clear_str)):
			result += '#' + ' ' * second_str + '#' + '\n'

		circle = int((first_str - 4) / 2)
		result += '#' + ' ' * circle + '**' + ' ' * circle + '#' + '\n'

		for i in range(int(n/2-1)):
			tmp = int(n/2-2)
			inner_circle = 2*(i+1)
			result += '#' + ' '*(n-i+tmp) + '*' + 'o'*inner_circle + '*' + ' '*(n-i+tmp) + '#' + '\n'

		for i in range(int(n/2-1)):
			tmp = int(n/2-1)
			inner_circle = abs(2*(i-tmp))
			result += '#' + ' '*(n+i) + '*' + 'o'*inner_circle + '*' + ' '*(n+i) + '#' + '\n'

		result += '#' + ' ' * circle + '**' + ' ' * circle + '#' + '\n'

		for i in range(int(clear_str)):
			result += '#' + ' ' * second_str + '#' + '\n'

		result += '#' * first_str
		return result