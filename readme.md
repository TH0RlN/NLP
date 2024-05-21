# Procesamiento del Lenguaje Natural (NLP)

## Gramática libre de contexto (CFG)

### ¿En que consiste?

Es una estructura formal utilizada en lingüística y en informática para definir las reglas de un lenguaje.

1. **Símbolos no terminales** : Estos son elementos abstractos que representan categorías gramaticales generales, como frases o partes de frases. No aparecen en la salida final, sino que se descomponen en símbolos terminales.
2. **Símbolos terminales** : Estos son los elementos más básicos del lenguaje y no se pueden descomponer más. Son las palabras o tokens reales que aparecen en las oraciones generadas.
3. **Reglas de producción** : Estas reglas indican cómo los símbolos no terminales pueden transformarse en otros símbolos no terminales o terminales. Cada regla tiene una parte izquierda (un símbolo no terminal) y una parte derecha (una secuencia de símbolos terminales y/o no terminales).
4. **Símbolo de inicio** : Es el punto de partida para la generación de oraciones. Es un símbolo no terminal desde el cual se inician las aplicaciones de las reglas de producción.

### Ventajas e inconvenientes

#### Ventajas

1. **Claridad y Formalidad** :

* **Estructura Definida** : Las CFG proporcionan una forma clara y precisa de definir la sintaxis de un lenguaje, lo que facilita la comprensión y la implementación.
* **Formalismo Matemático** : Basadas en teorías formales, las CFG permiten una representación exacta y manipulable de las reglas gramaticales.

2. **Capacidad de Modelado** :

* **Descripción de Estructuras Complejas** : Pueden describir estructuras gramaticales complejas y jerárquicas, lo cual es esencial para el análisis sintáctico de oraciones.
* **Flexibilidad** : Pueden adaptarse a una amplia variedad de lenguajes y estructuras sintácticas.

#### Inconvenientes

1. **Ambigüedad** :

* **Múltiples Derivaciones** : Algunas frases pueden tener múltiples árboles de derivación posibles, lo que introduce ambigüedad y puede complicar el análisis sintáctico.
* **Resolución Compleja** : La resolución de ambigüedades puede requerir heurísticas adicionales o información contextual no capturada por la CFG.

2. **Limitaciones en el Manejo de Dependencias Contextuales** :

* **Falta de Contexto** : Las CFG no pueden manejar dependencias contextuales y semánticas que son comunes en los lenguajes naturales. Por ejemplo, no pueden capturar fácilmente las relaciones de concordancia entre sujetos y verbos o entre pronombres y sus antecedentes.
* **Lenguaje Natural Complejo** : Los lenguajes naturales a menudo tienen dependencias de largo alcance y construcciones idiomáticas que las CFG no pueden representar adecuadamente.

3. **Complejidad en Lenguajes Naturales Reales** :

* **Gramáticas Complejas** : Las CFG que describen lenguajes naturales reales pueden volverse muy complejas y difíciles de manejar, requiriendo numerosas reglas para capturar todas las variaciones sintácticas posibles.
* **Escalabilidad** : Manejar la complejidad y la escala de los lenguajes naturales puede ser un desafío significativo.

### Aplicaciones

1. **Análisis Sintáctico (Parsing)**

   * **Qué es** : Dividir una oración en sus partes gramaticales y construir un árbol que muestra su estructura.
   * **Para qué sirve** :
   * **Procesadores de texto** : Ayudar a corregir la gramática.
   * **Compiladores** : Comprobar que el código de programación es correcto.
   * **Asistentes virtuales** : Entender la estructura de las preguntas para responder mejor.
2. **Generación de Lenguaje Natural (NLG)**

   * **Qué es** : Crear oraciones o textos automáticamente que sean gramaticalmente correctos.
   * **Para qué sirve** :
   * **Chatbots** : Generar respuestas correctas y coherentes.
   * **Sistemas de recomendación** : Crear descripciones automáticas de productos.
   * **Narración automática** : Escribir historias o informes basados en datos.
3. **Reconocimiento de Patrones en Texto**

   * **Qué es** : Encontrar estructuras específicas dentro de un texto.
   * **Para qué sirve** :
   * **Extracción de información** : Identificar nombres, fechas, lugares, etc.
   * **Análisis de sentimiento** : Determinar si un comentario es positivo o negativo.
   * **Filtrado de contenido** : Detectar y bloquear contenido inapropiado o spam.
4. **Desarrollo de Lenguajes de Programación**

   * **Qué es** : Definir las reglas gramaticales para nuevos lenguajes de programación.
   * **Para qué sirve** :
   * **Creación de lenguajes de programación** : Desarrollar nuevos lenguajes y sus compiladores.
   * **Transformación de código** : Analizar y optimizar el código fuente.
5. **Traducción Automática**

   * **Qué es** : Descomponer y entender la estructura de una oración para traducirla a otro idioma.
   * **Para qué sirve** :
   * **Sistemas de traducción** : Mejorar la calidad de las traducciones automáticas.
   * **Interpretación en tiempo real** : Facilitar la traducción instantánea en aplicaciones multilingües.
6. **Validación de Entrada de Datos**

   * **Qué es** : Verificar que los datos ingresados en formularios sigan una estructura correcta.
   * **Para qué sirve** :
   * **Formularios web** : Asegurar que los datos ingresados por los usuarios sean válidos.
   * **Sistemas empresariales** : Garantizar la coherencia de los datos en bases de datos.
7. **Desarrollo de Juegos y Narrativas Interactivas**

   * **Qué es** : Crear diálogos y historias que se adaptan a las acciones del jugador.
   * **Para qué sirve** :
   * **Juegos de rol** : Generar historias y diálogos interactivos.
   * **Narrativas interactivas** : Desarrollar historias que cambian según la interacción del usuario.

### Nuestro ejemplo

Hemos aprovechado las capacidades de las cfg para crear un pequeño generador de frases motivacionales aleatorias.
