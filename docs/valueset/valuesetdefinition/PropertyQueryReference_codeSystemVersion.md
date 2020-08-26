
# Type: PropertyQueryReference_codeSystemVersion


The version of the code system that makes the assertions. If present, codeSystemVersion must be a version of
codeSystem. If this attribute is present, the referenced version of the code system will always be used to
resolve the attributes or properties. If absent, the specific version of the code system to be used in
resolution is determined in the resolve value set definition call itself.

URI: [tccm:PropertyQueryReference_codeSystemVersion](https://hotecosystem.org/tccm/PropertyQueryReference_codeSystemVersion)


## Domain and Range

[PropertyQueryReference](PropertyQueryReference.md) ->  <sub>OPT</sub> [CodeSystemVersionReference](CodeSystemVersionReference.md)

## Parents

 *  is_a: [codeSystemVersion](codeSystemVersion.md)

## Children


## Used by

 * [PropertyQueryReference](PropertyQueryReference.md)
