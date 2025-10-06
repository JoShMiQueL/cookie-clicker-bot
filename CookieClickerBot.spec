# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/config.py', 'src'),
        ('src/window_finder.py', 'src'),
        ('src/clicker.py', 'src'),
        ('src/overlay.py', 'src'),
        ('src/__init__.py', 'src'),
    ],
    hiddenimports=[
        'win32api',
        'win32con',
        'win32gui',
        'keyboard',
        'tkinter',
        'threading',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CookieClickerBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
