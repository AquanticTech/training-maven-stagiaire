## Conventions Maven

### 1. Le code source
- **Chemin par défaut :** `src/main/java`
- Maven s'attend à ce que le code source soit dans ce répertoire.

### 2. Le code de tests
- **Chemin par défaut :** `src/test/java`
- Maven s'attend à ce que le code de tests soit dans ce répertoire.

### 3. L'utilisation de plugin
- Les plugins Maven fournissent des fonctionnalités supplémentaires à Maven.
- Pour utiliser un plugin, il doit être défini dans la section `<plugins>` du `pom.xml`.
- Chaque plugin peut avoir des objectifs qui peuvent être exécutés en utilisant la commande : `mvn [nom-du-plugin]:[nom-de-l'objectif]`.

### 4. L'utilisation et la configuration de sécurité
- Maven utilise le fichier `settings.xml` pour configurer les informations d'authentification pour les dépôts distants.
- Les informations sensibles, comme les mots de passe, peuvent être chiffrées en utilisant le `maven-encrypt-password` de Maven.

### 5. Informations de chemin par défaut et autres
- **Répertoire des ressources :** `src/main/resources`
- **Répertoire des ressources de test :** `src/test/resources`
- **Répertoire de sortie par défaut (où les fichiers compilés sont stockés) :** `target/`
- **Fichier POM :** `pom.xml`
  - C'est le fichier de configuration principal de Maven.

