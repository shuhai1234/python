import os

import jpype
from jpype import *

from Common import dirconfig

filepath = dirconfig.testdatas_path + "/InterfaceTester.jar"
jarpath = os.path.join(os.path.abspath('.'), filepath)
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath))
java.lang.System.out.println("Hello World")

shutdownJVM()