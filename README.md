

## Project Structur

```
├── 📁 .github
│   └── 📁 workflows
│       └── ⚙️ ci.yml              # GitHub Actions pipeline (lint, tests, Docker build)
│
├── 📁 backend                     # FastAPI backend application
│   ├── 📁 app                     # Main application source code
│   │   ├── 📁 ml                  # Machine Learning module
│   │   │   └── 📁 Notebook        # ML experimentation & analysis
│   │   │       └── 📄 eda.ipynb   # Exploratory Data Analysis (salary analysis, data cleaning, visualization)
│   │   │
│   │   ├── 📁 models              # SQLAlchemy database models (tables definition)
│   │   ├── 📁 routes              # FastAPI API endpoints (/jobs, /predict, etc.)
│   │   ├── 📁 schemas             # Pydantic schemas (request/response validation)
│   │   ├── 📁 services            # Business logic (NER, ingestion, salary processing, prediction)
│   │   ├── 📁 utils               # Helper utilities
│   │   │   └── 🐍 database.py     # Azure SQL connection & session management
│   │   └── 🐍 main.py             # FastAPI entrypoint (app initialization & route registration)
│   │
│   ├── 📁 tests                   # Pytest unit and integration tests
│   └── 🐳 Dockerfile              # Backend Docker image configuration
│
├── 📁 terraform                   # Infrastructure as Code (Azure resources provisioning)
│   ├── 📄 ai.tf                   # Azure AI Language (Cognitive Service) resource definition
│   ├── 📄 backend.tf              # Remote Terraform state configuration (Azure Storage)
│   ├── 📄 outputs.tf              # Outputs (SQL connection string, AI endpoint, keys)
│   ├── 📄 provider.tf             # Azure provider configuration
│   ├── 📄 sql.tf                  # Azure SQL Server & Database resources
│   ├── 📄 terraform.tfvars        # Values for Terraform variables
│   ├── 📄 variables.tf            # Input variable definitions
│   └── 📄 versions.tf             # Terraform & provider version constraints
│
├── ⚙️ .gitignore                  # Files & folders excluded from Git tracking
├── 📝 README.md                   # Project documentation & setup instructions
└── ⚙️ docker-compose.yml          # Multi-container orchestration (backend + Jaeger, etc.)
```