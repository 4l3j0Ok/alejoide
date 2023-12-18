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
    DESCRIPTION = [
        "Estos son algunos de los proyectos personales en los que he trabajado, tanto en mi tiempo libre.",
        "Tengo muchos más proyectos además de estos, pero los que se muestran aquí son los que considero más importantes.",
        "¡También podés ver todos mis proyectos en mi GitHub!"
    ]
    CARDS = [
        {
            "icon": "fa-brands fa-python | fa-brands fa-react",
            "title": "Alejoide",
            "description": [
                "Este sitio web. Desarrollado con Reflex.",
                "¡También es un proyecto de código abierto! Podés ver el código en mi GitHub."
            ],
            "image": "projects/alejoide.png",
            "repo_url": Links.APP_REPO_URL.value,
            "app_url": Links.APP_URL.value,
            "is_disabled": True
        },
        {
            "icon": "fa-brands fa-python | fa-solid fa-globe",
            "title": "BCRA Scraper API",
            "description": [
                "Una API de código abierto que permite obtener los bancos registrados en el BCRA.",
            ],
            "image": "projects/bcra_scraper_api.png",
            "repo_url": "https://github.com/4l3j0Ok/bcra-scraper-api",
            "app_url": "https://bcra-scraper-api.alejoide.com",
            "is_disabled": False
        },
        {
            "icon": "fa-brands fa-python | fa-brands fa-windows",
            "title": "Fall Guys Anti Sniper",
            "description": [
                "Este sitio web. Desarrollado con Reflex.",
                "¡También es un proyecto de código abierto! Podés ver el código en mi GitHub."
            ],
            "image": "projects/fg_anti_sniper.png",
            "repo_url": "https://github.com/4l3j0Ok/fall-guys-anti-sniper",
            "is_disabled": False
        },
        {
            "icon": "fa-brands fa-python | fa-brands fa-docker",
            "title": "Prodesk Stacks",
            "description": [
                "Echale un vistazo a los stacks que tengo levantados en mi propio servidor de casa.",
            ],
            "image": "projects/prodesk_stacks.png",
            "repo_url": "https://github.com/4l3j0Ok/prodesk-stacks",
            "is_disabled": False
        }
    ]

    GITHUB_BUTTON = {
        "icon": "fa-brands fa-github",
        "text": "Ver en GitHub"
        }

    APP_BUTTON = {
        "icon": "fa-solid fa-link",
        "text": "Ver app"
    }

class Scripts(Enum):
    FONT_AWESOME = "https://kit.fontawesome.com/ed6fce8479.js"