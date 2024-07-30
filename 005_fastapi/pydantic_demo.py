from pydantic import BaseModel


class Instructor(BaseModel):
    name: str
    age: int
    course: str
    ratings: list[int] = []


data = {
    "name": "Murthy",
    "age": "28",
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "4", "5", 4]
}

user = Instructor(**data)

print(f"Found a Instructor: {user}")