from pydantic import BaseModel


class AutomobiliaiSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    kaina: float

    class Config:
        from_attributes = True
