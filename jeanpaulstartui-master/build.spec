# -*- mode: python -*-

import os, sys, platform

directory = '.'
rcpath = './jeanpaulstartui/resources'
binpath = os.path.join( directory, 'bin' )

ext = ''
icon = ''
syst = ''
pathex = []
bundle = True	# Create .app bundle
app_name = 'Jean-Paul Start'
app_version = 2

p = platform.system()
name = sys.argv[ 1 ][ :-5 ]

if p.find( 'Windows' ) >= 0:
	ext = '.exe'
	icon = 'ico'
	syst = 'win'
	pathex.append( 'C:\\Users\\' + os.getenv( 'USERNAME' ) + '\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\PyQt5' )
	pathex.append( 'C:\\Users\\' + os.getenv( 'USERNAME' ) + '\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\PyQt5\\Qt\\bin' )
	pathex.append( 'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x64' )
elif p.find( 'Darwin' ) >= 0:
	ext = '.app'
	icon = 'icns'
	syst = 'osx'
	pathex.append( '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PyQt5' )
elif p.find( 'Linux' ) >= 0:
	icon = 'png'
	syst = 'lnx'
	pathex.append( '/home/' + os.getenv( 'USER' ) + '/.local/lib/python3.7/site-packages/PyQt5' )
else:
	raise ( Exception( 'Unsupported System' ) )
	sys.exit( 1 )

block_cipher = None
binpath = os.path.join( binpath, syst )

a = Analysis(
	[ 'jeanpaulstartui/__main__.py' ],
	pathex					= pathex,
	binaries				= [],
	datas					= [
		( os.path.join( rcpath, 'stylesheet.css' ),					'./rc' ),
		( os.path.join( rcpath, 'ceci-n-est-pas-une-icone.png' ),	'./rc' )
	],
	hiddenimports			= [],
	hookspath				= [],
	runtime_hooks			= [],
	excludes				= [],
	win_no_prefer_redirects	= False,
	win_private_assemblies	= False,
	cipher					= block_cipher
)

a.datas += Tree( binpath, prefix = './bin', excludes = [ 'Thumbs.db', '.DS_Store' ], typecode = 'DATA' )

pyz = PYZ(
	a.pure,
	a.zipped_data,
	cipher					= block_cipher
)

if syst != 'osx':
	name = app_name

exe = EXE(
	pyz,
	a.scripts,
	a.binaries,
	a.zipfiles,
	a.datas,
	name					= name,
	debug					= False,
	strip					= False,
	upx						= False,
	console					= False,
	icon					= os.path.join( rcpath, 'ceci-n-est-pas-une-icone.' + icon )
)

# MacOS Bundle (.app) don't open console
if bundle:
	app = BUNDLE(
		exe,
		name				= app_name + ext,
		icon				= os.path.join( rcpath, 'ceci-n-est-pas-une-icone.' + icon ),
		bundle_identifier	= None,
		info_plist			= {
			'LSBackgroundOnly':			'True',
			'NSHighResolutionCapable':	'True'
		}
	)
