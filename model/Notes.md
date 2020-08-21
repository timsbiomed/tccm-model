# Notes on enhancements to Biolinkml
1) Requiring a default range is a bit heavy handed.  Shouldn't bother with it until you encounter an unspecified
range and, even then, you may want to hard-code the basic string range.

2) If you don't supply a default namespace, jsonldcontextgen.py errors out on line 50.  What do do instead

3) Prefixes section doesn't support CURIES. When you supply one, you get:
  File "/Users/solbrig/.local/share/virtualenvs/tccm-CoY-QjRv/lib/python3.8/site-packages/biolinkml/utils/metamodelcore.py", line 131, in __init__
Without a line number reference.  We should be able to pass identifiers and the line number generator should be
smart enough to know whether it has them or not

4) Imports has to work as advertised even if the BiolinkML isn't the same (**Fixed**)

5) Local imports need to be in the form "from .X import foo" (or full path?) (Duplicate: see below)

6) SchemaLoader line 101 -- commented out a couple of lines because loaded_file doesn't have a path while the
comparison does

7) Default prefix isn't set in Python if it isn't declared in yaml

8) Importing entrydescription appears to pull OpaqueData in to the python even if it is never used... why?

9) The warnings about slot_usages should be suppressible without suppressing all warnings (Fixed: Changed to info)

10) Namespacemanager line 169 -- should have a file/line reference.

11) Mixins are not showing on diagrams that have the things they are mixed in to - see ResourceDescription as an example

12) Need to add Any type -- note that you can set it as the default range if needed

13) If no default prefix, use the model ID (?) 

14) Context generater should have an option to emit JSON-LD 1.1 prefixes when necessary

15) default_prefix should work against imported prefixes as well as prefixcommons prefixes

16) Priority on prefixes in imports vs. local

17) Mappings -- are they emitted *anywhere*?  Should they be?  It seems at bare minimum they should be in the
    markdown.  Also, does ADM:Specimen.id work?  (Fixed 8/21)
    
18) slot_usage -- injects a global slot into the namespace -- can be ugly.  We need a policy on this.

19) Mappings doesn't check prefixes (!) (Fixed 8/21)

20) Mappings on slot_usage don't show up ... (see Specimen.yaml in ccdhmodel) (Fixed 8/21)

21) Broader, narrower, etc. mappings -- are they ALL in the metamodel?  Should they be?  Should their behavior be the 
    same as generic mappings?
    
22) for unqualified imports, add a '.' in python NOTE: We tried this but it caused the unit tests to whine.  Proposed
alternative -- mark the containing directory as a source directory in PyCharm (Deferred 8/22)

23) Import Id on the ccdh Specimen -- should be EntityId (Fixed 8/22)

24) SpecimenId should be EntityId -- (Fixed 8/22)

25) Importmap should be part of the package and generator should ALWAYS map biolinkml stuff

26) setup.cfg - includes should be INSIDE biolinkml. (look at how w3id redirects work before you continue)
 
---- Input ---
classes:
   c1:
      slot_usage:
         s1:
            key: true
            required: true
            
         
   c2:
      slot_usage:
         s1:
            identifier: true
            required: false

   
------- output ---
slots:
    s1:
        key: true
        identifier: true
        required: ???
    c1_s1:
        is_a: s1
    c2_s1:
        is_a: s1

        
classes:
    c1:
        slots:
            - c1_s1
    c2:
        slots:
            - c2_s1
            
        

classes:
    c1:
        slots
        - s1
        
    c2:
       is_a: c1
       slot_usage:
          s1:
            required: true
slots:
    s1: 
       domain_of:
       - c1
    c2_s1:
       is_a: s1
       domain_of:
       - c2
         
classes:
    c1:
        slots:
        - s1
        
    c2:
        slots:
        - c2_s1
        
    slot_usage:
        - s1
   
