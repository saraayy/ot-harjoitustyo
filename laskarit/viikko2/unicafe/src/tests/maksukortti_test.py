import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20)

    def test_raha_vahenee_oikein_kun_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo, 900)

    def test_saldo_ei_muutu_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000) 

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahat_riittavat(self):
        if self.maksukortti.ota_rahaa(2000) > self.maksukortti.saldo:
            return False

        else:
            return True 
