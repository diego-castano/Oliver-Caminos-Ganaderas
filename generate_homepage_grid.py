#!/usr/bin/env python3
"""
Script to generate the improved homepage grid for Ganadera website.
"""

# Estancia data with technical information
ESTANCIAS_HOMEPAGE = {
    'fortin-yunka': {
        'name': 'Fortín Yunká',
        'folder': 'fortinyunca',
        'surface': '20.600',
        'description': 'Ganadería + agricultura, ciclo completo',
        'access': 'Ruta Nacional 86 pavimentada',
        'emoji': '🌾',
        'tech_info': [
            '🏠 Casa patronal de 700m²',
            '🐂 Capacidad: 21.000 cabezas',
            '🌾 6.200 ha cultivables',
            '💧 30 potreros funcionales'
        ]
    },
    'el-yarara': {
        'name': 'El Yarará',
        'folder': 'elyarara',
        'surface': '1.800',
        'description': 'Ganadería, 30 potreros, agua de calidad',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🐍',
        'tech_info': [
            '💧 Tanque australiano 200.000 lts',
            '🌿 100 ha pasturas implantadas',
            '🐂 30 potreros subdivididos',
            '🏠 Hermosa casa principal'
        ]
    },
    'la-federacion': {
        'name': 'La Federación',
        'folder': 'federacion',
        'surface': '3.100',
        'description': 'Ganadería intensiva + agricultura',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌽',
        'tech_info': [
            '🌾 1.500 ha agrícolas',
            '🌿 2.000 ha pasturas implantadas',
            '🏗️ 2 galpones grandes',
            '💧 Riacho Porteño atraviesa'
        ]
    },
    'agua-dulce': {
        'name': 'Agua Dulce',
        'folder': 'aguadulce',
        'surface': '13.500',
        'description': 'Cría y recría, praderas, ruta atravesada',
        'access': 'Ruta Provincial 23',
        'emoji': '💧',
        'tech_info': [
            '🐂 4.500 cabezas capacidad',
            '🌿 9.000 ha pasturas naturales',
            '🛣️ 60 km caminos internos',
            '🏠 2 puestos estratégicos'
        ]
    },
    'campo-lindo': {
        'name': 'Campo Lindo',
        'folder': 'campolindo',
        'surface': '1.300',
        'description': 'Ganadero con potencial forestal',
        'access': 'Ruta Provincial 23',
        'emoji': '🌿',
        'tech_info': [
            '🐂 1.000 cabezas capacidad',
            '🌳 90-95% campo limpio',
            '🏠 Casa recientemente renovada',
            '🛣️ Sobre Ruta 23'
        ]
    },
    'el-cacuy': {
        'name': 'El Cacuy',
        'folder': 'cucuy',
        'surface': '500',
        'description': '220 ha agrícolas (maíz, soja, algodón)',
        'access': 'Acceso vecinal desde Ruta 86',
        'emoji': '🌾',
        'tech_info': [
            '🌾 220 ha actualmente sembradas',
            '🌽 Maíz, soja, algodón, trigo',
            '🏠 Galpón amplio operativo',
            '💧 Represa y molino'
        ]
    },
    'campo-alegre': {
        'name': 'Campo Alegre',
        'folder': 'campoalegre',
        'surface': '1.050',
        'description': 'Ganadero con 450 ha de Gatton Panic',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌳',
        'tech_info': [
            '🌿 450 ha Gatton Panic',
            '🐂 Campo limpio 90-95%',
            '🏠 Casa de empleado funcional',
            '🛣️ 2.000m frente ruta'
        ]
    },
    'la-loli': {
        'name': 'La Loli',
        'folder': 'laloli',
        'surface': '1.050',
        'description': 'Ganadero + agrícola (maíz implantado)',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🐮',
        'tech_info': [
            '🌿 450 ha Gatton Panic',
            '🌽 150 ha maíz implantado',
            '🏠 Galpón amplio cubierto',
            '🛣️ 2.000m frente ruta'
        ]
    },
    'las-lantanas': {
        'name': 'Las Lantanas',
        'folder': 'laslantana',
        'surface': '1.050',
        'description': 'Ganadero intensivo, campo limpio',
        'access': 'Ruta 86 pavimentada',
        'emoji': '🌼',
        'tech_info': [
            '🌿 450 ha Gatton Panic',
            '🐂 Campo limpio 90-95%',
            '🏠 Casa de empleado funcional',
            '🛣️ 2.000m frente ruta'
        ]
    }
}

def generate_estancia_card(estancia_id, estancia_data):
    """Generate HTML card for an estancia in the homepage grid."""
    
    # Determine image source
    image_src = f"media/{estancia_data['folder']}/hero.jpg"
    
    # Generate technical info HTML
    tech_info_html = ""
    for info in estancia_data['tech_info']:
        tech_info_html += f'<p class="text-gray-600">{info}</p>\n                                '
    
    return f'''                <!-- {estancia_data["name"]} -->
                <a href="estancias/{estancia_id}.html" class="group">
                    <div class="bg-white rounded-lg shadow-lg overflow-hidden card-hover border border-gray-200">
                        <div class="relative h-64 overflow-hidden">
                            <img src="{image_src}" alt="{estancia_data["name"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy">
                            <div class="absolute inset-0 bg-black bg-opacity-30"></div>
                        </div>
                        <div class="p-6 bg-gradient-to-b from-white to-gray-50">
                            <h3 class="text-xl font-bold text-gray-900 mb-3">{estancia_data["emoji"]} {estancia_data["name"]}</h3>
                            <p class="text-gray-700 mb-3 font-medium">{estancia_data["surface"]} ha - {estancia_data["description"]}</p>
                            <div class="space-y-2 text-sm">
                                <p class="text-green-700 font-semibold">📍 {estancia_data["access"]}</p>
                                {tech_info_html}
                            </div>
                        </div>
                    </div>
                </a>'''

def main():
    """Generate the improved homepage grid HTML."""
    
    print("Generating improved homepage grid...")
    
    # Generate all estancia cards
    cards_html = ""
    for estancia_id, estancia_data in ESTANCIAS_HOMEPAGE.items():
        cards_html += generate_estancia_card(estancia_id, estancia_data) + "\n"
    
    print("✓ Generated improved homepage grid HTML")
    print("\nCopy this HTML to replace the grid section in index.html:")
    print("=" * 80)
    print(cards_html)
    print("=" * 80)

if __name__ == "__main__":
    main() 