from awsglue.transforms import GlueTransform as GlueTransform

class Coalesce(GlueTransform):
    def __call__(self, frame, num_partitions, shuffle: bool = ..., transformation_ctx: str = ..., info: str = ..., stageThreshold: int = ..., totalThreshold: int = ...): ...
    @classmethod
    def describeArgs(cls): ...
    @classmethod
    def describeTransform(cls): ...
    @classmethod
    def describeErrors(cls): ...
    @classmethod
    def describeReturn(cls): ...
