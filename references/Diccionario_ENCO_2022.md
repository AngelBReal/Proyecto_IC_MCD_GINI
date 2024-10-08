# ENCO Dicionario de Datos

Este diccionario de datos describe las columnas del archivo CSV, incluyendo información sobre identificadores, ubicaciones geográficas, ingresos y respuestas a preguntas de encuesta.

| **Nombre de Columna**      | **Longitud** | **Tipo** | **NEMÓNICO** | **Rango de Claves**    | **Catálogo** | **Clave** | **Descripción**                     |
|----------------------------|--------------|----------|--------------|------------------------|--------------|-----------|-------------------------------------|
| Folio                      | 6            | C        | fol          | alfanumérico            |              |           | Identificador único de la vivienda. |
| Entidad                    | 2            | C        | ent          | [01-32]                 | ent          |           | Código de la entidad federativa.    |
| Control                    | 5            | C        | con          | 00001-99999             |              |           | Código de control de la vivienda.   |
| Vivienda seleccionada       | 1            | C        | v_sel        | [1-4]                   | v_sel        | 1         | Vivienda uno.                       |
|                            |              |          |              |                        |              | 2         | Vivienda dos.                       |
|                            |              |          |              |                        |              | 3         | Vivienda tres.                      |
|                            |              |          |              |                        |              | 4         | Vivienda cuatro.                    |
| Número de hogar             | 1            | C        | n_hog        | 1                      | n_hog        | 1         | Hogar principal.                    |
| Hogar mudado                | 1            | C        | h_mud        | 0-4                    | h_mud        | 0         | Hogar sin cambio.                   |
|                            |              |          |              |                        |              | 1         | Primer cambio.                      |
|                            |              |          |              |                        |              | 2         | Segundo cambio.                     |
|                            |              |          |              |                        |              | 3         | Tercer cambio.                      |
|                            |              |          |              |                        |              | 4         | Cuarto cambio.                      |
| Periodo del Ingreso         | 1            | C        | i_per        | [1-5]                  | i_per        | 1         | Cada semana.                        |
|                            |              |          |              |                        |              | 2         | Cada 15 días.                       |
|                            |              |          |              |                        |              | 3         | Cada mes.                           |
|                            |              |          |              |                        |              | 4         | Cada año.                           |
|                            |              |          |              |                        |              | 5         | No recibe ingreso.                  |
| Ingreso mensual estimado    | 6            | C        | ing          | 000001-999999           |              |           |                                     |
| Número de municipio según entidad | 3       | C        | mpio         | 001-575                | mpio         |           | Código del municipio según la entidad.|
| Ageb                       | 5            | C        | ageb         | 00000-99999             |              |           | Área geoestadística básica (AGEB).  |
| Fecha resultado definitivo  | 10           | C        | fch_def      |                        |              |           | Fecha del resultado definitivo.     |
| Pregunta 1                 | 1            | C        | p1           | [1-6]                  | p1           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 2                 | 1            | C        | p2           | [1-6]                  | p2           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 3                 | 1            | C        | p3           | [1-6]                  | p3           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 4                 | 1            | C        | p4           | [1-6]                  | p4           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 5                 | 1            | C        | p5           | [1-6]                  | p5           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 6                 | 1            | C        | p6           | [1-6]                  | p6           | 1         | Mucho mejor.                        |
|                            |              |          |              |                        |              | 2         | Mejor.                              |
|                            |              |          |              |                        |              | 3         | Igual.                              |
|                            |              |          |              |                        |              | 4         | Peor.                               |
|                            |              |          |              |                        |              | 5         | Mucho peor.                         |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 7                 | 1            | C        | p7           | [1-4]                  | p7           | 1         | Sí.                                 |
|                            |              |          |              |                        |              | 2         | Igual posibilidades.                |
|                            |              |          |              |                        |              | 3         | No.                                 |
|                            |              |          |              |                        |              | 4         | No sabe.                            |
| Pregunta 8                 | 1            | C        | p8           | [1-4]                  | p8           | 1         | Mayores.                            |
|                            |              |          |              |                        |              | 2         | Iguales.                            |
|                            |              |          |              |                        |              | 3         | Menores.                            |
|                            |              |          |              |                        |              | 4         | No sabe.                            |
| Pregunta 9                 | 1            | C        | p9           | [1-3]                  | p9           | 1         | Sí.                                 |
|                            |             
| Pregunta 10                | 1            | C        | p10          | [1-4]                  | p10          | 1         | Sí.                                 |
|                            |              |          |              |                        |              | 2         | No.                                 |
|                            |              |          |              |                        |              | 3         | No sabe.                            |
|                            |              |          |              |                        |              | 4         | No tiene ingresos.                  |
| Pregunta 11                | 1            | C        | p11          | [1-6]                  | p11          | 1         | Muy buenas.                         |
|                            |              |          |              |                        |              | 2         | Buenas.                             |
|                            |              |          |              |                        |              | 3         | Iguales.                            |
|                            |              |          |              |                        |              | 4         | Malas.                              |
|                            |              |          |              |                        |              | 5         | Muy malas.                          |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 12                | 1            | C        | p12          | [1-7]                  | p12          | 1         | Disminuir mucho.                    |
|                            |              |          |              |                        |              | 2         | Disminuir poco.                     |
|                            |              |          |              |                        |              | 3         | Permanecer igual.                   |
|                            |              |          |              |                        |              | 4         | Aumentar poco.                      |
|                            |              |          |              |                        |              | 5         | Aumentar igual.                     |
|                            |              |          |              |                        |              | 6         | Aumentar mucho.                     |
|                            |              |          |              |                        |              | 7         | No sabe.                            |
| Pregunta 13                | 1            | C        | p13          | [1-6]                  | p13          | 1         | Aumentar mucho.                     |
|                            |              |          |              |                        |              | 2         | Aumentar poco.                      |
|                            |              |          |              |                        |              | 3         | Permanecer igual.                   |
|                            |              |          |              |                        |              | 4         | Disminuir poco.                     |
|                            |              |          |              |                        |              | 5         | Disminuir mucho.                    |
|                            |              |          |              |                        |              | 6         | No sabe.                            |
| Pregunta 14                | 1            | C        | p14          | [1-4]                  | p14          | 1         | Sí.                                 |
|                            |              |          |              |                        |              | 2         | Probablemente.                      |
|                            |              |          |              |                        |              | 3         | No.                                 |
|                            |              |          |              |                        |              | 4         | No sabe.                            |
| Pregunta 15                | 1            | C        | p15          | [1-4]                  | p15          | 1         | Sí.                                 |
|                            |              |          |              |                        |              | 2         | Probablemente.                      |
|                            |              |          |              |                        |              | 3         | No.                                 |
|                            |              |          |              |                        |              | 4         | No sabe.                            |
