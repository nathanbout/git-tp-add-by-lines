from argparse import ArgumentParser
from fibonacci import fibo_cached
from fibonacci import fibo

parser = ArgumentParser(description="permet de renvoyer les resultats de la suite de fibonacci")
parser.add_argument('n', type = int, help = 'entier en argument de la suite')
parser.add_argument('--cached', '-c', action='store_true', help="definit si la version ameliorée 'cached' est utilisée")
args = parser.parse_args()

if args.cached :
    print(f"fibo_cached({args.n}) = {fibo_cached(args.n)}")
else :
    print(f"fibo({args.n}) = {fibo_cached(args.n)}")