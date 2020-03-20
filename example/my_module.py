from bd.import_tool import ImportTool
ImportTool(locals_dict=locals())\
    .from_("example.foo").import_(["a"])\
    .from_("example.bar").import_(["x", "y"])\
    .from_("example.baz").import_(["f"])\
    .from_("example.baz").import_(["g"])\
    .import_("example.qux") #.as_("yeezy")

# Look ma no keyword imports
# assert a + x + f + yeezy.i == 5
