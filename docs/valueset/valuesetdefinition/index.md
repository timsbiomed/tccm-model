
# Valuesetdefinition schema


A ValueSetDefinition describes the rules that determine which entity references (value meanings) belong to a value
set at a given point in time. The definition of what belongs in a value set can evolve over time, and it is possible
for there to be multiple definitions active at any given point in time - perhaps one for a system in general use, a
second for a newer system, and a third for testing. A ValueSetDefinition may or may not identify a specific version
of a code system. The decision of which version is to be used depends on the context and needs of the community.
ValueSetDefinition and the supporting model has been designed to allow multiple variations on the “binding” of
definitions to value sets, code system versions to definitions, and the combination to concept domains.


### Classes

 * [AssociatedEntitiesReference](AssociatedEntitiesReference.md) - The description of a set of entities that are associated with a referenced entity. This description names a
 * [CompleteValueSetReference](CompleteValueSetReference.md) - A reference to a value set that, when resolved, results in a set of entity references that are included in this
 * [EntityReference](EntityReference.md) - The URI, namespace/name (if known) and a list of code systems that make assertions about the entity.
 * [EntityReferenceList](EntityReferenceList.md) - A collection (set) of zero or more entity references that belong to the same scoping namespace
    * [SpecificEntityList](SpecificEntityList.md) - A list of specific entity references that are to be included in the definition. When specified in this form,
 * [Filter](Filter.md) - A collection of one or more filters. The result of applying a Filter component is the intersection of the sets of
 * [FilterComponent](FilterComponent.md) - A restriction on an attribute, property, or special field.
 * [FormalDefinition](FormalDefinition.md) - A value set definition choice
    * [CompleteCodeSystemReference](CompleteCodeSystemReference.md) - An entry that, when resolved, returns all of the active entity references in a given code system. This includes
 * [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of
    * [AssociationReference](AssociationReference.md) - A name or identifier that uniquely names an association instance in a code system.
    * [BindingQualifierReference](BindingQualifierReference.md) - A reference to an entity that describes the role that a given value set binding plays for a concept domain. T
    * [CaseSignificanceReference](CaseSignificanceReference.md) - A reference to an entity that describes significance of the case in term or designation.
    * [CodeSystemCategoryReference](CodeSystemCategoryReference.md) - A reference to information about a paradigm model used to create an ontology (a.k.a. knowledge
    * [CodeSystemReference](CodeSystemReference.md) - A reference to a code system or ontology.
    * [CodeSystemVersionReference](CodeSystemVersionReference.md) - A reference to a specific version of code system and, if known, the code system which it is a version of.
    * [ConceptDomainReference](ConceptDomainReference.md) - A reference to a concept domain.
    * [ContextReference](ContextReference.md) - A reference to a realm or context.
    * [DesignationFidelityReference](DesignationFidelityReference.md) - A reference to a description about designation faithfulness or accuracy.
    * [DesignationTypeReference](DesignationTypeReference.md) - A reference to a designation type or form such as “short name,” “abbreviation,” “eponym.”
    * [FormalityLevelReference](FormalityLevelReference.md) - A reference to a description of the relative formality an ontology.
    * [FormatReference](FormatReference.md) - A reference to a particular way that information is encoded for storage or transmission.
    * [LanguageReference](LanguageReference.md) - A reference to a spoken or written human language.
    * [MapCorrelationReference](MapCorrelationReference.md) - A reference to a way that the source and target in a map can be related or assessed.
    * [MapReference](MapReference.md) - A reference to an abstract map.
    * [MapVersionReference](MapVersionReference.md) - A reference to a map version and the corresponding map, if known.
    * [MatchAlgorithmReference](MatchAlgorithmReference.md) - A reference to an algorithm used for selecting and filtering data.
    * [ModelAttributeReference](ModelAttributeReference.md) - A reference to an attribute defined in the CTS2 specification.
    * [NamespaceReference](NamespaceReference.md) - A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name
    * [OntologyDomainReference](OntologyDomainReference.md) - A reference to a subject domain for an ontology.
    * [OntologyEngineeringMethodologyReference](OntologyEngineeringMethodologyReference.md) - A reference to a method model that can be used to create an ontology.
    * [OntologyEngineeringToolReference](OntologyEngineeringToolReference.md) - A reference to a tool that can be used to create an ontology.
    * [OntologyLanguageReference](OntologyLanguageReference.md) - A reference to a language in which an ontology may be implemented.
    * [OntologySyntaxReference](OntologySyntaxReference.md) - A reference to a syntax in which an ontology may be represented.
    * [OntologyTaskReference](OntologyTaskReference.md) - A reference to a purpose for which an ontology can be designed.
    * [OntologyTypeReference](OntologyTypeReference.md) - A reference to the nature of the content of an ontology.
    * [ReasoningAlgorithmReference](ReasoningAlgorithmReference.md) - A reference to a formal algorithm for making inferences about an ontology.
    * [RoleReference](RoleReference.md) - A reference to a role that an individual, organization, or bibliographic reference can play in the construction
    * [SourceAndRoleReference](SourceAndRoleReference.md) - A reference to a source that also includes the role that the source played and/or fixes the particular chapter,
    * [SourceReference](SourceReference.md) - A reference to an individual, organization of bibliographic reference.
    * [StatusReference](StatusReference.md) - A reference to a state in an external ontology authoring workflow.
    * [ValueSetDefinitionReference](ValueSetDefinitionReference.md) - A reference to a set of rules for constructing a value set along with the corresponding value set if known.
    * [ValueSetReference](ValueSetReference.md) - A reference to a named set of entity references.
    * [VersionTagReference](VersionTagReference.md) - A reference to a tag that can be assigned to versionable resources within the context of a service implementation.
 * [OpaqueData](OpaqueData.md) - Opaque data is the equivalent of an ASN.1 External Type or the XML Schema anyType . An OpaqueData instance
    * [EntryDescription](EntryDescription.md) - EntryDescription is a subclass of OpaqueData. The purpose behind this is that there are certain textual fields
    * [ExternalValueSetDefinition](ExternalValueSetDefinition.md) - A definition of a value set whose format and semantics is specified outside of the core
 * [PredicateReference](PredicateReference.md) - An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of
 * [PropertyQueryReference](PropertyQueryReference.md) - A description of a set of entity references that are determined by applying a filter to the attribute(s) or
 * [ResourceDescription](ResourceDescription.md) - ResourceDescription represents the shared characteristics common to both abstract and resource version
    * [AbstractResourceDescription](AbstractResourceDescription.md) - The description of the characteristics of a resource that are independent of the resource content.
    * [ResourceVersionDescription](ResourceVersionDescription.md) - Information about the source, format, release date, version identifier, etc. of a specific version of an
       * [ValueSetDefinition](ValueSetDefinition.md) - A ValueSetDefinition describes the rules that determine which entity references (value meanings) belong to a
 * [SourceAndNotation](SourceAndNotation.md) - Format and notation that some or all the releases (versions) of this resource are published in
 * [ValueSetDefinitionEntry](ValueSetDefinitionEntry.md) - An element of a value set definition that, when resolved yields a set of entity references that are to be included
 * [Extension](Extension.md) - a tag/value pair used to add non-model information to an entry
    * [Annotation](Annotation.md) - a tag/value pair with the semantics of OWL Annotation

### Mixins

 * [Annotatable](Annotatable.md) - mixin for classes that support annotations
 * [Extensible](Extensible.md) - mixin for classes that support extension

### Slots

 * [➞releaseDocumentation](abstractResourceDescription__releaseDocumentation.md) - Documentation about the frequency and nature of releases (version) of this resource.
 * [➞releaseFormat](abstractResourceDescription__releaseFormat.md) - A format and notation that the releases (versions) of this resource are published in.
 * [➞codeSystem](associatedEntitiesReference__codeSystem.md) - The code system that makes the association assertions.
 * [➞codeSystemVersion](associatedEntitiesReference__codeSystemVersion.md) - The version of the code system that makes the association assertions. If present, codeSystemVersion must be
 * [➞leafOnly](associatedEntitiesReference__leafOnly.md) - False means that all entities in a transitive closure are included.  True means only entities that are not
 * [➞objectToSubject](associatedEntitiesReference__objectToSubject.md) - False means that `rererencedEntity` serves in the subject role.  True means object.
 * [➞predicate](associatedEntitiesReference__predicate.md) - The association predicate to be used in resolving the definition entry. Depending on the setting of `reverse`,
 * [➞referencedEntity](associatedEntitiesReference__referencedEntity.md) - The entity reference that is the root of the association description. referencedEntity is not considered to
 * [➞transitiveClosure](associatedEntitiesReference__transitiveClosure.md) - If true and `predicate` is defined as being transitive, the transitive closure of `predicate` selects the
 * [➞codeSystem](codeSystemVersionReference__codeSystem.md)
 * [➞codeSystem](completeCodeSystemReference__codeSystem.md) - A reference to the code system whose codes are to be included.
 * [➞codeSystemVersion](completeCodeSystemReference__codeSystemVersion.md) - A reference to the specific version of the code system to include. If not supplied, the specific
 * [➞referenceCodeSystemVersion](completeValueSetReference__referenceCodeSystemVersion.md) - A reference to a CodeSystemVersion that will be used to resolve this call. referenceCodeSy will only be used
 * [➞valueSet](completeValueSetReference__valueSet.md) - A reference to the value set whose definition supplies a set of entity references.
 * [➞valueSetDefinition](completeValueSetReference__valueSetDefinition.md) - A reference to a particular definition of valueSet that is to be used in resolving this reference. If absent,
 * [➞entities](entityReferenceList__entities.md) - The entity references ("concept codes") in the list
 * [➞namespaceName](entityReferenceList__namespaceName.md) - The local identifier assigned to this namespace
 * [➞namespaceURI](entityReferenceList__namespaceURI.md) - The URI associated with the supplied namespace as determined by the author/service instance
 * [➞about](entityReference__about.md) - The external, permanant URI by which this entity is known.
 * [➞code](entityReference__code.md) - The namespace and name by which this entity is known within the context of the service implementation
 * [➞description](entityReference__description.md) - A description or definition of the referenced entity determined by the service
 * [➞designation](entityReference__designation.md) - The preferred label for the entity in the context of the service
 * [➞href](entityReference__href.md) - A reference to the "official" description of the entity in the context of the defining code system
 * [➞see_also](entityReference__see_also.md) - Additional external links that serve to define or otherwise clarify the intent of the reference
 * [extension➞tag](extension_tag.md) - a tag associated with an extension
 * [extension➞value](extension_value.md) - the actual annotation
    * [annotation➞value](annotation_extension_value.md)
 * [extensions](extensions.md) - a tag/text tuple attached to an arbitrary element
    * [annotations](annotations.md) - a collection of tag/text tuples with the semantics of OWL Annotation
 * [➞filterComponent](filterComponent__filterComponent.md) - The name or URI of the property or model element to be filtered. Properties are referenced by
 * [➞matchAlgorithm](filterComponent__matchAlgorithm.md) - The algorithm to be used for testing the referenced component. Examples might include “starts with,”
 * [➞matchValue](filterComponent__matchValue.md) - The value to be used in comparison. The structure and format of matchValue depends on the specific
 * [➞component](filter__component.md) - An entry in a filter
 * [➞description](filter__description.md) - A textual description of the intent and purpose of the filter
 * [➞entityquery](formalDefinition__associated_entities.md)
 * [➞codesystem](formalDefinition__complete_code_system.md)
 * [➞valueset](formalDefinition__complete_value_set.md)
 * [➞entitylist](formalDefinition__entity_list.md)
 * [➞externaldefinition](formalDefinition__external_value_set_definition.md)
 * [➞valuequery](formalDefinition__property_query.md)
 * [➞definition](formalDefinition__value_set_definition.md)
 * [➞map](mapVersionReference__map.md)
 * [➞href](nameAndMeaningReference__href.md)
 * [➞name](nameAndMeaningReference__name.md) - An identifier that uniquely names the reference within the context of the particular reference type.
 * [➞synopsis](nameAndMeaningReference__synopsis.md) - A summary of the role and purpose of the actual reference
 * [➞uri](nameAndMeaningReference__uri.md)
 * [➞format](opaqueData__format.md) - The format or encoding for value. This is typically recorded as the URI of a Mime Type
 * [➞language](opaqueData__language.md) - A reference to the written or spoken language used in value.
 * [➞schema](opaqueData__schema.md) - If the format of the document involves an XML encoding, this contains the URI of a document that carries
 * [➞value](opaqueData__value.md) - The instance value. Note that instance value should be encoded in such a way that it allows embedded
 * [➞designation](predicateReference__designation.md)
 * [➞href](predicateReference__href.md)
 * [➞name](predicateReference__name.md)
 * [➞uri](predicateReference__uri.md)
 * [➞codeSystem](propertyQueryReference__codeSystem.md) - The code system that contains the assertions that form the attributes or properties to be tested.
 * [➞codeSystemVersion](propertyQueryReference__codeSystemVersion.md) - The version of the code system that makes the assertions. If present, codeSystemVersion must be a version of
 * [➞filter](propertyQueryReference__filter.md) - The filter to be applied to entities in the referenced code system.
 * [➞about](resourceDescription__about.md) - The (or a) definitive URI that represents the resource being described. Note that this is NOT the URI of the
 * [➞additionalDocumentation](resourceDescription__additionalDocumentation.md) - A reference to a document that provide additional information about the resource.
 * [➞alternateID](resourceDescription__alternateID.md) - An alternative identifier that uniquely names this resource in other environments as contexts.
 * [➞formalName](resourceDescription__formalName.md) - The formal or officially assigned name of this resource, if any.
 * [➞keyword](resourceDescription__keyword.md) - Additional identifiers that are used to index and locate the resource.
 * [➞id](resourceDescription__resourceID.md) - A local identifier that uniquely names the resource within the context of the describedResourceType and
 * [➞resourceSynopsis](resourceDescription__resourceSynopsis.md) - A textual summary of the resource - what it is, what it is for, etc.
 * [➞rights](resourceDescription__rights.md) - Copyright and IP information. Note that rights applies to the source resource, not the CTS2 rendering.
 * [➞documentURI](resourceVersionDescription__documentURI.md) - A URI that identifies the specific version, language, and notation of the about resource. This URI needs to be constructed in such a way that, if necessary, it will be possible to differentiate resource versions that were loaded from different document syntaxes. As an example, if an image of a wine ontology was loaded from a resource that was in Manchester Syntax, it should be given a different URI than the image loaded from the RDF/XML syntax. The reasoning behind this is, even in cases where different syntaxes are 100% compatible the transformation into the TCCM model may not be identical.
 * [➞officialActivationDate](resourceVersionDescription__officialActivationDate.md) - The date that this version of the resource is stated by its publishers to go into effect.
 * [➞officialReleaseDate](resourceVersionDescription__officialReleaseDate.md) - The date that this version of the resource officially became available.
 * [➞officialResourceVersionID](resourceVersionDescription__officialResourceVersionID.md) - An official label or identifier that was assigned to this version by its publisher
 * [➞predecessor](resourceVersionDescription__predecessor.md) - A reference to the name and URI version of the resource from which this current version is derived - the
 * [➞sourceAndNotation](resourceVersionDescription__sourceAndNotation.md) - A description of where the (or a) source of the version may be found, what format and language it is
 * [➞sourceAndNotationDescription](sourceAndNotation__sourceAndNotationDescription.md) - A textual description of where the specified resource version was derived from. This parameter
 * [➞sourceDocument](sourceAndNotation__sourceDocument.md) - A persistentURI that references the document from which the resource version was derived. This URI may be
 * [➞sourceDocumentSyntax](sourceAndNotation__sourceDocumentSyntax.md) - The syntax of the source of the resource version, if known. Examples might include rdf/xml, Turtle,
 * [➞sourceLanguage](sourceAndNotation__sourceLanguage.md) - The formal language, if any, that the source for the resource version is expressed in. Examples include
 * [➞bibliographicLink](sourceAndRoleReference__bibliographicLink.md)
 * [➞role](sourceAndRoleReference__role.md)
 * [➞exclude](valueSetDefinitionEntry__exclude.md) - Exclude the resolution of this definition in the valueset
 * [➞include](valueSetDefinitionEntry__include.md) - Include the resolution of this definition in the valueset
 * [➞intersect](valueSetDefinitionEntry__intersect.md) - Include only the elements that are common between this definition and the valueset to this point
 * [➞definitionOf](valueSetDefinition__definitionOf.md) - A reference to the value set being defined.
 * [➞entry](valueSetDefinition__entry.md) - A component in a value set definitio
 * [➞versionTag](valueSetDefinition__versionTag.md) - A version tag assigned to this definition by the implementing service.

### Types


#### Built in

 * **Bool**
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

 * [ASSOCIATION](types/ASSOCIATION.md)  ([ValueSet](types/ValueSet.md))  - A formal “semantic” assertion about a named entity, in the form of subject, predicate, and object including any
 * [BINDINGQUALIFIER](types/BINDINGQUALIFIER.md)  ([ValueSet](types/ValueSet.md))  - An assertion about the semantics of a concept domain / value set binding. This model element exists specifically
 * [CASESIGNIFICANCE](types/CASESIGNIFICANCE.md)  ([ValueSet](types/ValueSet.md))  - Identifies the significance of case in a term or designation.
 * [CODESYSTEM](types/CODESYSTEM.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about the provenance, use, and distribution of a code system or ontology.
 * [CODESYSTEMCATEGORY](types/CODESYSTEMCATEGORY.md)  ([ValueSet](types/ValueSet.md))  - The general category of a code system (flat list, subject heading system, taxonomy, thesaurus, classification,
 * [CODESYSTEMVERSION](types/CODESYSTEMVERSION.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about content and distribution format of a particular version or release of a code system.
 * [CONCEPTDOMAIN](types/CONCEPTDOMAIN.md)  ([ValueSet](types/ValueSet.md))  - The description of the conceptual domain of a field in a message, column in a database, field on a form, etc.
 * [CONTEXT](types/CONTEXT.md)  ([ValueSet](types/ValueSet.md))  - External and environmental factors that serve to discriminate among multiple possible selections. While it is
 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - The unique identifier of a set of change instructions that can potentially transform the contents of a TCCM
 * [CodeSystemName](types/CodeSystemName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystem.
 * [CodeSystemVersionName](types/CodeSystemVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystemVersion.
 * [ConceptDomainName](types/ConceptDomainName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a ConceptDomain.
 * [DESIGNATIONFIDELITY](types/DESIGNATIONFIDELITY.md)  ([ValueSet](types/ValueSet.md))  - Identifies how well a particular designation represents the intended meaning of the referenced entity. TCCM
 * [DESIGNATIONTYPE](types/DESIGNATIONTYPE.md)  ([ValueSet](types/ValueSet.md))  - The particular form or type of a given designation: can be “short name,” “long name,” “abbreviation,” “eponym.”
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed results in a list of resources that, in the context of a given
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a “work” in the bibliographic sense. It is not necessary that a Document URI be directly or
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable
 * [FORMALITYLEVEL](types/FORMALITYLEVEL.md)  ([ValueSet](types/ValueSet.md))  - The level of formality of an ontology (OMV 5.9).
 * [FORMAT](types/FORMAT.md)  ([ValueSet](types/ValueSet.md))  - A particular way that information is encoded for storage in a computer file
 * [LANGUAGE](types/LANGUAGE.md)  ([ValueSet](types/ValueSet.md))  - A spoken or written language intended for human consumption.
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
 * [LocalURI](types/LocalURI.md)  (**URIorCURIE**)  - A URI or handle whose scope is local to the implementing service. LocalURI cannot be used as a permanent
 * [MAP](types/MAP.md)  ([ValueSet](types/ValueSet.md))  - A set of rules that associate a set of entity references from one domain into those in another.
 * [MAPCORRELATION](types/MAPCORRELATION.md)  ([ValueSet](types/ValueSet.md))  - An assertion about the strength or significance of a specific rule in a Map.
 * [MAPVERSION](types/MAPVERSION.md)  ([ValueSet](types/ValueSet.md))  - The state of a Map at a given point in time.
 * [MATCHALGORITHM](types/MATCHALGORITHM.md)  ([ValueSet](types/ValueSet.md))  - A predicate that determines whether an entity resource qualities for membership in a set based on supplied
 * [MODELATTRIBUTE](types/MODELATTRIBUTE.md)  ([ValueSet](types/ValueSet.md))  - An attribute defined in CTS2 information model.
 * [MapName](types/MapName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a Map.
 * [MapVersionName](types/MapVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a MapVersion.
 * [NAMESPACE](types/NAMESPACE.md)  ([ValueSet](types/ValueSet.md))  - A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name but different meanings.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [ONTOLOGYDOMAIN](types/ONTOLOGYDOMAIN.md)  ([ValueSet](types/ValueSet.md))  - While the domain can refer to any topic ontology it is advised to use one of the established general purpose
 * [ONTOLOGYENGINEERINGMETHODOLOGY](types/ONTOLOGYENGINEERINGMETHODOLOGY.md)  ([ValueSet](types/ValueSet.md))  - Information about the ontology engineering methodology (OMV 5.4) (sic).
 * [ONTOLOGYENGINEERINGTOOL](types/ONTOLOGYENGINEERINGTOOL.md)  ([ValueSet](types/ValueSet.md))  - A tool used to create the ontology (OMV 5.5).
 * [ONTOLOGYLANGUAGE](types/ONTOLOGYLANGUAGE.md)  ([ValueSet](types/ValueSet.md))  - Information about the language in which the ontology is implemented (OMV 5.7).
 * [ONTOLOGYSYNTAX](types/ONTOLOGYSYNTAX.md)  ([ValueSet](types/ValueSet.md))  - Information about the syntax used by an ontology (OMV 5.6).
 * [ONTOLOGYTASK](types/ONTOLOGYTASK.md)  ([ValueSet](types/ValueSet.md))  - Information about the task the ontology was intended to be used for (OMV 5.10).
 * [ONTOLOGYTYPE](types/ONTOLOGYTYPE.md)  ([ValueSet](types/ValueSet.md))  - Categorizes ontologies (OMV 5.2).
 * [PREDICATE](types/PREDICATE.md)  ([ValueSet](types/ValueSet.md))  - A property or relation between entities.
 * [PersistentURI](types/PersistentURI.md)  (**URIorCURIE**)  - A Universal Resource Identifier (URI) that persists across service instances. PersistentURIs have enduring
 * [REASONINGALGORITHM](types/REASONINGALGORITHM.md)  ([ValueSet](types/ValueSet.md))  - A set of formal rules that allow the deduction of additional assertions from a
 * [RESOURCETYPE](types/RESOURCETYPE.md)  ([ValueSet](types/ValueSet.md))  - A class of which a referencing resource is an instance of.
 * [ROLE](types/ROLE.md)  ([ValueSet](types/ValueSet.md))  - A role that a SOURCE can play in the construction or dissemination of a terminological resource.
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or handle that is directly readable by a specific instance of a TCCM service implementation. RenderingURI
 * [SOURCE](types/SOURCE.md)  ([ValueSet](types/ValueSet.md))  - An individual, organization, or bibliographic reference.
 * [STATEMENT](types/STATEMENT.md)  ([ValueSet](types/ValueSet.md))  - An atomic assertion about a CTS2 resource.
 * [STATUS](types/STATUS.md)  ([ValueSet](types/ValueSet.md))  - The state of a resource or other entry in an external workflow.
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [VALUESET](types/VALUESET.md)  ([ValueSet](types/ValueSet.md))  - A set of entity references.
 * [VALUESETDEFINITION](types/VALUESETDEFINITION.md)  ([ValueSet](types/ValueSet.md))  - A set of rules that can be applied to specified versions or one or more code systems to yield a set of entity
 * [VERSIONTAG](types/VERSIONTAG.md)  ([ValueSet](types/ValueSet.md))  - An identifier that can be assigned to resource versions by a service implementation to identify their state
 * [ValueSet](types/ValueSet.md)  (**URIorCURIE**)  - A URI that can be indirectly resolved to a set of entity descriptions
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
