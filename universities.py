"""
Base de données des universités françaises proposant la MIAGE.

Chaque entrée contient :
- nom : Nom de l'université
- ville : Ville principale
- region : Région
- selectivite : Niveau de sélectivité (1=très accessible, 5=très sélectif)
- accepte_bts : Si l'université accepte les BTS en L3 MIAGE
- alternance : Si l'alternance est proposée
- taux_acceptation_estime : Taux d'acceptation estimé en % (pour L3)
- commentaire : Notes spécifiques

Sources : miage.fr, Wikipedia, Thotis, sites des universités (données 2025).
"""

UNIVERSITIES_MIAGE = [
    # =========================================================================
    # Île-de-France
    # =========================================================================
    {
        "nom": "Université Paris-Dauphine PSL",
        "ville": "Paris",
        "region": "Île-de-France",
        "selectivite": 5,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 17,
        "points_forts_formation": "Prestige PSL, réseau entreprises, finance/SI",
        "commentaire": "Très sélective. Profils Licence privilégiés. BTS possible mais rare.",
    },
    {
        "nom": "Université Paris-Saclay",
        "ville": "Orsay / Évry",
        "region": "Île-de-France",
        "selectivite": 5,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 17,
        "points_forts_formation": "Informatique décisionnelle, ingénierie logicielle web",
        "commentaire": "Très sélective. Forte demande, peu de places.",
    },
    {
        "nom": "Université Paris 1 Panthéon-Sorbonne",
        "ville": "Paris",
        "region": "Île-de-France",
        "selectivite": 5,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 15,
        "points_forts_formation": "Business informatics, SI durable",
        "commentaire": "Plus d'un millier de candidatures pour quelques dizaines de places.",
    },
    {
        "nom": "Université Paris Cité",
        "ville": "Paris",
        "region": "Île-de-France",
        "selectivite": 4,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 25,
        "points_forts_formation": "Valorisation et protection des données",
        "commentaire": "Sélective mais plus accessible que Dauphine/Saclay.",
    },
    {
        "nom": "Université Paris Nanterre",
        "ville": "Nanterre",
        "region": "Île-de-France",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 35,
        "points_forts_formation": "Systèmes d'information, intelligence des données",
        "commentaire": "Bonne option IDF. Accueille des BTS avec bon dossier.",
    },
    {
        "nom": "Université Gustave Eiffel",
        "ville": "Champs-sur-Marne",
        "region": "Île-de-France",
        "selectivite": 2,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 45,
        "points_forts_formation": "Proximité géographique UPEC, ville numérique",
        "commentaire": "Accessible, bonne option pour profils BTS motivés.",
    },
    {
        "nom": "Université d'Évry (Paris-Saclay)",
        "ville": "Évry",
        "region": "Île-de-France",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 38,
        "points_forts_formation": "Formation intégrée Paris-Saclay, alternance",
        "commentaire": "Moins sélective que le campus Orsay de Paris-Saclay.",
    },
    # =========================================================================
    # Province
    # =========================================================================
    {
        "nom": "Université Grenoble Alpes",
        "ville": "Grenoble",
        "region": "Auvergne-Rhône-Alpes",
        "selectivite": 4,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 29,
        "points_forts_formation": "Écosystème tech grenoblois, recherche",
        "commentaire": "Sélective (~29% d'acceptation). Bon cadre tech.",
    },
    {
        "nom": "Université Claude Bernard Lyon 1",
        "ville": "Lyon",
        "region": "Auvergne-Rhône-Alpes",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 35,
        "points_forts_formation": "90% d'insertion à la sortie, réseau entreprises lyonnais",
        "commentaire": "Bon compromis sélectivité/qualité. Accueille des BTS.",
    },
    {
        "nom": "Université Toulouse Capitole",
        "ville": "Toulouse",
        "region": "Occitanie",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 33,
        "points_forts_formation": "Écosystème aéronautique et tech toulousain",
        "commentaire": "Plusieurs centaines de candidatures pour 15-60 places.",
    },
    {
        "nom": "Université de Bordeaux",
        "ville": "Bordeaux",
        "region": "Nouvelle-Aquitaine",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 35,
        "points_forts_formation": "Formation reconnue, réseau Nouvelle-Aquitaine",
        "commentaire": "Modérément sélective, accueille bien les BTS.",
    },
    {
        "nom": "Université de Rennes",
        "ville": "Rennes",
        "region": "Bretagne",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 30,
        "points_forts_formation": "Écosystème numérique breton, alternance",
        "commentaire": "10-40 places selon parcours, plusieurs centaines de candidats.",
    },
    {
        "nom": "Université de Lille",
        "ville": "Lille",
        "region": "Hauts-de-France",
        "selectivite": 4,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 25,
        "points_forts_formation": "Ingénierie projets IT, alternance",
        "commentaire": "Très sélective en alternance (5 places / 400 candidats).",
    },
    {
        "nom": "Université de Nantes",
        "ville": "Nantes",
        "region": "Pays de la Loire",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 35,
        "points_forts_formation": "Écosystème numérique nantais dynamique",
        "commentaire": "Bonne formation, accueille les profils BTS.",
    },
    {
        "nom": "Université Côte d'Azur (Nice)",
        "ville": "Nice",
        "region": "Provence-Alpes-Côte d'Azur",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 35,
        "points_forts_formation": "Sophia Antipolis, tech/innovation",
        "commentaire": "Cadre attractif, sélectivité modérée.",
    },
    {
        "nom": "Université Aix-Marseille",
        "ville": "Marseille",
        "region": "Provence-Alpes-Côte d'Azur",
        "selectivite": 3,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 33,
        "points_forts_formation": "Grande université, réseau entreprises PACA",
        "commentaire": "Modérément sélective.",
    },
    {
        "nom": "Université d'Orléans",
        "ville": "Orléans",
        "region": "Centre-Val de Loire",
        "selectivite": 2,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 50,
        "points_forts_formation": "Formation professionnalisante, 10 mois de stage",
        "commentaire": "Accessible. Accepte explicitement BTS après examen de dossier.",
    },
    {
        "nom": "Université de Lorraine (Nancy)",
        "ville": "Nancy",
        "region": "Grand Est",
        "selectivite": 2,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 45,
        "points_forts_formation": "Alternance, coût de la vie modéré",
        "commentaire": "Accessible, peu de places en alternance mais formation initiale ok.",
    },
    {
        "nom": "Université de Haute-Alsace (Mulhouse)",
        "ville": "Mulhouse",
        "region": "Grand Est",
        "selectivite": 2,
        "accepte_bts": True,
        "alternance": False,
        "taux_acceptation_estime": 55,
        "points_forts_formation": "Taux d'insertion proche de 100% à 3 mois",
        "commentaire": "Très accessible, excellente insertion professionnelle.",
    },
    {
        "nom": "Université de Picardie (Amiens)",
        "ville": "Amiens",
        "region": "Hauts-de-France",
        "selectivite": 2,
        "accepte_bts": True,
        "alternance": True,
        "taux_acceptation_estime": 50,
        "points_forts_formation": "Proximité Paris, coût de vie avantageux",
        "commentaire": "Accessible, bon tremplin vers le marché parisien.",
    },
    {
        "nom": "Université des Antilles",
        "ville": "Pointe-à-Pitre",
        "region": "Outre-mer",
        "selectivite": 1,
        "accepte_bts": True,
        "alternance": False,
        "taux_acceptation_estime": 65,
        "points_forts_formation": "Contexte ultramarin, réseau MIAGE national",
        "commentaire": "Très accessible, effectifs réduits.",
    },
]


def get_universities_by_region():
    """Regroupe les universités par région."""
    regions = {}
    for uni in UNIVERSITIES_MIAGE:
        region = uni["region"]
        if region not in regions:
            regions[region] = []
        regions[region].append(uni)
    return regions


def get_universities_idf():
    """Retourne les universités d'Île-de-France."""
    return [u for u in UNIVERSITIES_MIAGE if u["region"] == "Île-de-France"]


def get_universities_by_selectivity(max_selectivite=5):
    """Retourne les universités filtrées par niveau de sélectivité max."""
    return [u for u in UNIVERSITIES_MIAGE if u["selectivite"] <= max_selectivite]
