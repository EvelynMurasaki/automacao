#!/bin/bash

output_file="results.txt"
echo "Informe URL, IP ou o caminho para um arquivo TXT:"
read -r target

# Verifica se o argumento é uma URL ou IP
if [[ "$target" =~ ^http:// || "$target" =~ ^https:// ]]; then
  nuclei -u "$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
elif [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  nuclei -u "http://$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
elif [[ -f "$target" ]]; then
  nuclei -l "$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
else
  echo "Formato inválido. Informe uma URL, um IP ou o caminho para um arquivo de texto válido."
  exit 1
fi
