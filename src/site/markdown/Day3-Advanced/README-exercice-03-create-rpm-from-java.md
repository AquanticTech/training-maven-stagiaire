# Exercice : Création d'un package RPM à partir d'un code source Java

## Objectif

Votre mission est de créer un package RPM pour une application Java simple. Cette application affichera simplement "Bonjour, RPM !" lorsqu'elle sera exécutée.

## Instructions

1. **Préparation de l'environnement** :
   - Installez les outils nécessaires pour la création de packages RPM. Sur une distribution basée sur Red Hat, vous pouvez utiliser la commande suivante :
     ```
     sudo yum install rpm-build rpmdevtools
     ```

2. **Configuration de l'environnement de construction RPM** :
   - Exécutez la commande suivante pour créer l'arborescence nécessaire :
     ```
     rpmdev-setuptree
     ```

3. **Création de l'application Java** :
   - Écrivez un programme Java simple nommé `HelloRPM.java` avec le contenu suivant :
     ```java
     public class HelloRPM {
         public static void main(String[] args) {
             System.out.println("Bonjour, RPM !");
         }
     }
     ```
   - Compilez le programme avec la commande :
     ```
     javac HelloRPM.java
     ```

4. **Création du fichier SPEC** :
   - Dans le répertoire `~/rpmbuild/SPECS`, créez un fichier nommé `hello-rpm.spec` avec le contenu suivant :
     ```spec
     Name: hello-rpm
     Version: 1.0
     Release: 1%{?dist}
     Summary: Une application Java simple pour dire bonjour

     License: GPLv3+
     URL: http://example.com/hello-rpm
     Source0: HelloRPM.class

     %description
     Une application Java simple qui affiche "Bonjour, RPM !".

     %install
     mkdir -p %{buildroot}/opt/hello-rpm
     cp %{SOURCE0} %{buildroot}/opt/hello-rpm

     %files
     /opt/hello-rpm/HelloRPM.class

     %post
     echo "Merci d'avoir installé hello-rpm !"

     %changelog
     # let's skip this from the moment
     ```

5. **Création du package RPM** :
   - Placez le fichier `HelloRPM.class` dans le répertoire `~/rpmbuild/SOURCES`.
   - Dans le répertoire `~/rpmbuild/SPECS`, exécutez la commande suivante pour créer le package RPM :
     ```
     rpmbuild -ba hello-rpm.spec
     ```

6. **Vérification** :
   - Vous devriez trouver votre package RPM dans le répertoire `~/rpmbuild/RPMS`.

## Question bonus

Comment pourriez-vous améliorer ce processus pour inclure des dépendances, comme une bibliothèque externe que votre application Java pourrait utiliser ?

---

# Réponse

Vous avez déjà la réponse détaillée dans les instructions ci-dessus. Pour la question bonus, voici une réponse possible :

Pour inclure des dépendances, vous pouvez utiliser des outils comme Maven ou Gradle pour gérer les dépendances de votre projet Java. Une fois que vous avez un fichier JAR exécutable avec toutes les dépendances incluses, vous pouvez l'inclure dans votre package RPM. Dans le fichier SPEC, vous devrez ajuster la section `%files` pour inclure ce JAR et éventuellement ajouter des scripts post-installation pour configurer les chemins ou les variables d'environnement nécessaires pour exécuter votre application.
