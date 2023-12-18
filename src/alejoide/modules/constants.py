from enum import Enum
import os


class App(Enum):
    NAME = "Alejoide"
    DESCRIPTION = "Alejoide, mi sitio web personal."


class Email(Enum):
    ADDRESS = os.getenv("EMAIL_ADDRESS", "alejofsarmiento@gmail.com")
    TOKEN = os.getenv("EMAIL_TOKEN", "token")
    SUBJECT = f"{App.NAME.value.upper()} | Contacto"
    MESSAGE_HEADER = "<h1>NUEVO CONTACTO</h1>"


class Links(Enum):
    HOME = "#"
    ABOUT = "#about_me"
    PROJECTS = "#projects"
    CONTACT = "#contact"
    APP_URL = os.getenv("APP_URL", "https://alejoide.com")
    APP_REPO_URL = os.getenv("APP_REPO_URL", "https://github.com/4l3j0Ok/alejoide-web")
    EMAIL = f"mailto:{Email.ADDRESS.value}"

class AboutMe(Enum):
    DESCRIPTION = [
        "Mi nombre es Alejo. Tengo 22 años y vivo en Argentina.",
        "En 2013 decidí orientar mis conocimientos hacia el mundo de la programación y la informática, estudiando informática en mi escuela secundaria técnica.",
        "En 2020, al finalizar mis estudios secundarios, comencé a trabajar como desarrollador backend en una empresa de desarrollo de software, donde aprendí a trabajar con Python, Flask, FastAPI, entre otras tecnologías.",
        "A comienzos de 2022, se me ofreció la oportunidad de trabajar como SRE/DevOps, un mundo nuevo con nuevos desafíos que me tocó enfrentar.",
        "A día de hoy me encuentro enamorado de esta nueva área, y apunto a seguir aprendiendo y creciendo profesionalmente en ella.",
    ]
    CARDS = [
        {
            "icon": "fa-solid fa-infinity",
            "title": "SRE / DevOps",
            "description": [
                "Actualmente me encuentro trabajando de SRE/DevOps, donde trabajo principalmente con tecnologías como Docker, Apache, Jenkins, GitLab, LXC, NGINX, que me permiten crear infraestructura y pipelines para aplicar prácticas de CI/CD.",
                "Además de eso, actualmente estoy aprendiendo otras tecnologías como Kubernetes y plataformas Cloud."
            ]
        },
        {
            "icon": "fa-brands fa-python",
            "title": "Backend",
            "description": [
                "Tengo experiencia trabajando como desarrollador backend, siendo mi fuerte principal el desarrollo en Python, lenguaje que me apasiona y con el que he trabajado tanto en proyectos personales como profesionales con frameworks como Flask, FastAPI, PyQT, Reflex, entre otros."
            ]
        },
        {
            "icon": "fa-brands fa-react",
            "title": "Frontend",
            "description": [
                "Me encuentro incursionando en el mundo del desarrollo de frontend, donde estoy aprendiendo Reflex, React y otras tecnologías con el objetivo de poder crear aplicaciones web y móviles.",
                "De hecho, ¡este sitio web está desarrollado por mí utilizando Reflex!"
            ]
        },
        {
            "icon": "fa-solid fa-user-tie",
            "title": "Profesor",
            "description": [
                "Me gusta mucho enseñar, por lo que también estoy apuntando a ser profesor de programación en escuelas de nivel superior."
            ]
        }
    ]


class Projects(Enum):
    CARDS = [
        {
            "icon": "fa-brands fa-python | fa-brands fa-react",
            "title": "Alejoide",
            "description": [
                "Este sitio web. Desarrollado con Reflex.",
                "¡También es un proyecto de código abierto! Podés ver el código en mi GitHub."
            ],
            "image": "projects/alejoide.png",
            "repo_url": "https://github.com/4l3j0Ok/alejoide-web",
            "app_url": Links.APP_URL.value,
            "is_here": True
        }
    ]

    GITHUB_BUTTON = {
        "icon": "fa-brands fa-github",
        "text": "Ver en GitHub"
        }

    APP_BUTTON = {
        "icon": "fa-solid fs-external-link",
        "text": "Ir a la aplicación"
    }

class Scripts(Enum):
    FONT_AWESOME = "https://kit.fontawesome.com/ed6fce8479.js"