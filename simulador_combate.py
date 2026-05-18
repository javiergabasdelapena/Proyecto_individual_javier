import networkx as nx
import matplotlib.pyplot as plt

info_luchadores = {
    "Javi": {"titulo": "Ninguno"},
    "Jorge": {"titulo": "Ninguno"},
    "Fausto": {"titulo": "Campeón de Italia"},
    "Darío": {"titulo": "Ninguno"},
    "Raúl": {"titulo": "Ninguno"},
    "Pablo": {"titulo": "Campeón de España"},
    "florentino": {"titulo": "Campeón de Europa"}
}

combates_historicos = [
    ("Javi", "Jorge"), 
    ("Jorge", "Fausto"), 
    ("Fausto", "Javi"),
    ("Javi", "Darío"), 
    ("Darío", "Raúl"), 
    ("Pablo", "Raúl"),
    ("Pablo", "Darío"), 
    ("florentino", "Pablo"), 
    ("florentino", "Jorge")
]

class SimuladorCombate:
    def __init__(self, datos):
        self.G = nx.DiGraph() 
        for ganador, perdedor in datos:
            self.G.add_edge(ganador, perdedor)

    def calcular_puntos(self):
        puntuaciones = {nodo: 0 for nodo in self.G.nodes}
        for peleador in self.G.nodes:
            vencidos = list(self.G.successors(peleador))
            for rival in vencidos:
                puntuaciones[peleador] += 3
                puntuaciones[peleador] += len(list(self.G.successors(rival)))
        return puntuaciones

    def mostrar_grafo(self):
        plt.figure(figsize=(10, 7))
        pos = nx.spring_layout(self.G, seed=42) 
        
        nx.draw(self.G, pos, 
                with_labels=True, 
                node_color='skyblue', 
                node_size=3000, 
                font_weight='bold', 
                arrows=True, 
                arrowsize=25,
                edge_color='black',
                width=1.5,
                connectionstyle='arc3,rad=0.1')
        
        plt.title("MAPA DE JERARQUÍA MASCULINA")
        plt.show()

    def predecir_resultado(self, p1, p2):
        print(f"\n--- ANALIZANDO: {p1} vs {p2} ---")
        pts = self.calcular_puntos()
        f1, f2 = info_luchadores.get(p1), info_luchadores.get(p2)
        
        print(f"[{p1}] Título: {f1['titulo']}")
        print(f"[{p2}] Título: {f2['titulo']}")
        
        try:
            camino = nx.shortest_path(self.G, source=p1, target=p2)
            print(f"\n[PREDICCIÓN] Ganador probable: {p1}")
            print(f"Ruta lógica: {' -> '.join(camino)}")
        except nx.NetworkXNoPath:
            ganador = p1 if pts[p1] > pts[p2] else p2
            print(f"\n[PREDICCIÓN] Ganador probable por puntos: {ganador} ({pts[p1]} vs {pts[p2]})")

def menu():
    sim = SimuladorCombate(combates_historicos)
    while True:
        print("\SIMULADOR DE COMBATE")
        print("1. Ver Ranking de Peleadores")
        print("2. Predecir pelea")
        print("3. Ver Grafo")
        print("4. Salir")
        op = input("\nElige una opción: ")
        
        if op == "1":
            p = sim.calcular_puntos()
            rank = sorted(p.items(), key=lambda x: x[1], reverse=True)
            print(f"\nRANKING OFICIAL:")
            for i, (nombre, pts) in enumerate(rank, 1):
                f = info_luchadores[nombre]
                print(f"{i}. {nombre} - {f['titulo']} ({pts} pts)")
        
        elif op == "2":
            p1 = input("Luchador A: ")
            p2 = input("Luchador B: ")
            if p1 in info_luchadores and p2 in info_luchadores:
                sim.predecir_resultado(p1, p2)
            else:
                print("Nombre no reconocido en la base de datos.")
        
        elif op == "3":
            sim.mostrar_grafo()
        
        elif op == "4":
            print("Saliste")
            break

if __name__ == "__main__":
    menu()