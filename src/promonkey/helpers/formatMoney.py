import decimal

class Money:
    """Classe para representar valores monetários em BRL."""

    
    def parse_brl(text: str) -> decimal.Decimal:
        """'R$ 1.299,90' -> Decimal('1299.90')"""
        cleaned = text.replace("R$", "").replace(".", "").replace(",", ".").strip()
        try:
            return decimal.Decimal(cleaned)
        except decimal.InvalidOperation:
            raise ValueError(f"valor inválido: {text!r}") from None

        
    def format_brl(value: decimal.Decimal) -> str:
        """Decimal('1299.9') -> 'R$ 1.299,90'"""
        inteiro, centavos = f"{value:,.2f}".split(".")
        return f"R$ {inteiro.replace(',', '.')},{centavos}"


    def discount_pct(old: decimal.Decimal, new: decimal.Decimal) -> decimal.Decimal:
        """Desconto em %, com uma casa decimal. (100, 80) -> Decimal('20.0')"""
        if old <= 0:
            raise ValueError("preço anterior deve ser maior que zero")
        return ((old - new) / old * 100).quantize(decimal.Decimal("0.1"))