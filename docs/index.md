
# Tccm schema


Terminology Core Common Model


### Classes

 * [EntityDescription](EntityDescription.md)
 * [EntityReference](EntityReference.md)
 * [NameAndMeaningReference](NameAndMeaningReference.md)
    * [ContextReference](ContextReference.md)
 * [OpaqueData](OpaqueData.md)
    * [Designation](Designation.md)

### Mixins


### Slots

 * [about](about.md)
 * [alternateURI](alternateURI.md)
 * [code](code.md)
 * [designation](designation.md)
 * [designationRole](designationRole.md)
 * [href](href.md)
 * [language](language.md)
 * [➞href](meaningHref.md)
 * [name](name.md)
 * [uri](uri.md)
 * [usageContext](usageContext.md)
 * [value](value.md)

### Types


#### Built in

 * **URI**
 * **URIorCURIE**
 * **XSDDateTime**
 * **int**
 * **str**

#### Defined

 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - A persisitent URI of a set of change instructions that can potentially transform the contents of the service instance from one state to another.
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [DesignationRole](types/DesignationRole.md)  ([String](types/String.md)) 
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed, results in a list of resources that, in the context of a given service, satisfy the query.
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a "work" in the bibliographic sense. It's not necessary to be directly or indirectly resolvable to a digital resource - it may simply be the name of a book, publication, or other abstraction.
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A persistent URI that names a unique resource. It's not assumed to be resolvable via an HTTP GET operation.
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource.
 * [LocalURI](types/LocalURI.md)  ([Uriorcurie](types/Uriorcurie.md))  - A URI or CURIE whose scope is local to the implementing service.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**str**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [PersistentURI](types/PersistentURI.md)  ([Uriorcurie](types/Uriorcurie.md))  - A persistent URI is a URI or CURIE that persists across service instances.
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or CURI that is directly readable by a specific instance of a service implementation.
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [String](types/String.md)  (**str**)  - A character string
 * [Uri](types/Uri.md)  (**URI**)  - A Universal Resource Identifier (URI) as defined in IETF RFC 3986.
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
