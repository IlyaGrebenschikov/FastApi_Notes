from pydantic import BaseModel


class Note(BaseModel):
    title: str
    subtitle: str
    introduction: str
    main_text: str
