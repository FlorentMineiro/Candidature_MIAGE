# MIAGE Admission Analyzer

Outil d'analyse des chances d'admission en MIAGE (Méthodes Informatiques Appliquées à la Gestion des Entreprises) pour un étudiant en BTS SIO SLAM.

## Description

Ce projet analyse les bulletins de notes de l'étudiant et génère un rapport détaillé incluant :

- **Profil académique** : moyennes par domaine, classement dans la classe
- **Analyse SWOT** : points forts et faiblesses du profil
- **Estimation par université** : chances d'admission pour chacune des 21 universités MIAGE de France
- **Recommandations** : stratégie de candidature personnalisée

## Structure du projet

- `grades_data.py` — Données brutes des bulletins (L1 Maths, L2 Maths, BTS SIO 1A/2A)
- `universities.py` — Base de données des 21 universités MIAGE avec niveaux de sélectivité
- `analyzer.py` — Moteur d'analyse (moyennes pondérées, scores par domaine, estimation des chances)
- `main.py` — Script principal générant le rapport complet

## Utilisation

```bash
python main.py
```

## Sources

- [Réseau MIAGE France](https://www.miage.fr/)
- Bulletins de notes UPEC (2019-2022) et Le Rebours (2024-2026)
- Données de sélectivité : Wikipedia, Thotis, sites des universités
