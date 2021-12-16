import typing


def parse_fasta(f: typing.TextIO) -> dict[str, str]:
    res: dict[str, str] = {}
    for recs in f.read().split('>')[1:]:
        header, *seqs = recs.split('\n')
        res[header.strip()] = "".join(seqs)
    return res
