from scipy.special import digamma
import argparse

def e_log(a, b):
	return digamma(a) - digamma(a+b)

def main(args):
	alpha_prime = args.y + args.y_prime + 1
	beta_prime = args.N - args.y - args.y_prime + args.x * args.ws + 1
	alpha = args.y + 1
	beta = args.N - args.y + 1

	print(f"Sigma is Beta({alpha_prime}, {beta_prime}) distributed")
	print(f"Lambda is Beta({alpha}, {beta}) distributed")

	mutual_information = e_log(alpha_prime, beta_prime) - e_log(alpha, beta)
	print(f"The expected mutual_information is {mutual_information}")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--N', type=int, default=50000000)
	parser.add_argument('--x', type=int, default=50)
	parser.add_argument('--y', type=int, default=75)
	parser.add_argument('--y_prime', type=int, default=1)
	parser.add_argument('--ws', type=int, default=8)
	args = parser.parse_args()
	main(args)