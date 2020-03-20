from typing import List, Union
from types import SimpleNamespace
import importlib

import enum

class ImportStage(enum.Enum):
    FRESH = 0
    FROM = 1
    FROMIMPORT = 2
    FRESHIMPORT = 3
    DONT = 4


class ImportTool(SimpleNamespace):
    """
    Import Builder.
    >>> import bd.import_tool
    >>> bd.import_tool.ImportTool(locals_dict=locals()).from_("example.foo").import_(["a"])
    ...
    >>> a
    1
    """
    def __init__(self, module=None, imports="__all__", locals_dict=None):
        self.module = module
        self.imports = imports
        self.locals_dict = locals_dict
        self.stage = ImportStage.FRESH

    def from_(self: "ImportTool", module_name: str):
        self.module = importlib.import_module(module_name)
        self.stage = ImportStage.FROM
        return self

    def import_(self: "ImportTool", imports: Union[str, List[str]]):  # TODO Qualified flag that adds subnamespace
        if self.stage in [ImportStage.FRESH, ImportStage.FRESHIMPORT, ImportStage.FROMIMPORT]:
            ns = SimpleNamespace()
            curr_sub_ns = ns
            submodules = str.split(imports, ".")
            prefix_modules = submodules[:-1]
            final_module = submodules[-1]

            first = True

            for submodule in prefix_modules:
                if first:
                    first = False
                else:
                    sub_ns = SimpleNamespace()
                    curr_sub_ns.__setattr__(submodule, sub_ns)
                    curr_sub_ns = curr_sub_ns.__getattribute__(submodule)
            curr_sub_ns.__setattr__(final_module, importlib.import_module(imports))
            self.locals_dict.update({
                submodules[0]: ns
            })
            self.stage = ImportStage.FRESHIMPORT
        elif self.stage == ImportStage.FROM:
            explicit_exports = self.module.__all__
            available_imports = [term for term in imports if term in explicit_exports]
            self.locals_dict.update({imprt: self.module.__dict__[imprt] for imprt in available_imports})
            self.stage = ImportStage.FROMIMPORT
        return self

    def as_(self: "ImportTool", alias: str):
        if self.stage == ImportStage.FRESHIMPORT:
            # TODO For multi part import (ex. `import my.module.my_module`), sub-namespaces need to be folded back up before aliasing
            # del self.locals_dict[self.module.__name__]  # FIXME What if it was imported with OG name before?
            pass
        elif self.stage == ImportStage.FROMIMPORT:
            # TODO Figure out singleton rename vs multiple rename syntax
            self.stage = ImportStage.FROMIMPORT
        return self
