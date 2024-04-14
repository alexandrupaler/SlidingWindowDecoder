from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

VERSION="0.0.0"
f = open("bpgdg/VERSION","w+")
f.write(VERSION)
f.close()

extension1 = Extension(
    name="bpgdg.mod2sparse",
    sources=["bpgdg/include/mod2sparse.cpp", "bpgdg/mod2sparse.pyx"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(), 'bpgdg/include'],
    extra_compile_args=['-std=c++11']
    )

extension2 = Extension(
    name="bpgdg.c_util",
    sources=["bpgdg/c_util.pyx", "bpgdg/include/mod2sparse.cpp"],
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(), 'bpgdg/include'],
    extra_compile_args=['-std=c++11']
    )

extension3 = Extension(
    name="bpgdg.bp_guessing_decoder",
    sources=["bpgdg/bp_guessing_decoder.pyx", "bpgdg/include/mod2sparse.cpp", "bpgdg/include/bpgd.cpp"],
    language='c++',
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(), 'bpgdg/include'],
    extra_compile_args=['-std=c++14']
    )

extension4 = Extension(
    name="bpgdg.osd_window",
    sources=["bpgdg/osd_window.pyx", "bpgdg/include/mod2sparse.cpp", "bpgdg/include/mod2sparse_extra.cpp", "bpgdg/include/bpgd.cpp"],
    language='c++',
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(), 'bpgdg/include'],
    extra_compile_args=['-std=c++17']
)

extension5 = Extension(
    name="bpgdg.bp4_osd",
    sources=["bpgdg/bp4_osd.pyx", "bpgdg/include/mod2sparse.cpp", "bpgdg/include/mod2sparse_extra.cpp", "bpgdg/include/bpgd.cpp"],
    language='c++',
    libraries=[],
    library_dirs=[],
    include_dirs=[numpy.get_include(), 'bpgdg/include'],
    extra_compile_args=['-std=c++17']
)

setup(
    name = "bpgdg",
    version=VERSION,
    ext_modules=cythonize([extension1, extension2, extension3, extension4, extension5]),
)
