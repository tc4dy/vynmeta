class VynMetaError(Exception):
    pass


class UnsupportedFormat(VynMetaError):
    pass


class MissingDependency(VynMetaError):
    pass


class ValidationFailed(VynMetaError):
    pass
