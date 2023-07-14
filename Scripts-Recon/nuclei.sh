#!/bin/bash

output_file="results.txt"
echo "Informe URL, IP ou o caminho para um arquivo TXT:"
read -r target

# Verifica se o argumento é uma URL ou IP
if [[ "$target" =~ ^http:// || "$target" =~ ^https:// ]]; then
  # É uma URL, então executa o comando Nuclei com -u
  nuclei -u "$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
elif [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  # É um IP, então executa o comando Nuclei com -u e transforma em URL
  nuclei -u "http://$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
elif [[ -f "$target" ]]; then
  # É um arquivo de texto, então executa o comando Nuclei com -l
  nuclei -l "$target" -t ./nuclei-templates/ -severity low,medium,high,critical -o "$output_file"
else
  echo "Formato inválido. Informe uma URL, um IP ou o caminho para um arquivo de texto válido."
  exit 1
fi
