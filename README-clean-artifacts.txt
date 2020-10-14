# Steps
 - Step 1/5: Force unix text files. Mostly, for newline characters.
 - Step 2/5: Remove common artifacts. Use GitHub developed by Aitor to fix common encoding errors.
 - Step 3/5: Remove common HTML errors. Substitute HTML characters that are usually missed when transforming HTML to plain text
 - Step 4/5: Quick substitution of common errors. Substitute other common patterns that may cause errors when using plain text.
 - Step 5/5: Check if there are lines starting with lowercase. We need to manually go to those files and check if those newlines are parsing/conversion mistakes.

# Usage
First, open clean-artifacts.sh and substitute OURPATH='' by the path to the folder with the text files
Then, execute in a command-line terminal:

chmod 775 clean-artifacts.sh
./clean-artifacts.sh

Processed files are stored in a folder named with -output in the parent directory of $OURPATH
