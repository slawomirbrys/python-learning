import sys
import argparse

def main(args):
    parser: ArgumentParser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--beer', '-b', type=str, required=True, help='What kind of beer do you like?')
    parser.add_argument('--count', '-c', type=int, required=True, help='How many beers do you want?')
    parsed_args = parser.parse_args(args[1:])
    
    if len(args) <= 1:
        parser.print_help()
        sys.exit(1)
    
    print(f"You like beer '{parsed_args.beer}' and you want {parsed_args.count} of them.")
    
    match parsed_args.count:
        case count if count <= 0:
            print("Wait... decide... you want 0 beers? That's not right!")
        case count if count > 10:
            print("Whoa! That's a lot of beers! Are you sure?")

if __name__ == "__main__":
    main(sys.argv)