

# valide si el archivo existe aqui
validate_file() {
    if [ -f "$1" ]; then
        return 0
    else
        return 1
    fi
}

# funcion con la que copio el fichero a los directorios
copy_file_to_directories() {
    for directory in "${directories[@]}"; do
        mkdir -p "$directory"
        cp "$filename" "$directory/"
    done
}

# con esta cambio de directorio mientras muestro donde estoy
change_directory_and_show() {
    cd "$1"
    echo "Directorio actual: $(pwd)"
    sleep 2
}

read -p "Ingrese el nombre del archivo a copiar: " filename

if validate_file "$filename"; then
    directories=("directory1" "directory2" "directory3")
    copy_file_to_directories

    for directory in "${directories[@]}"; do
        change_directory_and_show "$directory"
    done

    echo "Archivo '$filename' copie el fichero en:"
    for directory in "${directories[@]}"; do
        echo "- $directory/$filename"
    done
else
    echo "El archivo no existe o no es un archivo válido."
fi
