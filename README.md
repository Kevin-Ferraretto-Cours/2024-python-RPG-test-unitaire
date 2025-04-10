# Python RPG - Développement piloté par les tests (TDD)

## Équipe
- Gabriel K ([@GabYan876](https://github.com/GabYan876)).
- Kevin F. ([@MrSuricate2](https://kevin-ferraretto.fr/))
- Anis H. ([@tduki](https://github.com/tduki))
- Killian B

## À propos du projet
Ce projet vise à développer un jeu de rôle (RPG) en Python dans le cadre d'un projet scolaire. Nous adoptons une approche de développement piloté par les tests (Test-Driven Development ou TDD) pour garantir la qualité et la robustesse du code tout au long du processus de développement.

## Structure du projet
```
python-rpg/
├── src/                # Dossier contenant les classes du RPG
├── tests/              # Tests unitaires et d'intégration
├── LICENSE             # Fichier de licence MIT
└── README.md           # Documentation du projet
```

## Méthodologie TDD (Test-Driven Development)
Notre projet suit rigoureusement l'approche TDD qui se déroule en trois phases :

1. **Red** : Écrire un test qui échoue pour une fonctionnalité à implémenter
2. **Green** : Écrire le minimum de code nécessaire pour faire passer le test
3. **Refactor** : Améliorer le code tout en s'assurant que les tests continuent de passer

Cette méthode nous permet de :
- Garantir une couverture de test complète
- Concevoir du code modulaire et facile à maintenir
- Documenter le comportement attendu de chaque composant
- Faciliter le développement collaboratif
- Réduire le nombre de bugs et de régressions

## Installation et utilisation
### Prérequis
- Python 3.12 ou version ultérieure
- pytest

### Installation
```bash
# Cloner le dépôt
git clone https://github.com/Kevin-Ferraretto-Cours/2024-python-RPG-test-unitaire.git
cd 2024-python-RPG-test-unitaire

# Installer les dépendances
pip install pytest
```

### Exécution des tests
```bash
# Lancer tous les tests
pytest

# Lancer les tests avec un rapport de couverture
pytest --cov=src
```

### Workflow de développement
1. Écrire un test pour une nouvelle fonctionnalité
2. Vérifier que le test échoue (Red)
3. Implémenter la fonctionnalité minimale pour faire passer le test (Green)
4. Améliorer le code sans casser les tests (Refactor)
5. Répéter pour chaque nouvelle fonctionnalité

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
