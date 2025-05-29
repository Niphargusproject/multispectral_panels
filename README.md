

# Multispectral Panels Control

## Overview

This repository provides a crue  php page to control multispectral LED panels.

## Features

* **Spectral Control**: Activate and manage LEDs across various spectral bands, including:
  * UV : 365nm, 385nm, 405nm
  * Blue: 425nm, 445nm, 460nm
  * Green: 530nm, 570nm
  * Red: 620nm, 670nm
  * Infrared: 730nm, 850nm, 950nm

* **Web Interface**: User-friendly PHP-based web interface for real-time control and monitoring.

* **Python Scripts**: Automation scripts for batch operations and integration with other systems.

* **Photogrammetry Support**: Tools to assist in capturing and processing multispectral images for photogrammetric analysis.

## Repository Structure

```
multispectral_panels/
├── css/                      # Stylesheets for the web interface
├── js/                       # JavaScript files for interactive UI elements
├── old/                      # Legacy scripts and backups
├── leds_anvil.py             # Python script for advanced LED control
├── leds_panels.py            # Main Python script for panel operations
├── leds_panels.php           # PHP script interfacing with the LED hardware
├── photogram_panels.py       # Python script for photogrammetry workflows
├── photogram_panels.php      # PHP counterpart for photogrammetry control
├── index.php                 # Main entry point for the web interface
├── backup.php                # Script for backing up configurations
├── edit.php                  # Interface for editing settings
├── kill.php                  # Script to terminate running processes
├── off.php                   # Script to turn off all LEDs
├── LICENSE                   # Project license (GPL-3.0)
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites

* A web server with PHP support (e.g., Apache, Nginx)
* Python 3.x installed on the system
* Hardware setup with multispectral LED panels connected and configured([iridesense.tech][1])

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Niphargusproject/multispectral_panels.git
   ```

2. **Set Up the Web Interface**:

   * Place the repository contents in your web server's root directory.
   * Ensure the server has the necessary permissions to execute PHP scripts.

3. **Configure Python Scripts**:

   * Install any required Python dependencies (if applicable).
   * Modify the scripts to match your hardware configuration and paths.

## Usage

* **Web Interface**:

  * Navigate to `http://your_server_address/index.php` in your web browser.
  * Use the interface to control individual spectral bands, initiate photogrammetry sessions, and manage settings.([slideplayer.com][2])

* **Python Scripts**:

  * Execute scripts like `leds_panels.py` or `photogram_panels.py` for automated operations.
  * Integrate these scripts into larger workflows or scheduling systems as needed.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or enhancements, please open an issue or submit a pull request.([tehranconvention.org][3])

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE)

RBINS-GSB 2025

