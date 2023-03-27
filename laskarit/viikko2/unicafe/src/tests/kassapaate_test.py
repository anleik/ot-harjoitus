import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_rahamaara_oikein(self):

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_luodut_lounaat_oikein(self):

        self.assertEqual(self.kassa.maukkaat + self.kassa.edulliset, 0)

#maukkaasti kateisella
    def test_syo_maukkaasti_kateisella_kassa(self):
        self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_vaihtoraha(self):
    
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_rahapuute_kassa(self):
        self.kassa.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_rahapuute_vaihtoraha(self):
        
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)

    def test_syo_maukkaasti_kateisella_rahapuute_lounaiden_maara(self):
        self.kassa.syo_maukkaasti_kateisella(350)
        
        self.assertEqual(self.kassa.maukkaat, 0)

#edullisesti kateisella
    def test_syo_edullisesti_kateisella_kassa(self):
        self.kassa.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_vaihtoraha(self):
    
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)

    def test_syo_edullisesti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kateisella_rahapuute_kassa(self):
        self.kassa.syo_edullisesti_kateisella(150)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_rahapuute_vaihtoraha(self):
        
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(150), 150)

    def test_syo_edullisesti_kateisella_rahapuute_lounaiden_maara(self):
        self.kassa.syo_edullisesti_kateisella(150)
        
        self.assertEqual(self.kassa.edulliset, 0)


#maukkaasti kortilla

    def test_syo_maukkaasti_kortilla_kassa(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_true(self):
    
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.maksukortti), True)


    def test_syo_maukkaasti_kortilla_veloitus(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    
    def test_syo_maukkaasti_kortilla_lounaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_rahapuute_kassa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)

    def test_syo_maukkaasti_kortilla_rahapuute_false(self):
        kortti = Maksukortti(200)
        

        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)

    def test_syo_maukkaasti_kortilla_rahapuute_lounaiden_maara(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(self.kassa.maukkaat, 0)

#edullisesti kortilla

    def test_syo_edullisesti_kortilla_kassa(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_true(self):
    
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksukortti), True)


    def test_syo_edullisesti_kortilla_veloitus(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    
    def test_syo_edullisesti_kortilla_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kortilla_rahapuute_kassa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)

    def test_syo_edullisesti_kortilla_rahapuute_false(self):
        kortti = Maksukortti(200)
        

        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)

    def test_syo_edullisesti_kortilla_rahapuute_lounaiden_maara(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(self.kassa.edulliset, 0)

#kortin lataus

    def test_kortin_lataus_kassa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 1000)
        
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortin_lataus_kortti(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 1000)
        
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortin_lataus_negatiivinen_kassa(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -5000)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortin_lataus_negatiivinen_kortti(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -5000)

        self.assertEqual(self.maksukortti.saldo, 1000)