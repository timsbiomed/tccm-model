
# Type: MatchAlgorithmReference


A reference to an algorithm used for selecting and filtering data.

URI: [https://hotecosystem.org/tccm/filtersandsorting/MatchAlgorithmReference](https://hotecosystem.org/tccm/filtersandsorting/MatchAlgorithmReference)


![img](images/MatchAlgorithmReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Referenced by class

 *  **[FilterComponent](FilterComponent.md)** *[FilterComponent➞matchAlgorithm](FilterComponent_matchAlgorithm.md)*  <sub>REQ</sub>  **[MatchAlgorithmReference](MatchAlgorithmReference.md)**
 *  **None** *[matchAlgorithm](matchAlgorithm.md)*  <sub>REQ</sub>  **[MatchAlgorithmReference](MatchAlgorithmReference.md)**

## Attributes


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
