import pytest
from LibreGaming.LibreGaming import *

def test_getPackageManager():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.getPackageManager() != 'Unknown distro'

def test_installAllPkgs():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.installAllPkgs() == 'success'

def test_BasicPkgs():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.BasicPkgs() == 'success'

def test_Lutris():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.Lutris() == 'success'

def test_Heroic():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.Heroic() == 'success'

def test_Overlays():
    LibreGaming_Object = LibreGaming()
    assert LibreGaming_Object.Overlays() == 'success'