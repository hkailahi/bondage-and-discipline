# bondage-and-discipline

Did you know Sneklang had private variables, explicit exports, and qualified from..imports?

## Behold
```python
import somelib
import otherlib
from blah import thing1, thing2

from bd.import_tool import ImportTool
ImportTool(locals_dict=locals())\
    .from_("foo").import_("a")\
    .from_("bar").import_(["x", "y"])\
    .from_("baz").import_("f")\
    .from_("baz").import_("g").as_("🔥🔥🔥")\
    .import_("qux").as_("yeezy")
    .import_("new.dis.who.🍌")
    
assert a + x + f == 4
```
