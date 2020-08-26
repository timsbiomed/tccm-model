
# Type: ExternalURI


A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable
via an http: GET operation - ExternalURIs should always be passed as parameters to service implementations
to get the sanctioned equivalent in a given service context.

URI: [tccm:ExternalURI](https://hotecosystem.org/tccm/ExternalURI)

|  |  |  |
| --- | --- | --- |
| Parent type | | [PersistentURI](types/PersistentURI.md) |
| Root (builtin) type | | **URIorCURIE** |
| Representation | | str |
