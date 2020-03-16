# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=-i


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: install tests build

# Build the TCCM model python library
python: tccm/model.py
docs: docs/index.md
shex: tccm.shex tccmn.shex tccm.shexj tccmn.shexj
json-schema: json-schema/tccm.json

build: python docs/index.md gen-golr-views tccm.graphql gen-graphviz java context.jsonld contextn.jsonld \
json-schema/tccm.json tccm.owl tccm.proto tccm.shex tccm.ttl

# TODO: Get this working
build_contrib: contrib_build_monarch contrib_build_translator contrib_build_go

install: env.lock



# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	pipenv install --dev
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
tccm/model.py: tccm.yaml env.lock
	pipenv run gen-py-classes $< > tmp.py && pipenv run python tmp.py &&  (pipenv run comparefiles tmp.py $@ && cp $@ $@-PREV && cp tmp.py $@); rm tmp.py


# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: tccm.yaml env.lock
	pipenv run gen-markdown --dir docs $(imgflags) $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: tccm.yaml dir-golr-views env.lock
	pipenv run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
tccm.graphql: tccm.yaml env.lock
	pipenv run gen-graphql $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: tccm.yaml dir-graphviz env.lock
	pipenv run gen-graphviz  -d graphviz $< -f gv
	pipenv run gen-graphviz  -d graphviz $< -f svg


# ~~~~~~~~~~~~~~~~~~~~
# Java
# ~~~~~~~~~~~~~~~~~~~~
java: json-schema/tccm.json dir-java env.lock
	jsonschema2pojo --source $< -T JSONSCHEMA -t java


# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: tccm.yaml env.lock
	pipenv run gen-jsonld-context $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

contextn.jsonld: tccm.yaml env.lock
	pipenv run gen-jsonld-context --metauris $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema/tccm.json: tccm.yaml dir-json-schema env.lock
	pipenv run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
tccm.owl: tccm.yaml env.lock
	pipenv run gen-owl -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
tccm.proto: tccm.yaml env.lock
	pipenv run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
tccm.ttl: tccm.yaml env.lock
	pipenv run gen-rdf -f ttl --context https://w3id.org/biolink/biolinkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
tccm.shex: tccm.yaml
	pipenv run gen-shex $< > $@
tccmn.shex: tccm.yaml
	pipenv run gen-shex --metauris $< > $@
tccm.shexj: tccm.yaml
	pipenv run gen-shex --format json $< > $@
tccmn.shexj: tccm.yaml
	pipenv run gen-shex --metauris --format json $< > $@


# ----------------------------------------
# Ontology conversion
# ----------------------------------------

# ontology/%.json: ontology/%.ttl
# 	owltools $< -o -f json $@

# ontology/%.obo: ontology/%.ttl
# 	owltools $< -o -f obo --no-check $@

# ontology/%.omn: ontology/%.ttl
# 	owltools $< -o -f omn --prefix '' http://w3id.org/biolink/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

# ontology/%.tree: ontology/%.json
# 	ogr --showdefs -t tree -r $< % > $@

# ontology/%.png: ontology/%.json
# 	ogr-tree -t png -o $@ -r $< %


# ~~~~~~~~~~~~~~~~~~~~
# Contrib
# ~~~~~~~~~~~~~~~~~~~~
contrib_build_%: contrib-dir-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/%.graphql \
contrib/%/%.owl contrib/%/schema.json contrib-java-% contrib/%/%.shex
	echo

contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml env.lock
	pipenv run gen-py-classes contrib/$*.yaml > tmp.py && (pipenv run comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

contrib/%/docs/index.md: contrib/%.yaml
	pipenv run gen-markdown --dir contrib/$*/docs $<

contrib/%/datamodel.py: contrib/%.yaml
	pipenv run gen-py-classes contrib/$*.yaml > $@

contrib-golr-%: contrib-dir-% contrib/%.yaml
	pipenv run gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	pipenv run gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	pipenv run gen-json-schema contrib/$*.yaml > $@

contrib/%/%.owl: contrib/%.yaml
	pipenv run gen-owl -o $@ contrib/$*.yaml

contrib/%/%.shex: contrib-dir-% contrib/%.yaml
	pipenv run gen-shex contrib/*.yaml > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
tests: tccm.yaml env.lock
	pipenv run python -m unittest discover -p 'test_*.py'


# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md golr-views graphql graphviz java json json-schema ontology proto rdf shex
	rm -f env.lock
	pipenv --rm

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*