# Notes on enhancements to Biolinkml
1) Requiring a default range is a bit heavy handed.  Shouldn't bother with it until you encounter an unspecified
range and, even then, you may want to hard-code the basic string range.
2) If you don't supply a default namespace, jsonldcontextgen.py errors out on line 50.  What do do instead
3) Prefixes section doesn't support CURIES. When you supply one, you get:
  File "/Users/solbrig/.local/share/virtualenvs/tccm-CoY-QjRv/lib/python3.8/site-packages/biolinkml/utils/metamodelcore.py", line 131, in __init__
Without a line number reference.  We should be able to pass identifiers and the line number generator should be
smart enough to know whether it has them or not
4) Imports has to work as advertised even if the BiolinkML isn't the same (**Fixed**)
5) Local imports need to be in the form "from .X import foo" (or full path?)
6) SchemaLoader line 101 -- commented out a couple of lines because loaded_file doesn't have a path while the
comparison does
7) Default prefix isn't set in Python if it isn't declared in yaml
8) Importing entrydescription appears to pull OpaqueData in to the python even if it is never used... why?
9) The warnings about slot_usages should be suppressible without suppressing all warnings (**Fixed: Changed to info**)
10) Namespacemanager line 169 -- should have a file/line reference.
11) Mixins are not showing on diagrams that have the things they are mixed in to - see ResourceDescription as an example
12) Need to add Any type -- note that you can set it as the default range if needed
