#!/usr/bin/env python3
"""
Analyseur de chances d'admission en MIAGE pour MINEIRO Florent.
Génère un rapport détaillé basé sur les bulletins de notes.
"""

from grades_data import STUDENT, BTS_SIO_1A, BTS_SIO_2A
from analyzer import (
    extract_bts_domain_scores,
    compute_bts_weighted_averages,
    compute_class_rankings,
    analyze_strengths_weaknesses,
    estimate_l3_miage_chances,
    estimate_l2_miage_chances,
    estimate_chances_per_university,
)


def print_separator(char="=", length=75):
    print(char * length)


def print_header(title):
    print()
    print_separator()
    print(f"  {title}")
    print_separator()


def print_subheader(title):
    print()
    print(f"--- {title} ---")


def selectivite_label(level):
    labels = {
        1: "★☆☆☆☆ Très accessible",
        2: "★★☆☆☆ Accessible",
        3: "★★★☆☆ Modérément sélective",
        4: "★★★★☆ Sélective",
        5: "★★★★★ Très sélective",
    }
    return labels.get(level, "?")


def chances_bar(pct, width=25):
    filled = int(pct / 100 * width)
    empty = width - filled
    if pct >= 70:
        indicator = "🟢"
    elif pct >= 50:
        indicator = "🟡"
    elif pct >= 35:
        indicator = "🟠"
    else:
        indicator = "🔴"
    return f"{indicator} [{'█' * filled}{'░' * empty}] {pct:.0f}%"


def main():
    print_separator("*")
    print("  ANALYSE DES CHANCES D'ADMISSION EN MIAGE")
    print(f"  Étudiant : {STUDENT['prenom']} {STUDENT['nom']}")
    print(f"  Formation actuelle : BTS SIO SLAM (2ème année)")
    print(f"  Établissement : Le Rebours, Paris")
    print_separator("*")

    # =========================================================================
    # 1. Résumé du profil académique
    # =========================================================================
    print_header("1. PROFIL ACADÉMIQUE")

    scores = extract_bts_domain_scores()
    bts_avgs = compute_bts_weighted_averages()
    rankings = compute_class_rankings()

    print_subheader("Moyennes par domaine (BTS SIO)")
    for domain, label in [
        ("mathematiques", "Mathématiques"),
        ("informatique", "Informatique"),
        ("gestion_management", "Gestion / Management"),
        ("anglais", "Anglais"),
        ("culture_generale", "Culture Générale"),
    ]:
        score = scores[domain]
        bar = chances_bar(score / 20 * 100, width=20)
        print(f"  {label:<25} : {score:>5.1f}/20  {bar}")

    print_subheader("Moyennes pondérées par semestre (BTS)")
    for sem, data in bts_avgs.items():
        print(f"  {sem:<25} : {data['moyenne_ponderee']:>5.2f}/20")
        if data["appreciation"]:
            print(f"    → {data['appreciation']}")

    print_subheader("Rang estimé dans la classe (percentile)")
    for sem, rang in rankings.items():
        print(f"  {sem:<25} : Top {100 - rang:.0f}% de la classe")

    # =========================================================================
    # 2. Points forts / Points faibles
    # =========================================================================
    print_header("2. ANALYSE DU PROFIL POUR LA MIAGE")

    strengths, weaknesses = analyze_strengths_weaknesses()

    print_subheader("Points forts ✅")
    for s in strengths:
        print(f"  + {s}")

    print_subheader("Points faibles ⚠️")
    for w in weaknesses:
        print(f"  - {w}")

    # =========================================================================
    # 3. Chances globales L3 / L2
    # =========================================================================
    print_header("3. ESTIMATION GLOBALE DES CHANCES")

    l3 = estimate_l3_miage_chances()
    l2 = estimate_l2_miage_chances()

    print_subheader("L3 MIAGE (entrée standard avec BTS)")
    print(f"  Score de profil global : {l3['score_brut']}/100")
    print(f"  - Score académique       : {l3['details']['score_academique']}/100")
    print(f"  - Score BTS global       : {l3['details']['score_bts_global']}/100")
    print(f"  - Rang dans la classe    : {l3['details']['score_rang_classe']}/100")
    print(f"  - Cohérence parcours     : {l3['details']['score_coherence']}/100")
    print(f"  - Historique (L2 Maths)  : {l3['details']['score_historique']}/100")

    print_subheader("L2 MIAGE (entrée avec une année supplémentaire)")
    print(f"  Score de profil global : {l2['score_brut']}/100")
    print(f"  ⚠️  {l2['note']}")

    # =========================================================================
    # 4. Chances par université - L3
    # =========================================================================
    print_header("4. CHANCES PAR UNIVERSITÉ — L3 MIAGE")
    print("  (classement par chances décroissantes)")

    l3_per_uni = estimate_chances_per_university("L3")

    current_region = None
    for i, uni in enumerate(l3_per_uni, 1):
        if uni["region"] != current_region:
            current_region = uni["region"]
            print_subheader(f"Région : {current_region}")

        alt = "🔄 Alternance" if uni["alternance"] else "📚 Initiale"
        print(f"  {i:>2}. {uni['universite']}")
        print(f"      📍 {uni['ville']}  |  {alt}")
        print(f"      Sélectivité : {selectivite_label(uni['selectivite'])}")
        print(f"      Vos chances : {chances_bar(uni['chances_pct'])}")
        print(f"      Verdict     : {uni['verdict']}")
        print(f"      💡 {uni['points_forts']}")
        print(f"      📝 {uni['commentaire']}")
        print()

    # =========================================================================
    # 5. Chances par université - L2
    # =========================================================================
    print_header("5. CHANCES PAR UNIVERSITÉ — L2 MIAGE")
    print("  (classement par chances décroissantes)")

    l2_per_uni = estimate_chances_per_university("L2")

    current_region = None
    for i, uni in enumerate(l2_per_uni, 1):
        if uni["region"] != current_region:
            current_region = uni["region"]
            print_subheader(f"Région : {current_region}")

        alt = "🔄 Alternance" if uni["alternance"] else "📚 Initiale"
        print(f"  {i:>2}. {uni['universite']}")
        print(f"      📍 {uni['ville']}  |  {alt}")
        print(f"      Sélectivité : {selectivite_label(uni['selectivite'])}")
        print(f"      Vos chances : {chances_bar(uni['chances_pct'])}")
        print(f"      Verdict     : {uni['verdict']}")
        print()

    # =========================================================================
    # 6. Recommandations
    # =========================================================================
    print_header("6. RECOMMANDATIONS STRATÉGIQUES")

    print("""
  🎯 STRATÉGIE RECOMMANDÉE : Viser la L3 MIAGE directement

  Avec votre BTS SIO option SLAM et vos excellentes notes en
  mathématiques, la L3 MIAGE est l'objectif naturel. Le BTS SIO
  est un diplôme Bac+2 qui donne accès directement à la L3.

  📋 PLAN D'ACTION :

  1. CANDIDATURES PRIORITAIRES (bonnes chances) :
     → Universités de sélectivité 1-2 (Orléans, Nancy, Mulhouse, Amiens...)
     → Ce sont vos meilleures chances, et la qualité de formation y est bonne.
     → Orléans accepte explicitement les BTS après examen du dossier.

  2. CANDIDATURES AMBITIEUSES (chances moyennes) :
     → Universités de sélectivité 3 (Nanterre, Lyon, Toulouse, Bordeaux...)
     → Votre profil maths + BTS SLAM est un atout, mais la concurrence
       est forte face aux profils Licence.

  3. CANDIDATURES DE PRESTIGE (chances faibles) :
     → Dauphine-PSL, Paris-Saclay, Sorbonne
     → Tentez quand même ! Ça ne coûte rien, et votre profil maths
       (18.9 en BTS 1A) peut attirer l'attention.

  4. ALTERNATIVE : L2 MIAGE (filet de sécurité)
     → Si aucune L3 n'est obtenue, la L2 reste une option viable.
     → Vous perdez un an mais vous intégrez le parcours MIAGE.

  💡 CONSEILS POUR LE DOSSIER :

  • Mettez en avant votre progression spectaculaire :
    L2 Maths (5.2/20) → BTS SIO (15+ de moyenne avec Félicitations)
  • Insistez sur vos notes de maths exceptionnelles (18.9, 19.7)
  • Valorisez la double compétence BTS SIO = Info + Gestion = MIAGE
  • Mentionnez les appréciations "étudiant moteur", "Félicitations"
  • Expliquez l'échec en L2 Maths par un décalage de parcours,
    pas un manque de capacités (vos notes BTS le prouvent)

  ⚠️  AVERTISSEMENT :
  Ces estimations sont indicatives et basées sur des critères
  généraux. Chaque commission d'admission évalue les dossiers
  selon ses propres critères. Les chances réelles peuvent varier
  significativement en fonction de la lettre de motivation,
  du nombre de candidats de l'année, et d'autres facteurs.
""")

    print_separator("*")
    print("  Rapport généré par miage-admission-analyzer")
    print("  Données : bulletins 2019-2026 de MINEIRO Florent")
    print_separator("*")


if __name__ == "__main__":
    main()
