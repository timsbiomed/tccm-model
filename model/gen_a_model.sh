#if [ $# -eq 0 ]
#  then
#    echo "Module must be supplied"
#  exit 1
#fi

MODULE=valueset/valuesetdefinition
PARMS="--no-mergeimports"
gen-python $PARMS $MODULE.yaml > ../src/$MODULE.py
#if [[ $? -eq 0 ]]; then
#  gen-markdown $parms $MODULE.yaml -d ../docs/$MODULE -i
#fi
sed -i '' 's/from \.\./from src./' ../src/$MODULE.py


