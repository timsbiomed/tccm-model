
# Type: completeValueSetReference__referenceCodeSystemVersion


A reference to a CodeSystemVersion that will be used to resolve this call. referenceCodeSy will only be used
if one or more components of the resolution of value Set identify a code system without specifying a specific
version. At most, only one version of a given code system may appear in the referenceCodeSystemVersion list.
While CTS2 service implementations must resolve resolution calls for definitions that carry unused reference
Code SystemV entries, they may choose to issue a warning at the time the definition is created or loaded.

URI: [tccm:completeValueSetReference__referenceCodeSystemVersion](https://hotecosystem.org/tccm/completeValueSetReference__referenceCodeSystemVersion)


## Domain and Range

None ->  <sub>OPT</sub> [CodeSystemVersionReference](CodeSystemVersionReference.md)

## Parents


## Children


## Used by

 * [CompleteValueSetReference](CompleteValueSetReference.md)
