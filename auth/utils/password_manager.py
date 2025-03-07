from .hash_password import hash_password

from dataclasses import dataclass, field
from string import digits, punctuation

from fastapi import HTTPException


@dataclass
class PasswordManager:
    password: str = field(default=None)
    length_req: bool = field(default=False)
    numbers_req: bool = field(default=False)
    special_chars_req: bool = field(default=False)
    min_length: int = field(default=4)
    max_length: int = field(default=50)

    def __post_init__(self):
        if self.min_length >= self.max_length:
            raise Exception('Minimum length must be less than maximum length')

        if self.min_length <= 0:
            raise Exception('Minimum length must be greater than 0')

    async def validate_password(self) -> None:
        if self.length_req:
            await self.validate_length()
        if self.numbers_req:
            await self.validate_numbers()
        if self.special_chars_req:
            await self.validate_special_chars()

    async def validate_length(self) -> None:
        if len(self.password) <= self.min_length or len(self.password) > self.max_length:
            raise HTTPException(status_code=400, detail=f"Password must be between {self.min_length} "
                                                        f"and {self.max_length} characters")

    async def validate_numbers(self) -> None:
        numbers = set(list(digits))
        if not any(char in numbers for char in self.password):
            raise HTTPException(status_code=400, detail="Password must contain at least one number")

    async def validate_special_chars(self) -> None:
        special_chars = set(list(punctuation))
        if not any(char in special_chars for char in self.password):
            raise HTTPException(status_code=400, detail="Password must contain at least one special character")

    def hash_password(self) -> str:
        return hash_password(self.password)
