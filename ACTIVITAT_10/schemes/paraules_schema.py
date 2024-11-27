def paraula_schema(paraula) -> dict:
    return {"paraula":paraula}

def paraules_schema(paraules) -> dict:
    return [paraula_schema(paraula) for paraula in paraules]