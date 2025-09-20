import os

def create_image_folders():
    """
    Script para crear carpetas de imágenes a partir del ID 7
    Ejecutar desde la carpeta 'images8'
    """
    
    # Lista de carpetas a crear (solo nombres de carpetas)
    folders = [
        "ferrari_sf24_sainz_miami",
        "rb19_verstappen_las_vegas", 
        "rb19_verstappen_austin",
        "ferrari_499p_lemans",
        "mclaren_mcl38_norris_monaco",
        "mclaren_mcl38_piastri_monaco",
        "renault_r25_alonso",
        "lotus_25_clark",
        "matra_ms10_stewart",
        "williams_fw14b_mansell",
        "brawn_gp01_button",
        "tyrrell_006_stewart",
        "williams_fw19_villeneuve",
        "brabham_bt24_hulme",
        "ferrari_312t3_scheckter",
        "brabham_bt52b_piquet",
        "williams_fw07_jones",
        "rb18_verstappen_japan",
        "alpine_a522_ocon",
        "mercedes_w11_hamilton"
    ]
    
    print("Creando carpetas de imágenes...")
    print("-" * 50)
    
    created_count = 0
    already_exists_count = 0
    
    for folder in folders:
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"✅ Creada: {folder}")
                created_count += 1
            else:
                print(f"📁 Ya existe: {folder}")
                already_exists_count += 1
                
        except Exception as e:
            print(f"❌ Error creando {folder}: {str(e)}")
    
    print("-" * 50)
    print(f"Resumen:")
    print(f"Carpetas creadas: {created_count}")
    print(f"Carpetas existentes: {already_exists_count}")
    print(f"Total procesadas: {len(folders)}")
    print("\n¡Proceso completado!")

if __name__ == "__main__":
    # Verificar que estamos en el directorio correcto
    current_dir = os.getcwd()
    print(f"Directorio actual: {current_dir}")
    
    if not current_dir.endswith("images"):
        print("⚠️  ADVERTENCIA: Asegúrate de estar en la carpeta 'images8'")
        response = input("¿Continuar de todos modos? (s/n): ")
        if response.lower() != 's':
            print("Operación cancelada.")
            exit()
    
    create_image_folders()