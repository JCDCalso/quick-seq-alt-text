import argparse

def create_alt_text(seq: str, indel_rep: str) -> str:
    alt_text: str = ""
    for i, char in enumerate(seq):
        if char == '-':
            new_char = indel_rep
        else: new_char = f"\"{char.upper()}\""

        if i > 0:
            alt_text += "-"
        alt_text += new_char

    return alt_text

def create_latex_text(seq: str, indel_rep: str) -> str:
    alt_text: str = ""
    for i, char in enumerate(seq):
        if char == '-':
            new_char = indel_rep
        else: new_char = f"`{char.upper()}\'"

        if i > 0:
            alt_text += "-"
        alt_text += new_char

    return alt_text


if __name__ == "__main__":
	# Create the argument parser
    parser = argparse.ArgumentParser(\
    	description="Transforms a given sequence by replacing \
    	'-' with 'dash' and quoting other characters.")

    # Add an argument for the sequence
    parser.add_argument('seq', type=str, \
    	help='The sequence of characters to transform.')

    # OPTIONAL: argument for representation of indels. Default is 'dash'
    parser.add_argument('-ir', '--indel_replacement', type=str, default='dash', \
        help='The word to use as a replacement for "-". Default is "dash".')

    # OPTIONAL: will replace " around letters with `` and '' for proper formatting in latex
    parser.add_argument('-lq', '--latex_quotes', action='store_true', \
        help='Replace " around letters with `` and \'\' for proper formatting in LaTeX. Defaults to False.')

    # Parse the arguments
    args = parser.parse_args()

    # Now use the 'seq' argument value from args, choosing formatting based on latex input:
    if args.latex_quotes:
        print(create_latex_text(args.seq, args.indel_replacement))
    else:
        print(create_alt_text(args.seq, args.indel_replacement))
