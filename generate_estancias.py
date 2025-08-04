#!/usr/bin/env python3
"""
Script to generate all estancia pages for Caminos Ganadera website.
This script reads the content from textos.txt and creates individual HTML pages for each estancia.
"""

import os
import re
from pathlib import Path

# Estancia data mapping
ESTANCIAS = {
    'fortin-yunka': {
        'name': 'Fortín Yunká',
        'folder': 'fortinyunca',
        'surface': '20.600',
        'description': 'Ganadería + agricultura, ciclo completo',
        'access': 'Ruta Nacional 86 pavimentada',
        'emoji': '🌾',
        'next': 'el-yarara',
        'prev': None
    },
    'el-yarara': {
        'name': 'El Yarará',
        'folder': 'elyarara',
        'surface': '1.800',
        'description': 'Ganadería, 30 potreros, agua de calidad',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🐍',
        'next': 'la-federacion',
        'prev': 'fortin-yunka'
    },
    'la-federacion': {
        'name': 'La Federación',
        'folder': 'federacion',
        'surface': '3.100',
        'description': 'Ganadería intensiva + agricultura',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌽',
        'next': 'agua-dulce',
        'prev': 'el-yarara'
    },
    'agua-dulce': {
        'name': 'Agua Dulce',
        'folder': 'aguadulce',
        'surface': '13.500',
        'description': 'Cría y recría, praderas, ruta atravesada',
        'access': 'Ruta Provincial 23',
        'emoji': '💧',
        'next': 'campo-lindo',
        'prev': 'la-federacion'
    },
    'campo-lindo': {
        'name': 'Campo Lindo',
        'folder': 'campolindo',
        'surface': '1.300',
        'description': 'Ganadero con potencial forestal',
        'access': 'Ruta Provincial 23',
        'emoji': '🌿',
        'next': 'el-cacuy',
        'prev': 'agua-dulce'
    },
    'el-cacuy': {
        'name': 'El Cacuy',
        'folder': 'cucuy',
        'surface': '500',
        'description': '220 ha agrícolas (maíz, soja, algodón)',
        'access': 'Acceso vecinal desde Ruta 86',
        'emoji': '🌾',
        'next': 'campo-alegre',
        'prev': 'campo-lindo'
    },
    'campo-alegre': {
        'name': 'Campo Alegre',
        'folder': 'campoalegre',
        'surface': '1.050',
        'description': 'Ganadero con 450 ha de Gatton Panic',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌳',
        'next': 'la-loli',
        'prev': 'el-cacuy'
    },
    'la-loli': {
        'name': 'La Loli',
        'folder': 'laloli',
        'surface': '1.050',
        'description': 'Ganadero + agrícola (maíz implantado)',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🐮',
        'next': 'las-lantanas',
        'prev': 'campo-alegre'
    },
    'las-lantanas': {
        'name': 'Las Lantanas',
        'folder': 'laslantana',
        'surface': '1.050',
        'description': 'Ganadero intensivo, campo limpio',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌼',
        'next': None,
        'prev': 'la-loli'
    }
}

def get_all_media_files(estancia_folder):
    """Get ALL media files for an estancia from the media folder and subfolders."""
    media_path = Path(f"media/{estancia_folder}")
    if not media_path.exists():
        return [], [], [], [], []
    
    # Get all files recursively (including subfolders)
    all_files = []
    for root, dirs, files in os.walk(media_path):
        for file in files:
            file_path = Path(root) / file
            # Get relative path from media folder
            relative_path = file_path.relative_to(media_path)
            all_files.append((file_path, relative_path))
    
    # Filter image and video files
    image_files = []
    video_files = []
    
    for file_path, relative_path in all_files:
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            image_files.append((file_path, relative_path))
        elif file_path.suffix.lower() == '.mp4':
            video_files.append((file_path, relative_path))
    
    # Find hero image
    hero_files = [f for f, rel_path in image_files if f.name.lower().startswith('hero')]
    hero_image = hero_files[0] if hero_files else None
    
    # Find destacada images
    destacada_files = [f for f, rel_path in image_files if 'destacada' in f.name.lower()]
    
    # Find plano images
    plano_files = [f for f, rel_path in image_files if 'plano' in f.name.lower()]
    
    # Find other images (ALL remaining images)
    other_images = [f for f, rel_path in image_files 
                   if not f.name.lower().startswith('hero') 
                   and 'destacada' not in f.name.lower() 
                   and 'plano' not in f.name.lower()]
    
    # Create a mapping of file paths to relative paths for easy access
    file_to_relative = {f: rel_path for f, rel_path in image_files}
    video_to_relative = {f: rel_path for f, rel_path in video_files}
    
    return hero_image, destacada_files, plano_files, video_files, other_images, file_to_relative, video_to_relative

def generate_estancia_page(estancia_id, estancia_data):
    """Generate HTML page for a specific estancia."""
    
    # Get media files
    hero_image, destacada_files, plano_files, video_files, other_images, file_to_relative, video_to_relative = get_all_media_files(estancia_data['folder'])
    
    print(f"Processing {estancia_data['name']}:")
    print(f"  - Hero images: {len([hero_image]) if hero_image else 0}")
    print(f"  - Destacada images: {len(destacada_files)}")
    print(f"  - Plano images: {len(plano_files)}")
    print(f"  - Other images: {len(other_images)}")
    print(f"  - Video files: {len(video_files)}")
    
    # Navigation removed - users should only navigate to homepage
    nav_prev = '<span></span>'
    nav_next = '<span></span>'
    
    # Generate gallery sections with lightbox
    destacada_html = ""
    if destacada_files:
        destacada_images = []
        for f in destacada_files:
            # Get relative path for src
            relative_path = file_to_relative[f]
            destacada_images.append(f'<a href="../media/{estancia_data["folder"]}/{relative_path}" data-fancybox="destacada-{estancia_id}" data-caption="{estancia_data["name"]} - Imagen Destacada"><img src="../media/{estancia_data["folder"]}/{relative_path}" alt="{estancia_data["name"]} - Destacada" class="w-full h-64 object-cover rounded-lg shadow-sm cursor-pointer hover:scale-105 transition-transform duration-300" loading="lazy"></a>')
        
        destacada_html = f"""
            <div class="mb-12">
                <h3 class="text-2xl font-semibold text-gray-900 mb-6">Imágenes Destacadas</h3>
                <div id="gallery-destacada" class="gallery-grid">
                    {chr(10).join(destacada_images)}
                </div>
            </div>
        """
    
    other_images_html = ""
    if other_images:
        other_images_list = []
        for f in other_images:
            # Get relative path for src
            relative_path = file_to_relative[f]
            other_images_list.append(f'<a href="../media/{estancia_data["folder"]}/{relative_path}" data-fancybox="general-{estancia_id}" data-caption="{estancia_data["name"]} - Galería"><img src="../media/{estancia_data["folder"]}/{relative_path}" alt="{estancia_data["name"]} - Imagen" class="w-full h-64 object-cover rounded-lg shadow-sm cursor-pointer hover:scale-105 transition-transform duration-300" loading="lazy"></a>')
        
        other_images_html = f"""
            <div class="mb-12">
                <h3 class="text-2xl font-semibold text-gray-900 mb-6">Galería General</h3>
                <div id="gallery-general" class="gallery-grid">
                    {chr(10).join(other_images_list)}
                </div>
            </div>
        """
    
    plano_html = ""
    if plano_files:
        plano_images = []
        for f in plano_files:
            # Get relative path for src
            relative_path = file_to_relative[f]
            plano_images.append(f'<a href="../media/{estancia_data["folder"]}/{relative_path}" data-fancybox="plano-{estancia_id}" data-caption="Plano {estancia_data["name"]}"><img src="../media/{estancia_data["folder"]}/{relative_path}" alt="Plano {estancia_data["name"]}" class="w-full rounded-lg shadow-sm cursor-pointer hover:scale-105 transition-transform duration-300" loading="lazy"></a>')
        
        plano_html = f"""
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div>
                    <div class="bg-white p-6 rounded-lg shadow-sm">
                        <h3 class="text-xl font-semibold text-gray-900 mb-4">Características del Plano</h3>
                        <ul class="space-y-3 text-gray-600">
                            <li class="flex items-start space-x-3">
                                <span class="text-green-600">•</span>
                                <span>Infraestructura distribuida estratégicamente</span>
                            </li>
                            <li class="flex items-start space-x-3">
                                <span class="text-green-600">•</span>
                                <span>Potreros organizados para rotación eficiente</span>
                            </li>
                            <li class="flex items-start space-x-3">
                                <span class="text-green-600">•</span>
                                <span>Accesos desde múltiples puntos</span>
                            </li>
                            <li class="flex items-start space-x-3">
                                <span class="text-green-600">•</span>
                                <span>Infraestructura centralizada</span>
                            </li>
                        </ul>
                    </div>
                </div>
                
                <div id="gallery-plano">
                    {chr(10).join(plano_images)}
                </div>
            </div>
        """
    
    video_html = ""
    if video_files:
        video_elements = []
        for f, rel_path in video_files:
            video_elements.append(f'''
            <div class="video-container">
                <video controls>
                    <source src="../media/{estancia_data["folder"]}/{rel_path}" type="video/mp4">
                    Tu navegador no soporta el elemento video.
                </video>
            </div>''')
        
        video_html = f"""
            <div>
                <h3 class="text-2xl font-semibold text-gray-900 mb-6">🎬 Videos</h3>
                <div class="grid md:grid-cols-2 gap-8">
                    {chr(10).join(video_elements)}
                </div>
            </div>
        """
    
    # Hero image source
    hero_src = f'../media/{estancia_data["folder"]}/{hero_image.name}' if hero_image else f'../media/{estancia_data["folder"]}/destacada.jpg'
    
    # Generate the HTML content
    html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{estancia_data["name"]} | {estancia_data["surface"]} hectáreas en Formosa</title>
        <meta name="description" content="{estancia_data["name"]} es una estancia ubicada en Formosa, Argentina. {estancia_data["surface"]} hectáreas dedicadas a {estancia_data["description"]}.">
        
        <!-- Open Graph / Facebook -->
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://caminosganadera.com/estancias/{estancia_id}.html">
        <meta property="og:title" content="{estancia_data["name"]} | {estancia_data["surface"]} hectáreas en Formosa">
        <meta property="og:description" content="{estancia_data["name"]} es una estancia ubicada en Formosa, Argentina. {estancia_data["surface"]} hectáreas dedicadas a {estancia_data["description"]}.">
        <meta property="og:image" content="https://caminosganadera.com/media/{estancia_data["folder"]}/hero.jpg">
        <meta property="og:image:width" content="1200">
        <meta property="og:image:height" content="630">
        
        <!-- Twitter -->
        <meta property="twitter:card" content="summary_large_image">
        <meta property="twitter:url" content="https://caminosganadera.com/estancias/{estancia_id}.html">
        <meta property="twitter:title" content="{estancia_data["name"]} | {estancia_data["surface"]} hectáreas en Formosa">
        <meta property="twitter:description" content="{estancia_data["name"]} es una estancia ubicada en Formosa, Argentina. {estancia_data["surface"]} hectáreas dedicadas a {estancia_data["description"]}.">
        <meta property="twitter:image" content="https://caminosganadera.com/media/{estancia_data["folder"]}/hero.jpg">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Lightbox CSS -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/css/lightbox.min.css" rel="stylesheet">
    
    <style>
        body {{
            font-family: 'Inter', sans-serif;
        }}
        
        .hero-gradient {{
            background: linear-gradient(135deg, #0f4c3a 0%, #1a5f3c 50%, #2d7a4f 100%);
        }}
        
        .card-hover {{
            transition: all 0.3s ease;
        }}
        
        .card-hover:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }}
        
        .text-shadow {{
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, #0f4c3a 0%, #1a5f3c 100%);
            transition: all 0.3s ease;
        }}
        
        .btn-primary:hover {{
            background: linear-gradient(135deg, #1a5f3c 0%, #2d7a4f 100%);
            transform: translateY(-2px);
        }}
        
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
        }}
        
        .video-container {{
            position: relative;
            width: 100%;
            height: 0;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
        }}
        
        .video-container video {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .text-high-contrast {{
            color: #1a202c !important;
        }}
    </style>
</head>
<body class="bg-gray-50 overflow-x-hidden">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center py-4">
                <div class="flex items-center">
                    <a href="../index.html" class="flex items-center">
                        <img src="../branding/logo.jpg" alt="" class="h-5 sm:h-6 md:h-8 w-auto object-contain max-w-none">
                        <span class="ml-2 sm:ml-3 text-lg sm:text-xl font-semibold text-gray-900"></span>
                    </a>
                </div>
                
                <div class="flex items-center space-x-2 sm:space-x-4">
                    <button id="language-toggle" class="text-xs sm:text-sm font-medium text-gray-700 hover:text-green-700 transition-colors">
                        EN
                    </button>
                    <a href="https://wa.link/gf7bfo" target="_blank" class="btn-primary text-white px-3 sm:px-6 py-2 rounded-lg text-xs sm:text-sm font-medium">
                        Contacto
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative h-96 overflow-hidden">
        <img src="{hero_src}" alt="{estancia_data["name"]}" class="w-full h-full object-cover">
        <div class="absolute inset-0 bg-black bg-opacity-50"></div>
        <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-center text-white">
                <h1 class="text-4xl md:text-6xl font-bold text-shadow mb-4">
                    {estancia_data["emoji"]} {estancia_data["name"]}
                </h1>
                <p class="text-xl md:text-2xl text-shadow">
                    {estancia_data["surface"]} hectáreas - {estancia_data["description"]}
                </p>
            </div>
        </div>
    </section>

    <!-- Navigation -->
    <nav class="bg-white border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col sm:flex-row items-center justify-between py-4 space-y-4 sm:space-y-0">
                <div class="flex items-center space-x-4 sm:space-x-8 text-sm sm:text-base">
                    <a href="#informacion" class="text-gray-700 hover:text-green-600 transition-colors">📍 Información</a>
                    <a href="#produccion" class="text-gray-700 hover:text-green-600 transition-colors">🌿 Producción</a>
                    <a href="#infraestructura" class="text-gray-700 hover:text-green-600 transition-colors">🏗️ Infraestructura</a>
                    <a href="#plano" class="text-gray-700 hover:text-green-600 transition-colors">🗺️ Plano</a>
                    <a href="#galeria" class="text-gray-700 hover:text-green-600 transition-colors">📸 Galería</a>
                </div>
                

            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <!-- Información General -->
        <section id="informacion" class="mb-16">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                    📍 Información General
                </h2>
                <div class="w-24 h-1 bg-green-600 mx-auto"></div>
            </div>
            
            <div class="grid md:grid-cols-2 gap-12">
                <div>
                    <div class="bg-white p-8 rounded-lg shadow-sm">
                        <h3 class="text-2xl font-semibold text-gray-900 mb-6">Características Principales</h3>
                        <div class="space-y-4">
                            <div class="flex items-center space-x-4">
                                <div class="text-green-600 text-2xl">🌾</div>
                                <div>
                                    <p class="font-semibold text-gray-900">Superficie total</p>
                                    <p class="text-gray-600">{estancia_data["surface"]} hectáreas</p>
                                </div>
                            </div>
                            
                            <div class="flex items-center space-x-4">
                                <div class="text-green-600 text-2xl">📍</div>
                                <div>
                                    <p class="font-semibold text-gray-900">Ubicación</p>
                                    <p class="text-gray-600">{estancia_data["access"]}, Formosa, Argentina</p>
                                </div>
                            </div>
                            
                            <div class="flex items-center space-x-4">
                                <div class="text-green-600 text-2xl">🐂</div>
                                <div>
                                    <p class="font-semibold text-gray-900">Uso principal</p>
                                    <p class="text-gray-600">{estancia_data["description"]}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div>
                    <div class="bg-green-50 p-8 rounded-lg">
                        <h3 class="text-2xl font-semibold text-gray-900 mb-6">Descripción Institucional</h3>
                        <p class="text-gray-700 leading-relaxed">
                            {estancia_data["name"]} es una estancia destacada ubicada estratégicamente 
                            en la provincia de Formosa. Con {estancia_data["surface"]} hectáreas operativas, 
                            representa una oportunidad única para la producción agroganadera en la provincia de Formosa.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Plano Operativo -->
        <section id="plano" class="mb-16">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                    🗺️ Plano Operativo
                </h2>
                <div class="w-24 h-1 bg-green-600 mx-auto"></div>
            </div>
            
            {plano_html}
        </section>

        <!-- Galería -->
        <section id="galeria" class="mb-16">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                    📸 Galería Multimedia
                </h2>
                <div class="w-24 h-1 bg-green-600 mx-auto"></div>
            </div>
            
            {destacada_html}
            {other_images_html}
            {video_html}
        </section>

        <!-- Contact Section -->
        <section id="contact" class="bg-white rounded-lg shadow-sm p-8">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">
                    ¿Interesado en {estancia_data["name"]}?
                </h2>
                <p class="text-lg text-gray-600">
                    Contáctanos para más información sobre esta estancia
                </p>
            </div>
            
            <div class="grid lg:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Información de Contacto</h3>
                    <div class="space-y-3">
                        <div class="flex items-center space-x-3">
                            <span class="text-green-600">📧</span>
                            <span class="text-gray-700">owcc@aol.com</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="text-green-600">📞</span>
                            <span class="text-gray-700">+1 (412) 417-6676</span>
                        </div>

                    </div>
                </div>
                
                <div>
                    <form action="mailto:owcc@aol.com" method="post" enctype="text/plain" class="space-y-4">
                        <div class="grid md:grid-cols-2 gap-4">
                            <input type="text" name="nombre" placeholder="Nombre" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" required>
                            <input type="text" name="apellido" placeholder="Apellido" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" required>
                        </div>
                        <div class="grid md:grid-cols-2 gap-4">
                            <input type="email" name="email" placeholder="Email" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" required>
                            <input type="tel" name="telefono" placeholder="Teléfono" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent">
                        </div>
                        <textarea name="mensaje" rows="4" placeholder="Mensaje sobre {estancia_data["name"]}..." class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"></textarea>
                        <button type="submit" class="btn-primary text-white px-8 py-3 rounded-lg font-semibold w-full">
                            Enviar
                        </button>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12 mt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-3 gap-8">
                <div>
                    <div class="flex items-center mb-4">
                        <img src="../branding/logo.jpg" alt="" class="h-6 sm:h-8 w-auto object-contain max-w-none">
                        <span class="ml-3 text-lg font-semibold"></span>
                    </div>
                    <p class="text-gray-400">
                        Productividad, escala y visión territorial en el corazón de Formosa, Argentina.
                    </p>
                </div>
                
                <div>
                    <h3 class="text-lg font-semibold mb-4">Contacto</h3>
                    <div class="space-y-2 text-gray-400">
                        <p><a href="mailto:owcc@aol.com" class="hover:text-white transition-colors">📧 owcc@aol.com</a></p>
                        <p><a href="tel:+14124176676" class="hover:text-white transition-colors">📞 +1 (412) 417-6676</a></p>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-lg font-semibold mb-4">Estancias</h3>
                    <div class="grid grid-cols-2 gap-2 text-sm text-gray-400">
                        <a href="fortin-yunka.html" class="hover:text-white transition-colors">Fortín Yunká</a>
                        <a href="el-yarara.html" class="hover:text-white transition-colors">El Yarará</a>
                        <a href="la-federacion.html" class="hover:text-white transition-colors">La Federación</a>
                        <a href="agua-dulce.html" class="hover:text-white transition-colors">Agua Dulce</a>
                        <a href="campo-lindo.html" class="hover:text-white transition-colors">Campo Lindo</a>
                        <a href="el-cacuy.html" class="hover:text-white transition-colors">El Cacuy</a>
                        <a href="campo-alegre.html" class="hover:text-white transition-colors">Campo Alegre</a>
                        <a href="la-loli.html" class="hover:text-white transition-colors">La Loli</a>
                        <a href="las-lantanas.html" class="hover:text-white transition-colors">Las Lantanas</a>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2025 Caminos Ganadera. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>

    <!-- WhatsApp Floating Button -->
    <div class="fixed bottom-4 right-4 sm:bottom-6 sm:right-6 z-50">
        <a href="https://wa.link/gf7bfo" target="_blank" class="bg-green-500 hover:bg-green-600 text-white p-3 sm:p-4 rounded-full shadow-lg transition-all duration-300 hover:scale-110 flex items-center justify-center">
            <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
            </svg>
        </a>
    </div>

    <!-- Fancybox CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css"/>
    
    <!-- Fancybox JS -->
    <script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Initialize Fancybox
            Fancybox.bind("[data-fancybox]", {{
                loop: true,
                buttons: ["zoom", "slideShow", "fullScreen", "thumbs", "close"],
                animationEffect: "fade",
                transitionEffect: "slide",
                thumbs: {{
                    autoStart: false
                }},
                on: {{
                    initLayout: (fancybox) => {{
                        // Add custom styles
                        const style = document.createElement('style');
                        style.textContent = '.fancybox__container {{ z-index: 9999; }} .fancybox__bg {{ background: rgba(0, 0, 0, 0.9); }} .fancybox__caption {{ font-family: "Inter", sans-serif; font-size: 16px; font-weight: 500; }} .fancybox__counter {{ font-family: "Inter", sans-serif; font-size: 14px; }}';
                        document.head.appendChild(style);
                    }}
                }}
            }});
        }});
    </script>

    <script>
        // Language toggle functionality
        const languageToggle = document.getElementById('language-toggle');
        let isEnglish = false;
        
        languageToggle.addEventListener('click', () => {{
            isEnglish = !isEnglish;
            languageToggle.textContent = isEnglish ? 'ES' : 'EN';
            // Here you would implement the actual language switching logic
        }});
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>'''
    
    return html_content

def main():
    """Main function to generate all estancia pages."""
    # Create estancias directory if it doesn't exist
    estancias_dir = Path("estancias")
    estancias_dir.mkdir(exist_ok=True)
    
    # Generate pages for all estancias
    for estancia_id, estancia_data in ESTANCIAS.items():
        print(f"Generating page for {estancia_data['name']}...")
        
        html_content = generate_estancia_page(estancia_id, estancia_data)
        
        # Write the HTML file
        output_file = estancias_dir / f"{estancia_id}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Generated {output_file}")
    
    print("\n🎉 All estancia pages have been generated successfully!")
    print("📁 Files created in the 'estancias' directory:")
    for estancia_id in ESTANCIAS.keys():
        print(f"  - {estancia_id}.html")

if __name__ == "__main__":
    main() 