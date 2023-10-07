#!/bin/bash

# Função para verificar o cabeçalho "Server"
check_server() {
  local url="$1"
  local response=$(curl -sI "$url")
  local server_header=$(echo "$response" | grep -i "^Server:")
  echo "Servidor: $server_header"
}

# Função para verificar se a página contém informações sobre a tecnologia usada
check_technology() {
  local url="$1"
  local page_content=$(curl -s "$url")
  if [[ $page_content =~ "Tecnologia Usada:" ]]; then
    echo "Tecnologia Usada: Encontrada na página"
  else
    echo "Tecnologia Usada: Não encontrada na página"
  fi
}

# Função principal
main() {
  echo "Digite o domínio, URL ou o caminho para um arquivo TXT contendo a aplicação:"
  read input

  # Verifica se o input é um arquivo TXT
  if [[ -f "$input" ]]; then
    # Lê a URL do arquivo TXT
    URL=$(cat "$input")
  else
    URL="$input"
  fi

  # Chama as funções para verificar o servidor e a tecnologia
  check_server "$URL"
  check_technology "$URL"
}

# Chama a função principal
main
