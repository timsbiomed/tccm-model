
# Type: ValueSetCatalogEntry


A ValueSetCatalogEntry carries information about the creators, distributors, purpose, use, etc. about a value set.
The catalog does not carry the actual definition of a value set as (a) this may vary over time and (b) it is
possible for more than one definition to be in use at any given point in time.

URI: [tccm:ValueSetCatalogEntry](https://hotecosystem.org/tccm/ValueSetCatalogEntry)


![img](images/ValueSetCatalogEntry.svg)

## Parents

 *  is_a: [ValueSetCatalogEntryOrReference](ValueSetCatalogEntryOrReference.md) - Either a description of ana abstract value set or a reference to an official entry

## Uses Mixins

 *  mixin: [AbstractResourceDescription](AbstractResourceDescription.md) - The description of the characteristics of a resource that are independent of the resource content.

## Attributes


### Own

 * [➞currentDefinition](valueSetCatalogEntry__currentDefinition.md)  <sub>OPT</sub>
    * range: [ValueSetDefinitionReference](ValueSetDefinitionReference.md)
 * [➞currentResolution](valueSetCatalogEntry__currentResolution.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [➞definitions](valueSetCatalogEntry__definitions.md)  <sub>0..*</sub>
    * range: [ValueSetDefinitionReference](ValueSetDefinitionReference.md)
 * [➞valueSetName](valueSetCatalogEntry__valueSetName.md)  <sub>REQ</sub>
    * range: [ValueSetName](types/ValueSetName.md)

### Mixed in from AbstractResourceDescription:

 * [➞releaseDocumentation](abstractResourceDescription__releaseDocumentation.md)  <sub>OPT</sub>
    * Description: Documentation about the frequency and nature of releases (version) of this resource.
    * range: [String](types/String.md)

### Mixed in from AbstractResourceDescription:

 * [➞releaseFormat](abstractResourceDescription__releaseFormat.md)  <sub>0..*</sub>
    * Description: A format and notation that the releases (versions) of this resource are published in.
    * range: [SourceAndNotation](SourceAndNotation.md)

### Mixed in from ResourceDescription:

 * [➞about](resourceDescription__about.md)  <sub>REQ</sub>
    * Description: The (or a) definitive URI that represents the resource being described. Note that this is NOT the URI of the
resource description in the TCCM or other format, but of the resource itself. As an example, the about URI
for the Wine ontology would be “http://www.w3.org/TR/2003/PR-owl-guide-2003 1209/wine#.” The NCI Thesaurus
has, among others, the about URI of http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#. HL7 uses ISO Object
Identifiers (OIDs) to label resources so, from the HL7 perspective, the about URI of the NCI Thesaurus would
be “urn:oid:2.16.840. 1.113883.3.26.1.1”
    * range: [ExternalURI](types/ExternalURI.md)

### Mixed in from ResourceDescription:

 * [➞additionalDocumentation](resourceDescription__additionalDocumentation.md)  <sub>0..*</sub>
    * Description: A reference to a document that provide additional information about the resource.
    * range: [PersistentURI](types/PersistentURI.md)

### Mixed in from ResourceDescription:

 * [➞alternateID](resourceDescription__alternateID.md)  <sub>OPT</sub>
    * Description: An alternative identifier that uniquely names this resource in other environments as contexts.
As an example, if a resource had both an ISO Object Identifier and a DNS name, the DNS name might be assigned
as the entryID of the resource by one service while the ISO OID would be recorded as an alternateURI using
the “urn:oid” prefix. Note that alternateIds can be added or removed during resource updates.
    * range: [String](types/String.md)

### Mixed in from ResourceDescription:

 * [➞describedResourceType](resourceDescription__describedResourceType.md)  <sub>OPT</sub>
    * Description: Enumeration of possible types
    * range: [String](types/String.md)

### Mixed in from ResourceDescription:

 * [➞formalName](resourceDescription__formalName.md)  <sub>OPT</sub>
    * Description: The formal or officially assigned name of this resource, if any.
    * range: [String](types/String.md)

### Mixed in from ResourceDescription:

 * [➞keyword](resourceDescription__keyword.md)  <sub>0..*</sub>
    * Description: Additional identifiers that are used to index and locate the resource.
    * range: [String](types/String.md)

### Mixed in from ResourceDescription:

 * [➞id](resourceDescription__resourceID.md)  <sub>REQ</sub>
    * Description: A local identifier that uniquely names the resource within the context of the describedResourceType and
implementing service. As an example, this might be “SCT” for the SNOMED-CT code system, “SCT-2010AA” for a
SNOMED-CT code system version.
    * range: [LocalIdentifier](types/LocalIdentifier.md)

### Mixed in from ResourceDescription:

 * [➞resourceSynopsis](resourceDescription__resourceSynopsis.md)  <sub>OPT</sub>
    * Description: A textual summary of the resource - what it is, what it is for, etc.
    * range: [String](types/String.md)

### Mixed in from ResourceDescription:

 * [➞rights](resourceDescription__rights.md)  <sub>OPT</sub>
    * Description: Copyright and IP information. Note that rights applies to the source resource, not the CTS2 rendering.
    * range: [String](types/String.md)
