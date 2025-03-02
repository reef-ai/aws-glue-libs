from awsglue.transforms import GlueTransform as GlueTransform
from typing import Any

class RenameField(GlueTransform):
    def __call__(self, frame, old_name, new_name, transformation_ctx: str = ..., info: str = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class DropFields(GlueTransform):
    def __call__(self, frame, paths, transformation_ctx: str = ..., info: str = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class SelectFields(GlueTransform):
    def __call__(self, frame, paths, transformation_ctx: str = ..., info: str = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class SplitFields(GlueTransform):
    def __call__(self, frame, paths, name1: Any | None = ..., name2: Any | None = ..., transformation_ctx: str = ..., info: str = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class SplitRows(GlueTransform):
    def __call__(self, frame, comparison_dict, name1: str = ..., name2: str = ..., transformation_ctx: str = ..., info: Any | None = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class Join(GlueTransform):
    def __call__(self, frame1, frame2, keys1, keys2, transformation_ctx: str = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...

class Spigot(GlueTransform):
    def __call__(self, frame, path, options, transformation_ctx: str = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...
