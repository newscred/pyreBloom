from distutils.core import setup

ext_files = ["pyreBloom/bloom.c", "hiredis/async.c", "hiredis/hiredis.c", "hiredis/net.c", "hiredis/sds.c"]

kwargs = {}

try:
    from Cython.Distutils import build_ext
    from Cython.Distutils import Extension
    print "Building from Cython"
    ext_files.append("pyreBloom/pyreBloom.pyx")
    kwargs['cmdclass'] = {'build_ext': build_ext}
except ImportError:
    from distutils.core import Extension
    ext_files.append("pyreBloom/pyreBloom.c")
    print "Building from C"

ext_modules = [Extension("pyreBloom", ext_files, include_dirs=['hiredis', "."])]

setup(
    name = 'pyreBloom',
    version = "0.1.2-1",
    author = "Dan Lecocq",
    author_email = "dan@seomoz.org",
    license = "MIT License",
    ext_modules = ext_modules,
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
  **kwargs
)
