
# Type: BINDING_QUALIFIER


An assertion about the semantics of a concept domain / value set binding. This model element exists specifically
to address section 2.4.2.23 of the HL7 SFM14, which needs a qualifier that indicates whether the binding is
“overall,” “minimal,” or “maximum.”

The TCCM specification does not formally define the semantics of the various possible BINDING_QUALIFIER elements:
it is up to specific implementations and service clients to interpret the meaning of the specific binding
qualifiers that may be represented in references of this type.

URI: [tccm:BINDINGQUALIFIER](https://hotecosystem.org/tccm/BINDINGQUALIFIER)

|  |  |  |
| --- | --- | --- |
| Parent type | | [ValueSet](types/ValueSet.md) |
| Root (builtin) type | | **URIorCURIE** |
| Representation | | str |
