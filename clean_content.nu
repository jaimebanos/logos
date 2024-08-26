# Script: limpiar_companies.nu

open "content.json"        
| uniq-by ISIN            
| to json               
| save -f "content.json" 
