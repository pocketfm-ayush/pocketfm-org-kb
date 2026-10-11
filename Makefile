.PHONY: validate refresh-evidence help tree

help:
	@echo "Targets:"
	@echo "  make validate           — handbook + org.yaml + packs manifest"
	@echo "  make refresh-evidence   — update evidence SHAs from local clones"
	@echo "  make tree               — show top-level layout"

validate:
	python3 handbook/scripts/validate_org_kb.py
	python3 scripts/validate_org_yaml.py

refresh-evidence:
	python3 scripts/refresh_evidence_from_clones.py --write

tree:
	@find . -maxdepth 2 -type d -not -path './.git*' -not -path './var*' | sort
