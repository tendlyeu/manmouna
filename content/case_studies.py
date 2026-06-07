"""
Case studies — named client precedents from prior engagements.
"""

BID_DERIVED = []

NAMED_PRECEDENTS = [
    {
        "id": "mckinsey-governance",
        "title": "Data governance infrastructure for global consulting",
        "buyer": "McKinsey & Company",
        "country": "Estonia",
        "flag": "🇪🇪",
        "sector": "Cross-sector",
        "status": "Active engagement",
        "problem": "Managing the governance infrastructure of McKinsey's internal solutions portfolio at global scale, with strict security and compliance requirements.",
        "approach": "Data pipeline orchestration across AWS services with infrastructure-as-code via Terraform, identity management through Keycloak, and continuous delivery across distributed teams.",
        "capability": "Enterprise-grade DevOps, infrastructure governance, cloud-native data engineering.",
        "tech": ["AWS", "Terraform", "Python", "EMR", "Athena", "Firehose", "Keycloak", "Docker"],
    },
    {
        "id": "dsm-etl-ml",
        "title": "End-to-end ETL and ML platform for product intelligence",
        "buyer": "DSM",
        "country": "Netherlands",
        "flag": "🇳🇱",
        "sector": "Enterprise",
        "status": "Delivered",
        "problem": "Product data scattered across APIs, S3, Athena, and web sources needed consolidation into a single platform serving in-house applications, customer-facing tools, BI dashboards, and ML predictions.",
        "approach": "Built ETL system from scratch ingesting multi-source product data into PostgreSQL, exposed via Lambda APIs. Developed NLP models for customer support on SageMaker, deployed with MLflow. Managed a team of five engineers.",
        "capability": "Full-stack data platform, NLP model deployment, team leadership.",
        "tech": ["AWS", "Python", "Airflow", "Glue", "SageMaker", "TensorFlow", "dbt", "CloudFormation"],
    },
    {
        "id": "arista-device-scoring",
        "title": "ML-driven device identification and data infrastructure",
        "buyer": "Arista Networks",
        "country": "United States",
        "flag": "🇺🇸",
        "sector": "Cloud infrastructure",
        "status": "Delivered",
        "problem": "Cloud infrastructure provider needed automated scoring of websites and identification of incoming devices, plus reliable daily data pipelines and quality checks across GCP and AWS.",
        "approach": "Developed and deployed ML scoring models, built data pipelines from databases to cloud storage, created Airflow DAGs for processing, backups, and data-quality monitoring. Code refactoring and dbt transformations across the stack.",
        "capability": "ML model deployment at scale, cross-cloud data engineering, data quality automation.",
        "tech": ["GCP", "Python", "Spark", "Scala", "PostgreSQL", "Airflow", "Cloud Run", "dbt"],
    },
]


ALL = BID_DERIVED + NAMED_PRECEDENTS
