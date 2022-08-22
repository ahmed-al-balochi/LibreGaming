import unittest
from LibreGaming.LibreGaming import *

class LibraGamingTests(unittest.TestCase):
    LibreGaming_Object = LibreGaming()

    def test_getPackageManager(self):
        self.assertNotEqual(self.LibreGaming_Object.getPackageManager(), 'Unknown distro')
    
    def test_installAllPkgs(self):
        self.assertEqual(self.LibreGaming_Object.installAllPkgs(), 'success')
    
    def test_BasicPkgs(self):
        self.assertEqual(self.LibreGaming_Object.BasicPkgs(), 'success')
    
    def test_Lutris(self):
        self.assertEqual(self.LibreGaming_Object.Lutris(), 'success')

    def test_Heroic(self):
        self.assertEqual(self.LibreGaming_Object.Heroic(), 'success')
    
    def test_Overlays(self):
        self.assertEqual(self.LibreGaming_Object.Overlays(), 'success')

if __name__ == '__main__':
    unittest.main()