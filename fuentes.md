# Inventario de fuentes de datos

Fuentes que uso en la ruta de datos. Antes de usar cualquier dato, completo y verifico su ficha.

**Estados:** `✅ verificado` (abrí el link y descargué algo) · `⏳ por verificar` · `⚠️ problema` (anotar cuál)

**Regla:** en cada caso publicado, cito la fuente, la fecha de descarga y la licencia.

---

## Resumen

| Fuente | Qué uso | Formato | Frecuencia | Acceso | Fases | Estado |
|---|---|---|---|---|---|---|
| BCCR · Indicadores Económicos | Tipo de cambio, IPC, TPM, TBP | Excel / CSV + servicio web | Diaria a trimestral | Libre; token por correo para el servicio web | F1, F6, F7 | ⏳ |
| INEC | Microdatos ENAHO / ECE, población por cantón | .sav / .dta / CSV + Excel | Anual (ENAHO), trimestral (ECE) | Registro para microdatos (confirmar) | F2, F3, F4, F7 | ⏳ |
| CGR (Contraloría) | Presupuestos y ejecución municipal (SIPP) | Por confirmar | Por confirmar | Por confirmar | F2 | ⏳ |
| Poder Judicial | Estadísticas policiales del OIJ | CSV / Excel (confirmar) | Por confirmar | Libre | F4 | ⏳ |
| ICT | Llegadas internacionales por aeropuerto | Excel / PDF | Mensual, semestral y anual | Libre | F7 | ⏳ |
| datos.go.cr | Catálogo nacional (plan B) | Varios | Varía por dataset | Libre | Plan B | ⏳ |
| SNIT | Límites cantonales (mapas) | GeoJSON / Shapefile / Excel + WFS | Esporádica | Libre (confirmar) | F4 | ⏳ |
| Banco Mundial | Indicadores para comparar CR con la región | CSV / Excel / JSON + API | Anual | Libre, API sin registro | Comparaciones | ⏳ |

---

## Fichas

### BCCR · Indicadores Económicos

- **URL:** https://www.bccr.fi.cr/indicadores-economicos (botón "Nuevo sitio de Indicadores Económicos")
- **Servicio web (API):** https://www.bccr.fi.cr/indicadores-economicos/servicio-web — se solicita un token con correo
- **Datos que uso:** tipo de cambio compra/venta (diario), IPC (mensual), Tasa de Política Monetaria, Tasa Básica Pasiva
- **Formato:** Excel (.xlsx), hoja “Series”. Encabezado en las filas 1 a 4; los datos empiezan en la fila 5 con las columnas Fecha, Tipo cambio compra y Tipo cambio venta. Decimales con coma y serie diaria desde 1983.
- **Frecuencia:** tipo de cambio diaria; IPC mensual; cuentas nacionales trimestral
- **Licencia / términos:** uso personal, empresarial u organizacional permitido sin alterar el contenido; [lo que diga el resto de la cláusula]. Citar “Fuente: Banco Central de Costa Rica.
- **Ojo:** el sitio de indicadores se renovó; los links al sitio antiguo (gee.bccr.fi.cr) dejaron de funcionar el 31/10/2025. Usar solo el sitio nuevo.
- **Fecha de verificación:** ______ · **Estado:** ⏳

### INEC · Instituto Nacional de Estadística y Censos

- **URL:** https://inec.cr
- **Microdatos:** catálogo de microdatos del INEC (antes en sistemas.inec.cr/pad4; confirmar la URL actual) → anotar aquí: ______
- **Datos que uso:** ENAHO (ingresos, pobreza, por región), ECE (empleo, desempleo), población por cantón
- **Formato:** microdatos en SPSS (.sav) / Stata (.dta) / CSV, con diccionario de variables; cuadros en Excel
- **Frecuencia:** ENAHO anual (se levanta en julio y agosto); ECE trimestral
- **Licencia / términos:** revisar las condiciones de uso del catálogo de microdatos → ______
- **Ojo:** los microdatos llevan factor de expansión; sin ponderar, los resultados no coinciden con las cifras oficiales.
- **Cambio importante:** desde 2027 el INEC reemplaza la ENAHO y la ECE por una sola encuesta, la Encuesta Continua de Hogares (ECH). Para la Fase 3 uso la ENAHO 2025 (ya publicada) y años anteriores; anotar en el caso que la serie cambia en 2027.
- **Fecha de verificación:** ______ · **Estado:** ⏳

### CGR · Contraloría General de la República

- **URL:** https://www.cgr.go.cr/01-cgr-transp/datos-abiertos/datos-abiertos.html
- **Datos que uso:** presupuesto aprobado vs. ejecutado por municipalidad, por rubro (sistema SIPP)
- **Formato:** por confirmar → ______
- **Frecuencia:** por confirmar → ______
- **Licencia / términos:** ______
- **Plan B:** buscar en datos.go.cr o usar los informes de la CGR en Excel.
- **Fecha de verificación:** ______ · **Estado:** ⏳ (confirmar antes de la semana 4)

### Poder Judicial · Datos Abiertos

- **URL:** portal de Datos Abiertos del Poder Judicial (rediseñado y presentado el 18 de mayo de 2026). Entrar desde poder-judicial.go.cr y buscar "Datos Abiertos" → anotar URL exacta: ______
- **Alternativa:** repositorio de estadísticas policiales del OIJ (mismo dato, a veces más actualizado) → URL: ______
- **Datos que uso:** estadísticas policiales del OIJ (delitos por tipo, cantón y fecha)
- **Formato:** por confirmar (CSV / Excel) → ______
- **Frecuencia:** ______
- **Licencia / términos:** ______
- **Fecha de verificación:** ______ · **Estado:** ⏳

### ICT · Instituto Costarricense de Turismo

- **URL:** https://www.ict.go.cr → sección Estadísticas → Informes estadísticos
- **Datos que uso:** llegadas internacionales por puesto migratorio, en particular el aeropuerto Daniel Oduber Quirós (Liberia)
- **Formato:** Excel / PDF (informes mensuales, semestrales y anuales)
- **Frecuencia:** mensual, con publicaciones semestral y anual
- **Fuente original:** ICT con datos de la Dirección General de Migración y Extranjería
- **Licencia / términos:** ______
- **Fecha de verificación:** ______ · **Estado:** ⏳

### datos.go.cr · Portal Nacional de Datos Abiertos

- **URL:** https://datos.go.cr
- **Para qué:** catálogo nacional de datos de instituciones públicas; plan B cuando una institución no publica descarga directa
- **Visto en la portada (nov 2026):** proyecto de presupuesto 2025 y datos del MTSS (PRONAE, PRONAMYPE). Buscar ahí CGR, INEC, ICT y Poder Judicial.
- **Administra:** Ministerio de la Presidencia y MICITT
- **Licencia / términos:** revisar en el portal → ______
- **Fecha de verificación:** ______ · **Estado:** ⏳

### SNIT · Sistema Nacional de Información Territorial

- **URL:** https://www.snitcr.go.cr → sección "Servicios OGC" → nodo IGN (División Territorial Administrativa)
- **Servicio WFS de la DTA:** https://geos.snitcr.go.cr/be/IGN_5_CO/wfs?
- **Datos que uso:** límites de cantones y distritos para mapas (82 cantones)
- **Formato:** descarga directa en GeoJSON, Shapefile o Excel; también por WFS. Para el portafolio: **GeoJSON** (lo leen GeoPandas y el navegador)
- **Licencia / términos:** ______
- **Fecha de verificación:** ______ · **Estado:** ⏳

### Banco Mundial · World Bank Open Data

- **URL:** https://data.worldbank.org
- **API:** https://api.worldbank.org/v2 (sin registro)
- **Datos que uso:** indicadores de desarrollo (WDI) para comparar Costa Rica con Centroamérica y Latinoamérica
- **Formato:** CSV, Excel, JSON y API
- **Frecuencia:** mayormente anual (el último año suele venir vacío)
- **Licencia:** CC BY 4.0, con atribución obligatoria → citar "Fuente: Banco Mundial (CC BY 4.0)"
- **Fecha de verificación:** ______ · **Estado:** ⏳

---

## Checklist para cada fuente

- [ ] Abrí el link y funciona
- [ ] Descargué al menos un archivo y lo abrí
- [ ] Anoté el formato real y las columnas principales
- [ ] Anoté la frecuencia de actualización y el último periodo disponible
- [ ] Leí y anoté la licencia o los términos de uso
- [ ] Guardé el archivo original en `data/raw/` con la fecha de descarga en el nombre
