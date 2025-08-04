# 🐂 Ganadera - Sitio Web Institucional

Un sitio web completo y optimizado para **Ganadera**, empresa agroganadera con base en Formosa, Argentina. El sitio es rápido, responsive, escalable y multilingüe (ES/EN), permitiendo la navegación entre chacras y la visualización multimedia con alto rendimiento.

## 🎯 Características Principales

- **Diseño Mobile-First**: Optimizado para dispositivos móviles y fácil navegación para usuarios de tercera edad
- **Responsive**: Se adapta perfectamente a todos los tamaños de pantalla
- **Multilingüe**: Soporte para español e inglés (estructura preparada)
- **Alto Rendimiento**: Imágenes con lazy loading y optimización de recursos
- **Navegación Intuitiva**: Estructura clara y jerárquica
- **Galería Multimedia**: Organización automática de imágenes y videos por estancia con lightbox
- **Planos Interactivos**: Visualización detallada de planos operativos
- **Contacto WhatsApp**: Enlaces directos a WhatsApp para consultas

## 📁 Estructura del Proyecto

```
Oliver - Campos Ganaderas/
├── index.html                 # Página principal
├── estancias/                 # Páginas individuales de cada estancia
│   ├── fortin-yunka.html
│   ├── el-yarara.html
│   ├── la-federacion.html
│   ├── agua-dulce.html
│   ├── campo-lindo.html
│   ├── el-cacuy.html
│   ├── campo-alegre.html
│   ├── la-loli.html
│   └── las-lantanas.html
├── media/                     # Archivos multimedia organizados por estancia
│   ├── fortinyunca/
│   ├── elyarara/
│   ├── federacion/
│   ├── aguadulce/
│   ├── campolindo/
│   ├── cucuy/
│   ├── campoalegre/
│   ├── laloli/
│   └── laslantana/
├── branding/                  # Material de marca
│   └── logo.jpg
├── textos.txt                 # Contenido textual completo
├── generate_estancias.py      # Script para generar páginas automáticamente
└── README.md                  # Este archivo
```

## 🏞️ Estancias Incluidas

| Estancia | Superficie | Producción Destacada | Acceso |
|----------|------------|---------------------|---------|
| 🌾 Fortín Yunká | 20.600 ha | Ganadería + agricultura, ciclo completo | Ruta Nacional 86 pavimentada |
| 🐍 El Yarará | 1.800 ha | Ganadería, 30 potreros, agua de calidad | Ruta 86 pavimentada |
| 🌽 La Federación | 3.100 ha | Ganadería intensiva + agricultura | Ruta 86 pavimentada |
| 💧 Agua Dulce | 13.500 ha | Cría y recría, praderas, ruta atravesada | Ruta Provincial 23 |
| 🌿 Campo Lindo | 1.300 ha | Ganadero con potencial forestal | Ruta Provincial 23 |
| 🌾 El Cacuy | 500 ha | 220 ha agrícolas (maíz, soja, algodón) | Acceso vecinal desde Ruta 86 |
| 🌳 Campo Alegre | 1.050 ha | Ganadero con 450 ha de Gatton Panic | Ruta 86 pavimentada |
| 🐮 La Loli | 1.050 ha | Ganadero + agrícola (maíz implantado) | Ruta 86 pavimentada |
| 🌼 Las Lantanas | 1.050 ha | Ganadero intensivo, campo limpio | Ruta 86 pavimentada |

## 🎨 Diseño y Branding

### Colores
- **Primario**: Verde (#0f4c3a, #1a5f3c, #2d7a4f) - Extraído del logo institucional con mayor contraste
- **Secundario**: Grises para texto y fondos
- **Acentos**: Verde claro para elementos interactivos
- **Alto Contraste**: Optimizado para usuarios de tercera edad

### Tipografía
- **Fuente Principal**: Inter (Google Fonts) - Legible y moderna
- **Jerarquía**: Tamaños claros para fácil lectura

### Características de UX
- **Contraste Alto**: Para usuarios de tercera edad
- **Botones Grandes**: Fácil interacción táctil
- **Navegación Clara**: Menús intuitivos y breadcrumbs
- **Formularios Simples**: Campos grandes y claros

## 📸 Organización de Multimedia

### Estructura de Archivos
- `hero.jpg` → Imagen principal (Hero section)
- `destacada*.jpg` → Imágenes destacadas (sección destacada con lightbox)
- `plano*.jpg` → Imágenes de planos o mapas (sección "🗺️ Plano operativo" con lightbox)
- `*.mp4` → Videos (sección "🎬 Videos")
- Otros `.jpg` o `.png` → Galería general (con lightbox)
- `PRINCIPAL.jpg` → Imagen hero del homepage

### Optimización
- **Lazy Loading**: Todas las imágenes cargan bajo demanda
- **Responsive Images**: Se adaptan al tamaño de pantalla
- **Compresión**: Optimizadas para web sin pérdida de calidad

## 🛠️ Tecnologías Utilizadas

- **HTML5**: Estructura semántica y accesible
- **Tailwind CSS**: Framework CSS utility-first para diseño responsive
- **JavaScript**: Funcionalidades interactivas mínimas
- **Google Fonts**: Tipografía optimizada para web

## 🚀 Instalación y Uso

### Requisitos
- Servidor web (Apache, Nginx, o servidor local)
- Navegador web moderno

### Instalación
1. Clona o descarga el proyecto
2. Coloca todos los archivos en tu servidor web
3. Accede a `index.html` desde tu navegador

### Generación de Páginas
Para regenerar las páginas de estancias:
```bash
python3 generate_estancias.py
```

## 📱 Características Responsive

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Optimizaciones Mobile
- Menú hamburguesa para navegación
- Imágenes optimizadas para pantallas pequeñas
- Formularios adaptados para touch
- Botones de tamaño adecuado para dedos

## 🌐 Funcionalidades

### Página Principal (`index.html`)
- Hero section con imagen PRINCIPAL.jpg de Fortín Yunká
- Presentación institucional de Ganadera
- Grid visual con las 10 chacras
- Call to Action institucional
- Enlaces directos a WhatsApp

### Páginas de Estancias
- Imagen hero como portada
- Secciones organizadas:
  - 📍 Información general
  - 🌿 Producción y uso del suelo
  - 🏗️ Infraestructura
  - 🗺️ Plano operativo (clickeable con lightbox)
  - 🏞️ Descripción institucional
- Galería multimedia completa con lightbox
- Videos con controles nativos
- Navegación lateral entre estancias
- Enlaces directos a WhatsApp

## 📞 Contacto

**Ganadera**
- 📧 Email: owcc@aol.com
- 📞 Teléfono: +1 (412) 417-6676
- 🌐 Web: www.caminosganadera.com
- 💬 WhatsApp: [https://wa.link/gf7bfo](https://wa.link/gf7bfo)

## 🔧 Personalización

### Modificar Contenido
1. Edita `textos.txt` para cambiar el contenido textual
2. Ejecuta `generate_estancias.py` para regenerar las páginas
3. Actualiza las imágenes en la carpeta `media/` según corresponda

### Agregar Nueva Estancia
1. Agrega la información en `generate_estancias.py`
2. Crea la carpeta correspondiente en `media/`
3. Ejecuta el script de generación

### Cambiar Estilo
1. Modifica las clases de Tailwind CSS en los archivos HTML
2. Ajusta los colores en las variables CSS
3. Personaliza las fuentes en el head de cada página

## 📊 SEO y Accesibilidad

### SEO
- Meta tags optimizados
- Estructura semántica HTML5
- URLs amigables
- Contenido estructurado

### Accesibilidad
- Alt text en todas las imágenes
- Navegación por teclado
- Contraste adecuado
- Textos legibles

## 🎯 Objetivos Cumplidos

✅ **Sitio completo y funcional**
✅ **Diseño responsive y mobile-first**
✅ **Optimizado para usuarios de tercera edad**
✅ **Navegación clara y jerárquica**
✅ **Galería multimedia completa con lightbox**
✅ **Planos interactivos clickeables**
✅ **Enlaces directos a WhatsApp**
✅ **Alto contraste para mejor legibilidad**
✅ **Estructura escalable**
✅ **Alto rendimiento**
✅ **Soporte multilingüe preparado**

## 📄 Licencia

© 2024 Ganadera. Todos los derechos reservados.

---

**Desarrollado con ❤️ para Ganadera**
*Productividad, escala y visión territorial en el corazón de Formosa, Argentina* 