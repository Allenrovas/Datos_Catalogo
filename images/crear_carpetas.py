import os 
 
def create_image_folders(): 
    """ 
    Script para crear carpetas de imágenes a partir del ID 27 
    Ejecutar desde la carpeta 'images' 
    """ 
     
    # Lista de carpetas a crear (solo nombres de carpetas) 
    folders = [ 
        "brabham_bt45_reutemann",
        "mclaren_m23_hunt",
        "vanwall_57_moss",
        "lotus_72d_fittipaldi",
        "brabham_bt44b_pace",
        "march_751_brambilla",
        "mclaren_m23_villeneuve",
        "ferrari_126c3_arnoux",
        "politoys_fx3_pescarolo",
        "williams_fw08_rosberg",
        "brabham_bt26a_ickx",
        "ferrari_312t2_villeneuve",
        "brm_p160b_beltoise"
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
        print("⚠️  ADVERTENCIA: Asegúrate de estar en la carpeta 'images'") 
        response = input("¿Continuar de todos modos? (s/n): ") 
        if response.lower() != 's': 
            print("Operación cancelada.") 
            exit() 
     
    create_image_folders()