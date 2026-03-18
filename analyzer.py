"""
Moteur d'analyse des chances d'admission en MIAGE (L2 et L3).

La MIAGE (Méthodes Informatiques Appliquées à la Gestion des Entreprises)
évalue les candidats sur :
- Niveau en mathématiques
- Niveau en informatique / programmation
- Niveau en gestion / économie / management
- Culture générale et anglais
- Cohérence du parcours et motivation
"""

from grades_data import L1_MATHS, L2_MATHS, BTS_SIO_1A, BTS_SIO_2A
from universities import UNIVERSITIES_MIAGE


def moyenne_ponderee(matieres):
    """Calcule la moyenne pondérée d'une liste de matières avec coefficients."""
    total_notes = 0
    total_coefs = 0
    for m in matieres:
        coef = m.get("coef", 1)
        total_notes += m["note"] * coef
        total_coefs += coef
    return total_notes / total_coefs if total_coefs > 0 else 0


def moyenne_simple(matieres):
    """Calcule la moyenne simple d'une liste de matières."""
    if not matieres:
        return 0
    return sum(m["note"] for m in matieres) / len(matieres)


def rang_dans_classe(note, classe_avg, min_note, max_note):
    """Estime le rang percentile dans la classe (100 = meilleur)."""
    if max_note == min_note:
        return 50
    return ((note - min_note) / (max_note - min_note)) * 100


def extract_bts_domain_scores():
    """
    Extrait les scores par domaine pertinent pour la MIAGE
    à partir des bulletins BTS SIO.
    Retourne un dict avec les moyennes par domaine.
    """
    all_maths = []
    all_info = []
    all_gestion = []
    all_general = []
    all_anglais = []

    for bts in [BTS_SIO_1A, BTS_SIO_2A]:
        for sem_key in ["semestre_1", "semestre_2"]:
            if sem_key not in bts:
                continue
            for m in bts[sem_key]["matieres"]:
                nom = m["nom"].lower()
                if "math" in nom:
                    all_maths.append(m["note"])
                elif any(k in nom for k in ["slam", "sisr", "smdsi", "cyber", "bloc"]):
                    all_info.append(m["note"])
                elif any(k in nom for k in ["éco", "eco", "jur", "manag"]):
                    all_gestion.append(m["note"])
                elif "anglais" in nom:
                    all_anglais.append(m["note"])
                elif any(k in nom for k in ["culture", "expression"]):
                    all_general.append(m["note"])

    return {
        "mathematiques": sum(all_maths) / len(all_maths) if all_maths else 0,
        "informatique": sum(all_info) / len(all_info) if all_info else 0,
        "gestion_management": sum(all_gestion) / len(all_gestion) if all_gestion else 0,
        "anglais": sum(all_anglais) / len(all_anglais) if all_anglais else 0,
        "culture_generale": sum(all_general) / len(all_general) if all_general else 0,
    }


def compute_bts_weighted_averages():
    """Calcule les moyennes pondérées pour chaque semestre BTS."""
    results = {}
    for label, bts in [("BTS SIO 1A", BTS_SIO_1A), ("BTS SIO 2A", BTS_SIO_2A)]:
        for sem_key in ["semestre_1", "semestre_2"]:
            if sem_key not in bts:
                continue
            sem = bts[sem_key]
            avg = moyenne_ponderee(sem["matieres"])
            sem_label = f"{label} - S{'1' if '1' in sem_key else '2'}"
            results[sem_label] = {
                "moyenne_ponderee": round(avg, 2),
                "appreciation": sem.get("appreciation_conseil", ""),
            }
    return results


def compute_class_rankings():
    """Calcule le rang estimé dans la classe pour chaque semestre BTS."""
    rankings = {}
    for label, bts in [("BTS SIO 1A", BTS_SIO_1A), ("BTS SIO 2A", BTS_SIO_2A)]:
        for sem_key in ["semestre_1", "semestre_2"]:
            if sem_key not in bts:
                continue
            sem = bts[sem_key]
            rangs = []
            for m in sem["matieres"]:
                if "classe" in m and "min" in m and "max" in m:
                    r = rang_dans_classe(m["note"], m["classe"], m["min"], m["max"])
                    rangs.append(r)
            avg_rang = sum(rangs) / len(rangs) if rangs else 50
            sem_label = f"{label} - S{'1' if '1' in sem_key else '2'}"
            rankings[sem_label] = round(avg_rang, 1)
    return rankings


def analyze_strengths_weaknesses():
    """Identifie les points forts et faibles du profil pour la MIAGE."""
    scores = extract_bts_domain_scores()
    strengths = []
    weaknesses = []

    # Maths
    if scores["mathematiques"] >= 16:
        strengths.append(
            f"Excellent niveau en mathématiques ({scores['mathematiques']:.1f}/20) "
            "— critère majeur pour la MIAGE"
        )
    elif scores["mathematiques"] >= 12:
        strengths.append(
            f"Bon niveau en mathématiques ({scores['mathematiques']:.1f}/20)"
        )
    else:
        weaknesses.append(
            f"Niveau en mathématiques insuffisant ({scores['mathematiques']:.1f}/20)"
        )

    # Informatique
    if scores["informatique"] >= 14:
        strengths.append(
            f"Très bon niveau en informatique ({scores['informatique']:.1f}/20) "
            "— BTS SIO option SLAM très pertinent"
        )
    elif scores["informatique"] >= 10:
        strengths.append(
            f"Niveau correct en informatique ({scores['informatique']:.1f}/20)"
        )
    else:
        weaknesses.append(
            f"Niveau en informatique à améliorer ({scores['informatique']:.1f}/20)"
        )

    # Gestion
    if scores["gestion_management"] >= 12:
        strengths.append(
            f"Bon niveau en gestion/management ({scores['gestion_management']:.1f}/20) "
            "— composante essentielle de la MIAGE"
        )
    elif scores["gestion_management"] >= 10:
        pass  # neutre
    else:
        weaknesses.append(
            f"Niveau en gestion/management faible ({scores['gestion_management']:.1f}/20)"
        )

    # Anglais
    if scores["anglais"] >= 14:
        strengths.append(
            f"Bon niveau en anglais ({scores['anglais']:.1f}/20)"
        )

    # Parcours antérieur
    weaknesses.append(
        "L2 Maths non validée à l'UPEC (5.2/20) — point négatif visible dans le dossier"
    )

    strengths.append(
        "L1 Maths S1 validée avec 12.14/20 (bonnes notes en algèbre/analyse)"
    )

    strengths.append(
        "Appréciations BTS très positives : Félicitations x2, étudiant moteur"
    )

    strengths.append(
        "Progression remarquable entre L2 Maths (échec) et BTS SIO (excellence)"
    )

    strengths.append(
        "BTS SIO SLAM = double compétence Informatique + Gestion, idéal pour la MIAGE"
    )

    return strengths, weaknesses


def estimate_l3_miage_chances():
    """
    Estime les chances d'admission en L3 MIAGE.

    Avec un BTS SIO, l'entrée standard en MIAGE est en L3.
    Critères principaux :
    - Niveau académique global (surtout maths + info)
    - Cohérence du parcours avec la MIAGE
    - Appréciations et progression
    - Sélectivité de la formation visée
    """
    scores = extract_bts_domain_scores()
    bts_avgs = compute_bts_weighted_averages()
    rankings = compute_class_rankings()

    # Score de base sur les matières clés (40%)
    math_score = min(scores["mathematiques"] / 20 * 100, 100)
    info_score = min(scores["informatique"] / 20 * 100, 100)
    gestion_score = min(scores["gestion_management"] / 20 * 100, 100)
    academic_base = (math_score * 0.35 + info_score * 0.40 + gestion_score * 0.25)

    # Moyenne générale BTS (20%)
    bts_moyennes = [v["moyenne_ponderee"] for v in bts_avgs.values()]
    bts_global = sum(bts_moyennes) / len(bts_moyennes) if bts_moyennes else 10
    bts_score = min(bts_global / 20 * 100, 100)

    # Rang dans la classe (15%)
    avg_ranking = sum(rankings.values()) / len(rankings) if rankings else 50
    ranking_score = avg_ranking

    # Cohérence parcours (15%) - BTS SIO SLAM = très cohérent pour MIAGE
    coherence_score = 80  # BTS SIO est un bon tremplin vers MIAGE

    # Pénalité parcours antérieur (10%)
    # L2 Maths échouée est un point négatif
    historical_penalty = 35  # Score faible à cause de l'échec en L2

    total = (
        academic_base * 0.40
        + bts_score * 0.20
        + ranking_score * 0.15
        + coherence_score * 0.15
        + historical_penalty * 0.10
    )

    # Ajustements
    # Bonus pour les félicitations du conseil de classe
    total += 3
    # Bonus pour la progression démontrée
    total += 2
    # Malus pour la baisse en 2A S1 (Bloc 2 SLAM à 8.8)
    total -= 2

    # La L3 MIAGE est sélective, on applique un facteur de sélectivité
    # Les universités comme Paris-Saclay, Paris-Dauphine sont très sélectives (~20-30%)
    # Les universités comme UPEC, Nanterre, Gustave Eiffel sont moins sélectives (~40-60%)
    chances_universite_selective = max(0, min(100, total * 0.55))
    chances_universite_moyenne = max(0, min(100, total * 0.75))
    chances_universite_accessible = max(0, min(100, total * 0.90))

    return {
        "score_brut": round(total, 1),
        "universite_tres_selective": round(chances_universite_selective, 1),
        "universite_moyennement_selective": round(chances_universite_moyenne, 1),
        "universite_accessible": round(chances_universite_accessible, 1),
        "details": {
            "score_academique": round(academic_base, 1),
            "score_bts_global": round(bts_score, 1),
            "score_rang_classe": round(ranking_score, 1),
            "score_coherence": coherence_score,
            "score_historique": historical_penalty,
        },
    }


def estimate_l2_miage_chances():
    """
    Estime les chances d'admission en L2 MIAGE.

    L'entrée en L2 MIAGE avec un BTS SIO est atypique (normalement on entre en L3).
    Certaines universités le permettent si le dossier est jugé insuffisant pour la L3,
    ou si l'étudiant le demande par prudence.
    """
    l3_chances = estimate_l3_miage_chances()

    # En L2, les exigences sont moindres, donc les chances sont plus élevées
    return {
        "score_brut": round(l3_chances["score_brut"] + 12, 1),
        "universite_tres_selective": round(
            min(100, l3_chances["universite_tres_selective"] + 15), 1
        ),
        "universite_moyennement_selective": round(
            min(100, l3_chances["universite_moyennement_selective"] + 12), 1
        ),
        "universite_accessible": round(
            min(100, l3_chances["universite_accessible"] + 8), 1
        ),
        "note": (
            "Avec un BTS SIO validé, l'entrée en L2 MIAGE est quasi certaine "
            "dans les universités accessibles. Cependant, entrer en L2 signifie "
            "perdre une année par rapport à une entrée directe en L3."
        ),
    }


def estimate_chances_per_university(niveau="L3"):
    """
    Estime les chances d'admission pour chaque université MIAGE.

    Paramètres:
        niveau: "L2" ou "L3"

    Retourne une liste de dicts triée par chances décroissantes.
    """
    scores = extract_bts_domain_scores()
    bts_avgs = compute_bts_weighted_averages()
    rankings = compute_class_rankings()

    # Score de profil global (0-100)
    math_score = min(scores["mathematiques"] / 20 * 100, 100)
    info_score = min(scores["informatique"] / 20 * 100, 100)
    gestion_score = min(scores["gestion_management"] / 20 * 100, 100)
    academic_base = math_score * 0.35 + info_score * 0.40 + gestion_score * 0.25

    bts_moyennes = [v["moyenne_ponderee"] for v in bts_avgs.values()]
    bts_global = sum(bts_moyennes) / len(bts_moyennes) if bts_moyennes else 10
    bts_score = min(bts_global / 20 * 100, 100)

    avg_ranking = sum(rankings.values()) / len(rankings) if rankings else 50

    # Score de profil brut
    profile_score = (
        academic_base * 0.40
        + bts_score * 0.25
        + avg_ranking * 0.15
        + 80 * 0.10  # cohérence BTS SIO -> MIAGE
        + 35 * 0.10  # pénalité historique L2 maths
    )
    profile_score += 3  # bonus félicitations

    if niveau == "L2":
        profile_score += 12  # L2 = moins exigeant

    results = []
    for uni in UNIVERSITIES_MIAGE:
        # Facteur de sélectivité : plus selectivite est élevé, plus c'est dur
        selectivity_factor = {
            1: 0.95,
            2: 0.85,
            3: 0.70,
            4: 0.55,
            5: 0.45,
        }.get(uni["selectivite"], 0.70)

        # Chance brute = profil * facteur de sélectivité
        chance = profile_score * selectivity_factor

        # Bonus BTS pour les universités qui les accueillent explicitement
        if uni["selectivite"] <= 2:
            chance += 5  # les universités accessibles valorisent plus les BTS

        # Malus pour les très sélectives (profils licence préférés)
        if uni["selectivite"] >= 5:
            chance -= 5  # les très sélectives préfèrent les profils licence

        chance = max(5, min(95, round(chance, 1)))

        # Niveau de confiance textuel
        if chance >= 70:
            verdict = "Très bonnes chances"
        elif chance >= 50:
            verdict = "Bonnes chances"
        elif chance >= 35:
            verdict = "Chances moyennes"
        elif chance >= 20:
            verdict = "Chances faibles"
        else:
            verdict = "Très difficile"

        results.append({
            "universite": uni["nom"],
            "ville": uni["ville"],
            "region": uni["region"],
            "selectivite": uni["selectivite"],
            "alternance": uni["alternance"],
            "chances_pct": chance,
            "verdict": verdict,
            "taux_acceptation_general": uni["taux_acceptation_estime"],
            "points_forts": uni["points_forts_formation"],
            "commentaire": uni["commentaire"],
        })

    results.sort(key=lambda x: x["chances_pct"], reverse=True)
    return results
