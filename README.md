# quick-seq-alt-text
Short code snippet written to easily make better alt text for DNA and RNA sequences. Very simple code. 

## Requirements
- Python obvi
- Python should be added to your path so you can run it from the command line

## Use:
Run from terminal like: `python quick-seq-alt-text.py [SEQUENCE]'

[SEQUENCE] is the string representing an RNA or DNA sequence. Output will be the same sequence with quotes around each character and dashes in between. This forces screen readers to read out each letter. [More info on why.](https://github.com/JCDCalso/accessible-tex-skeletonizer/wiki/How-to-write-Alt-Text-for-DNA-and-RNA-Sequences)

### Example:

Input: `python quick-seq-alt-text.py ATGATT`

Output: 
```
"A"-"T"-"G"-"A"-"T"-"T"

```

If your input has hyphens, often used to represent gaps, indels, etc, then the word "dash" will be subbed in. Again this forces screen readers to read out that there was a dash.

### Example:

Input: `python quick-seq-alt-text.py ATGA-T`

Output: 
```
"A"-"T"-"G"-"A"-dash-"T"

```

### Options:

#### Indel replacement word:

`ir` [string] / `--indel_replacement='[string]

Instead of outputting "dash" you can use a word that is more closely aligned with the language used in context to describe indels.

##### Examples:

Input `python quick_seq_alt_text.py ATGA-T -ir gap`
Input `python quick_seq_alt_text.py ATGA-T --indel_replacement=gap`

Output 
```
"A"-"T"-"G"-"A"-gap-"T"

```

If you want to have a space within your output (I don't think it's a good idea but if you want it) wrap your string in quotes:

Input `python quick_seq_alt_text.py ATGA-T -ir "deletion error"`

Output 
```
"A"-"T"-"G"-"A"-deletion error-"T"

```

#### LaTeX Quotes:

'-lq' or '--latex_quotes'

Base LaTeX wants quotes `like this' (backtick, like this, apostrophe). Useful if you're writing [accompanying accessibility documents](https://github.com/JCDCalso/accessible-tex-skeletonizer/wiki/About#structure-of-the-accompanying-document)

##### Examples:

Input `

Output 
```
`A'-`T'-`G'-`A'-`T'-`T'

```
