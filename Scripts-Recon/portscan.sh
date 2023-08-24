#!/bin/bash

read -p "Passe o domínio: " nomehost
portas=(22 80 443)

declare -A port_names
port_names[22]="ssh"
port_names[80]="http"
port_names[443]="https"

for p in "${portas[@]}"; do
    { echo > /dev/tcp/"$nomehost"/"$p"; } 2>/dev/null &&
    echo "Porta aberta: $p ${port_names[$p]}"
done || echo "Alvo inexistente"
