# [Nombre del caso]

> **Pregunta:** [La pregunta en lenguaje cotidiano]
> **Respuesta corta:** [La conclusión en una frase]

Caso publicado en: https://datos.brandoncarrillo.dev/casos/[slug]

## Datos

| Fuente | Qué se usó | Descargado el | Licencia |
|---|---|---|---|
| [Ej. BCCR] | [Tipo de cambio diario 2020–2026] | [AAAA-MM-DD] | [Términos] |

Los archivos originales no están en el repo. Para reproducir, descargalos en `data/raw/` según `fuentes.md`.

## Cómo reproducirlo

```
uv sync
uv run jupyter lab
```

Abrí los notebooks en orden (`notebooks/01-...`, `02-...`) y ejecutá **Kernel → Restart Kernel and Run All Cells**.

## Estructura

```
data/raw/         datos originales, sin tocar (no se suben)
data/processed/   datos limpios que generan los scripts
sql/              consultas y scripts de base de datos
notebooks/        exploración y análisis, en orden
src/              código reutilizable (limpieza, conexión a la base)
reports/          resultados finales: JSON para el sitio, gráficos, memo
```

## Hallazgos

1. [Hallazgo 1]
2. [Hallazgo 2]
3. [Hallazgo 3]

## Limitaciones

- [Qué no cubren los datos o qué supuestos se hicieron]

---
Brandon Carrillo Álvarez · [LinkedIn](https://www.linkedin.com/in/brandonca/) · [Portafolio](https://datos.brandoncarrillo.dev)
