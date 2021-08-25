import ctypes
import pkg_resources

lib = ctypes.CDLL(pkg_resources.resource_filename(__name__, "bin/libwinmedia.dll"))
