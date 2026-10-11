.PHONY: validate help tree

help:
	@echo "Targets:"
	@echo "  make validate  — validate org.yaml + handbook catalog/entities"
	@echo "  make tree      — show layout"

validate:
	python3 scripts/validate_handbook.py
	python3 scripts/validate_org_yaml.py

tree:
	@find . -type f -not -path './.git/*' -not -path './var/*' | sort
