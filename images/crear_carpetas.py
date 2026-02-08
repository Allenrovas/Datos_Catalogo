import os

def rename_jpgs_in_folder(folder_path):
    """
    Renombra todas las imágenes JPG dentro de una carpeta a:
    1.jpg, 2.jpg, 3.jpg, ...
    """

    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg"))
    ]

    if not images:
        print(f"   ⚠️  No hay imágenes JPG en {folder_path}")
        return

    images.sort()

    # Paso 1: renombrar a nombres temporales
    temp_names = []
    for i, img in enumerate(images, start=1):
        temp_name = f"__temp_{i}.jpg"
        os.rename(
            os.path.join(folder_path, img),
            os.path.join(folder_path, temp_name)
        )
        temp_names.append(temp_name)

    # Paso 2: renombrar al formato final
    for i, temp in enumerate(temp_names, start=1):
        final_name = f"{i}.jpg"
        os.rename(
            os.path.join(folder_path, temp),
            os.path.join(folder_path, final_name)
        )

    print(f"   🔁 {len(images)} imágenes renombradas en {folder_path}")


def create_image_folders_and_rename():
    """
    Crea carpetas y enumera las imágenes JPG dentro de cada una
    Ejecutar desde la carpeta 'images'
    """

    folders = [
        "ferrari_sf25_leclerc_miami",
        "ferrari_sf24_leclerc_monaco",
        "ferrari_sf24_leclerc_italy"
    ]

    print("Procesando carpetas de imágenes...")
    print("-" * 50)

    for folder in folders:
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"✅ Creada: {folder}")
            else:
                print(f"📁 Existe: {folder}")

            rename_jpgs_in_folder(folder)

        except Exception as e:
            print(f"❌ Error en {folder}: {str(e)}")

    print("-" * 50)
    print("¡Proceso completado!")


if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Directorio actual: {current_dir}")

    if not current_dir.endswith("images"):
        print("⚠️  ADVERTENCIA: Asegúrate de estar en la carpeta 'images'")
        response = input("¿Continuar de todos modos? (s/n): ")
        if response.lower() != 's':
            print("Operación cancelada.")
            exit()

    create_image_folders_and_rename()
