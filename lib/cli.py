import os
from models import Component, Build

class CLI:
    """Command Line Interface for PC Builder application"""
    
    def __init__(self):
        self.current_build = None
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        """Print a formatted header"""
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"{title.center(60)}")
        print("=" * 60 + "\n")
    
    def get_input(self, prompt, options=None):
        """Get input from user with validation"""
        while True:
            user_input = input(prompt)
            
            if options is None:
                return user_input
            
            if user_input in options:
                return user_input
            
            print(f"Invalid input. Please enter one of: {', '.join(options)}")
    
    def get_number_input(self, prompt, min_value=None, max_value=None):
        """Get numeric input from user with validation"""
        while True:
            user_input = input(prompt)
            
            try:
                value = int(user_input)
                
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}")
                    continue
                
                return value
            except ValueError:
                print("Please enter a valid number")
    
    def main_menu(self):
        """Display the main menu"""
        self.print_header("PC BUILDER - MAIN MENU")
        
        if self.current_build:
            print(f"Current Build: {self.current_build.name}")
            print(f"Total components: {len(self.current_build.get_components())}")
        
        print("1. Browse Components")
        print("2. View/Manage Builds")
        if self.current_build:
            print("3. View Current Build")
            print("4. Add Component to Current Build")
        print("0. Exit")
        
        if self.current_build:
            choice = self.get_input("\nSelect an option: ", ["0", "1", "2", "3", "4"])
        else:
            choice = self.get_input("\nSelect an option: ", ["0", "1", "2"])
        
        if choice == "1":
            self.browse_components()
        elif choice == "2":
            self.view_builds()
        elif choice == "3" and self.current_build:
            self.view_current_build()
        elif choice == "4" and self.current_build:
            self.add_component_to_build()
        elif choice == "0":
            print("Thank you for using PC Builder!")
            exit()
    
    def browse_components(self):
        """Browse components by category"""
        self.print_header("BROWSE COMPONENTS")
        
        # Verify components table exists first
        try:
            import sqlite3
            conn = sqlite3.connect('pc_builder.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='components'")
            if not cursor.fetchone():
                print("Components table doesn't exist! Please run the seed_data.py script first.")
                input("\nPress Enter to continue...")
                self.main_menu()
                return
        except Exception as e:
            print(f"Database error: {str(e)}")
            input("\nPress Enter to continue...")
            self.main_menu()
            return
    
        
        categories = ["CPU", "GPU", "Motherboard", "RAM", "Storage", "PSU", "Case", "Cooling", "All"]
        
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        print("0. Back to Main Menu")
        
        choice = self.get_number_input("\nSelect a category: ", 0, len(categories))
        
        if choice == 0:
            self.main_menu()
            return
        
        category = categories[choice - 1]
        
        if category == "All":
            # Get all components from database
            components = []
            for cat in categories[:-1]:  # Exclude "All"
                # Execute a SQL query to get components by category
                # This is a simplified version, you might want to implement this in your Component class
                import sqlite3
                conn = sqlite3.connect('pc_builder.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM components WHERE category = ?", (cat,))
                rows = cursor.fetchall()
                for row in rows:
                    components.append(Component(row[1], row[2], row[3], row[0]))
        else:
            # Get components by category from database
            import sqlite3
            conn = sqlite3.connect('pc_builder.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM components WHERE category = ?", (category,))
            rows = cursor.fetchall()
            components = [Component(row[1], row[2], row[3], row[0]) for row in rows]
        
        self.display_components(components, category)
    
    def display_components(self, components, category):
        """Display a list of components"""
        self.print_header(f"{category.upper()} COMPONENTS")
        
        if not components:
            print(f"No {category} components found.")
            input("\nPress Enter to continue...")
            self.browse_components()
            return
        
        for i, component in enumerate(components, 1):
            print(f"{i}. {component.name} - ${component.price:.2f}")
        
        print("\n1. View Component Details")
        if self.current_build:
            print("2. Add Component to Current Build")
        print("0. Back")
        
        if self.current_build:
            choice = self.get_input("\nSelect an option: ", ["0", "1", "2"])
        else:
            choice = self.get_input("\nSelect an option: ", ["0", "1"])
        
        if choice == "1":
            component_num = self.get_number_input("Enter component number: ", 1, len(components))
            self.view_component_details(components[component_num - 1])
        elif choice == "2" and self.current_build:
            component_num = self.get_number_input("Enter component number to add: ", 1, len(components))
            self.current_build.add_component(components[component_num - 1].id)
            print(f"\n{components[component_num - 1].name} added to {self.current_build.name}!")
            input("\nPress Enter to continue...")
            self.browse_components()
        elif choice == "0":
            self.browse_components()
    
    def view_component_details(self, component):
        """View details of a specific component"""
        self.print_header(f"COMPONENT DETAILS: {component.name}")
        
        print(f"Name: {component.name}")
        print(f"Category: {component.category}")
        print(f"Price: ${component.price:.2f}")
        print(f"ID: {component.id}")
        
        if self.current_build:
            print("\n1. Add to Current Build")
        print("0. Back")
        
        if self.current_build:
            choice = self.get_input("\nSelect an option: ", ["0", "1"])
            if choice == "1":
                self.current_build.add_component(component.id)
                print(f"\n{component.name} added to {self.current_build.name}!")
        else:
            choice = self.get_input("\nSelect an option: ", ["0"])
        
        input("\nPress Enter to continue...")
        self.browse_components()
    
    def view_builds(self):
        """View and manage builds"""
        self.print_header("VIEW/MANAGE BUILDS")
        
        # Get all builds from database
        import sqlite3
        conn = sqlite3.connect('pc_builder.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM builds")
        rows = cursor.fetchall()
        builds = [Build(row[1], row[2], row[0]) for row in rows]
        
        if not builds:
            print("No builds found.")
            print("\n1. Create New Build")
            print("0. Back to Main Menu")
            
            choice = self.get_input("\nSelect an option: ", ["0", "1"])
            
            if choice == "1":
                self.create_new_build()
            elif choice == "0":
                self.main_menu()
            return
        
        for i, build in enumerate(builds, 1):
            print(f"{i}. {build.name}")
        
        print("\n1. View Build Details")
        print("2. Create New Build")
        print("0. Back to Main Menu")
        
        choice = self.get_input("\nSelect an option: ", ["0", "1", "2"])
        
        if choice == "1":
            build_num = self.get_number_input("Enter build number: ", 1, len(builds))
            self.view_build_details(builds[build_num - 1])
        elif choice == "2":
            self.create_new_build()
        elif choice == "0":
            self.main_menu()
    
    def view_build_details(self, build):
        """View details of a specific build"""
        self.print_header(f"BUILD DETAILS: {build.name}")
        
        print(f"Name: {build.name}")
        print(f"Description: {build.description}")
        
        components = build.get_components()
        
        if components:
            print("\nComponents:")
            total_price = 0
            for i, component in enumerate(components, 1):
                print(f"{i}. {component.category}: {component.name} - ${component.price:.2f}")
                total_price += component.price
            
            print(f"\nTotal Price: ${total_price:.2f}")
        else:
            print("\nNo components in this build yet.")
        
        print("\n1. Set as Current Build")
        print("2. Delete Build")
        print("0. Back")
        
        choice = self.get_input("\nSelect an option: ", ["0", "1", "2"])
        
        if choice == "1":
            self.current_build = build
            print(f"\n{build.name} set as current build!")
            input("\nPress Enter to continue...")
            self.main_menu()
        elif choice == "2":
            confirm = self.get_input(f"Are you sure you want to delete {build.name}? (y/n): ", ["y", "n"])
            if confirm == "y":
                # Delete the build from the database
                self.delete_build(build)
                print(f"\n{build.name} deleted!")
            input("\nPress Enter to continue...")
            self.view_builds()
        elif choice == "0":
            self.view_builds()
    
    def create_new_build(self):
        """Create a new build"""
        self.print_header("CREATE NEW BUILD")
        
        name = input("Enter build name: ")
        description = input("Enter build description: ")
        
        # Create new build in database
        build = Build(name, description)
        build.save()
        
        print(f"\n{name} created successfully!")
        
        set_current = self.get_input("Set as current build? (y/n): ", ["y", "n"])
        if set_current == "y":
            self.current_build = build
        
        input("\nPress Enter to continue...")
        self.main_menu()
    
    def view_current_build(self):
        """View details of the current build"""
        if not self.current_build:
            print("No current build selected.")
            input("\nPress Enter to continue...")
            self.main_menu()
            return
        
        self.view_build_details(self.current_build)
    
    def add_component_to_build(self):
        """Add a component to the current build"""
        if not self.current_build:
            print("No current build selected.")
            input("\nPress Enter to continue...")
            self.main_menu()
            return
        
        self.browse_components()
    
    def delete_build(self, build):
        """Delete a build and its associated components"""
        # First, delete all build_components entries
        import sqlite3
        conn = sqlite3.connect('pc_builder.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM build_components WHERE build_id = ?", (build.id,))
        
        # Then delete the build
        cursor.execute("DELETE FROM builds WHERE id = ?", (build.id,))
        conn.commit()
        
        # If the deleted build was the current build, reset current_build
        if self.current_build and self.current_build.id == build.id:
            self.current_build = None

def main():
    """Main entry point for the CLI"""
    cli = CLI()
    
    while True:
        try:
            cli.main_menu()
        except KeyboardInterrupt:
            print("\nThank you for using PC Builder!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()