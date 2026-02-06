estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota_media": 8.5, "asignaturas_aprobadas": 12},
    {"nombre": "Carlos", "edad": 22, "nota_media": 6.2, "asignaturas_aprobadas": 9},
    {"nombre": "Lucía", "edad": 19, "nota_media": 9.1, "asignaturas_aprobadas": 15},
    {"nombre": "Pedro", "edad": 21, "nota_media": 7.8, "asignaturas_aprobadas": 11},
    {"nombre": "Marta", "edad": 23, "nota_media": 5.9, "asignaturas_aprobadas": 8},
    {"nombre": "Javier", "edad": 20, "nota_media": 8.9, "asignaturas_aprobadas": 14},
    {"nombre": "Sofía", "edad": 19, "nota_media": 7.5, "asignaturas_aprobadas": 13},
    {"nombre": "Diego", "edad": 22, "nota_media": 6.8, "asignaturas_aprobadas": 10},
    {"nombre": "Elena", "edad": 21, "nota_media": 9.3, "asignaturas_aprobadas": 16},
    {"nombre": "Raúl", "edad": 20, "nota_media": 7.0, "asignaturas_aprobadas": 12},
]

aprobados = [e for e in estudiantes if e["nota_media"] >= 7.0]

mejor = max(estudiantes, key=lambda e: e["asignaturas_aprobadas"])

edad_promedio = sum(e["edad"] for e in aprobados) / len(aprobados)

print("Aprobados:")
for e in aprobados:
    print(f"- {e['nombre']} ({e['nota_media']})")

print(
    f"\nMás asignaturas: {mejor['nombre']} ({mejor['asignaturas_aprobadas']})")

print(f"Edad promedio aprobados: {edad_promedio:.1f} años")
