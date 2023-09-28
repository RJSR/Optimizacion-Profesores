# Intentar importar la biblioteca PuLP
try:
    import pulp
except ImportError:
    # Si no está instalada, intentar instalarla
    try:
        import pip
        pip.main(['install', 'pulp'])
        import pulp
    except ImportError:
        raise ImportError("No se pudo importar la biblioteca 'pulp' y no se encontró 'pip' para instalarla. Asegúrate de que PuLP esté instalada en tu entorno de Python.")

# Definir los profesores y los cursos
profesores = ["A", "B", "C", "D", "E"]
cursos = ["C1", "C2", "C3", "C4", "C5"]

# Crear el problema de maximización
problema = pulp.LpProblem("Asignacion_de_Profesores", pulp.LpMaximize)

# Crear las variables binarias para la asignación de profesores a cursos
asignacion = pulp.LpVariable.dicts("Asignacion", [(profesor, curso) for profesor in profesores for curso in cursos], cat='Binary')

# Definir la matriz de preferencias de profesores
preferencias = {
    "A": {"C1": 5, "C2": 7, "C3": 9, "C4": 8, "C5": 6},
    "B": {"C1": 8, "C2": 2, "C3": 10, "C4": 7, "C5": 9},
    "C": {"C1": 5, "C2": 3, "C3": 8, "C4": 9, "C5": 9},
    "D": {"C1": 9, "C2": 6, "C3": 9, "C4": 7, "C5": 10},
    "E": {"C1": 7, "C2": 8, "C3": 8, "C4": 8, "C5": 5}
}

# Definir la función objetivo (total de preferencias)
problema += pulp.lpSum(preferencias[profesor][curso] * asignacion[(profesor, curso)] for profesor in profesores for curso in cursos)

# Restricción: Cada profesor debe dictar solo un curso
for profesor in profesores:
    problema += pulp.lpSum(asignacion[(profesor, curso)] for curso in cursos) == 1

# Restricción: Cada curso debe tener un profesor
for curso in cursos:
    problema += pulp.lpSum(asignacion[(profesor, curso)] for profesor in profesores) == 1

# Resolver el problema
problema.solve()

# Mostrar la asignación óptima
print("Asignación óptima de profesores a cursos:")
for profesor in profesores:
    for curso in cursos:
        if pulp.value(asignacion[(profesor, curso)]) == 1:
            print(f"Profesor {profesor} -> Curso {curso} (Preferencia: {preferencias[profesor][curso]})")

# Mostrar el valor óptimo de la función objetivo
print(f"Total de preferencias maximizado: {pulp.value(problema.objective)}")
