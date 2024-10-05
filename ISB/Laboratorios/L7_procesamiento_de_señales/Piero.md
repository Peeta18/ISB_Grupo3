def generate_markdown_report(file_name, img_files):
    with open(file_name, 'w') as md_file:
        md_file.write(f"# Análisis de Señales Filtradas\n\n")
        md_file.write(f"## Filtros Aplicados\n")
        md_file.write(f"Se aplicaron tres tipos de filtros (Butterworth, Notch, y FIR) para mejorar la señal eliminando componentes no deseadas.\n\n")
        md_file.write(f"### Justificación de los Filtros\n")
        md_file.write(f"- **Butterworth IIR Pasa-Bajo**: Respuesta suave y control de fase.\n")
        md_file.write(f"- **Filtro Notch**: Eliminación selectiva de ruido en frecuencias específicas.\n")
        md_file.write(f"- **Filtro FIR Pasa-Alto**: Precisión en la eliminación de componentes de baja frecuencia y DC.\n\n")
        
        # Insertar imágenes de resultados en el archivo Markdown
        for img in img_files:
            md_file.write(f"![{img}]({img})\n\n")

# Llamar a la función para crear el reporte Markdown
generate_markdown_report('/content/drive/MyDrive/isb/analisis_senal.md', [
    'stft_plot.png',
    'poles_zeros.png',
    'bode_fir.png'
])
print("Reporte generado y guardado como 'analisis_senal.md' en Google Drive.")
