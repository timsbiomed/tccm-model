
# Type: MapRule


A set of instructions that, when interpreted in the proper context, returns a true/false value, where true means
that the context meets the requirements set forth by the rule and false means that it doesn’t. Neither the syntax
nor the semantics of map rules are included as part of the TCCM specification.

URI: [tccm:MapRule](https://hotecosystem.org/tccm/MapRule)


![img](images/MapRule.svg)

## Parents

 *  is_a: [OpaqueData](OpaqueData.md) - Opaque data is the equivalent of an ASN.1 External Type or the XML Schema anyType . An OpaqueData instance

## Referenced by class

 *  **None** *[➞rule](mapTarget__rule.md)*  <sub>OPT</sub>  **[MapRule](MapRule.md)**

## Attributes


### Inherited from OpaqueData:

 * [➞format](opaqueData__format.md)  <sub>OPT</sub>
    * Description: The format or encoding for value. This is typically recorded as the URI of a Mime Type
    * range: [FormatReference](FormatReference.md)
 * [➞language](opaqueData__language.md)  <sub>OPT</sub>
    * Description: A reference to the written or spoken language used in value.
    * range: [LanguageReference](LanguageReference.md)
 * [➞schema](opaqueData__schema.md)  <sub>OPT</sub>
    * Description: If the format of the document involves an XML encoding, this contains the URI of a document that carries
the corresponding XML Schema or DTD.
    * range: [DocumentURI](types/DocumentURI.md)
 * [➞value](opaqueData__value.md)  <sub>REQ</sub>
    * Description: The instance value. Note that instance value should be encoded in such a way that it allows embedded
structures. As an example, in XML Schema, this encoding should be to xs:anyType or an equivalent.
    * range: [String](types/String.md)
