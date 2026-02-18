provider "azurerm" {
  features {}
}

# 1. On pointe vers le serveur du formateur
data "azurerm_mssql_server" "formateur_server" {
  name                = "sql-server-hr-pulse-2026"
  resource_group_name = "RG-HR-PULSE-MGMT-YENNAYA" # Ton RG de formateur
}

# 2. L'élève crée sa base dans SON propre groupe de ressources
resource "azurerm_mssql_database" "db_student" {
  name      = "db-maryem" # L'élève change par son nom
  server_id = data.azurerm_mssql_server.formateur_server.id
  sku_name  = "Basic"
}