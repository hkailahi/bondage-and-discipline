# bondage-and-discipline

Did you know Sneklang had private variables, explicit exports, and qualified from-imports?

Behold...
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
               .import_( "g" ).as_( "e" )\
.from_( "synthpop.vinyl" ).as_( "cats" )\
               .import_({ "frankenthaler": "f.h",
                          "cy.twombly": "c.t",
                          "stephen.shore": "s.s",
                          "ed.blackwell": "e.d",
                          "diet.dr.pepper": "pp.md"})

assert a == 1
assert x == 1
assert f == 2
assert cats.pp.md == 6
assert a + x + f + cats.pp.md == 10
```

# Table of Contents
- [bondage-and-discipline](#bondage-and-discipline)
- [Table of Contents](#table-of-contents)
  - [Project Status](#project-status)
  - [Quick Start](#quick-start)
  - [Step By Step](#step-by-step)
  - [Professional Edition](#professional-edition)
  - [Contributing](#contributing)

[↥ back to top](#bondage-and-discipline)

## Project Status

Status: **Pre-αɸωβΘδΓɸɸ**
  * Not all features from example are currently supported

[↥ back to top](#bondage-and-discipline)

## Quick Start

```
pip install bondage-and-discipline
```

[↥ back to top](#bondage-and-discipline)

## Step By Step

[↥ back to top](#bondage-and-discipline)

## Professional Edition

```python
from bd.import_tool import ImportTool
ImportTool(locals_dict=locals())\
.import_( "qux" ).as_( "yeezy" )\
.import_( "new.🐕.who.🍌" )\
.from_( "foo" ).import_( "a" )\
.from_( "bar" ).import_( ["x", "y"] )\
.from_( "baz" ).import_( "f" )\
.from_( "baz" ).import_( "e" ).as_( "🔥🔥🔥" )\
               .import_( "g" ).as_( "e" )\
.from_( "synthpop.vinyl" ).as_( "cats" )\
               .import_({ "frankenthaler": "f.h",
                          "cy.twombly": "c.t",
                          "stephen.shore": "s.s",
                          "ed.blackwell": "e.d",
                          "diet.dr.pepper": "pp.md"})\
.ffi_( "java" )\
  .from_( "java.time" )\
    .import_( "*" )\
  .package_("org.package.com.fizz.buzz" )\
    .import_( "beanfunctor.optics.*" )\
.ffi_( "hs" )\
  .pragma_( ["RecordWildcards", "NPlusKPatterns", "PostfixOperators", "InterruptibleFFI", "Trustworthy"] )\
  .from_( "Prelude" )\
    .import_( [ "head", "IO (IO)", "stackNub" ] )\
.ffi_( "js" )\
  .package_( "left-pad" )\
    .import_( "leftPad" )
```

[↥ back to top](#bondage-and-discipline)

## Contributing

doituwont

[↥ back to top](#bondage-and-discipline)
