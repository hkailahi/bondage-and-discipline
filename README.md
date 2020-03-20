# bondage-and-discipline

Did you know Sneklang had private variables, explicit exports, and qualified from..imports?

## Behold
```python
# Standard
import somelib
import otherlib
from blah import thing1, thing2

# Extended
from bd.import_tool import ImportTool
ImportTool(locals_dict=locals())\
.import_( "qux" ).as_( "yeezy" )\
.import_( "new.🐕.who.🍌" )\
.from_( "foo" ).import_( "a" )\
.from_( "bar" ).import_( ["x", "y"] )\
.from_( "baz" ).import_( "f" )\
.from_( "baz" ).import_( "e" ).as_( "🔥🔥🔥" )\
               .import_( "g" ).as_( "e")\
.from_( "synthpop.vinyl" ).as_( "cats" )\
               .import_({ "frankenthaler": "f.h",
                          "cy.twombly": "c.t",
                          "stephen.shore": "s.s",
                          "ed.blackwell": "e.d"
                          "diet.dr.pepper": "pp.md"
                        })

assert a == 1
assert x == 1
assert f == 2
assert cats.pp.md == 6    
assert a + x + f + cats.pp.md == 10
```
