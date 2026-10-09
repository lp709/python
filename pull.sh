#!/bin/bash

printf "\nA iniciar a atualizacao\n"

if git pull; then
    printf "\nFinalizada com sucesso\n"
else
    printf "Erro: falha ao atualizar o repo.\n"
fi