# anniversaire_app_advanced.py
import streamlit as st
import random

# ---------------------
# CONFIG
st.set_page_config(page_title="Anniversaire 🎉", page_icon="🎂", layout="centered")

st.title("🎉 Joyeux Anniversaire ! 🎂")
st.write("Bienvenue sur l'app spéciale pour toi, Alex!")

# ---------------------
# CAROUSEL DE PHOTOS
st.header("📸 Souvenirs, ( j'ai pas d'images perso parce que l'app est publique donc pas de diulgation de phtos dossiers ou autre tkt )")
photos = [
    "photos/ami1.jpg",
    "photos/ami2.jpg",
    "photos/ami3.jpg",
    "photos/ami4.jpg",
    # Exemple de lien internet (ajoute tes propres liens !)
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUqVHMws1zRWxBs_0_QxjFAo6zHSK7BetB0A&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzYXymBjm0T5QymIGls-OJU9N7NFBGwlbfaA&s", 
    "https://media.licdn.com/dms/image/v2/C4D03AQGkdak3w976gg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1615416791947?e=2147483647&v=beta&t=3xRdAb4pbTp-5meCgDCf9rDL2OVYrUtL99NpOX8y2-E"
]


if "index" not in st.session_state:
    st.session_state.index = 0

col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.button("⬅️ Précédente"):
        st.session_state.index = (st.session_state.index - 1) % len(photos)
with col2:
    st.image(photos[st.session_state.index], use_container_width=True)
with col3:
    if st.button("➡️ Suivante"):
        st.session_state.index = (st.session_state.index + 1) % len(photos)

st.markdown("---")

# ---------------------
# MINI-JEUX PHYSIQUE
st.header("🧪 Mini-jeux Physique (niveau expert)")

score_physique = 0

# --- Jeu 1 : Formules manquantes
st.subheader("1️⃣ Formules manquantes")
formules = [
    {"question": "Énergie cinétique : E_c = ? * m * v^2", "answer": "1/2"},
    {"question": "Équation de Schrödinger : iħ ∂ψ/∂t = ? ψ", "answer": "- (ħ² / 2m) ∇²"},
    {"question": "Force de Lorentz : F = q * (v × ?)", "answer": "B"}
]
for i, f in enumerate(formules):
    reponse = st.text_input(f"{i+1}. {f['question']}", key=f"form_{i}")
    if reponse:
        if reponse.strip().lower() == f['answer'].lower():
            st.success("✅ Correct !")
            score_physique += 1
        else:
            st.error(f"❌ Incorrect. Réponse attendue : {f['answer']}")

# --- Jeu 2 : Devinez la loi
st.subheader("2️⃣ Devinez la loi ou principe")
lois = [
    {"problem": "Une sphère roule sans glisser sur un plan incliné. Relation vitesse rotation v/ω ?", "answer": "v = rω"},
    {"problem": "Champ gravitationnel autour d'une masse M ?", "answer": "g = GM/r^2"},
    {"problem": "Oscillateur harmonique : relation entre ω et k,m ?", "answer": "ω = sqrt(k/m)"}
]
for i, l in enumerate(lois):
    reponse = st.text_input(f"{i+1}. {l['problem']}", key=f"law_{i}")
    if reponse:
        if reponse.strip().lower() == l['answer'].lower():
            st.success("✅ Correct !")
            score_physique += 1
        else:
            st.error(f"❌ Incorrect. Réponse attendue : {l['answer']}")

# --- Jeu 3 : Quiz calculatoire express
st.subheader("3️⃣ Quiz calculatoire express")
calculs = [
    {"q": "Force centripète pour satellite de masse 500kg, rayon 7000km, vitesse 7.5km/s ? (en N)", 
     "answer": str(round(500 * (7500**2) / 7_000_000))},
    {"q": "Énergie potentielle mgh, m=2kg, h=10m, g=9.81 ?", 
     "answer": str(round(2*9.81*10))}
]
for i, c in enumerate(calculs):
    reponse = st.text_input(f"{i+1}. {c['q']}", key=f"calc_{i}")
    if reponse:
        if reponse.strip() == c['answer']:
            st.success("✅ Correct !")
            score_physique += 1
        else:
            st.error(f"❌ Incorrect. Réponse attendue : {c['answer']}")

st.success(f"Score total Physique : {score_physique}/9")
st.markdown("---")

# ---------------------
# QUIZ COURSE À PIED AVANCÉ
st.header("🏃‍♂️ Quiz Course à pied (niveau expert)")

score_course = 0

# Liste de questions interactives
questions_course = [
    {"q": "Record marathon hommes 2024 ?", "options": ["Eliud Kipchoge", "Kelvin Kiptum", "Haile Gebrselassie"], "answer": "Kelvin Kiptum"},
    {"q": "VO2max typique pour un coureur élite (ml/kg/min) ?", "options": ["60-65","70-85","90-100"], "answer": "70-85"},
    {"q": "Quel type d’entraînement améliore le plus la vitesse sur 10km ?", "options": ["Sortie longue","Fractionné court","Renforcement musculaire"], "answer": "Fractionné court"},
    {"q": "Allure marathon si objectif 2h30 ?", "options": ["~3:33/km","~4:00/km","~5:00/km"], "answer": "~3:33/km"},
    {"q": "Temps pour parcourir 5km à 18 km/h ?", "options": ["16min40s","15min","20min"], "answer": "16min40s"}
]

for i, quest in enumerate(questions_course):
    choix = st.radio(f"{i+1}. {quest['q']}", quest["options"], key=f"run_{i}")
    if choix == quest["answer"]:
        score_course += 1

st.success(f"Score Course : {score_course}/{len(questions_course)}")
st.markdown("---")

# ---------------------
# CADEAU FINAL
st.header("🎁 Cadeau Final")
if score_physique == 9 and score_course == len(questions_course):
    st.balloons()
    st.success("Bravo ! Tu as débloqué ton cadeau 🎉")
    st.success("Nous t'invitons dans le restaurant le plus chicos de Paris la semaine pro, donc donne tes dispos pour que nous nous organisions 🎉")
    
else:
    st.info("Réponds correctement à tous les quiz pour débloquer le cadeau final !")
