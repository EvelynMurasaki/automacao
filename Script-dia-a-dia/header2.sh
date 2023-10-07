#!/bin/bash

# Função para verificar a presença de um cabeçalho em uma URL
check_header() {
  url="$1"
  header="$2"
  headers=$(curl -I "$url" 2>/dev/null)
  if echo "$headers" | grep -qi "$header"; then
    echo -e "[$header] \e[32mestá implementado\e[0m em $url."
  else
    echo -e "[$header] \e[31mnão está implementado\e[0m em $url."
  fi
}

# Verifica se foi fornecido um arquivo de texto como argumento
if [ $# -eq 1 ] && [ -f "$1" ]; then
  # Leitura de URLs a partir do arquivo
  while IFS= read -r url; do
    check_header "$url" "Content-Security-Policy"
    check_header "$url" "X-Frame-Options"
    check_header "$url" "Strict-Transport-Security"
    check_header "$url" "Referrer-Policy"
    check_header "$url" "Public-Key-Pins"
    check_header "$url" "X-XSS-Protection"
    check_header "$url" "X-Content-Type-Options"
    echo ""
  done < "$1"
else
  # Se nenhum arquivo for fornecido, assume que o argumento é uma URL
  if [ $# -eq 1 ]; then
    url="$1"
    check_header "$url" "Content-Security-Policy"
    check_header "$url" "X-Frame-Options"
    check_header "$url" "Strict-Transport-Security"
    check_header "$url" "Referrer-Policy"
    check_header "$url" "Public-Key-Pins"
    check_header "$url" "X-XSS-Protection"
    check_header "$url" "X-Content-Type-Options"
  else
    echo "Por favor, forneça um arquivo de texto contendo URLs ou uma única URL como argumento."
    exit 1
  fi
fi
