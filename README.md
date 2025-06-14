

# Multispectral panels control

## Overview

This repository provides a crude php page to control multispectral LED panels using a raspberry pi. 
The LED driver circuits are switched on and off using two Microchip MCP23017 - i2c 16 input/output port expanders.
The camera (Canon 5D MkIV DSLR) is controlled via gphoto: http://www.gphoto.org/

* **Spectral control**: Activate and manage LEDs across various spectral bands, including:
  * UV : 365nm, 385nm, 405nm
  * Blue: 425nm, 445nm, 460nm
  * Green: 530nm, 570nm
  * Red: 620nm, 670nm
  * Infrared: 730nm, 850nm, 950nm



## Repository structure

```
multispectral_panels/
├── panel 3D model/           # 3D printable model of one panel
├── panel circuit/            # circuit for 16 3W LEDs
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

## Getting started

### Prerequisites
* rapsberry pi 3, 4 or 5
* A web server with PHP support (e.g., Apache, Nginx)
* Python 3.x installed on the system
* i2ctools and gphoto 

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Niphargusproject/multispectral_panels.git
   ```

2. **Set up the Web interface**:

   * Place the repository contents in your web server's root directory.
   * Ensure the server has the necessary permissions to execute PHP scripts.


## Usage

* **Web interface**:

  * Navigate to `http://your_server_address/index.php` in your web browser.
  * Use the interface to control individual spectral bands, initiate photogrammetry sessions, and manage settings.
  * Execute scripts like `leds_panels.py` or `photogram_panels.py` for automated operations.
  * Integrate these scripts into larger workflows or scheduling systems as needed.



This project is licensed under the [GNU General Public License v3.0](LICENSE)

RBINS-GSB 2025

