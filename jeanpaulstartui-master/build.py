#!/usr/bin/env python3 -B
# -*- coding: utf-8 -*-

import os, subprocess

path = '..'
spec = 'build.spec'
subprocess.run( [ 'pyinstaller', spec, '--distpath', os.path.join( path, 'dist' ), '--workpath', os.path.join( path, 'build' ) ], cwd = '.' )

try:
	os.remove( os.path.join( 'dist', '.'.join( spec.split( '.' )[ 0:-1 ] ) ) )
except:
	pass
