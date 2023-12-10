from enum import Enum


class App(Enum):
    NAME = "Alejoide"
    URL = "https://alejoide.com"

class Links(Enum):
    HOME = "#"
    ABOUT = "#about"
    PROJECTS = "#projects"
    CONTACT = "#contact"

class AboutMe(Enum):
    TITLE = "Sobre mí"
    DESCRIPTION = ["Actualmente me encuentro trabajando de SRE/DevOps, donde trabajo principalmente con tecnologías como Docker, Apache, Jenkins, GitLab, LXC, NGINX, y diferentes pipelines para aplicar prácticas de CI/CD.",
        "Además de eso, apunto actualmente a seguir aprendiendo de otras tecnologías como Kubernetes y plataformas Cloud.",
        "Aunque actualmente uso Python - lenguaje que me apasiona- para scripting, empecé utilizándolo para desarrollo backend, trabajando tanto en proyectos personales como profesionales con frameworks como Flask, FastAPI, PyQT, entre otros.",
        "Me gusta mucho enseñar, por lo que también estoy apuntando a ser profesor de programación en escuelas de nivel superior."
    ]