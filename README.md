# basic-text-preprocessing <img src="images/mop-logo.png" alt="Logo" align="right"  width="150" height="150">

<p align="left">
    Library to perform a basic text preprocessing on a corpus of documents.
    <br />
    <a href="https://github.com/tonifuc3m/basic-text-preprocessing"><strong>Explore the docs »</strong></a>
</p>

## Usage

Execute in a Unix terminal:

```
chmod 775 clean-artifacts.sh

./clean-artifacts.sh -a IN_PATH -b OUT_PATH 
```

Processed files are stored in OUT_PATH


## Steps

 - Step 1/5: Force unix text files. Mostly, for newline characters.
 
 - Step 2/5: Remove common artifacts. Use GitHub repo developed by [Aitor](https://github.com/gonzalez-agirre) to fix common encoding errors.
 
 - Step 3/5: Remove common HTML errors. Substitute HTML characters that are usually missed when transforming HTML to plain text.
 
 - Step 4/5: Quick substitution of common errors (substitute other common patterns that may cause errors when using plain text). As well, replace all whitespaces by \n or ' ' and force NFKC Unicode normalization.
 
 - Step 5/5: Check if there are lines starting with lowercase. We need to manually go to those files and check if those newlines are parsing/conversion mistakes.
 
## Additional step

This repo provides as well a script to detect near-duplicated documents in the corpus. Its usage is:

```
python find_duplicates.py --datapath CORPUS_PATH
```

It prints in terminal the list of duplicated files.


<p align="center">
    <a href="https://github.com/tonifuc3m/basic-text-preprocessing/issues">Report Bug</a>
    ·
    <a href="https://github.com/tonifuc3m/basic-text-preprocessing/issues">Request Feature</a>
</p>


<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
