# Tasohyppelypeli  
Pelissä ohjataan hahmoa nuolinäppäimillä.  
Tavoite on ohjata hahmo tason lopussa olevaan maaliin.  
ESC = Save and Exit  


## Uusin release  
[Viikko 6](https://github.com/anleik/ot-harjoitus/releases/tag/viikko6)  


## Dokumentaatio  
[Käyttöohje](/dokumentaatio/kayttoohje.md)  
[Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
[Changelog](dokumentaatio/changelog.md)  
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)  
[Testausdokumentti](dokumentaatio/testaus.md)  

## Asennus ja käynnistys  
Kirjoita komentoriville:  
```bash
poetry install  
poetry run invoke start  
```

## Komentoja  

Lint:  
```bash
poetry run invoke lint  
```

Testaus:  
```bash
poetry run invoke test  
```

Testikattavuusraportti:  
```bash
poetry run invoke coverage-report  
```
