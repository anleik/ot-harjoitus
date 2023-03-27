import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)

    def test_saldo_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(5000)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_false_jos_ei_tarpeeksi_rahaa(self):

        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)

    def test_true_jos_tarpeeksi_rahaa(self):

        self.assertEqual(self.maksukortti.ota_rahaa(500), True)