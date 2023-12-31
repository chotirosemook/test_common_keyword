from AscendQaCommonLibrary.version import VERSION
from .utils.DateUtils import DateUtils
from .utils.GeneralUtils import GeneralUtils
from .utils.ImageUtils import ImageUtils
from .utils.JsonUtils import JsonUtils
from .utils.AdbUtils import AdbUtils
from .utils.AppiumUtils import AppiumUtils
from robot.api.deco import keyword,not_keyword,library
from AscendQaCommonLibrary.keywords import common_keyword

__version__ = VERSION

@library
class AscendQaCommonLibrary(common_keyword,DateUtils,GeneralUtils,ImageUtils,JsonUtils,AdbUtils,AppiumUtils):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        common_keyword(self)