import argparse
from fasta import parse_fasta


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    # parse and output the records
    for name, seq in parse_fasta(args.fasta).items():
        print(name, seq, sep='\t')
    args.fasta.close()


if __name__ == '__main__':
    main()
