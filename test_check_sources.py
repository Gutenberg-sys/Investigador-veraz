"""
Tests para scripts/check_sources.py

Ejecutar con: python3 -m pytest tests/ -v
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from check_sources import validate, domain_of  # noqa: E402


def three_good_sources():
    return [
        {"url": "https://www.reuters.com/noticia-1", "title": "Noticia 1", "date": "2026-10-18"},
        {"url": "https://www.bbc.com/noticia-1", "title": "Noticia 1 BBC", "date": "2026-10-19"},
        {"url": "https://elpais.com/noticia-1", "title": "Noticia 1 El País", "date": "2026-10-19"},
    ]


def test_tres_fuentes_independientes_pasa_sin_errores():
    errors, warnings = validate(three_good_sources())
    assert errors == []


def test_menos_de_tres_dominios_falla():
    sources = [
        {"url": "https://www.reuters.com/a", "title": "A", "date": "2026-10-18"},
        {"url": "https://www.reuters.com/b", "title": "B", "date": "2026-10-18"},
    ]
    errors, warnings = validate(sources)
    assert any("dominio" in e.lower() for e in errors)


def test_url_invalida_genera_error():
    sources = three_good_sources() + [{"url": "no-es-una-url", "title": "mal"}]
    errors, warnings = validate(sources)
    assert any("inválida" in e for e in errors)


def test_lista_vacia_falla():
    errors, warnings = validate([])
    assert len(errors) == 1


def test_falta_fecha_genera_aviso_no_error():
    sources = three_good_sources()
    del sources[0]["date"]
    errors, warnings = validate(sources)
    assert errors == []
    assert any("fecha" in w.lower() for w in warnings)


def test_www_se_normaliza_al_mismo_dominio():
    assert domain_of("https://www.example.com/a") == domain_of("https://example.com/b")


def test_dominio_repetido_con_www_no_cuenta_como_independiente():
    sources = [
        {"url": "https://www.reuters.com/a", "title": "A", "date": "2026-10-18"},
        {"url": "https://reuters.com/b", "title": "B", "date": "2026-10-18"},
        {"url": "https://elpais.com/c", "title": "C", "date": "2026-10-18"},
    ]
    errors, warnings = validate(sources)
    # reuters.com y www.reuters.com cuentan como el mismo dominio -> solo 2 independientes
    assert any("dominio" in e.lower() for e in errors)
