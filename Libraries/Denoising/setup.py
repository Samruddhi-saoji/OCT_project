from setuptools import setup
from Cython.Build import cythonize

#external libraries used in the modules
import numpy as np
import cv2

def get_opencv_include():
    build_info = cv2.getBuildInformation()
    include_dirs = [dir.strip() for dir in build_info.split('\n') if 'INCLUDE_DIRS' in dir]
    if include_dirs:
        return include_dirs[0].split(';')
    else:
        return []


######### the set up function #######
setup(
    # list all the modules in the library
    ext_modules = cythonize([
        "Denoise.py",
        "image_handling.py",
        # dont include the "main.py" file 
    ]),

    # get the header files of the external libraries used in the modules
    include_dirs=[np.get_include()] + get_opencv_include(),

    install_requires=[
        #list all the external libraries used in the modules
        'opencv-python',
        'matplotlib',
        'numpy',
        'os'
    ]
)
