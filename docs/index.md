
# Tccm schema


Terminology Core Common Model


### Classes

 * [EntityReference](EntityReference.md)
 * [NameAndMeaningReference](NameAndMeaningReference.md)
 * [OpaqueData](OpaqueData.md)

### Mixins


### Slots

 * [about](about.md)
 * [code](code.md)
 * [href](href.md)
 * [language](language.md)
 * [➞href](meaningHref.md)
 * [name](name.md)
 * [uri](uri.md)
 * [value](value.md)

### Types


#### Built in

 * **URI**
 * **URIorCURIE**
 * **XSDDateTime**
 * **int**
 * **str**

#### Defined

 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md)) 
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [DesignationRole](types/DesignationRole.md)  ([String](types/String.md)) 
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md)) 
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md)) 
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md)) 
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource
 * [LocalURI](types/LocalURI.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**str**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - An integer
 * [PersistentURI](types/PersistentURI.md)  ([Uriorcurie](types/Uriorcurie.md)) 
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md)) 
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md)) 
 * [String](types/String.md)  (**str**)  - A character string
 * [Uri](types/Uri.md)  (**URI**)  - A Universal Resource Identifier (URI) as defined in IETF RFC 3986
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
