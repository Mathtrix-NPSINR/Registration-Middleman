import os

import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI
from loguru import logger
from pydantic import BaseModel

load_dotenv()
logger.add("mathtrix.log", enqueue=True)

router = APIRouter()

API_URL = "http://0.0.0.0:8000/api"
API_KEY = os.getenv("API_KEY")


form_ids = {
    "Agon": (1, "1C3nr44s7p3VNF_WHxWkKAaunQ1QvN-WcrwiKEYvUyNY"),
    "Apollo": (2, "10Fy406Lz0h7azBY3BYcKD82R2UnnxWCUjO4CvQwOl1k"),
    "Auctus": (3, "1utGuIQ8pyj9EYRmlNPl4q5xVgccCQEX94c_WJ9Gizzo"),
    "Enigmata": (4, "15qXV8Q-YLzfkWMOxbdKLkkHkEIyRJj0tpZQi8dvU3j8"),
    "Mask A Raid": (5, "1s7om5bwTshQWPsQE3f7OkDvXvAMOuvsM8jF1Xnp50YQ"),
    "Mercatus": (6, "1B5oP2MBaYZEjDPhw_IHroehbS7gV8hZhO79V-GaO0-Y"),
    "Nemesis": (7, "1GxPRC5T2npL-ablix1q8Dhi5Gy-3lXZelcNhsOplmDc"),
    "Saturn": (8, "1-Wo5IzWj26KzyQeZIR5511qELXnVw5ObJMJt8JXC1DU"),
    "Sonneto": (9, "19AiL7fX8DQBR4NaHoHARo0k40xeWSPeRUq1__HIoYM0"),
    "Sum it Up!": (10, "1ym1ce1LbFMHfFTiweFJWHd6dzc4-NMCUj-XNQLxtqOA"),
    "Breaking Barriers": (11, "1F3zPii3cI8_eJYC6-kkXmpQ4UPm2uv6cu9NAx7YbDRQ"),
    "Cognitoria": (12, "1369PReP12e8nXqP-VeOqs6V3BrwUTE1UfDoVU4UdTc0"),
    "Forum Infinitum": (13, "1tdmkxT4eqTqzMX03uvDCzbYP0iWbbN6oH-kn2ZyYQTM"),
    "Hacksquads": (14, "1gZTAg5N7GO1Ia6BAMPkyD9Kuxz59nQWKrF5Jf4WIiTA"),
    "Mathletics": (15, "1nAqaFo23NdtRS_HOWH0PVslkMo74JzU7dR3YkhgdvYg"),
    "Mathopoly": (16, "1mX-crEIcDtGcwnzmq-j1xAUVCysYl5s-nCon8Nuoirg"),
    "Mystifiezzera": (17, "1_0sFSIU1QEjHuKgtPGWBKn0wCS787Qq4IdsuyaHL4DI"),
    "Operation Breakout": (18, "1bQhHMnbJ3OjH2Rv_5GyWwmFYKAhud4Hz73ut0GNdZ5Y"),
    "Picstraction": (19, "1k2BH9lOvJwhFL63M-tLQDxDi--FkDAh898sdjhBKhco"),
    "Rhythmatics": (20, "1NiQ8pAxk-oFEp3otKuTT8oOj3IDrUcWeqTj7RrnL70k"),
}


class EventBase(BaseModel):
    form_id: str
    school: str
    team_name: str

    name_1: str | None = None
    email_1: str | None = None
    phone_number_1: str | None = None

    name_2: str | None = None
    email_2: str | None = None
    phone_number_2: str | None = None

    name_3: str | None = None
    email_3: str | None = None
    phone_number_3: str | None = None

    name_4: str | None = None
    email_4: str | None = None
    phone_number_4: str | None = None

    name_5: str | None = None
    email_5: str | None = None
    phone_number_5: str | None = None

    name_6: str | None = None
    email_6: str | None = None
    phone_number_6: str | None = None


@router.post("/")
async def forward(*, event: EventBase):
    for event_name, details in form_ids.items():
        if event.form_id == details[1]:
            event_id = details[0]
            event_name = event_name
            break

    async with httpx.AsyncClient(timeout=None) as client:
        team = await client.post(
            f"{API_URL}/team/",
            params={"api-key": API_KEY},
            json={
                "team_name": event.team_name,
                "team_school": event.school,
                "team_event": event_name,
                "event_id": event_id,
            },
        )

        team_data = team.json()
        team_id = team_data["id"]

        if (
            event.name_1 is not None
            and event.email_1 is not None
            and event.phone_number_1 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_1,
                    "user_email": event.email_1,
                    "user_phone": event.phone_number_1,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

        if (
            event.name_2 is not None
            and event.email_2 is not None
            and event.phone_number_2 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_2,
                    "user_email": event.email_2,
                    "user_phone": event.phone_number_2,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

        if (
            event.name_3 is not None
            and event.email_3 is not None
            and event.phone_number_3 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_3,
                    "user_email": event.email_3,
                    "user_phone": event.phone_number_3,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

        if (
            event.name_4 is not None
            and event.email_4 is not None
            and event.phone_number_4 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_4,
                    "user_email": event.email_4,
                    "user_phone": event.phone_number_4,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

        if (
            event.name_5 is not None
            and event.email_5 is not None
            and event.phone_number_5 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_5,
                    "user_email": event.email_5,
                    "user_phone": event.phone_number_5,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

        if (
            event.name_6 is not None
            and event.email_6 is not None
            and event.phone_number_6 is not None
        ):
            await client.post(
                f"{API_URL}/user/",
                params={"api-key": API_KEY},
                json={
                    "user_name": event.name_6,
                    "user_email": event.email_6,
                    "user_phone": event.phone_number_6,
                    "user_school": event.school,
                    "team_id": team_id,
                },
            )

    logger.info(
        f"{event.team_name} from {event.school} has successfully registered for the event {event_name}!"
    )


app = FastAPI(title="Registration MiddleMan")
app.include_router(router)
