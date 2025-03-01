# PC Builder

A command-line application for building and managing custom PC configurations.

## Overview

PC Builder allows you to:
- Browse a catalog of PC components by category
- Create custom PC builds by selecting compatible components
- View detailed information about each component
- Calculate the total price of each build
- Save and manage multiple builds

## Project Structure

```
pc_builder/
├── models/
│   ├── __init__.py
│   ├── component.py
│   ├── build.py
│   └── database.py
├── seed_data.py
├── cli.py
├── main.py
└── README.md
```

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/pc-builder.git
cd pc-builder
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the application:
```
python main.py
```

This will:
1. Create the database if it doesn't exist
2. Seed it with sample data
3. Start the command-line interface

## Features

### Component Management
- Browse components by category (CPU, GPU, Motherboard, etc.)
- View detailed component specifications
- Add new components to the catalog

### Build Management
- Create new custom PC builds
- Add components to builds
- Remove components from builds
- Calculate total price of builds
- Check component compatibility

## Database Schema

### Tables

1. **components**
   - id (INTEGER PRIMARY KEY)
   - name (TEXT)
   - category (TEXT)
   - price (REAL)

2. **builds**
   - id (INTEGER PRIMARY KEY)
   - name (TEXT)
   - description (TEXT)

3. **build_components** (Join table)
   - id (INTEGER PRIMARY KEY)
   - build_id (INTEGER, FOREIGN KEY)
   - component_id (INTEGER, FOREIGN KEY)

## Future Enhancements

- Advanced compatibility checking
- Price comparison from different retailers
- Performance benchmarking
- Export/import builds
- Web interface