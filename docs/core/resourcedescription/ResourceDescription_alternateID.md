
# Type: ResourceDescription_alternateID


An alternative identifier that uniquely names this resource in other environments as contexts. As an example, if a resource had both an ISO Object Identifier and a DNS name, the DNS name might be assigned as the entryID of the resource by one service while the ISO OID would be recorded as an alternateURI using the “urn:oid” prefix. Note that alternateIds can be added or removed during resource updates.

URI: [tccm:ResourceDescription_alternateID](https://hotecosystem.org/tccm/ResourceDescription_alternateID)


## Domain and Range

[ResourceDescription](ResourceDescription.md) ->  <sub>OPT</sub> [String](types/String.md)

## Parents

 *  is_a: [alternateID](alternateID.md)

## Children


## Used by

 * [AbstractResourceDescription](AbstractResourceDescription.md)
 * [ResourceDescription](ResourceDescription.md)
 * [ResourceVersionDescription](ResourceVersionDescription.md)
