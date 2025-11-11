import unittest
from kassapaate import Kassapaate

class TestKassapaate:
    def setUp(self):
        self.kassassa_rahaa = Kassapaate()

    def test_syo_edullisesti_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassassa_rahaa, 760)