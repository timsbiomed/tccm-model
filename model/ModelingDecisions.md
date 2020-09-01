# Modeling Decisions
## Type declarations
With the exception of the topmost resources, which don't have any slots identifying them, types will be mapped to
slot names, with the slot name itself being the same (w/ case differences) as that in the CTS2 specification and the
alias set to whatever works best in real world use situations.
## Abstract resources and versions
The general problem is that code system reference appears both in the code system reference itself AND the version.
Versions should be specializations of the abstraction with just a version string -- not full fledged name and meaning
reference

