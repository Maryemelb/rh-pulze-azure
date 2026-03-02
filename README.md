# HR-Pulse – Data Engineering & AI Recruitment Platform

HR-Pulse est une solution de Data Engineering et d'Intelligence Artificielle conçue pour moderniser le processus de recrutement.

L'objectif est de transformer un ensemble d'offres d'emploi textuelles brutes en une base de connaissances structurée, exploitable et prédictive, déployée dans un environnement Cloud Azure industrialisé.

---

## Référentiel

Projet réalisé dans le cadre de la certification :

[2023] Certification RNCP Développeur.se en Intelligence Artificielle

---

## Objectifs du Projet

- Automatiser l'analyse des offres d'emploi
- Structurer et stocker les données dans Azure SQL
- Extraire les compétences via Azure AI (NER)
- Prédire le salaire moyen via un modèle de régression
- Exposer les fonctionnalités via une API REST
- Développer une interface utilisateur moderne
- Industrialiser la solution avec Docker et CI/CD
- Garantir qualité et conformité (Linting + Tests)

---

## Architecture Globale

```
jobs.csv
   ↓
Data Cleaning & Preprocessing
   ↓
Azure AI Language (NER)
   ↓
Azure SQL Database
   ↓
Machine Learning Model (Salary Prediction)
   ↓
FastAPI Backend
   ↓
NextJS Frontend
   ↓
Docker + CI/CD + Observability
```

---

## Stack Technique

### Cloud & Infrastructure

- Microsoft Azure
- Azure SQL Database (Serverless)
- Azure AI Language
- Terraform (Infrastructure as Code)
- Azure CLI (Linux)

### Backend

- FastAPI
- SQLAlchemy
- PyODBC (ODBC Driver 18)
- Pydantic
- JWT Authentication

### Data & Machine Learning

- Pandas / NumPy
- Scikit-learn (Régression)
- Azure AI Text Analytics (NER)
- MLflow

### Frontend

- NextJS

### DevOps & Qualité

- Docker / Docker Compose
- Terraform Docker Provider
- Pytest
- Flake8
- GitHub Actions
- uv (gestionnaire de dépendances obligatoire)

---

## Structure du Projet

```
├── 📁 .github
│   └── 📁 workflows
│       └── ⚙️ ci.yml
├── 📁 .pytest_cache
│   ├── 📁 v
│   ├── ⚙️ .gitignore
│   ├── 📄 CACHEDIR.TAG
│   └── 📝 README.md
├── 📁 backend
│   ├── 📁 app
│   │   ├── 📁 data
│   │   │   ├── 📄 cleaned_jobs.csv
│   │   │   ├── 📄 dataset_with_skills.csv
│   │   │   ├── 📄 extracted_skills_only.csv
│   │   │   └── 📄 uncleaned-ds-jobs.csv
│   │   ├── 📁 db
│   │   │   ├── 🐍 database.py
│   │   │   └── 🐍 dependencies.py
│   │   ├── 📁 loggins
│   │   │   ├── 🐍 backend_logs_config.py
│   │   │   └── 🐍 ml_logs_config.py
│   │   ├── 📁 ml
│   │   │   ├── 📁 Nootbook
│   │   │   │   ├── 📄 eda.ipynb
│   │   │   │   └── 📄 training.ipynb
│   │   │   ├── 📁 data_processing
│   │   │   │   ├── 🐍 __init__.py
│   │   │   │   ├── 🐍 embedding.py
│   │   │   │   ├── 🐍 encoding.py
│   │   │   │   └── 🐍 processing.py
│   │   │   ├── 🐍 __init__.py
│   │   │   └── 🐍 training_pipeline.py
│   │   ├── 📁 models
│   │   │   ├── 🐍 jobs.py
│   │   │   ├── 🐍 skills.py
│   │   │   └── 🐍 user.py
│   │   ├── 📁 routes
│   │   │   ├── 🐍 extract_skills.py
│   │   │   ├── 🐍 health.py
│   │   │   ├── 🐍 jobs.py
│   │   │   ├── 🐍 login.py
│   │   │   ├── 🐍 predict.py
│   │   │   └── 🐍 register.py
│   │   ├── 📁 saved_model
│   │   │   └── 📄 rf_model.pkl
│   │   ├── 📁 schemas
│   │   │   ├── 🐍 job_schema.py
│   │   │   └── 🐍 user_schema.py
│   │   ├── 📁 services
│   │   │   ├── 🐍 authService.py
│   │   │   ├── 🐍 azure_service.py
│   │   │   ├── 🐍 extract_skills_service.py
│   │   │   ├── 🐍 jobService.py
│   │   │   └── 🐍 predict.py
│   │   ├── 📁 utils
│   │   │   └── 🐍 database.py
│   │   └── 🐍 main.py
│   ├── 📁 tests
│   │   ├── 🐍 tes_register.py
│   │   └── 🐍 test_predict.py
│   └── 🐍 __init__.py
├── 📁 data
├── 📁 infra
│   ├── 📁 airflow
│   ├── 📁 docker
│   │   ├── 📄 backend.Dockerfile
│   │   ├── ⚙️ docker-compose.yml
│   │   └── 📄 mlflow.Dockerfile
│   └── 📁 mlflow
├── ⚙️ .dockerignore
├── ⚙️ .gitignore
├── 📝 README.md
├── ⚙️ pyproject.toml
└── 📄 uv.lock
```

---

## Installation & Configuration

### Prérequis

- Python >= 3.10
- uv (obligatoire)
- Docker & Docker Compose
- Azure CLI
- Terraform
- ODBC Driver 18 (Linux)

### Installation des dépendances

```bash
uv sync
```

### Configuration des variables d'environnement

Créer un fichier `.env` :

```env
DATABASE_URL=mssql+pyodbc://<username>:<password>@<server>.database.windows.net/<database>?driver=ODBC+Driver+18+for+SQL+Server

AZURE_LANGUAGE_ENDPOINT=<endpoint>
AZURE_LANGUAGE_KEY=<key>

SECRET_KEY=<jwt_secret>
```

---

## Infrastructure as Code (Terraform)

### Initialisation

```bash
cd infra
terraform init
```

### Provisioning

```bash
terraform apply
```

Les ressources créées :

- Azure SQL Database
- Azure AI Language
- Remote Backend Terraform

---

## Pipeline Data & IA

- Nettoyage du fichier jobs.csv
- Extraction des compétences via Azure AI
- Injection des données dans Azure SQL
- Transformation des salaires en moyenne numérique
- Entraînement d'un modèle de régression
- Suivi des expériences et des métriques via MLflow

---

## Module Predictor

Objectif : déterminer si l'entreprise est compétitive sur le marché.

- Nettoyage de la colonne Salary Estimate
- Transformation en valeur numérique moyenne
- Entraînement d'un modèle supervisé
- Évaluation via MAE et RMSE
- Suivi des expériences, des paramètres et des métriques via MLflow

---

## API & Frontend

### Backend – FastAPI

Endpoints disponibles :

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/Auth/login` | Signin |
| `POST` | `/Auth/register` | Register |
| `POST` | `/health/` | Health check |
| `POST` | `/predict-salary/` | Salary prediction |
| `GET`  | `/jobs/` | Get jobs |
| `POST` | `/jobs/` | Add jobs |

### Frontend – NextJS

Fonctionnalités :

- Visualisation des offres
- Upload de fichiers
- Consultation des prédictions salariales

---

## Conteneurisation

### Build & Run

```bash
docker-compose up --build
```

Services :

- Backend API
- Frontend
- Jaeger (Observabilité)

---

## Tests & Qualité

### Linting

```bash
ruff check .
```

### Tests

```bash
pytest
```

---

## CI/CD – GitHub Actions

Pipeline automatisée :

- Linting (Ruff / Flake8)
- Exécution des tests Pytest
- Build des images Docker

Si une étape échoue, la pipeline échoue.

---

## Observabilité

- Instrumentation via OpenTelemetry
- Visualisation des traces via Jaeger
- Analyse du temps de réponse API
- Monitoring des requêtes SQL

---

## Critères de Performance

- Zéro erreur de linting
- 100% succès Pytest
- Pipeline CI fonctionnelle
- Infrastructure Terraform valide
- API sécurisée et fonctionnelle
- Conteneurisation opérationnelle

---

## Sécurité

- Aucune clé API en dur
- Utilisation de `.env`
- Authentification JWT
- Isolation via Docker

---

## Conclusion

HR-Pulse propose une solution complète combinant :

- Data Engineering
- Intelligence Artificielle
- Cloud Azure
- DevOps & Industrialisation