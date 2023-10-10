#############################################
# Install un module et une dépendance dans un fichier pom.xml si on ne veut pas modifier le fichier à la main
#############################################

import os
import xml.etree.ElementTree as ET

def add_dependency_to_pom(pomPath, group_id, artifact_id, version):
    # Parse le pom.xml
    tree = ET.parse(pomPath + '/pom.xml')
    root = tree.getroot()

    # Espace de noms Maven
    ns = {'mvn': 'http://maven.apache.org/POM/4.0.0'}

    # Trouve ou crée l'élément <dependencies>
    dependencies = root.find('mvn:dependencies', ns)
    if dependencies is None:
        dependencies = ET.SubElement(root, 'dependencies')

    # Ajoute la nouvelle dépendance
    dependency = ET.SubElement(dependencies, 'dependency')
    ET.SubElement(dependency, 'groupId').text = group_id
    ET.SubElement(dependency, 'artifactId').text = artifact_id
    ET.SubElement(dependency, 'version').text = version

    # Enregistre le pom.xml modifié
    tree.write('pom.xml')

    # Exécute mvn install
    os.system('mvn install')

# Utilisation
pomPath = input("Entrez le chemin du répertoire où se trouve votre pom : ")
group_id = input("Entrez le groupId de la dépendance : ")
artifact_id = input("Entrez l'artifactId de la dépendance : ")
version = input("Entrez la version de la dépendance : ")

add_dependency_to_pom(pomPath, group_id, artifact_id, version)
