# Tasohyppelypeli  
Pelissä ohjataan hahmoa nuolinäppäimillä.  
Tavoite on ohjata hahmo maaliin (99m)  
ESC = Save and Exit  


## Uusin release  
[Viikko 6](https://github.com/anleik/ot-harjoitus/releases/tag/viikko6)  


## Dokumentaatio  
[Käyttöohje](/dokumentaatio/kayttoohje.md)  
[Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
[Changelog](dokumentaatio/changelog.md)  
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)  

## Asennus ja käynnistys  
Komentoriville:  
- poetry install  
- poetry run invoke start  

## Komentoja  

Lint:  
- poetry run invoke lint  
  
Testikattavuusraportti:  
- poetry run invoke coverage-report  
