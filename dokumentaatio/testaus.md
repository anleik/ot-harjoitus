# Testausdokumentti

Ohjelmaa voidaan testata komentoriviltä:  
```bash
poetry run invoke test  
```

Testikattavuusraportti generoidaan komennolla:    
```bash
poetry run invoke coverage-report  
```

- Testikattavuuden ulkopuolelle on jätetty ui-hakemisto ja main.py jossa on gameloop.  

  
Pelin asennus ja toiminta on testattu manuaalisesti Windowsilla ja Linuxilla.  
Tallennusominaisuus on testattu olemassaolevalla data.db-tiedostolla ja silloin kun se puuttuu.  
