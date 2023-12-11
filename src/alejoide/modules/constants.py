from enum import Enum


class App(Enum):
    NAME = "Alejoide"
    URL = "https://alejoide.com"

class Links(Enum):
    HOME = "#"
    ABOUT = "#about_me"
    PROJECTS = "#projects"
    CONTACT = "#contact"
    APP_URL = "http://www.alejoide.com"
    EMAIL = "mailto:alejofsarmiento@gmail.com"

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
            "body": [
                "Actualmente me encuentro trabajando de SRE/DevOps, donde trabajo principalmente con tecnologías como Docker, Apache, Jenkins, GitLab, LXC, NGINX, que me permiten crear infraestructura y pipelines para aplicar prácticas de CI/CD.",
                "Además de eso, actualmente estoy aprendiendo otras tecnologías como Kubernetes y plataformas Cloud."
            ]
        },
        {
            "icon": "fa-brands fa-python",
            "title": "Backend",
            "body": [
                "Tengo experiencia trabajando como desarrollador backend, siendo mi fuerte principal el desarrollo en Python, lenguaje que me apasiona y con el que he trabajado tanto en proyectos personales como profesionales con frameworks como Flask, FastAPI, PyQT, Reflex, entre otros."
            ]
        },
        {
            "icon": "fa-brands fa-react",
            "title": "Frontend",
            "body": [
                "Me encuentro incursionando en el mundo del desarrollo de frontend, donde estoy aprendiendo Reflex, React y otras tecnologías con el objetivo de poder crear aplicaciones web y móviles.",
                "De hecho, ¡este sitio web está desarrollado por mí utilizando Reflex!"
            ]
        },
        {
            "icon": "fa-solid fa-user-tie",
            "title": "Profesor",
            "body": [
                "Me gusta mucho enseñar, por lo que también estoy apuntando a ser profesor de programación en escuelas de nivel superior."
            ]
        }
    ]