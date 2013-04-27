import os
import sys
import string

from SCons.Script import *

Env = None

def PrepareBuilding(env, root_directory, has_libcpu=False, remove_components = []):
    # import SCons.cpp
    import avrconfig

    global Env

    Env = env

    # add program path
    env.PrependENVPath('PATH', avrconfig.EXEC_PATH)

    # board build script
    objs = SConscript('SConscript', variant_dir='build', duplicate=0)

    return objs

def GetCurrentDir():
    conscript = File('SConscript')
    fn = conscript.rfile()
    name = fn.name
    path = os.path.dirname(fn.abspath)
    return path
    
def DefineGroup(name, src, **parameters):
    global Env

    group = parameters
    group['name'] = name
    if type(src) == type(['src1', 'str2']):
        group['src'] = File(src)
    else:
        group['src'] = src

    if group.has_key('CCFLAGS'):
        Env.Append(CCFLAGS = group['CCFLAGS'])
    if group.has_key('CPPPATH'):
        Env.Append(CPPPATH = group['CPPPATH'])
    if group.has_key('CPPDEFINES'):
        Env.Append(CPPDEFINES = group['CPPDEFINES'])
    if group.has_key('LINKFLAGS'):
        Env.Append(LINKFLAGS = group['LINKFLAGS'])
    if group.has_key('LIBS'):
        Env.Append(LIBS = group['LIBS'])
    if group.has_key('LIBPATH'):
        Env.Append(LIBPATH = group['LIBPATH'])

    objs = Env.Object(group['src'])

    if group.has_key('LIBRARY'):
        objs = Env.Library(name, objs)

    return objs
    
def EndBuilding(target, program = None):
    import avrconfig

    Env.AddPostAction(target, avrconfig.POST_ACTION)

