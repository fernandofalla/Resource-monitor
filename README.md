# Resource-monitor

Monitor resource consumption in server clusters by processing metrics in real time.

## Features
- **HPC Simulation:** Simulates live server workload metrics using Google Cluster Data traces.
- **Modular Design:** Built following Clean Architecture principles separating UI, Business Logic, and Components.
- **Performance Optimized:** Uses Pandas vectorization to efficiently handle large tabular datasets.

## Project Structure
```text
Resource-monitor/
├── src/
│   ├── services/
│   │   └── data_loader.py    # Pandas backend logic
│   └── ui/
│       ├── console_menu.py   # CLI Interface
│       └── file_dialog.py    # GUI File dialog component
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Resource-monitor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To launch the interactive resource monitor menu, run the main entry point:
```bash
python main.py
```