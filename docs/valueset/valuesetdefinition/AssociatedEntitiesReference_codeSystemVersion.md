
# Type: AssociatedEntitiesReference_codeSystemVersion


The version of the code system that makes the association assertions. If present, codeSystemVersion must be
a version of codeSystem. If this attribute is present, the referenced version of the code system will always
be used to resolve the associations. If absent, the specific version of the code system to be used in
resolution is determined in the resolve value set definition call itself.

URI: [tccm:AssociatedEntitiesReference_codeSystemVersion](https://hotecosystem.org/tccm/AssociatedEntitiesReference_codeSystemVersion)


## Domain and Range

[AssociatedEntitiesReference](AssociatedEntitiesReference.md) ->  <sub>OPT</sub> [CodeSystemVersionReference](CodeSystemVersionReference.md)

## Parents

 *  is_a: [codeSystemVersion](codeSystemVersion.md)

## Children


## Used by

 * [AssociatedEntitiesReference](AssociatedEntitiesReference.md)
