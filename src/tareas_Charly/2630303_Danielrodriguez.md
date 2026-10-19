# Investigación sobre Tipos de Robots Móviles



## Conceptos basicos



**¿Qué es un robot móvil?**
Es una máquina o mcanismo automatico que se desplaza de un punto A a un punto B, puede hacer tareas utilizando ruedas, patas, brazos entre otros sistemas de movimiento.



**¿Qué diferencia existe entre un robot móvil y un robot manipulador fijo?**
El robot móvil puede desplazarse por diferentes lugarese es decir moverze con libertad en el espacio, mientras que el manipulador fijo permanece sujeto a una base y no puede moverze en el espacio.



**¿Qué función existe entre el sistema de locomoción de un robot?**
Permite que el robot se desplace, cambie de dirección y se adapte a la superficie donde esta trabajando, como lo es el cruzar obstaculos o lograr atravezar distintos terrenos.



**¿Qué significa que un robot tenga movilidad omnidireccional?**
Significa que puede moverse a donde sea sin tener que cambiar la orientación de su cuerpo, es decir que para transladarse adelante/atras o izquierda/derecha no hace falta que cambie la direccion de su cuerpo.



**¿Qué relación existe entre la disposición de las ruedas y los movimientos que puede realizar el robot?**
La posición y el tipo de ruedas determinan cómo se mueve el robot, la dirección a la que puede ir y que tan facil gira o desplaza lateralmente.



**Lugares donde se utilicen robots móviles.**
Principalmente suelen ser utilizados en hogares para limpiar pisos, exploración espacial para investgar otros planetas, fábricas y almacenes para transportar materiales.



#### Robot diferencial con rueda de castor



**¿Como estan colocadas las ruedas motrices?**
Las ruedas motrices están colocadas a los lados del robot, una a cadalado, alineadas sobre el mismo eje y conectadas a diferentes motores. Esto permite controlar la velocidad y el sentido de giro de cada rueda.



**¿Para qué sirve la rueda de castor o rueda loca?**
No es motriz y no tiene tracción. Solo sirve como tercer punto de apoyo para dar estabilidad y equilibrio. Gira libre 360° sobre su eje vertical, por eso se adapta a cualquier dirección que le impongan las dos ruedas motrices sin oponer resistencia. Sin ella, el robot se caería.



**¿Como avanza en línea recta?**
Cuando ambas ruedas motrices giran a la misma velocidad y en el mismo sentido. Si la velocidad angular es 0, entonces avanza recto hacia adelante. Si ambas giran hacia atrás a igual velocidad, va recto hacia atrás.



**¿ Como puede girar hacia la izquierda o derecha?**
Variando la diferencia de velocidad. Giro a la izquierda: Rueda derecha más rápida que la izquierda. Giro a la derecha: Rueda izquierda más rápida que la derecha.



**¿Qué sucede cuando una rueda gira más rápido que la otra?**
El robot describe una curva. No gira sobre su centro, sino que sigue un arco de circunferencia. La velocidad angular es la distancia entre ruedas.Si una rueda se detiene y la otra avanza, el robot gira pivotando sobre la rueda detenida.



**¿Como puede realizar un giro en su propio eje?**
Haciendo que las ruedas giren a la misma velocidad pero en sentidos opuestos. El robot rota en su mismo lugar. Es un giro de radio cero, ideal para espacios reducidos. Si una va atrás y la otra hacia adelante, gira a la derecha; si es al revés, gira a la izquierda.



**Ventajas de esta configuración.**
Mecánica muy simple: solo 2 motores, sin dirección. Control muy fácil de programar. Giro sobre su propio eje, excelente maniobrabilidad. Bajo costo y muy eficiente energéticamente.



**Limitaciones**
No puede moverse de lado (no es omnidireccional). Si las ruedas patinan, pierde la odometría y se desorienta. La rueda loca se atora fácil en terrenos irregulares, alfombras gruesas o con carga pesada. Avanzar perfectamente recto depende de que ambos motores estén exactamente igual calibrados.



**Aplicaciones donde se utiliza**
Robots aspiradora (Roomba). Robots educativos (Arduino, mBot, TurtleBot). AGV y robots de almacén de Amazon. Sillas de ruedas eléctricas. Robots de reparto y de exploración de interiores. Plataformas de competencias como sumo-bots y seguidores de línea.



!\[Robot diferencial con rueda de castor.](robot\_rcastor.png)



|Rueda izquierda|Rueda derecha|Movimiento del robot|Explicación|
|-|-|-|-|
|Avanza|Avanza|Avanza recto hacia adelante|Mismo sentido misma cordinación.|
|Detenida|Avanza|Gira hacia la izquierda hacia adelante|Pivota sobre la rueda izquierda. Hace una curva a la izquierda con radio.|
|Avanza|Detenida|Gira hacia la derecha hacia adelante|Pivota sobre la rueda derecha. Hace una curva a la derecha con radio.|
|Avanza|Retrocede|Giro sobre su propio eje a la DERECHA (horario)|No avanza, solo rota en su lugar hacia la derecha. Es el giro de 360° más rápido.|
|Retrocede|Avanza|Giro sobre su propio eje a la IZQUIERDA (antihorario)|No avanza, solo rota en su lugar hacia la izquierda.|
|Retrocede|Retrocede|Retrocede recto hacia atrás|Retroceso porque ambas giran hacia atras.|



\####Robot omnidireccional con ruedas Mecanum
¿Como estan construidas?
Núcleo central: Un disco o llanta normal donde va el motor, como una rueda común .Rodillos periféricos: Alrededor de toda la circunferencia lleva entre 6 y 12 rodillos pequeños que giran libremente. Cada rodillo tiene su propio eje y rodamiento. No necesitan sistema de dirección. La omnidireccionalidad sale de esos rodillos.
¿Como estan colocados sus rodillos?
Rueda Omni convencional: Rodillos colocados a 90° respecto al eje de la rueda. Es decir, perpendiculares a la dirección de avance. Cuando la rueda tracciona hacia adelante, los rodillos permiten que se deslice lateralmente sin resistencia. Rueda Mecanum: Rodillos colocados a 45° respecto al eje de la rueda. Cada rodillo está inclinado. Esto hace que al girar la rueda genere una fuerza con dos componentes: una hacia adelante y otra lateral.
¿Qué diferencia hayb entre una Mecanum y una Omni convencional?
La rueda Mecanum genera componentes de fuerza que permiten al robot desplazarse lateralmente al combinar el giro de varias ruedas y la rueda Omni convencional facilita el desplazamiento lateral porque sus rodillos giran libremente en esa dirección.
¿Porque generalmente se utilizan cuatro ruedas?
Porque con una sola rueda no puedes controlar a dónde va la fuerza lateral. Con 4 ruedas puedes sumar y cancelar vectores: Si las 4 giran hacia adelante, las componentes laterales se cancelan entre sí y el robot avanza recto. Si las izquierdas van adelante y las derechas atrás, las componentes de frente se cancelan y queda solo la fuerza lateral: el robot hace strafe (movimiento lateral puro sin girar).
¿Cómo deben orientarse las ruedas respecto al chasis?
Las ruedas Mecanum suelen colocarse en las cuatro esquinas con los rodillos formando un patrón en X Las Omni convencionales se orientan según la configuración del robot, por ejemplo, a 120° si utiliza tres ruedas.

Explica cómo se combinan los movimientos de las cuatro ruedas para conseguir:
Avance: Las 4 componentes laterales de los rodillos a 45° se cancelan entre sí. Solo queda la fuerza hacia adelante.
Retroceso: El retroceso se consigue invirtiendo el sentido de giro de los motores, mientras el controlador coordina las ruedas para mantener la dirección deseada.
Movimiento hacia la izquierda:Las ruedas Mecanum permiten que el robot se desplace lateralmente hacia la izquierda gracias a la combinación de sus rodillos inclinados y al control independiente de los cuatro motores.
Movimiento hacia la derecha: para moverse hacia la derecha, se invierten los sentidos de giro respecto al movimiento lateral hacia la izquierda. Los sentidos exactos dependen de cómo estén instaladas las ruedas y conectados los motores.
Movimiento diagonal: Las ruedas Mecanum permiten desplazarse en diagonal mediante el control independiente de sus motores. Para una diagonal hacia adelante y a la izquierda, se activa el lado contrario.
Giro sobre su propio eje: Las ruedas Mecanum permiten girar sobre el propio eje gracias al movimiento coordinado de sus cuatro motores. La configuración exacta puede variar según cómo estén instaladas las ruedas.



|Movimiento|Delantera izquierda|Delantera derecha|Trasera izquierda|Trasera derecha|
|-|-|-|-|-|
|Avanzar|Horario|Horario|Horario|Horario|
|Retroceder|Antihorario|Antihorario|Antihorario|Antihorario|
|Desplazarse hacia a la izquierda|Antihorario|Horario|Horario|Antihorario|
|Desplazarse hacia a la derecha|Horario|Antihorario|Antihorario|Horario|
|Girar a la izquierda|Antiorario|Horario|Antiorario|Horario|
|Girar a la derecha|Horario|Antihorario|Horario|Antiorario|



Robot con dirección Ackermann
Cómo se distribuyen las ruedas
Las cuatro ruedas se distribuyen en las esquinas de la base del robot, dos en la parte delantera y dos en la parte trasera, en un robot omnidireccional con ruedas mecanum.
¿Qué ruedas normalmente proporcinan la dirección?
las ruedas delanteras proporcionan la dirección, ya que giran hacia la izquierda o hacia la derecha para cambiar la trayectoria del vehículo.
¿Qué ruedas pueden proporcionar la tracción?
Las cuatro ruedas normalmente proporcionan la tracción, ya que cada una cuenta con un motor que permite controlar su sentido y velocidad de giro de manera independiente.
¿Por qué las ruedas interiores y exteriores no giran exactamente con el mismo ángulo durante una curva?
Las ruedas interiores y exteriores no giran exactamente con el mismo ángulo durante una curva porque cada rueda recorre una distancia diferente. Las ruedas interiores recorren una trayectoria más corta, mientras que las exteriores recorren una trayectoria más larga.
¿Qué es el radio de giro?
El radio de giro es la distancia entre el centro de giro de un robot y la trayectoria que sigue una de sus ruedas o un punto específico del vehículo al realizar un giro. Este radio determina qué tan cerrado o amplio puede ser un giro: cuanto menor sea el radio de giro, más cerrado será el giro; cuanto mayor sea, más amplio será.
¿Por qué un vehículo Ackermann no puede desplazarse directamente hacia un costado?
Un vehículo con dirección Ackermann no puede desplazarse directamente hacia un costado porque sus ruedas están diseñadas para rodar principalmente hacia adelante y hacia atrás. Su sistema de dirección permite girar siguiendo una trayectoria curva, pero no moverse lateralmente sin cambiar la orientación del vehículo. Esto se debe a que las ruedas no pueden deslizarse de lado de manera normal sin generar resistencia y fricción.
¿Qué semejanzas tiene con la dirección de un automóvil convencional?
Que ambas permiten cambiar la dirección del vehículo mediante el giro de las ruedas delanteras. Además, durante una curva, las ruedas interiores y exteriores giran con ángulos diferentes para seguir trayectorias distintas y reducir el deslizamiento de las llantas, mejorando la estabilidad y el control del vehículo.



#### Comparación de configuraciones

##### Tabla comparativa de sistemas de locomoción y dirección

|Sistema|Configuración/número típico de ruedas|Movimiento lateral|Giro sobre su eje|Complejidad mecánica|Complejidad de control|Aplicaciones|
|-|-|-|-|-|-|-|
|Diferencial + castor|2 ruedas motrices y 1 o 2 ruedas locas (castor)|No directamente|Sí|Baja|Baja|Robots educativos, seguidores de línea y robots pequeños|
|Omni de 3 rueda|3 ruedas omnidireccionales, generalmente a 120°|Sí|Sí|Media|Media-alta|Robots móviles ágiles y robots de competencia|
|Omni de 4 ruedas|4 ruedas omnidireccionales distribuidas alrededor del chasis|Sí|Sí|Media|Alta|Robots de servicio y plataformas móviles|
|Mecanum|4 ruedas con rodillos inclinados, generalmente a 45°|Sí|Sí|Alta|Alta|Robots industriales, almacenes y transporte de materiales|
|Ackermann|Generalmente 4 ruedas, con dirección en las delanteras|No|No normalmente|Media-alta|Media-alta|Automóviles, vehículos autónomos y robots de transporte|

°1. Robot pequeño para aprender programación y control: elegiría la tracción diferencial, porque es sencilla de construir y programar.
°2. Robot para un almacén con espacios reducidos: elegiría las ruedas Mecanum, porque permiten moverse en varias direcciones y aprovechar mejor el espacio.
°3. Plataforma que necesita moverse lateralmente sin cambiar su orientación: elegiría las ruedas Mecanum, porque permiten desplazarse hacia los lados sin girar el chasis.
°4. Vehículo autónomo similar a un automóvil: elegiría la dirección Ackermann, porque funciona de manera parecida a la dirección de un automóvil real.
°5. Robot para una competencia que necesita cambiar rápidamente de dirección: elegiría las ruedas Mecanum, porque permiten realizar movimientos rápidos en diferentes direcciones.
°6. Robot móvil sencillo que utilice únicamente dos motores: elegiría la tracción diferencial, porque utiliza dos motores independientes para controlar el avance, el retroceso y los giros.



#### Análisis Cinematográfico y Físico de Configuraciones de Robots Móviles

\---

##### 1\. Configuración Diferencial

###### Movimiento Requerido

Para que el robot gire sobre su propio eje (rotación pura sobre el centro geométrico del eje de tracción), las dos ruedas motrices deben **girar a la misma velocidad angular pero en sentidos opuestos** ($\\omega\_{\\text{derecha}} = -\\omega\_{\\text{izquierda}}$).

###### Explicación Física y Geométrica

* **Ubicación del CIR:** El Centro Instantáneo de Rotación (CIR) de un vehículo depende de la relación entre las velocidades lineales de sus ruedas motrices ($v = \\omega \\cdot r$). La posición del CIR a lo largo del eje de las ruedas se calcula geométricamente mediante la proporción de sus velocidades.
* **Mecanismo de Rotación:** Cuando ambas ruedas giran en el mismo sentido a diferente velocidad, el CIR se ubica fuera del robot; si una rueda se detiene ($v=0$), el CIR se traslada exactamente a la rueda detenida.
* **Cancelación de Traslación:** Al aplicar velocidades iguales con signos opuestos ($v\_{\\text{der}} = -v\_{\\text{izq}}$), la diferencia de vectores de velocidad sitúa el CIR exactamente en el punto medio del eje que une ambas ruedas. Dado que la velocidad lineal neta en el centro del robot es cero:
$$v\_{\\text{centro}} = \\frac{v\_{\\text{der}} + v\_{\\text{izq}}}{2} = 0$$
El chasis no experimenta traslación espacial y la energía cinemática se convierte enteramente en velocidad angular pura ($\\dot{\\theta}$).

\---

##### 2\. Configuración Omni (Ruedas Omnidireccionales)

###### Explicación del Movimiento Lateral

Los rodillos pasivos (dispuestos a $90^\\circ$ respecto al eje principal de la rueda) **eliminan la restricción holonómica de no-deslizamiento lateral** (*non-holonomic constraint*).

###### Explicación Física y Vectorial

* **Desplazamiento sin Fricción Transversal:** Una rueda convencional solo permite movimiento en la dirección tangencial de su plano de giro, generando una fuerza de fricción estática infinita en sentido transversal que impide el desplazamiento lateral. En una rueda omnidireccional, al aplicar una fuerza transversal sobre la rueda, los rodillos locos giran libremente sobre sus propios ejes sin oponer resistencia por fricción (fricción por rodadura despreciable en dirección perpendicular al disco).
* **Composición Vectorial:** Al disponer 3 o 4 ruedas omnidireccionales en ángulos de $90^\\circ$ o $120^\\circ$, la fuerza resultante total ejercida sobre el chasis se calcula mediante la suma vectorial de las componentes de velocidad de cada rueda:
$$\\vec{V}*{\\text{robot}} = \\sum*{i=1}^{n} \\vec{v}\_i$$
* **Resultado:** Para moverse lateralmente, las ruedas orientadas en el eje longitudinal giran para impulsar el robot, mientras que los rodillos de las ruedas perpendiculares giran libremente, permitiendo que el vehículo se desplace de lado sin necesidad de reorientar su chasis.

\---

##### 3\. Configuración Mecanum

###### Explicación del Desplazamiento Lateral

El movimiento lateral se logra mediante la **descomposición y cancelación vectorial de las fuerzas transversales y longitudinales** generadas por los rodillos inclinados a $45^\\circ$.

###### Explicación Física y Vectorial

* **Descomposición de Fuerza a $45^\\circ$:** Cada rueda Mecanum posee rodillos pasivos montados en un ángulo de $\\pm 45^\\circ$ respecto a la dirección del disco. Debido a esta inclinación, cuando una rueda gira, la fuerza que transmite al suelo se divide en dos componentes ortogonales de igual magnitud:
$$F\_{\\text{longitudinal}} = F \\cdot \\cos(45^\\circ)$$
$$F\_{\\text{transversal}} = F \\cdot \\sin(45^\\circ)$$
* **Disposición Simétrica:** Las ruedas se montan en una configuración simétrica de tipo "X" u "O" vista desde arriba (alternando la orientación de los rodillos entre las cuatro esquinas).
* **Suma y Cancelación de Vectores:** Para un desplazamiento lateral puro (por ejemplo, hacia la izquierda), las ruedas del lado derecho giran en sentido opuesto entre sí, y las del lado izquierdo de igual forma. Esto provoca que las componentes de fuerza **longitudinales** (hacia adelante/atrás) de las cuatro ruedas se anulen mutuamente ($\\sum F\_x = 0$), mientras que las componentes **transversales** ($F\_y$) creadas por la reacción de los rodillos a $45^\\circ$ se sumen constructivamente en la misma dirección lateral, "empujando" el chasis hacia el costado.

\---

##### 4\. Configuración Ackermann (Geometría Automotriz)

##### Explicación de la Necesidad de Avanzar/Retroceder

Se debe a que esta configuración posee una **restricción cinemática no holonómica severa**, donde la dirección de la velocidad lineal instante a instante está fijada por la orientación del eje trasero no orientable.

###### Explicación Física y Geométrica

* **Restricción Cinemática:** Las ruedas traseras están fijas en una dirección paralela al eje longitudinal del vehículo. Esto significa que el vehículo **únicamente puede experimentar velocidad lineal en la dirección a la que apuntan las ruedas traseras** ($v\_y = 0$ en el sistema local del eje trasero).
* **Geometría de Giro:** La dirección de las ruedas delanteras orientables no "empuja" al coche lateralmente, sino que modifica el radio de curvatura ($R$) del trayecto trazado por el Centro Instantáneo de Rotación (CIR), de acuerdo con la geometría de Ackermann:
$$\\cot(\\delta\_{\\text{ext}}) - \\cot(\\delta\_{\\text{int}}) = \\frac{w}{L}$$
*(donde $L$ es la distancia entre ejes y $w$ el ancho de la vía).*
* **Integración de Trayectoria:** Como el CIR siempre se encuentra sobre la prolongación de la línea del eje trasero fijo, para cambiar la coordenada lateral del vehículo ($y$), es matemáticamente imposible modificarla si la velocidad longitudinal ($v\_x$) es cero. Se requiere un vector de desplazamiento en el tiempo ($\\int v\_x , dt \\neq 0$) para integrar la trayectoria curva y lograr la traslación en el eje transversal.



## MiR250



Nombre del robot: MiR250
Fabricante: Mobile Industrial Robots (MiR)
Tipo de locomoción:
Tracción Diferencial: Utiliza dos ruedas motrices independientes montadas en un eje central común para controlar la velocidad lineal y la velocidad angular de giro.
Número y tipo de ruedas:2 ruedas motrices
fijas: Ruedas estándar de alta tracción ubicadas en el centro lateral, cada una conectada a un motor independiente.
4 ruedas locas (caster wheels): Ruedas pivotantes no motrices distribuidas en las cuatro esquinas del chasis para brindar estabilidad mecánica y soporte de carga.
Sensores principales:LIDAR de seguridad 2D (x2):
Micro-escáneres láser ubicados en las esquinas opuestas para un campo de visión de 360° (mapeo SLAM, localización y navegación segura).
Cámaras 3D de visión (ToF/Estereoscópicas): Montadas en la parte frontal para detección de obstáculos a diferentes alturas y objetos pequeños en el suelo.
Encoders en las ruedas motrices: Sensores de posición angular absoluta/incremental para odometría en tiempo real.
Sensor IMU (Unidad de Medición Inercial): Acelerómetro y giroscopio de 6 ejes para estimación de orientación y estabilidad.
Sensores de proximidad / parachoques de seguridad: Sensores inductivos y de contacto para paradas de emergencia en caso de colisión inminente.
Actuadores utilizados para el movimiento:Servomotores Brushless (BLDC) con encoders integrados (x2): Un actuador para cada una de las ruedas motrices centrales, controlados mediante modulación $\\text{PWM}$ y bucles cerrados de velocidad y posición.Frenos electromagnéticos de seguridad: Actuadores que se activan automáticamente al detenerse o en caso de corte de energía.



Aplicación del robot:Transporte interno de materiales e intralogística (AGV/AMR): Automatización de flujos de trabajo en plantas de manufactura y almacenes industriales (movimiento de carros, tarimas, estanterías y componentes pesados de hasta 250 kg entre celdas de trabajo sin necesidad de líneas marcadas en el suelo).



La configuración Diferencial destaca como la más intuitiva de comprender gracias a que su cinemática responde a la diferencia de velocidades entre dos ruedas independientes sobre un mismo eje, permitiendo modelar y predecir el comportamiento del vehículo mediante trigonometría básica sin recurrir a transformaciones matriciales complejas o descomposición vectorial. Por otro lado, las configuraciones holonómicas como la Omni y la Mecanum ofrecen la mayor libertad de movimiento al proporcionar tres grados de libertad independientes en el plano ($x$, $y$, $\\theta$), lo que les permite trasladarse instantáneamente en cualquier dirección sin necesidad de reorientar el chasis, superando las restricciones no holonómicas de las geometrías tipo Ackermann o Diferencial en espacios estrechos.Debido a su sencillez mecánica, bajo costo y facilidad de control, la configuración Diferencial representa la elección óptima para construir un primer robot móvil, ya que requiere únicamente dos actuadores con encoders y dos ruedas estándar, facilitando una implementación directa del algoritmo de odometría para estimar la posición $(x, y, \\theta)$. La razón por la que no existe una sola configuración de ruedas adecuada para todos los robots radica en el compromiso inevitable (trade-off) entre maniobrabilidad, capacidad de carga, eficiencia y estabilidad según la aplicación; mientras las ruedas Mecanum ganan en maniobrabilidad en interiores planos, pierden adherencia y generan vibraciones en terrenos irregulares, lugar donde la geometría Ackermann o las ruedas convencionales de una tracción diferencial ofrecen una superioridad mecánica, tracción y eficiencia energética insustituibles.

###### Referencias



R. Siegwart, I. R. Nourbakhsh, y D. Scaramuzza, Introduction to Autonomous Mobile Robots, 2a ed. Cambridge, MA, EE. UU.: MIT Press, 2011.

S. S. Saha, Introduction to Robotics, 2a ed. Nueva Delhi, India: McGraw-Hill Education, 2014.

O. Diegel, A. Badve, G. Bright, J. Potgieter, y S. Tlale, "Improved mecanum wheel design for omni-directional robots," en Proc. 2002 Australasian Conf. Robotics and Automation (ACRA), Auckland, Nueva Zelanda, 2002, pp. 117–121.

B. Innocenti, "Mobile robotics: Kinematics, dynamics and control," Documentación técnica de docencia, Universidad de Gerona, España, 2020. \[En línea]. Disponible en: https://dspace.udg.edu

J. Borenstein, H. R. Everett, y L. Feng, Navigating Mobile Robots: Sensors and Techniques. Wellesley, MA, EE. UU.: A K Peters / Ltd., 1996.

