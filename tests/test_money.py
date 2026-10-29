from decimal import Decimal

import pytest

from promonkey.helpers.formatMoney import discount_pct, format_brl, parse_brl


@pytest.mark.parametrize(
    ("texto", "esperado"),
    [
        ("R$ 1.299,90", Decimal("1299.90")),
        ("299,90", Decimal("299.90")),
        ("R$ 50", Decimal("50")),
        ("  R$ 0,99 ", Decimal("0.99")),
    ],
)
def test_parse_brl(texto, esperado):
    assert parse_brl(texto) == esperado


def test_parse_brl_invalido():
    with pytest.raises(ValueError):
        parse_brl("abc")


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        (Decimal("1299.9"), "R$ 1.299,90"),
        (Decimal("50"), "R$ 50,00"),
        (Decimal("0.99"), "R$ 0,99"),
        (Decimal("1234567.5"), "R$ 1.234.567,50"),
    ],
)
def test_format_brl(valor, esperado):
    assert format_brl(valor) == esperado


def test_discount_pct():
    assert discount_pct(Decimal("100"), Decimal("80")) == Decimal("20.0")
    assert discount_pct(Decimal("299.90"), Decimal("199.90")) == Decimal("33.3")


def test_discount_pct_preco_zero():
    with pytest.raises(ValueError):
        discount_pct(Decimal("0"), Decimal("10"))
