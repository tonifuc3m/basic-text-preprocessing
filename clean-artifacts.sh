#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterA -b parameterB"
   echo -e "\t-a Absolute route to input data directory."
   echo -e "\t-b Absolute route to output data directory"
   exit 1 # Exit script after printing help
}

while getopts "a:b:c:" opt
do
   case "$opt" in
      a ) IN_DIR="$OPTARG" ;;
      b ) OUT_DIR="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$IN_DIR" ] || [ -z "$OUT_DIR" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

echo "$IN_DIR"
echo "$OUT_DIR"

# Build INI_DIR if it does not exist
echo "mkdir -p $OUT_DIR"
mkdir -p $OUT_DIR

printf "\n\nCreate a copy of directory\n"
echo "cp -r ${IN_DIR} ${OUT_DIR}"
cp -r $IN_DIR $OUT_DIR
echo "------------------------------------------------"

## dos2unix 
printf "\n\nStep 1/5: Force unix newline characters\n"
ALLFILES="${OUT_DIR}/*"
echo "dos2unix ${ALLFILES}"
dos2unix $ALLFILES
echo "------------------------------------------------"

## Remove artifacts
printf "\n\nStep 2/5: Remove common artifacts\n"
if [ ! -d "utils/FixEncodingErrors" ]
then
	echo "git clone https://github.com/PlanTL-SANIDAD/utils.git"
	git clone https://github.com/PlanTL-SANIDAD/utils.git
fi
echo "chmod 775 utils/FixEncodingErrors/FixEncodingErrors.pl
perl utils/FixEncodingErrors/FixEncodingErrors.pl --dir ${OUT_DIR}"
chmod 775 utils/FixEncodingErrors/FixEncodingErrors.pl
perl utils/FixEncodingErrors/FixEncodingErrors.pl --dir $OUT_DIR
echo "------------------------------------------------"

## Remove HTML errors 
printf "\n\nStep 3/5: Remove common HTML errors\n"
echo "find ${OUT_DIR} -name '*txt' -exec sed -i 's/&mu;/µ/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&rsquo;/'\''/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&ge;/≥/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&le;/≤/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&beta;/β/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&alpha;/α/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&mdash;/-/g' {} \;"
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&mu;/µ/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&rsquo;/'\''/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&ge;/≥/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&le;/≤/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&beta;/β/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&alpha;/α/g' {} \;
find ${OUT_DIR} -name '*txt' -exec sed -i 's/&mdash;/-/g' {} \;
echo "------------------------------------------------"

## Extra: quick-prepro.py
printf "\n\nStep 4/5: Quick substitution of common errors\n"
echo "python quick-prepro.py -d ${OUT_DIR}"
python quick-prepro.py -d $OUT_DIR
echo "------------------------------------------------"

## Find lines to manually check
printf "\n\nStep 5/5: Check if there are lines starting with lowercase. I need to manually go to those files and correct them if newlines are wrongly added\n"
echo "python check-newlines.py -d ${OUT_DIR}"
python check-newlines.py -d $OUT_DIR
echo "------------------------------------------------"

printf "\n\nFinished!\n"

