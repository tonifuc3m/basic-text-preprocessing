OURPATH='/home/antonio/Documents/Projects/covid-19/cc/CORPUS-ES-200'
APPENDIX='-output'
NEWPATH="${OURPATH}${APPENDIX}"
printf "\n\nCreate a copy of directory\n"
echo "cp -r ${OURPATH} ${NEWPATH}"
cp -r $OURPATH $NEWPATH
echo "------------------------------------------------"

## dos2unix 
printf "\n\nStep 1/5: Force unix newline characters\n"
ALLFILES="${NEWPATH}/*"
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
perl utils/FixEncodingErrors/FixEncodingErrors.pl --dir ${NEWPATH}"
chmod 775 utils/FixEncodingErrors/FixEncodingErrors.pl
perl utils/FixEncodingErrors/FixEncodingErrors.pl --dir $NEWPATH
echo "------------------------------------------------"

## Remove HTML errors 
printf "\n\nStep 3/5: Remove common HTML errors\n"
ALLTXT="${NEWPATH}/*.txt"
echo "sed -i 's/&mu;/µ/g' ${ALLTXT}
sed -i 's/&rsquo;/'\''/g' ${ALLTXT}
sed -i 's/&ge;/≥/g' ${ALLTXT}
sed -i 's/&le;/≤/g' ${ALLTXT}
sed -i 's/&beta;/β/g' ${ALLTXT}
sed -i 's/&alpha;/α/g' ${ALLTXT}
sed -i 's/&mdash;/-/g' ${ALLTXT}"
sed -i 's/&mu;/µ/g' $ALLTXT
sed -i 's/&rsquo;/'\''/g' $ALLTXT
sed -i 's/&ge;/≥/g' $ALLTXT
sed -i 's/&le;/≤/g' $ALLTXT
sed -i 's/&beta;/β/g' $ALLTXT
sed -i 's/&alpha;/α/g' $ALLTXT
sed -i 's/&mdash;/-/g' $ALLTXT
echo "------------------------------------------------"

## Extra: quick-prepro.py
printf "\n\nStep 4/5: Quick substitution of common errors\n"
echo "python quick-prepro.py -d ${NEWPATH}"
python quick-prepro.py -d $NEWPATH
echo "------------------------------------------------"

## Find lines to manually check
printf "\n\nStep 5/5: Check if there are lines starting with lowercase. I need to manually go to those files and correct them if newlines are wrongly added\n"
echo "python check-newlines.py -d ${NEWPATH}"
python check-newlines.py -d $NEWPATH
echo "------------------------------------------------"

printf "\n\nFinished!\n"

