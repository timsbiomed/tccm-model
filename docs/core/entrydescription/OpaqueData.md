
# Type: OpaqueData


Opaque data is the equivalent of an ASN.1 External Type or the XML Schema anyType . An OpaqueData instance may represent text with an optional spoken or written language code or a formal structure such as embedded HTML, XML, or MIME encoded data. When a formal structure is included, its type should be specified in the format attribute and, when the type is an XML variant, the corresponding schema (or DTD) should be included in the schema parameter.
The OpaqueData data type must be encoded in such a way that the content can be represented by a character string. Binary data is not permitted, although hyperlinks to binary data are.

URI: [tccm:OpaqueData](https://hotecosystem.org/tccm/OpaqueData)


![img](images/OpaqueData.svg)

## Children

 * [EntryDescription](EntryDescription.md) - EntryDescription is a subclass of OpaqueData. The purpose behind this is that there are certain textual fields that some CTS2 service implementations may want to constrain. As an example, Designation text is of type EntryDescription, but implementations may want to restrict the OpaqueData value attribute to a simple string rather than xs: anyType. When OpaqueData appears directly as a model element, implementations must be able to support the full OpaqueData model. EntryDescription, however, may be constrained by implementations or specialized PSM.

## Referenced by class


## Attributes


### Own

 * [OpaqueData➞format](OpaqueData_format.md)  <sub>OPT</sub>
    * Description: The format or encoding for value. This is typically recorded as the URI of a Mime Type
    * range: [FormatReference](FormatReference.md)
 * [OpaqueData➞language](OpaqueData_language.md)  <sub>OPT</sub>
    * Description: A reference to the written or spoken language used in value.
    * range: [LanguageReference](LanguageReference.md)
 * [OpaqueData➞schema](OpaqueData_schema.md)  <sub>OPT</sub>
    * Description: If the format of the document involves an XML encoding, this contains the URI of a document that carries the corresponding XML Schema or DTD.
    * range: [DocumentURI](types/DocumentURI.md)
 * [OpaqueData➞value](OpaqueData_value.md)  <sub>REQ</sub>
    * Description: The instance value. Note that instance value should be encoded in such a way that it allows embedded structures. As an example, in XML Schema, this encoding should be to xs:anyType or an equivalent.
    * range: [String](types/String.md)