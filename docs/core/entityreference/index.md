
# Entityreference schema


TCCM differentiates between a simple resource reference, such as a code system, code system version, value set, etc.
and a reference to an Entity - a class, predicate, or individual. Simple resource references are identified by a
single URI. Entity references, however, are subdivided into two parts - a scoping namespace and an identifier that is
unique within the context of the namespace.

This model defines three building blocks that are used for referencing entities throughout the specification.
The first form, URIAndEntityName provides the URI and local name by which the entity is known within the context of
the service. An optional href may also be supplied that resolves to the EntityDescription that is contextually
appropriate.

The second form, EntityReference, supplies the uri and name but also includes a list of code system versions that
make one or more assertions about (or using) the referenced entity. There will be at most one version of any given
code system in this list, the choice of which will depend on the context of the query.
The third form, EntityExpression, is a description of an Entity in an external language and syntax such as RDF/ OWL,
Manchester OWL, or SNOMED CT Compositional Grammar.


### Classes

 * [EntityReference](EntityReference.md) - The URI, namespace/name (if known) and a list of code systems that make assertions about the entity.
 * [EntityReferenceList](EntityReferenceList.md) - A collection (set) of zero or more entity references that belong to the same scoping namespace

### Mixins


### Slots

 * [about](about.md) - The external, permanant URI by which this entity is known.
    * [EntityReference➞about](EntityReference_about.md)
 * [code](code.md) - The namespace and name by which this entity is known within the context of the service implementation
    * [EntityReference➞code](EntityReference_code.md)
 * [description](description.md) - A description or definition of the referenced entity determined by the service
    * [EntityReference➞description](EntityReference_description.md)
 * [designation](designation.md) - The preferred label for the entity in the context of the service
    * [EntityReference➞designation](EntityReference_designation.md)
 * [entities](entities.md) - The entity references ("concept codes") in the list
    * [EntityReferenceList➞entities](EntityReferenceList_entities.md)
 * [href](href.md) - A reference to the "official" description of the entity in the context of the defining code system
    * [EntityReference➞href](EntityReference_href.md)
 * [namespaceName](namespaceName.md) - The local identifier assigned to this namespace
    * [EntityReferenceList➞namespaceName](EntityReferenceList_namespaceName.md)
 * [namespaceURI](namespaceURI.md) - The URI associated with the supplied namespace as determined by the author/service instance
    * [EntityReferenceList➞namespaceURI](EntityReferenceList_namespaceURI.md)
 * [see_also](see_also.md) - Additional external links that serve to define or otherwise clarify the intent of the reference
    * [EntityReference➞see_also](EntityReference_see_also.md)

### Types


#### Built in

 * **Bool**
 * **Curie**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [CURIE](types/CURIE.md)  (**Curie**) 
 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - The unique identifier of a set of change instructions that can potentially transform the contents of a TCCM
 * [CodeSystemName](types/CodeSystemName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystem.
 * [CodeSystemVersionName](types/CodeSystemVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystemVersion.
 * [ConceptDomainName](types/ConceptDomainName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a ConceptDomain.
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed results in a list of resources that, in the context of a given
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a “work” in the bibliographic sense. It is not necessary that a Document URI be directly or
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
 * [LocalURI](types/LocalURI.md)  ([URIorCurie](types/URIorCurie.md))  - A URI or handle whose scope is local to the implementing service. LocalURI cannot be used as a permanent
 * [MapName](types/MapName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a Map.
 * [MapVersionName](types/MapVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a MapVersion.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [PersistentURI](types/PersistentURI.md)  ([URIorCurie](types/URIorCurie.md))  - A Universal Resource Identifier (URI) that persists across service instances. PersistentURIs have enduring
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or handle that is directly readable by a specific instance of a TCCM service implementation. RenderingURI
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [URI](types/URI.md)  (**URI**)  - A Universal Resource Identifier (URI) as defined in IETF RFC 3986. TCCM implementations are encouraged to
 * [URIorCurie](types/URIorCurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [ValueSetName](types/ValueSetName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a ValueSet.
 * [VersionTagName](types/VersionTagName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a VersionTag.
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
