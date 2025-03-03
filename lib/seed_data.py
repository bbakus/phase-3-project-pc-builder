
from models.components import Component
from models.builds import Build
from models.database import CONN, CURSOR, create_tables

def seed_data():
   
    print("Starting to seed database...")
    
    # CPUs
    cpus = [
        {"name": "AMD Ryzen 5 5600X", "category": "CPU", "price": 199.99},
        {"name": "AMD Ryzen 7 5800X", "category": "CPU", "price": 299.99},
        {"name": "AMD Ryzen 9 5900X", "category": "CPU", "price": 399.99},
        {"name": "AMD Ryzen 9 5950X", "category": "CPU", "price": 549.99},
        {"name": "Intel Core i5-12600K", "category": "CPU", "price": 279.99},
        {"name": "Intel Core i7-12700K", "category": "CPU", "price": 379.99},
        {"name": "Intel Core i9-12900K", "category": "CPU", "price": 589.99},
        {"name": "Intel Core i5-13600K", "category": "CPU", "price": 329.99},
        {"name": "Intel Core i7-13700K", "category": "CPU", "price": 409.99},
        {"name": "Intel Core i9-13900K", "category": "CPU", "price": 599.99}
    ]
    
    # GPUs
    gpus = [
        {"name": "NVIDIA GeForce RTX 3060", "category": "GPU", "price": 329.99},
        {"name": "NVIDIA GeForce RTX 3060 Ti", "category": "GPU", "price": 399.99},
        {"name": "NVIDIA GeForce RTX 3070", "category": "GPU", "price": 499.99},
        {"name": "NVIDIA GeForce RTX 3070 Ti", "category": "GPU", "price": 599.99},
        {"name": "NVIDIA GeForce RTX 3080", "category": "GPU", "price": 699.99},
        {"name": "NVIDIA GeForce RTX 3080 Ti", "category": "GPU", "price": 899.99},
        {"name": "NVIDIA GeForce RTX 3090", "category": "GPU", "price": 1499.99},
        {"name": "AMD Radeon RX 6600", "category": "GPU", "price": 299.99},
        {"name": "AMD Radeon RX 6600 XT", "category": "GPU", "price": 379.99},
        {"name": "AMD Radeon RX 6700 XT", "category": "GPU", "price": 479.99},
        {"name": "AMD Radeon RX 6800", "category": "GPU", "price": 579.99},
        {"name": "AMD Radeon RX 6800 XT", "category": "GPU", "price": 649.99},
        {"name": "AMD Radeon RX 6900 XT", "category": "GPU", "price": 999.99}
    ]
    
    # Motherboards
    motherboards = [
        {"name": "ASUS ROG Strix B550-F Gaming", "category": "Motherboard", "price": 189.99},
        {"name": "ASUS TUF Gaming X570-Plus", "category": "Motherboard", "price": 209.99},
        {"name": "ASUS ROG Crosshair VIII Hero X570", "category": "Motherboard", "price": 379.99},
        {"name": "MSI MAG B550 Tomahawk", "category": "Motherboard", "price": 169.99},
        {"name": "MSI MPG B550 Gaming Edge WiFi", "category": "Motherboard", "price": 199.99},
        {"name": "MSI MEG X570 ACE", "category": "Motherboard", "price": 369.99},
        {"name": "Gigabyte B550 AORUS Elite", "category": "Motherboard", "price": 159.99},
        {"name": "Gigabyte X570 AORUS Elite", "category": "Motherboard", "price": 199.99},
        {"name": "Gigabyte X570 AORUS Master", "category": "Motherboard", "price": 359.99},
        {"name": "ASRock B550 Pro4", "category": "Motherboard", "price": 134.99},
        {"name": "ASUS ROG Strix Z690-A Gaming", "category": "Motherboard", "price": 289.99},
        {"name": "MSI PRO Z690-A", "category": "Motherboard", "price": 229.99},
        {"name": "Gigabyte Z690 AORUS Elite", "category": "Motherboard", "price": 269.99},
        {"name": "ASRock Z690 Steel Legend", "category": "Motherboard", "price": 259.99}
    ]
    
    # RAM
    rams = [
        {"name": "Corsair Vengeance LPX 16GB (2x8GB) DDR4-3200", "category": "RAM", "price": 69.99},
        {"name": "Corsair Vengeance RGB Pro 16GB (2x8GB) DDR4-3600", "category": "RAM", "price": 89.99},
        {"name": "Corsair Vengeance LPX 32GB (2x16GB) DDR4-3200", "category": "RAM", "price": 119.99},
        {"name": "Corsair Vengeance RGB Pro 32GB (2x16GB) DDR4-3600", "category": "RAM", "price": 149.99},
        {"name": "G.Skill Ripjaws V 16GB (2x8GB) DDR4-3200", "category": "RAM", "price": 64.99},
        {"name": "G.Skill Trident Z RGB 16GB (2x8GB) DDR4-3600", "category": "RAM", "price": 94.99},
        {"name": "G.Skill Ripjaws V 32GB (2x16GB) DDR4-3200", "category": "RAM", "price": 114.99},
        {"name": "G.Skill Trident Z RGB 32GB (2x16GB) DDR4-3600", "category": "RAM", "price": 154.99},
        {"name": "Crucial Ballistix 16GB (2x8GB) DDR4-3200", "category": "RAM", "price": 74.99},
        {"name": "Crucial Ballistix RGB 16GB (2x8GB) DDR4-3600", "category": "RAM", "price": 84.99},
        {"name": "Crucial Ballistix 32GB (2x16GB) DDR4-3200", "category": "RAM", "price": 129.99},
        {"name": "Crucial Ballistix RGB 32GB (2x16GB) DDR4-3600", "category": "RAM", "price": 144.99},
        {"name": "Kingston FURY Beast 16GB (2x8GB) DDR4-3200", "category": "RAM", "price": 69.99},
        {"name": "Kingston FURY RGB 32GB (2x16GB) DDR4-3600", "category": "RAM", "price": 139.99},
        {"name": "Corsair Dominator Platinum RGB 32GB (2x16GB) DDR5-5200", "category": "RAM", "price": 289.99},
        {"name": "G.Skill Trident Z5 RGB 32GB (2x16GB) DDR5-5600", "category": "RAM", "price": 309.99}
    ]
    
    # Storage
    storages = [
        {"name": "Samsung 970 EVO Plus 500GB NVMe SSD", "category": "Storage", "price": 79.99},
        {"name": "Samsung 970 EVO Plus 1TB NVMe SSD", "category": "Storage", "price": 129.99},
        {"name": "Samsung 970 EVO Plus 2TB NVMe SSD", "category": "Storage", "price": 249.99},
        {"name": "Samsung 980 PRO 1TB NVMe PCIe 4.0 SSD", "category": "Storage", "price": 169.99},
        {"name": "Samsung 980 PRO 2TB NVMe PCIe 4.0 SSD", "category": "Storage", "price": 319.99},
        {"name": "Western Digital Black SN750 1TB NVMe SSD", "category": "Storage", "price": 139.99},
        {"name": "Western Digital Black SN850 1TB NVMe PCIe 4.0 SSD", "category": "Storage", "price": 179.99},
        {"name": "Crucial P5 1TB NVMe SSD", "category": "Storage", "price": 119.99},
        {"name": "Crucial P5 Plus 1TB NVMe PCIe 4.0 SSD", "category": "Storage", "price": 159.99},
        {"name": "Samsung 870 EVO 1TB SATA SSD", "category": "Storage", "price": 109.99},
        {"name": "Samsung 870 EVO 2TB SATA SSD", "category": "Storage", "price": 209.99},
        {"name": "Crucial MX500 1TB SATA SSD", "category": "Storage", "price": 99.99},
        {"name": "Western Digital Blue 1TB SATA SSD", "category": "Storage", "price": 94.99},
        {"name": "Seagate Barracuda 2TB 7200RPM HDD", "category": "Storage", "price": 54.99},
        {"name": "Seagate Barracuda 4TB 5400RPM HDD", "category": "Storage", "price": 89.99},
        {"name": "Western Digital Blue 2TB 7200RPM HDD", "category": "Storage", "price": 49.99},
        {"name": "Western Digital Black 4TB 7200RPM HDD", "category": "Storage", "price": 149.99}
    ]
    
    # Power Supplies (PSUs)
    psus = [
        {"name": "Corsair RM650x 80+ Gold Fully Modular", "category": "PSU", "price": 109.99},
        {"name": "Corsair RM750x 80+ Gold Fully Modular", "category": "PSU", "price": 129.99},
        {"name": "Corsair RM850x 80+ Gold Fully Modular", "category": "PSU", "price": 149.99},
        {"name": "Corsair RM1000x 80+ Gold Fully Modular", "category": "PSU", "price": 189.99},
        {"name": "EVGA SuperNOVA 650 G5 80+ Gold Fully Modular", "category": "PSU", "price": 99.99},
        {"name": "EVGA SuperNOVA 750 G5 80+ Gold Fully Modular", "category": "PSU", "price": 119.99},
        {"name": "EVGA SuperNOVA 850 G5 80+ Gold Fully Modular", "category": "PSU", "price": 139.99},
        {"name": "Seasonic FOCUS GX-650 80+ Gold Fully Modular", "category": "PSU", "price": 104.99},
        {"name": "Seasonic FOCUS GX-750 80+ Gold Fully Modular", "category": "PSU", "price": 124.99},
        {"name": "Seasonic FOCUS GX-850 80+ Gold Fully Modular", "category": "PSU", "price": 144.99},
        {"name": "be quiet! Straight Power 11 750W 80+ Gold", "category": "PSU", "price": 134.99},
        {"name": "Thermaltake Toughpower GF1 850W 80+ Gold", "category": "PSU", "price": 149.99},
        {"name": "Cooler Master V850 Gold V2 80+ Gold", "category": "PSU", "price": 139.99},
        {"name": "Corsair AX1600i 80+ Titanium Fully Modular", "category": "PSU", "price": 499.99}
    ]
    
    # Cases
    cases = [
        {"name": "NZXT H510", "category": "Case", "price": 69.99},
        {"name": "NZXT H510i", "category": "Case", "price": 99.99},
        {"name": "NZXT H710", "category": "Case", "price": 139.99},
        {"name": "NZXT H710i", "category": "Case", "price": 169.99},
        {"name": "Corsair 4000D Airflow", "category": "Case", "price": 94.99},
        {"name": "Corsair 5000D Airflow", "category": "Case", "price": 159.99},
        {"name": "Corsair iCUE 5000X RGB", "category": "Case", "price": 189.99},
        {"name": "Lian Li O11 Dynamic", "category": "Case", "price": 149.99},
        {"name": "Lian Li O11 Dynamic XL", "category": "Case", "price": 199.99},
        {"name": "Lian Li Lancool II Mesh", "category": "Case", "price": 109.99},
        {"name": "Phanteks Eclipse P400A", "category": "Case", "price": 79.99},
        {"name": "Phanteks Eclipse P500A", "category": "Case", "price": 119.99},
        {"name": "Fractal Design Meshify C", "category": "Case", "price": 99.99},
        {"name": "Fractal Design Meshify 2", "category": "Case", "price": 149.99},
        {"name": "be quiet! Pure Base 500DX", "category": "Case", "price": 109.99},
        {"name": "Cooler Master MasterBox TD500 Mesh", "category": "Case", "price": 99.99}
    ]
    
    # Cooling
    cooling = [
        {"name": "Noctua NH-D15", "category": "Cooling", "price": 99.99},
        {"name": "Noctua NH-U12S", "category": "Cooling", "price": 69.99},
        {"name": "be quiet! Dark Rock Pro 4", "category": "Cooling", "price": 89.99},
        {"name": "be quiet! Dark Rock 4", "category": "Cooling", "price": 74.99},
        {"name": "Cooler Master Hyper 212 RGB Black Edition", "category": "Cooling", "price": 44.99},
        {"name": "Cooler Master Hyper 212 EVO V2", "category": "Cooling", "price": 39.99},
        {"name": "ARCTIC Freezer 34 eSports DUO", "category": "Cooling", "price": 54.99},
        {"name": "Corsair iCUE H100i ELITE CAPELLIX", "category": "Cooling", "price": 159.99},
        {"name": "Corsair iCUE H150i ELITE CAPELLIX", "category": "Cooling", "price": 189.99},
        {"name": "NZXT Kraken X53 240mm", "category": "Cooling", "price": 129.99},
        {"name": "NZXT Kraken X63 280mm", "category": "Cooling", "price": 149.99},
        {"name": "NZXT Kraken X73 360mm", "category": "Cooling", "price": 179.99},
        {"name": "ARCTIC Liquid Freezer II 240", "category": "Cooling", "price": 99.99},
        {"name": "ARCTIC Liquid Freezer II 280", "category": "Cooling", "price": 119.99},
        {"name": "ARCTIC Liquid Freezer II 360", "category": "Cooling", "price": 139.99},
        {"name": "Lian Li Galahad 240", "category": "Cooling", "price": 129.99},
        {"name": "Lian Li Galahad 360", "category": "Cooling", "price": 159.99}
    ]
    
    
    all_components = cpus + gpus + motherboards + rams + storages + psus + cases + cooling
    
    
    print(f"Adding {len(all_components)} components to database...")
    
    component_objects = {} 
    
    for component_data in all_components:
        try:
            # Create a Component object
            component = Component(
                component_data["name"],
                component_data["category"],
                component_data["price"]
            )
            # Save to database
            component.save()
            
            # Store the component object for later lookup
            category = component_data["category"]
            name = component_data["name"]
            if category not in component_objects:
                component_objects[category] = {}
            component_objects[category][name] = component
            
            print(f"Added {category}: {name} (ID: {component.id})")
        except Exception as e:
            print(f"Error adding component {component_data['name']}: {str(e)}")
    
    # Create sample builds
    try:
        print("\nCreating sample builds...")
        
        # High-end Gaming PC
        gaming_build = Build("Ultimate Gaming Rig", "High-end gaming PC for 4K gaming")
        gaming_build.save()
        
        
        gaming_build.add_component(component_objects["CPU"]["AMD Ryzen 9 5950X"].id)
        gaming_build.add_component(component_objects["GPU"]["NVIDIA GeForce RTX 3090"].id)
        gaming_build.add_component(component_objects["Motherboard"]["ASUS ROG Crosshair VIII Hero X570"].id)
        gaming_build.add_component(component_objects["RAM"]["G.Skill Trident Z RGB 32GB (2x16GB) DDR4-3600"].id)
        gaming_build.add_component(component_objects["Storage"]["Samsung 980 PRO 2TB NVMe PCIe 4.0 SSD"].id)
        gaming_build.add_component(component_objects["Storage"]["Seagate Barracuda 4TB 5400RPM HDD"].id)
        gaming_build.add_component(component_objects["PSU"]["Corsair RM1000x 80+ Gold Fully Modular"].id)
        gaming_build.add_component(component_objects["Case"]["Lian Li O11 Dynamic XL"].id)
        gaming_build.add_component(component_objects["Cooling"]["NZXT Kraken X73 360mm"].id)
        print(f"Created 'Ultimate Gaming Rig' build with ID: {gaming_build.id}")
        
        # Mid-range Gaming PC
        mid_build = Build("Mid-range Gaming PC", "Balanced gaming PC for 1440p gaming")
        mid_build.save()
        
        
        mid_build.add_component(component_objects["CPU"]["AMD Ryzen 5 5600X"].id)
        mid_build.add_component(component_objects["GPU"]["NVIDIA GeForce RTX 3070"].id)
        mid_build.add_component(component_objects["Motherboard"]["MSI MAG B550 Tomahawk"].id)
        mid_build.add_component(component_objects["RAM"]["Corsair Vengeance LPX 16GB (2x8GB) DDR4-3200"].id)
        mid_build.add_component(component_objects["Storage"]["Samsung 970 EVO Plus 1TB NVMe SSD"].id)
        mid_build.add_component(component_objects["PSU"]["Corsair RM750x 80+ Gold Fully Modular"].id)
        mid_build.add_component(component_objects["Case"]["Corsair 4000D Airflow"].id)
        mid_build.add_component(component_objects["Cooling"]["be quiet! Dark Rock 4"].id)
        print(f"Created 'Mid-range Gaming PC' build with ID: {mid_build.id}")
        
        # Budget Gaming PC
        budget_build = Build("Budget Gaming PC", "Affordable gaming PC for 1080p gaming")
        budget_build.save()
        
        
        budget_build.add_component(component_objects["CPU"]["Intel Core i5-12600K"].id)
        budget_build.add_component(component_objects["GPU"]["NVIDIA GeForce RTX 3060"].id)
        budget_build.add_component(component_objects["Motherboard"]["ASRock B550 Pro4"].id)
        budget_build.add_component(component_objects["RAM"]["G.Skill Ripjaws V 16GB (2x8GB) DDR4-3200"].id)
        budget_build.add_component(component_objects["Storage"]["Crucial P5 1TB NVMe SSD"].id)
        budget_build.add_component(component_objects["PSU"]["EVGA SuperNOVA 650 G5 80+ Gold Fully Modular"].id)
        budget_build.add_component(component_objects["Case"]["Phanteks Eclipse P400A"].id)
        budget_build.add_component(component_objects["Cooling"]["Cooler Master Hyper 212 RGB Black Edition"].id)
        print(f"Created 'Budget Gaming PC' build with ID: {budget_build.id}")
        
        # Content Creator Workstation
        creator_build = Build("Content Creator Workstation", "PC optimized for video editing and 3D rendering")
        creator_build.save()
        
       
        creator_build.add_component(component_objects["CPU"]["Intel Core i9-12900K"].id)
        creator_build.add_component(component_objects["GPU"]["AMD Radeon RX 6900 XT"].id)
        creator_build.add_component(component_objects["Motherboard"]["ASUS ROG Strix Z690-A Gaming"].id)
        creator_build.add_component(component_objects["RAM"]["Corsair Vengeance RGB Pro 32GB (2x16GB) DDR4-3600"].id)
        creator_build.add_component(component_objects["Storage"]["Samsung 980 PRO 2TB NVMe PCIe 4.0 SSD"].id)
        creator_build.add_component(component_objects["Storage"]["Samsung 870 EVO 2TB SATA SSD"].id)
        creator_build.add_component(component_objects["PSU"]["Seasonic FOCUS GX-850 80+ Gold Fully Modular"].id)
        creator_build.add_component(component_objects["Case"]["Fractal Design Meshify 2"].id)
        creator_build.add_component(component_objects["Cooling"]["ARCTIC Liquid Freezer II 360"].id)
        print(f"Created 'Content Creator Workstation' build with ID: {creator_build.id}")
        
    except Exception as e:
        print(f"Error creating sample builds: {str(e)}")
    
    
    print("\nVerifying database contents:")
    
    
    all_components = CURSOR.execute("SELECT COUNT(*) FROM components").fetchone()[0]
    print(f"Total components in database: {all_components}")
    
    
    all_builds = CURSOR.execute("SELECT COUNT(*) FROM builds").fetchone()[0]
    print(f"Total builds in database: {all_builds}")
    
    print("\nDatabase seeded successfully!")

if __name__ == "__main__":
    
    create_tables()
    seed_data()