# Optimizacion-Profesores
Programa de optimización en `Python 3.11` para maximizar el resultado, usando la librería Pulp

## Librerías Usadas
### Pulp
Librería usada para la resolución de problemas lineales, se instala con:
```
python -m pip install pulp
```

## Problema a solucionar
```
Una universidad está programando las clases para el próximo semestre académico y requiere buscar la mejor asignación posible de profesores a los distintos cursos que se deben dictar. Considere que existen 5profesores: A, B, C, D, E y 5 cursos (asignaturas): C1, C2, C3, C4, C5. Adicionalmente, los profesores han manifestado sus preferencias por dictar los distintos cursos en una escala de 1 a 10, donde 10 es la máxima puntuación y 1 la mínima puntuación o preferencia. Se asume que cada profesor es apto para dictar cualquier curso, Independiente del puntaje de su preferencia.
```
Es decir, se debe maximizar la respuesta para obtener el mayor beneficio. Tabla a usar en este caso
![image](https://github.com/RJSR/Optimizacion-Profesores/assets/78589528/903b0a15-8c93-441e-8466-f3b46cf3e608)


## Puntos a mejorar

- Implementación de una GUI en la que se muestre el enunciado el problema con su tabla, y la resolución de la respuesta, usando las librerías `Django`, `Flet` o `PyQT6`
- Modificación de la funcionalidad, al preguntarle al usuario la función objetivo, las restricciones, y los datos de cada valor en la tabla, para obtener la optimización de otros problemas de este tipo, esto requiere previa familiarización del usuario con el tema.
- Implementación de una respuesta gráfica usando la tabla, mostrando la ruta tomada para la resolución del problema.
