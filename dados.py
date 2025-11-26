#Arquivo que guarda dados que serão usados
circuitos = [
    ["Circuito 1", "iluminacao", 220.0, 8.5, 0.95, 60.0, "05/11/2025"],
    ["Motor Bomba", "motor", 220.0, 14.0, 0.78, 60.0, "05/11/2025"],
]
#Adicionando circuitos
circuitos.append(["Alimentador Principal", "alimentador", 220.0, 25.0, 0.92, 60.0, "05/11/2025"])
circuitos.append(["Banco Tomadas Sala 2", "tomada", 127.0, 9.5, 0.88, 60.0, "03/11/2025"])

limites = {
    "iluminacao": {"i_max": 10.0, "fp_min": 0.9, "tensao_nom": 220},
    "motor": {"i_max": 20.0, "fp_min": 0.75, "tensao_nom": 220},
    "tomada": {"i_max": 15.0, "fp_min": 0.8, "tensao_nom": 127},
    "alimentador": {"i_max": 40.0, "fp_min": 0.92, "tensao_nom": 220},
}

tolerancia_tensao = 0.10