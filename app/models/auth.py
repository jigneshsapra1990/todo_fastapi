from pydantic import BaseModel, Field, EmailStr, ValidationInfo, field_validator

class Login(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=20)




class Register(BaseModel):
     name : str = Field(..., min_length=3, max_length=50)
     email: EmailStr
     password: str = Field(..., min_length=6, max_length=20)   
     confirm_password: str = Field(..., min_length=6, max_length=20)


     @field_validator("confirm_password")
     def confirm_password_match(cls, v, info: ValidationInfo):
         if "password" in info.data and v != info.data["password"]:
             raise ValueError("Passwords do not match")
         return v

