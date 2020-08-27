PARMS="--no-mergeimports"
ALLS="__all__ = ["
IMPS="from core import ("
for filename in core/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    echo Generating $filename
    gen-python $PARMS core/$BASE.yaml > ../src/core/$BASE.py
    ALLS=$ALLS"'$BASE', "
    IMPS=$IMPS$BASE", "
    # rm -rf ../docs/core/$BASE
    # gen-markdown $PARMS core/$BASE.yaml -d ../docs/core/$BASE -i
done
echo $ALLS"]\n" > ../src/core/__init__.py
echo $IMPS")\n" >> ../src/core/__init__.py
# gen-jsonld-context $PARMS core/prefixes.yaml > ../includes/prefixes.context.jsonld
sed -i '' 's/from \.\./from src./' ../src/core/*.py
