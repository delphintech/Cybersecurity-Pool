# Nom du projet
NAME = inquisitor

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
COLOR = \e[1;41m
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
	@printf "$(COLOR) ▄▄ ▄▄  ▄▄  ▄▄▄  ▄▄ ▄▄ ▄▄  ▄▄▄▄ ▄▄ ▄▄▄▄▄▄ ▄▄▄  ▄▄▄▄  $(RESET)\n"
	@printf "$(COLOR) ██ ███▄██ ██▀██ ██ ██ ██ ███▄▄ ██   ██  ██▀██ ██▄█▄ $(RESET)\n"
	@printf "$(COLOR) ██ ██ ▀██ ▀███▀ ▀███▀ ██ ▄▄██▀ ██   ██  ▀███▀ ██ ██ $(RESET)\n"
	@printf "$(COLOR)              ▀▀                                     $(RESET)\n"

# pour lancer le shell de l'environnement
activate: $(VENV)
	@printf "💻 Activating virtual environment ...\n"
	@source $(VENV)/bin/activate && PS1='$(PROMPT)  ' bash --norc

# 1️⃣ Créer et activer l'environnement virtuel
$(VENV):
	@printf "🛠️ Creating virtual environment ... \n"
	@test -d $(VENV) || python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip

# Installe les dépendances (utile si on modifie requirements.txt)
install: $(VENV)
	@printf "📦 Installing dependencies ... \n"
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi

# Supprime les fichiers temporaires et l'environnement virtuel
clean: 
	@printf "🧹 Cleaning ...\n"
	@rm -rf $(VENV) $(NAME)
	@find . -type d -name "__pycache__" -exec rm -rf {} +

# Relance tout depuis zéro
re: clean all

# Lance la norme
norm: $(VENV)
	@$(VENV)/bin/flake8 $(SRC_DIR) --exclude=$(VENV),__pycache__

.PHONY: activate install run clean re

