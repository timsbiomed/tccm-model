#if [ $# -eq 0 ]
#  then
#    echo "Module must be supplied"
#  exit 1
#fi

PARMS="--no-mergeimports"
gen-python $PARMS valueset/valuesetdefinition.yaml > ../src/valueset/valuesetdefinition.py
if [[ $? -eq 0 ]]; then
  gen-markdown $parms valueset/valuesetdefinition.yaml -d ../docs/valueset/valuesetdefinition -i
fi
