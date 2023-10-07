#!/bin/bash

read -p "Digite a URL, domínio ou caminho do arquivo TXT: " input

# Função para verificar uma URL
check_url() {
  local url="$1"
  local http_response=$(curl -s -o /dev/null -w "%{http_code}" "http://$url")
  local https_response=$(curl -s -o /dev/null -w "%{http_code}" "https://$url")

  echo "URL: $url"

  if [ "$http_response" == "200" ]; then
    echo "Disponível em HTTP."
  else
    echo "Não disponível em HTTP."
  fi

  if [ "$https_response" == "200" ]; then
    echo "Disponível em HTTPS."
  else
    echo "Não disponível em HTTPS."
  fi

  echo "-------------------------"
}

# Verifica se o input é um arquivo TXT
if [ -f "$input" ]; then
  while IFS= read -r line; do
    check_url "$line"
  done < "$input"
else
  check_url "$input"
fi
