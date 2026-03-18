"""
Données académiques extraites des bulletins de notes de MINEIRO Florent.
"""

STUDENT = {
    "nom": "MINEIRO",
    "prenom": "Florent",
    "date_naissance": "08/05/2001",
    "ine": "090815042EE",
    "numero_etudiant": "21913873",
}

# =============================================================================
# L1 Mathématiques - UPEC Paris 12 - 2019/2020
# =============================================================================
L1_MATHS = {
    "etablissement": "Université Paris 12 - Val de Marne (UPEC)",
    "annee": "2019/2020",
    "formation": "Licence 1 Mathématiques parcours Mathématiques",
    "semestre_1": {
        "moyenne": 12.141,
        "resultat": "Admis",
        "credits_valides": 30,
        "matieres": [
            {"nom": "Algèbre 1", "note": 15.99, "resultat": "Admis", "credits": 6},
            {"nom": "Analyse 1", "note": 17.997, "resultat": "Admis", "credits": 6},
            {"nom": "Anglais", "note": 11.0, "resultat": "Admis", "credits": 3},
            {"nom": "Initiation algorithmique et outils info", "note": 12.5, "resultat": "Admis", "credits": 3},
            {"nom": "Introduction à la physique", "note": 9.468, "resultat": "Ajourné", "credits": 0},
            {"nom": "Programmation 1", "note": 1.0, "resultat": "Ajourné", "credits": 0},
            {"nom": "Techniques d'expression et méthodologie", "note": 10.0, "resultat": "Admis", "credits": 3},
        ],
    },
    "semestre_2": {
        "moyenne": 9.96,
        "resultat": "Ajourné",
        "credits_valides": 15,
        "matieres": [
            {"nom": "Algèbre 2", "note": 16.0, "resultat": "Admis", "credits": 6},
            {"nom": "Analyse 2", "note": 16.0, "resultat": "Admis", "credits": 6},
            {"nom": "Anglais L1S2", "note": 8.5, "resultat": "Ajourné", "credits": 0},
            {"nom": "Électrocinétique", "note": 15.1, "resultat": "Admis", "credits": 3},
            {"nom": "Option transversale", "note": 0.0, "resultat": "Ajourné", "credits": 0},
            {"nom": "Programmation 2", "note": 3.75, "resultat": "Ajourné", "credits": 0},
            {"nom": "Techniques d'expression", "note": 4.5, "resultat": "Ajourné", "credits": 0},
        ],
    },
}

# =============================================================================
# L2 Mathématiques - UPEC Paris 12 - 2021/2022
# =============================================================================
L2_MATHS = {
    "etablissement": "Université Paris 12 - Val de Marne (UPEC)",
    "annee": "2021/2022",
    "formation": "Licence 2 Mathématiques",
    "semestre_3": {
        "moyenne": 3.66,
        "resultat": "Ajourné",
        "matieres": [
            {"nom": "Anglais scientifique", "note": 2.25, "resultat": "Ajourné"},
            {"nom": "Espaces euclidiens", "note": 8.0, "resultat": "Ajourné"},
            {"nom": "Option Mathématiques", "note": 0.675, "resultat": "Ajourné"},
            {"nom": "Option Méca ou Electromag", "note": 0.675, "resultat": "Ajourné"},
            {"nom": "Arts et nouveaux médias", "note": 0.0},
            {"nom": "Proba Discrète et BD", "note": 2.0, "resultat": "Ajourné"},
            {"nom": "Séries et intégrales", "note": 6.5, "resultat": "Ajourné"},
        ],
    },
    "semestre_4": {
        "moyenne": 6.745,
        "resultat": "Ajourné",
        "matieres": [
            {"nom": "Anglais scientifique", "note": 9.75, "resultat": "Ajourné"},
            {"nom": "Accompagnement personnalisé", "note": 11.5, "resultat": "Admis", "credits": 3},
            {"nom": "Fonctions de plusieurs variables", "note": 3.5, "resultat": "Ajourné"},
            {"nom": "Groupes et anneaux", "note": 9.0, "resultat": "Ajourné"},
            {"nom": "Réduction des endomorphismes", "note": 6.6, "resultat": "Ajourné"},
            {"nom": "Suites et séries de fonctions", "note": 4.0, "resultat": "Ajourné"},
        ],
    },
    "resultat_global": {
        "moyenne": 5.203,
        "resultat": "Ajourné",
    },
}

# =============================================================================
# BTS SIO 1ère Année - Le Rebours - 2024/2025 (Option SLAM)
# =============================================================================
BTS_SIO_1A = {
    "etablissement": "Le Rebours - Paris",
    "annee": "2024/2025",
    "formation": "BTS Services Informatiques aux Organisations 1ère Année - Option SLAM",
    "effectif": 29,
    "semestre_1": {
        "appreciation_conseil": "Étudiant moteur dans sa formation. Félicitations.",
        "matieres": [
            {"nom": "Culture Générale et Expression", "coef": 2, "note": 16.4, "classe": 12.5, "min": 4.4, "max": 17.2},
            {"nom": "Anglais LV1", "coef": 2, "note": 16.7, "classe": 12.8, "min": 6.4, "max": 16.9},
            {"nom": "Maths pour Informatique", "coef": 3, "note": 18.9, "classe": 8.4, "min": 1.4, "max": 18.9},
            {"nom": "Culture Éco. Juridique et Managériale", "coef": 3, "note": 13.5, "classe": 11.2, "min": 5.8, "max": 13.7},
            {"nom": "Bloc 1 - SMDSI", "coef": 8, "note": 15.8, "classe": 9.0, "min": 3.0, "max": 17.0},
            {"nom": "Bloc 3 - Cyber Sécurité", "coef": 2, "note": 11.9, "classe": 9.6, "min": 4.5, "max": 14.0},
            {"nom": "AT. Professionnalisation", "coef": 2, "note": 14.2, "classe": 13.8, "min": 9.7, "max": 16.7},
            {"nom": "Maths Approfondies", "coef": 1, "note": 19.7, "classe": 9.3, "min": 0.7, "max": 19.7},
        ],
    },
    "semestre_2": {
        "appreciation_conseil": "Très bon semestre. Étudiant sérieux et moteur. Félicitations.",
        "matieres": [
            {"nom": "Culture Générale et Expression", "coef": 2, "note": 14.4, "classe": 11.0, "min": 5.0, "max": 15.2},
            {"nom": "Anglais LV1", "coef": 2, "note": 15.8, "classe": 14.6, "min": 8.2, "max": 18.5},
            {"nom": "Maths pour Informatique", "coef": 3, "note": 17.2, "classe": 9.6, "min": 2.5, "max": 17.2},
            {"nom": "Culture Éco. Juridique et Managériale", "coef": 3, "note": 12.6, "classe": 11.9, "min": 10.0, "max": 14.0},
            {"nom": "Bloc 1 - SISR/SLAM", "coef": 3, "note": 17.2, "classe": 12.0, "min": 4.5, "max": 17.6},
            {"nom": "Bloc 2 - SLAM", "coef": 4, "note": 16.7, "classe": 12.7, "min": 7.7, "max": 18.5},
            {"nom": "Bloc 3 - Cyber Sécurité", "coef": 3, "note": 13.3, "classe": 10.6, "min": 4.7, "max": 15.5},
            {"nom": "AT. Professionnalisation", "coef": 2, "note": 11.8, "classe": 12.0, "min": 8.3, "max": 16.2},
            {"nom": "Maths Approfondies", "coef": 1, "note": 18.3, "classe": 14.1, "min": 9.4, "max": 18.3},
        ],
    },
}

# =============================================================================
# BTS SIO 2ème Année - Le Rebours - 2025/2026 (Option SLAM)
# =============================================================================
BTS_SIO_2A = {
    "etablissement": "Le Rebours - Paris",
    "annee": "2025/2026",
    "formation": "BTS Services Informatiques aux Organisations 2ème Année",
    "effectif": 25,
    "semestre_1": {
        "appreciation_conseil": "Semestre positif, mais vous pouvez mieux faire. Compliments.",
        "matieres": [
            {"nom": "Culture Générale et Expression", "coef": 2, "note": 17.0, "classe": 11.6, "min": 3.4, "max": 17.0},
            {"nom": "Anglais LV1", "coef": 2, "note": 12.9, "classe": 12.7, "min": 7.6, "max": 17.4},
            {"nom": "Maths Informatique", "coef": 2, "note": 16.5, "classe": 10.3, "min": 4.9, "max": 16.5},
            {"nom": "Culture Éco. Juridique et Managériale", "coef": 3, "note": 12.5, "classe": 12.2, "min": 6.2, "max": 15.5},
            {"nom": "Bloc 1 - SMDSI", "coef": 1, "note": 9.8, "classe": 10.7, "min": 3.0, "max": 15.0},
            {"nom": "Bloc 2 - SLAM", "coef": 5, "note": 8.8, "classe": 6.0, "min": 1.8, "max": 11.1},
            {"nom": "Bloc 3 - SLAM", "coef": 3, "note": 12.5, "classe": 10.7, "min": 6.5, "max": 14.7},
            {"nom": "Maths Approfondies", "coef": 1, "note": 16.2, "classe": 10.6, "min": 2.3, "max": 16.8},
        ],
    },
}
