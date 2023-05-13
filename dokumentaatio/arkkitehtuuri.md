# Arkkitehtuuri  

## Ohjelman rakenne  

![Rakenne](.kuvat/rakenne.png)

Pakkaus ui vastaa käyttöliittymästä.  
Pakkaus database vastaa tiedon tallennuksesta.  
Pakkaus entities vastaa pelin objekteista.  
Pakkaus services vastaa pelin toiminnasta ja hyödyntää/kutsuu muita paketteja tarvittaessa.  



## Tiedon tallennus (sequence chart)  

```mermaid
sequenceDiagram
    GameState->> GameState: Is there data.db?
    GameState ->> GameState: False: Create data.db
    GameState ->>+ Database: True: Retrieve progress from data.db
    Database-->>-GameState: Progress
    GameState ->> Database: Exit: save progress in data.db
```
