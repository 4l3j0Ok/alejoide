import os
from enum import Enum


class App(Enum):
    NAME = "Alejoide"
    VERSION = "v1"
    AUTHOR = "Alejo Sarmiento"
    DESCRIPTION = "Alejoide, mi sitio web personal."


class Email(Enum):
    ADDRESS = os.getenv("EMAIL_ADDRESS", "alejofsarmiento@gmail.com")
    PUBLIC_ADDRESS = os.getenv("EMAIL_PUBLIC_ADDRESS", "contacto@alejoide.com")
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
    EMAIL = f"mailto:{Email.PUBLIC_ADDRESS.value}"


class GoogleAnalytics(Enum):
    TAG = os.getenv("GOOGLE_ANALYTICS_TAG", "G-XXXXXXX")
    INIT_SCRIPT_URL = f"https://www.googletagmanager.com/gtag/js?id={TAG}"
    SEND_DATA_SCRIPT = f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{window.dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{TAG}');
"""


class AboutMe(Enum):
    DESCRIPTION = [
        "Mi nombre es Alejo. Tengo 23 años y vivo en Argentina.",
        "En 2013 decidí orientar mis conocimientos hacia el mundo de la programación y la informática, estudiando informática en mi escuela secundaria técnica.",
        "En 2020, al finalizar mis estudios secundarios, comencé a trabajar como desarrollador backend en una empresa de desarrollo de software, donde aprendí a trabajar con Python, Flask, FastAPI, entre otras tecnologías.",
        "A comienzos de 2022, se me ofreció la oportunidad de trabajar como SRE/DevOps, un mundo nuevo con nuevos desafíos que me tocó enfrentar.",
        "A día de hoy me encuentro enamorado de esta nueva área, y apunto a seguir aprendiendo y creciendo profesionalmente en ella.",
    ]
    CARDS = [
        {
            "icons": "fa6-solid:infinity",
            "title": "SRE / DevOps",
            "description": [
                "Actualmente me encuentro trabajando de SRE/DevOps, donde trabajo principalmente con tecnologías como Docker, Apache, Jenkins, GitLab, LXC, NGINX, que me permiten crear infraestructura y pipelines para aplicar prácticas de CI/CD.",
                "Además de eso, actualmente estoy aprendiendo otras tecnologías como Kubernetes y plataformas Cloud.",
            ],
        },
        {
            "icons": "fa-brands:python",
            "title": "Backend",
            "description": [
                "Tengo experiencia trabajando como desarrollador backend, siendo mi fuerte principal el desarrollo en Python, lenguaje que me apasiona y con el que he trabajado tanto en proyectos personales como profesionales con frameworks como Flask, FastAPI, PyQT, Reflex, entre otros."
            ],
        },
        {
            "icons": "nonicons:react-16",
            "title": "Frontend",
            "description": [
                "Me encuentro incursionando en el mundo del desarrollo de frontend, donde estoy aprendiendo Reflex, React y otras tecnologías con el objetivo de poder crear aplicaciones web y móviles.",
                "De hecho, ¡este sitio web está desarrollado por mí utilizando Reflex!",
            ],
        },
        {
            "icons": "ic:baseline-school",
            "title": "Profesor",
            "description": [
                "Me gusta mucho enseñar, por lo que también estoy apuntando a ser profesor de programación en escuelas de nivel superior."
            ],
        },
    ]


class Projects(Enum):
    DESCRIPTION = [
        "Estos son algunos de los proyectos personales en los que he trabajado, tanto en mi tiempo libre.",
        "Tengo muchos más proyectos además de estos, pero los que se muestran aquí son los que considero más importantes.",
        "¡También podés ver todos mis proyectos en mi GitHub!",
    ]
    CARDS = [
        {
            "icons": "fa-brands:python|nonicons:react-16",
            "title": "My Links",
            "description": [
                "Mi web de links profesionales y personales.",
            ],
            "image": "projects/my-links.jpg",
            "repo_url": "https://github.com/4l3j0Ok/my-links-web",
            "app_url": "https://links.alejoide.com",
        },
        {
            "icons": "fa-brands:python|eos-icons:api",
            "title": "BCRA Scraper API",
            "description": [
                "Una API de código abierto que permite obtener los bancos registrados en el BCRA.",
            ],
            "image": "projects/bcra_scraper_api.png",
            "repo_url": "https://github.com/4l3j0Ok/bcra-scraper-api",
            "app_url": "https://bcra-scraper-api.alejoide.com",
            "is_disabled": False,
        },
        {
            "icons": "fa-brands:python|heroicons:window-20-solid",
            "title": "Fall Guys Anti Sniper",
            "description": [
                "Aplicación para streamers de Fall Guys que permite evitar el stream-sniping."
            ],
            "image": "projects/fg_anti_sniper.png",
            "repo_url": "https://github.com/4l3j0Ok/fall-guys-anti-sniper",
            "is_disabled": False,
        },
        {
            "icons": "fa-brands:docker",
            "title": "Prodesk Stacks",
            "description": [
                "Echale un vistazo a los stacks que tengo levantados en mi propio servidor de casa.",
            ],
            "image": "projects/prodesk_stacks.png",
            "repo_url": "https://github.com/4l3j0Ok/prodesk-stacks",
            "is_disabled": False,
        },
    ]

    GITHUB_BUTTON = {"icon": "fa-brands:github", "text": "Ver en GitHub"}

    APP_BUTTON = {"icon": "fa-solid:link", "text": "Ver app"}


class Footer(Enum):
    ICONS = [
        # {"icon": "fa-brands:instagram", "link": "https://instagram.com/4l3j0"},
        # {"icon": "fa-brands:twitter", "link": "https://twitter.com/alejoide_"},
        {"icon": "fa-brands:github", "link": "https://github.com/4l3j0Ok"},
        {"icon": "fa-brands:linkedin", "link": "https://www.linkedin.com/in/alejoide"},
        {"icon": "tabler:mail-filled", "link": Links.EMAIL.value, "new_tab": False},
        # {
        #     "icon": "fa-solid:ellipsis-h",
        #     "link": "https://links.alejoide.com"
        # }
    ]
