import platform
import ctypes.util
import os
import ctypes

if platform.system() == "Linux":
    lib_name = "libwinmedia.so"
elif platform.system() == "Windows":
    lib_name = "libwinmedia.dll"


def find_lib() -> ctypes.CDLL:
    """Search for the library.

    You can place the DLL somewhere in %PATH% or set
    the environment variable "LIBWINMEDIA_PATH".

    Raises:
        OSError: The "LIBWINMEDIA_PATH" env variable is invalid.
        OSError: libwinmedia.dll is not found.

    Returns:
        ctypes.CDLL: An instance of the DLL.
    """

    # search in env variables
    if "LIBWINMEDIA_PATH" in os.environ:
        try:
            lib_path = os.path.join(os.environ["LIBWINMEDIA_PATH"], lib_name)
            return ctypes.CDLL(lib_path)
        except OSError:
            raise OSError("Invalid LIBWINMEDIA_PATH specified. Please fix.")

    # search in PATH
    try:
        path = ctypes.util.find_library(lib_name)
        if not path:
            raise FileNotFoundError
        return ctypes.CDLL(path)
    except FileNotFoundError:
        # not found
        raise OSError(
            "Cannot find libwinmedia.dll in your system %PATH%. One way to deal with this is to "
            "ship libwinmedia.dll with your script and put the directory where your script is "
            'located in %PATH% before "import libwinmedia": '
            'os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"] '
            'If libwinmedia.dll is located elsewhere, you can add that path to os.environ["PATH"].'
        )


lib = find_lib()
