# GitHub Classroom + Codespaces

Estado actual:

- si Codespaces aun no esta aprobado para tu organizacion o para GitHub Education, usa `No IDE`
- el flujo operativo actual del alumnado queda en `Google Colab` para estudiar + `github.dev` o local para resolver `entrega/`
- esta guia conserva tambien la configuracion para Codespaces en cuanto quede disponible

Objetivo:

- usar este proyecto como plantilla de una tarea en GitHub Classroom
- abrir el trabajo del alumnado en GitHub Codespaces sin instalacion local
- mantener juntos `resumen/`, `cuadernos/` y `practica/`

## Decisiones tomadas

- la configuracion de Codespaces vive en [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json)
- el codespace se abre directamente en la raiz del repo
- se instala Python `3.12`, JupyterLab y las extensiones de Python/Jupyter para VS Code web
- al abrir por primera vez el codespace se muestran:
  - `README.md` del proyecto
  - `cuadernos/README.md`
  - `B01`

## Flujo recomendado

### Si Codespaces todavia no esta disponible

1. Usa el repo [xabierolaz/estructura-datos-repaso](https://github.com/xabierolaz/estructura-datos-repaso) como repositorio base.
2. En GitHub, marca el repositorio como template si quieres reutilizarlo en varias tareas.
3. En [GitHub Classroom](https://classroom.github.com/), crea o abre tu classroom.
4. Crea una tarea nueva desde un template repository.
5. Elige este repo como template.
6. En el paso del editor soportado, selecciona `No IDE`.
7. Publica la tarea.
8. El alumnado estudiara `cuadernos/` en Colab y entregara `entrega/entrega_spyder.py` editando en `github.dev` o en local.

### Si Codespaces ya esta disponible

1. Usa el repo [xabierolaz/estructura-datos-repaso](https://github.com/xabierolaz/estructura-datos-repaso) como repositorio base.
2. En GitHub, marca el repositorio como template si quieres reutilizarlo en varias tareas.
3. En [GitHub Classroom](https://classroom.github.com/), crea o abre tu classroom.
4. En la organizacion del classroom, habilita GitHub Codespaces.
5. Crea una tarea nueva desde un template repository.
6. Elige este repo como template.
7. En el paso del editor soportado, selecciona GitHub Codespaces.
8. Publica la tarea.

## Recomendacion operativa

- este repo ya esta recortado para el repaso final
- no hace falta arrastrar el resto del curso al Classroom
- si cambias el nombre del repo en GitHub, actualiza las constantes de `metadata/rebuild_cuadernos.py` y regenera los cuadernos

## Lo que vera el alumnado

- si usas `No IDE`: repo de Classroom + cuadernos de estudio en Colab + entrega en `entrega/` via `github.dev` o local
- si usas Codespaces: boton para abrir el repo de la tarea en Codespaces
- en ambos casos: cuadernos `.ipynb`, `resumen/` y `practica/` ya estructurados

## Limites reales

- GitHub Classroom no crea el contenido pedagogico; solo distribuye el repo
- los enlaces de Colab apuntan al repo canonico de estudio; la entrega real sigue viviendo en el repo individual de Classroom
- si eliges `No IDE`, conviene explicar al alumnado que debe volver siempre a `entrega/` para entregar
- si eliges Codespaces como editor preferido, el flujo principal puede pasar a ser Codespaces
- si activas Codespaces para Classroom, el consumo se imputa a la organizacion del classroom

## Fuentes oficiales

- Classroom con Codespaces: [docs.github.com](https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom)
- Features de Codespaces: [docs.github.com](https://docs.github.com/en/codespaces/about-codespaces/codespaces-features)
- Dev containers para Python: [docs.github.com](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces)
- Abrir archivos automaticamente: [docs.github.com](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/automatically-opening-files-in-the-codespaces-for-a-repository)
