from enum import Enum, auto
from typing import List
from AccessManager import AccessManager

class ApplicationScreen(Enum):
    ORDER = auto()
    ORDER_SUMMARY = auto()
    PRODUCTS_SETUP = auto()
    SYSTEM_SETTINGS = auto()
    CLIENT_INTERACTIONS = auto()

class AccessLevel(Enum):
    VIEW = auto()
    CREATE = auto()
    MODIFY = auto()
    DELETE = auto()

access_manager = AccessManager[str, str, ApplicationScreen, AccessLevel]()

access_manager.add_user("Livia.Bowe@printweave.biz")
access_manager.add_user("Arjan.Hartman@printweave.biz")
access_manager.add_user("Cleo.Short@printweave.biz")
access_manager.add_user("Mae.Mellor@printweave.biz")
access_manager.add_user("Frankie.Koch@printweave.biz")
access_manager.add_user("Deborah.Moss@printweave.biz")
access_manager.add_user("Kishan.Buchanan@printweave.biz")
access_manager.add_user("Seb.Sutton@printweave.biz")
access_manager.add_user("Bo.Wagner@printweave.biz")
access_manager.add_user("Tye.Knights@printweave.biz")

access_manager.add_group("Sales")
access_manager.add_group("SalesManagers")
access_manager.add_group("Managers")
access_manager.add_group("IT")
access_manager.add_group("CustomerService")
access_manager.add_group("AllStaff")

# Setup the company structure - user to team mapping
access_manager.add_user_to_group_mapping("Livia.Bowe@printweave.biz", "Sales")
access_manager.add_user_to_group_mapping("Arjan.Hartman@printweave.biz", "Sales")
access_manager.add_user_to_group_mapping("Frankie.Koch@printweave.biz", "Sales")
access_manager.add_user_to_group_mapping("Cleo.Short@printweave.biz", "SalesManagers")
access_manager.add_user_to_group_mapping("Mae.Mellor@printweave.biz", "SalesManagers")
access_manager.add_user_to_group_mapping("Deborah.Moss@printweave.biz", "CustomerService")
access_manager.add_user_to_group_mapping("Kishan.Buchanan@printweave.biz", "CustomerService")
access_manager.add_user_to_group_mapping("Seb.Sutton@printweave.biz", "IT")
access_manager.add_user_to_group_mapping("Bo.Wagner@printweave.biz", "Managers")
access_manager.add_user_to_group_mapping("Tye.Knights@printweave.biz", "Managers")

# Setup the team/group mappings
access_manager.add_group_to_group_mapping("SalesManagers", "Sales")
access_manager.add_group_to_group_mapping("Sales", "AllStaff")
access_manager.add_group_to_group_mapping("Managers", "AllStaff")
access_manager.add_group_to_group_mapping("IT", "AllStaff")
access_manager.add_group_to_group_mapping("CustomerService", "AllStaff")

access_manager.add_group_to_application_component_and_access_level_mapping("AllStaff", ApplicationScreen.ORDER_SUMMARY, AccessLevel.VIEW)
access_manager.add_group_to_application_component_and_access_level_mapping("AllStaff", ApplicationScreen.CLIENT_INTERACTIONS, AccessLevel.VIEW)
access_manager.add_group_to_application_component_and_access_level_mapping("Sales", ApplicationScreen.ORDER, AccessLevel.MODIFY)
access_manager.add_group_to_application_component_and_access_level_mapping("SalesManagers", ApplicationScreen.PRODUCTS_SETUP, AccessLevel.MODIFY)
access_manager.add_group_to_application_component_and_access_level_mapping("CustomerService", ApplicationScreen.CLIENT_INTERACTIONS, AccessLevel.MODIFY)
access_manager.add_group_to_application_component_and_access_level_mapping("IT", ApplicationScreen.SYSTEM_SETTINGS, AccessLevel.MODIFY)

access_manager.add_entity_type("Clients")
access_manager.add_entity("Clients", "CompanyA")
access_manager.add_entity("Clients", "CompanyB")
access_manager.add_entity("Clients", "CompanyC")
access_manager.add_entity_type("Products")
access_manager.add_entity("Products", "PrintingMachines")
access_manager.add_entity("Products", "WeavingMachines")

access_manager.add_user_to_entity_mapping("Livia.Bowe@printweave.biz", "Products", "PrintingMachines")
access_manager.add_user_to_entity_mapping("Arjan.Hartman@printweave.biz", "Products", "PrintingMachines")
access_manager.add_user_to_entity_mapping("Cleo.Short@printweave.biz", "Products", "PrintingMachines")
access_manager.add_user_to_entity_mapping("Frankie.Koch@printweave.biz", "Products", "WeavingMachines")
access_manager.add_user_to_entity_mapping("Mae.Mellor@printweave.biz", "Products", "WeavingMachines")
access_manager.add_user_to_entity_mapping("Deborah.Moss@printweave.biz", "Clients", "CompanyA")
access_manager.add_user_to_entity_mapping("Deborah.Moss@printweave.biz", "Clients", "CompanyB")
access_manager.add_user_to_entity_mapping("Kishan.Buchanan@printweave.biz", "Clients", "CompanyA")
access_manager.add_user_to_entity_mapping("Kishan.Buchanan@printweave.biz", "Clients", "CompanyB")
access_manager.add_user_to_entity_mapping("Kishan.Buchanan@printweave.biz", "Clients", "CompanyC")

print(access_manager.has_access_to_application_component("Livia.Bowe@printweave.biz", ApplicationScreen.PRODUCTS_SETUP, AccessLevel.MODIFY))

print(access_manager.has_access_to_application_component("Mae.Mellor@printweave.biz", ApplicationScreen.PRODUCTS_SETUP, AccessLevel.MODIFY))

print(access_manager.has_access_to_entity("Frankie.Koch@printweave.biz", "Products", "WeavingMachines"))

print(access_manager.has_access_to_entity("Arjan.Hartman@printweave.biz", "Products", "WeavingMachines"))

viewableClients: List[str] = list(access_manager.get_accessible_entities("Kishan.Buchanan@printweave.biz", "Clients"))
print(viewableClients)
