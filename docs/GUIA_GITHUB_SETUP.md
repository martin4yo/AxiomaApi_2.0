# Guía: Setup de GitHub para Documentación Axioma ERP

## Opción Recomendada: Crear Repositorio Nuevo

### 1. Crear el repositorio en GitHub

**En el navegador (GitHub.com):**

1. Ir a https://github.com/martin4yo
2. Click en "New repository" (botón verde)
3. Configurar:
   - **Repository name:** `axioma-data-dictionary` (o el nombre que elijan)
   - **Description:** "Diccionario de datos y documentación técnica de Axioma ERP"
   - **Visibility:**
     - ✅ **Private** (recomendado - solo ustedes lo ven)
     - ⬜ Public (si quieren que sea público)
   - ✅ **Add a README file** (marcar esta opción)
   - **Add .gitignore:** Python
   - **Choose a license:** MIT (opcional)
4. Click "Create repository"

### 2. Clonar el repositorio a tu máquina

```bash
# Navegar a la carpeta raíz del proyecto
cd "C:\Ex drive\AXIOMA\ERP"

# Clonar el nuevo repositorio
git clone https://github.com/martin4yo/axioma-data-dictionary.git

# Entrar al repositorio
cd axioma-data-dictionary
```

### 3. Copiar archivos iniciales

```bash
# Copiar el HTML de propuesta
cp ../Propuesta_Diccionario_Datos.html .

# Copiar el documento de referencia actual
cp ../AXIOMA_ERP_REFERENCE.md .

# Opcional: Copiar el diseño drawio
cp "../Diseño MVP.drawio" .
```

### 4. Crear estructura inicial del proyecto

```bash
# Crear carpetas básicas
mkdir -p docs/data-dictionary
mkdir -p docs/business-rules
mkdir -p docs/api-reference
mkdir -p schemas/postgresql
mkdir -p schemas/mysql
mkdir -p scripts
```

### 5. Crear README.md descriptivo

Crear archivo `README.md` con este contenido:

```markdown
# Axioma ERP - Diccionario de Datos

Documentación técnica completa del sistema Axioma ERP, incluyendo diccionario de datos, reglas de negocio, y referencias de API.

## 📋 Contenido

- **Propuesta_Diccionario_Datos.html** - Propuesta de sistema de documentación (en evaluación)
- **AXIOMA_ERP_REFERENCE.md** - Referencia técnica completa actual
- **docs/** - Documentación organizada por categorías
- **schemas/** - Schemas de bases de datos (PostgreSQL y MySQL)

## 🚀 Estado

🔄 **En Desarrollo** - Evaluando opciones de implementación

## 👥 Colaboradores

- [martin4yo](https://github.com/martin4yo)
- [Tu socio]

## 📄 Licencia

Privado - Axioma ERP
```

### 6. Hacer el primer commit y push

```bash
# Ver qué archivos hay
git status

# Agregar todos los archivos
git add .

# Commit inicial
git commit -m "Initial commit: Propuesta de diccionario de datos y referencia técnica"

# Push a GitHub
git push origin main
```

### 7. Tu socio puede clonarlo ahora

Tu socio ejecuta en su máquina:

```bash
cd "C:\ruta\donde\trabaja"
git clone https://github.com/martin4yo/axioma-data-dictionary.git
cd axioma-data-dictionary
```

---

## Workflow de Colaboración Recomendado

### Flujo básico (simple, recomendado para empezar)

```bash
# Antes de empezar a trabajar: SIEMPRE hacer pull
git pull origin main

# Hacer cambios en los archivos...

# Ver qué cambió
git status
git diff

# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "Descripción clara de los cambios"

# Push a GitHub
git push origin main
```

### Flujo con branches (recomendado para cambios grandes)

```bash
# Crear branch para nueva feature
git checkout -b feature/implementar-mkdocs

# Hacer cambios...

# Commit en el branch
git add .
git commit -m "Implementar estructura MkDocs"

# Push del branch
git push origin feature/implementar-mkdocs

# En GitHub: Crear Pull Request
# Tu socio revisa y aprueba
# Luego hacer merge a main
```

---

## Alternativa: Subir a Repositorio Existente

Si deciden **NO** crear un nuevo repo y usar uno existente:

### Opción A: Agregar a `project/`

```bash
cd "C:\Ex drive\AXIOMA\ERP\project"

# Crear carpeta docs si no existe
mkdir -p docs

# Copiar archivos
cp ../Propuesta_Diccionario_Datos.html docs/
cp ../AXIOMA_ERP_REFERENCE.md docs/

# Git workflow
git add docs/
git commit -m "Add: Documentación de propuesta de diccionario de datos"
git push origin main
```

### Opción B: Agregar a `AxiomaApi_2.0/`

```bash
cd "C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0"

# Crear carpeta docs si no existe
mkdir -p docs

# Copiar archivos
cp ../Propuesta_Diccionario_Datos.html docs/
cp ../AXIOMA_ERP_REFERENCE.md docs/

# Git workflow
git add docs/
git commit -m "Add: Documentación de propuesta de diccionario de datos"
git push origin main
```

---

## Mejores Prácticas para Trabajar en Equipo

### 1. SIEMPRE hacer pull antes de empezar

```bash
git pull origin main
```

Esto evita conflictos al asegurarse de tener la última versión.

### 2. Commits frecuentes con mensajes claros

```bash
# ✅ BIEN
git commit -m "Add: Sección de validaciones en diccionario de datos"
git commit -m "Fix: Corrección en diagrama de relaciones"
git commit -m "Update: Agregar tabla de impuestos"

# ❌ MAL
git commit -m "cambios"
git commit -m "fix"
git commit -m "asdf"
```

### 3. Usar .gitignore apropiado

Crear archivo `.gitignore`:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# Node
node_modules/
npm-debug.log*
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporales
*.tmp
*.bak
~$*
```

### 4. Comunicación sobre cambios grandes

Antes de hacer cambios grandes:
- Avisar al otro socio
- Usar branches separados
- Hacer Pull Requests para revisar cambios

---

## Resolución de Conflictos (si suceden)

Si ambos modifican el mismo archivo:

```bash
# Al hacer pull pueden ver:
# CONFLICT (content): Merge conflict in archivo.md

# Abrir el archivo, verán algo como:
<<<<<<< HEAD
Tu versión
=======
Versión de tu socio
>>>>>>> branch-name

# Editar manualmente para combinar ambas versiones
# Luego:
git add archivo.md
git commit -m "Resolve: Conflicto en archivo.md"
git push origin main
```

---

## GitHub Pages (si quieren publicar la documentación)

Si implementan MkDocs y quieren que esté en línea:

### 1. Configurar GitHub Pages

En GitHub.com:
1. Ir al repositorio
2. Settings → Pages
3. Source: "GitHub Actions"

### 2. Crear workflow de deploy

Crear `.github/workflows/deploy.yml`:

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install mkdocs-material

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
```

### 3. URL pública

Estará disponible en:
```
https://martin4yo.github.io/axioma-data-dictionary/
```

---

## Comandos Git de Referencia Rápida

```bash
# Ver estado
git status

# Ver historial
git log --oneline

# Ver diferencias
git diff

# Deshacer cambios no commiteados
git restore archivo.txt

# Deshacer último commit (mantiene cambios)
git reset --soft HEAD~1

# Ver branches
git branch

# Cambiar de branch
git checkout nombre-branch

# Crear y cambiar a nuevo branch
git checkout -b nuevo-branch

# Actualizar desde remoto
git pull origin main

# Subir cambios
git push origin main

# Ver archivos ignorados
git status --ignored
```

---

## Recomendación Final para Ustedes

Para **este proyecto específico**:

1. ✅ **Crear nuevo repositorio** `axioma-data-dictionary`
   - Mantiene la documentación separada del código
   - Más limpio y organizado
   - Fácil de compartir solo la documentación si es necesario

2. ✅ **Workflow simple al principio**
   - Ambos trabajan en `main`
   - Hacer `pull` antes de cada sesión
   - `commit` + `push` al terminar
   - Cuando tengan más experiencia, pasar a branches

3. ✅ **Commits descriptivos**
   - "Add: ...", "Update: ...", "Fix: ..."
   - Facilita entender qué cambió

4. ✅ **Comunicación**
   - Avisar si van a hacer cambios grandes
   - Revisar los commits del otro periódicamente

---

## Próximos Pasos Inmediatos

1. **Decidir:** ¿Nuevo repo o usar uno existente?
2. **Crear/configurar** el repositorio según la decisión
3. **Subir** la propuesta HTML y el documento de referencia
4. **Compartir URL** del repositorio con tu socio
5. **Tu socio clona** el repositorio
6. **Evalúan juntos** las opciones del HTML
7. **Deciden** qué implementar
8. **Comunican decisión** para proceder con implementación

---

**Última actualización:** Diciembre 2025
