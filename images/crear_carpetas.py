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
        "bar_002_villeneuve",
        "lotus_72e_peterson",
        "mercedes_w07_rosberg",
        "ferrari_f2001_schumacher_italiangp",
        "ligier_js11_laffite",
        "march_judd_881_capelli",
        "minardi_m191_martini",
        "mercedes_w05_hamilton",
        "benetton_b186_berger",
        "williams_fw23_ralf_schumacher",
        "eifelland_e21_stommelen",
        "renault_rs10_jabouille",
        "lotus_72d_fittipaldi",
        "surtees_ts98_de_adamich",
        "williams_fw15c_prost",
        "mclaren_mp4_23_hamilton",
        "brabham_bt49_piquet",
        "lotus_79_andretti",
        "benetton_b194_schumacher_panini",
        "ferrari_312t2_lauda_braziliangp",
        "bmw_sauber_f1_08_kubica",
        "williams_fw45_albon_singaporegp",
        "ferrari_sf1000_leclerc_tuscangp"
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
