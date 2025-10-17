# Nom du projet
NAME = Spider

# Répertoire de l'environnement virtuel
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Bash et prompt definition
SHELL := /bin/bash
PROMPT := \[\e[1;36m\](venv)\[\e[0m\] \W \$$

# Répertoire du code source
SRC_DIR = srcs

# Fichier principal à exécuter
MAIN = $(SRC_DIR)/main.py

# Couleur
COLOR = \e[1;31m
RESET = \e[0m

# ===========================================================
# Commandes principales
# ===========================================================

# Par défaut : créer l'environnement et lancer le projet
all: $(NAME)

# Créer l'exécutable wrapper
$(NAME): $(VENV) install $(MAIN)
	@printf "🔨 Creating executable wrapper...\n"
	@echo '#!/bin/bash' > $(NAME)
	@echo 'DIR="$$(cd "$$(dirname "$${BASH_SOURCE[0]}")" && pwd)"' >> $(NAME)
	@echo 'source "$$DIR/$(VENV)/bin/activate"' >> $(NAME)
	@echo 'python "$$DIR/$(MAIN)" "$$@"' >> $(NAME)
	@chmod +x $(NAME)
	@printf "$(COLOR)"
	@printf "  _____ .___  _ .___   .____  .___\n"
	@printf " (      /   \\ | /   \`  /      /   \\ \n"
	@printf "  \`--.  |,_-' | |    | |__.   |__-'\n"
	@printf "     |  |     | |    | |      |  \\\\ \n"
	@printf "\\\___.'  /     / /---/  /----/ /   \\ \n"
	@printf "$(RESET)"

# pour lancer le shell de l'environnement
activate: $(VENV)
	@printf "💻 Activating virtual environment ...\n"
	@source $(VENV)/bin/activate && PS1='$(PROMPT)  ' bash --norc

# 1️⃣ Créer et activer l'environnement virtuel
$(VENV):
	@printf "🛠️  Activation de l'environnement virtuel ... \n"
	@test -d $(VENV) || python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip

# Installe les dépendances (utile si on modifie requirements.txt)
install: $(VENV)
	@printf "📦 Installing dependencies ... \n"
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@printf "✅\n"

# Supprime les fichiers temporaires et l'environnement virtuel
clean: 
	@printf "🧹 Cleaning ..."
	@rm -rf $(VENV) $(NAME)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@printf "✅\n"

# Relance tout depuis zéro
re: clean all

.PHONY: activate install run clean re

test: $(NAME)
	./$(NAME) https://fr.wikihow.com/Accueil

