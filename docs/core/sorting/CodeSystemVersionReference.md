
# Type: CodeSystemVersionReference


A reference to a specific version of code system and, if known, the code system which it is a version of.

URI: [https://hotecosystem.org/tccm/filtersandsorting/CodeSystemVersionReference](https://hotecosystem.org/tccm/filtersandsorting/CodeSystemVersionReference)


![img](images/CodeSystemVersionReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Referenced by class


## Attributes


### Own

 * [CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)  <sub>OPT</sub>
    * range: [CodeSystemReference](CodeSystemReference.md)

### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * Description: An identifier that uniquely names the reference within the context of the particular reference type.
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞synopsis](NameAndMeaningReference_synopsis.md)  <sub>OPT</sub>
    * Description: A summary of the role and purpose of the actual reference
    * range: [String](types/String.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
