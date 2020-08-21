PARMS="--no-mergeimports"
for filename in core/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    echo Generating $filename
    gen-python $PARMS core/$BASE.yaml > ../src/core/$BASE.py
    rm -rf ../docs/core/$BASE
    gen-markdown $PARMS core/$BASE.yaml -d ../docs/core/$BASE -i
done
gen-jsonld-context $PARMS core/prefixes.yaml > ../includes/prefixes.context.jsonld