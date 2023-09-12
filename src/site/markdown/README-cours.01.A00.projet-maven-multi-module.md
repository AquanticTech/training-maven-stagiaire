## Conventions Maven pour les Projets Multi-modules

### 1. Structure du Répertoire
Un projet multi-modules a généralement une structure de répertoire parent-enfant. Le projet parent contient un fichier `pom.xml` qui liste tous les modules (sous-projets) dans la section `<modules>`.

```plaintext
mon-projet-parent/
|-- pom.xml
|-- module1/
|   |-- pom.xml
|   |-- src/
|-- module2/
    |-- pom.xml
    |-- src/
```

### 2. POM Parent
Le POM parent (fichier pom.xml à la racine) contient une section <modules> qui liste tous les sous-modules.

xml
Copy code
<modules>
    <module>module1</module>
    <module>module2</module>
</modules>

Il peut également définir des dépendances, des propriétés et des plugins communs pour tous les sous-modules.

### 3. POM des Sous-modules

Chaque sous-module a son propre `pom.xml`. Le POM du sous-module hérite du POM parent en spécifiant le groupId, l'artifactId et la version du parent dans la section `<parent>`.

```xml
<parent>
    <groupId>com.exemple</groupId>
    <artifactId>mon-projet-parent</artifactId>
    <version>1.0.0</version>
</parent>
```

## **4. Dépendances entre les Sous-modules**
Les sous-modules peuvent avoir des dépendances les uns envers les autres. 
Par exemple, si `module2` dépend de `module1`, cela serait spécifié dans le fichier `pom.xml` de `module2`,
dans la section `<dependencies>`.

## **5. Compilation et Packaging**
Lors de la compilation à partir du répertoire parent, Maven traite chaque module dans l'ordre spécifié dans le POM parent.
Les artefacts de chaque module sont généralement stockés dans le répertoire `target/` de chaque module.

## **6. Avantages**
- Facilite la gestion de projets de grande envergure.
- Permet une modularisation claire du projet.
- Les dépendances, propriétés et plugins communs peuvent être gérés centralement dans le POM parent.
