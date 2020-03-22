# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _UTVolumeLibrary
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class VolumeRenderer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VolumeRenderer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VolumeRenderer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _UTVolumeLibrary.new_VolumeRenderer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _UTVolumeLibrary.delete_VolumeRenderer
    __del__ = lambda self : None;
    def initRenderer(*args): return _UTVolumeLibrary.VolumeRenderer_initRenderer(*args)
    def setAspectRatio(*args): return _UTVolumeLibrary.VolumeRenderer_setAspectRatio(*args)
    def setTextureSubCube(*args): return _UTVolumeLibrary.VolumeRenderer_setTextureSubCube(*args)
    def setQuality(*args): return _UTVolumeLibrary.VolumeRenderer_setQuality(*args)
    def getQuality(*args): return _UTVolumeLibrary.VolumeRenderer_getQuality(*args)
    def setNearPlane(*args): return _UTVolumeLibrary.VolumeRenderer_setNearPlane(*args)
    def getNearPlane(*args): return _UTVolumeLibrary.VolumeRenderer_getNearPlane(*args)
    def isShadedRenderingAvailable(*args): return _UTVolumeLibrary.VolumeRenderer_isShadedRenderingAvailable(*args)
    def enableShadedRendering(*args): return _UTVolumeLibrary.VolumeRenderer_enableShadedRendering(*args)
    def disableShadedRendering(*args): return _UTVolumeLibrary.VolumeRenderer_disableShadedRendering(*args)
    def uploadColorMappedData(*args): return _UTVolumeLibrary.VolumeRenderer_uploadColorMappedData(*args)
    def uploadColorMappedDataWithBorder(*args): return _UTVolumeLibrary.VolumeRenderer_uploadColorMappedDataWithBorder(*args)
    def testColorMappedData(*args): return _UTVolumeLibrary.VolumeRenderer_testColorMappedData(*args)
    def testColorMappedDataWithBorder(*args): return _UTVolumeLibrary.VolumeRenderer_testColorMappedDataWithBorder(*args)
    def uploadRGBAData(*args): return _UTVolumeLibrary.VolumeRenderer_uploadRGBAData(*args)
    def uploadGradients(*args): return _UTVolumeLibrary.VolumeRenderer_uploadGradients(*args)
    def calculateGradientsFromDensities(*args): return _UTVolumeLibrary.VolumeRenderer_calculateGradientsFromDensities(*args)
    def uploadColorMap(*args): return _UTVolumeLibrary.VolumeRenderer_uploadColorMap(*args)
    def getNumberOfPlanesRendered(*args): return _UTVolumeLibrary.VolumeRenderer_getNumberOfPlanesRendered(*args)
    def renderVolume(*args): return _UTVolumeLibrary.VolumeRenderer_renderVolume(*args)
    def uploadZeroPaddedData(*args): return _UTVolumeLibrary.VolumeRenderer_uploadZeroPaddedData(*args)
VolumeRenderer_swigregister = _UTVolumeLibrary.VolumeRenderer_swigregister
VolumeRenderer_swigregister(VolumeRenderer)

InitTexParameteri = _UTVolumeLibrary.InitTexParameteri
QueryExtension = _UTVolumeLibrary.QueryExtension

createNumArr = _UTVolumeLibrary.createNumArr

