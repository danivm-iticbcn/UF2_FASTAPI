def theme_schema(theme) -> dict:
    return {"tema":theme}

def themes_schema(themes) -> dict:
    return [theme_schema(thema) for thema in themes]