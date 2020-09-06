if [ -z "$1" ]
  then
    echo "Usage: gen_model module [schema]"; exit 1
fi
PARMS="--no-mergeimports"
ALLS="__all__ = ["
MODULE=$1
IMPS="from $MODULE import ("
for filename in $MODULE/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    if [[ -z "$2" || "$2" == "$BASE" ]]; then
      echo Generating $filename
      gen-python $PARMS $MODULE/$BASE.yaml > ../src/$MODULE/$BASE.py
      if [[ $? -ne 0 ]]; then
        exit 1
      fi
#      rm -rf ../docs/$MODULE/$BASE
#      gen-markdown $PARMS $MODULE/$BASE.yaml -d ../docs/$MODULE/$BASE -i
    fi
    ALLS=$ALLS"'$BASE', "
    IMPS=$IMPS$BASE", "
done
echo $ALLS"]\n" > ../src/$MODULE/__init__.py
echo $IMPS")\n" >> ../src/$MODULE/__init__.py

if [[ "$MODULE" == "core"   &&  -z "$2" ]]
  then
    gen-jsonld-context $PARMS $MODULE/prefixes.yaml > ../includes/prefixes.context.jsonld
fi
sed -i '' 's/from \.\./from src./' ../src/$MODULE/*.py
