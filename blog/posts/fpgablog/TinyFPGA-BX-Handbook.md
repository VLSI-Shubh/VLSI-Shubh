# TinyFPGA BX Programming Handbook (Windows Edition)
**Complete Guide for Modern FPGA Development Using Apio 1.2.1**

**Last Updated:** January 2026  
**Target OS:** Windows 10/11  
**Apio Version:** 1.2.1 (Latest Release)  
**Board:** TinyFPGA BX (Lattice iCE40LP8K-CM81)



## 📋 Table of Contents

1. [Introduction](#introduction)
2. [What's Changed Since 2018](#whats-changed-since-2018)
3. [Windows Installation Guide](#windows-installation-guide)
4. [Universal Project Structure](#universal-project-structure)
5. [Development Workflow](#development-workflow)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Pin Reference Guide](#pin-reference-guide)
8. [Quick Reference](#quick-reference)
9. [Resources & Links](#resources--links)



## Introduction

### The Problem: Outdated Official Guide

**The Issue:** The [official TinyFPGA BX guide](https://tinyfpga.com/bx/guide.html) recommends:
- **Atom Editor** (discontinued December 2022 ❌)
- **Apio 0.4.0b5** (from 2018, 8 years old ❌)
- **Old commands** like `apio verify` and `apio build`

**The Solution:** This handbook uses modern tools:
- ✅ **Any text editor** (VS Code, Notepad++, Sublime, or just Command Prompt)
- ✅ **Apio 1.2.1** (latest as of January 2026)
- ✅ **New commands** like `apio lint` and `apio upload`

### What is TinyFPGA BX?

- **FPGA:** Lattice iCE40LP8K-CM81  
- **Logic Elements:** 7,680 LUTs (Logic cells)  
- **RAM:** 128 KB (32 × 4KB blocks)  
- **User I/O Pins:** 41 pins  
- **Size:** 18mm × 36mm (breadboard-friendly)  
- **USB:** Built-in bootloader (no external programmer needed)  
- **Toolchain:** 100% open-source (Project IceStorm)

### How Programming Works

```
Verilog Code
    ↓
Yosys (Synthesis) → Converts to netlist
    ↓
NextPNR (Place & Route) → Physical layout
    ↓
IcePack (Bitstream Generation) → .bin file
    ↓
tinyprog (USB Upload) → Programs FPGA
```

**Apio automates all of these steps!**



## What's Changed Since 2018

### Major Updates

| Old (2018) | New (2026) | Notes |
|------------|------------|-------|
| `apio==0.4.0b5` | `apio==1.2.1` | Complete rewrite |
| `pip install apio` | Installer `.exe` | Professional packaging |
| `apio install ...` | Built-in packages | No separate installation |
| `apio verify` | `apio lint` | Command renamed |
| `apio build` | Integrated in `upload` | Automatic build |
| Atom IDE | Any editor | No IDE required |
| Python 3.6 | Python 3.14 | Modern Python |

### Why You Can't Use Old Guides

1. **Apio 0.4.0b5 requires manual package installation** → Modern Apio bundles everything
2. **Old commands don't exist** → `apio verify` is now `apio lint`
3. **Different project structure** → `apio.ini` format changed
4. **USB drivers** → Windows 10/11 handles automatically



## Windows Installation Guide

### Prerequisites

- **Windows 10 or Windows 11** (64-bit)
- **USB data cable** (NOT charge-only)
- **TinyFPGA BX board**
- **Administrator privileges** (for installation only)

### Step 1: Download Apio CLI Installer

**Official Release Page:** https://github.com/FPGAwars/apio/releases

1. **Find Latest Stable Release:** Look for the most recent release **without** "Pre-release" tag
   - As of January 2026: `2026-01-08` or later
   
2. **Download Windows Installer:**
   ```
   apio-cli-windows-amd64-[DATE]-installer.exe
   ```
   Example: `apio-cli-windows-amd64-20260108-installer.exe`

3. **IMPORTANT: Unblock the File**
   - Right-click the downloaded `.exe` file
   - Select **Properties**
   - Check the **Unblock** checkbox at the bottom
   - Click **OK**
   - *This allows Windows to run the unsigned installer*

### Step 2: Install Apio CLI

1. **Double-click** the installer file
2. **Windows SmartScreen Warning:** Click "More info" → "Run anyway"
3. **Follow the installer wizard:**
   - Accept license
   - Choose installation location (default: `C:\Program Files\apio`)
   - Installer automatically adds Apio to PATH
4. **Click "Finish"** when complete

### Step 3: Verify Installation

**IMPORTANT:** Open a **NEW** Command Prompt window after installation.

```cmd
apio --version
```

**Expected Output:**
```
apio, version 1.2.1
```

If you see `apio is not recognized...`, restart your computer and try again.

### Step 4: Install tinyprog (USB Programmer)

Apio CLI does NOT include tinyprog, so we install it separately:

```cmd
pip install tinyprog
```

**Verify tinyprog:**
```cmd
tinyprog --help
```

### Step 5: Test Board Connection

1. **Connect TinyFPGA BX** via USB
2. **Press RESET button** on board
   - **Boot LED should pulse** slowly (breathing effect)
   - This means bootloader is active
3. **List connected boards:**

```cmd
tinyprog -l
```

**Expected Output:**
```
TinyFPGA BX detected at:
    Bootloader (v1.0.1)
    Serial: 12345678-1234-1234-1234-123456789012
    Type: TinyFPGA BX
```

If you see errors, see [Troubleshooting](#troubleshooting-guide).

### Step 6: Update Bootloader (Recommended)

```cmd
tinyprog --update-bootloader
```

Follow prompts. This fixes USB issues on older boards.



## Universal Project Structure

Every TinyFPGA BX project needs exactly 3 files:

```
my-project/
├── apio.ini       # Project configuration (REQUIRED)
├── pins.pcf       # Pin mappings (REQUIRED)
└── main.v         # Top-level Verilog (REQUIRED)
```

**That's it!** No extra folders, no complex structure.

### File 1: apio.ini (Project Configuration)

**Purpose:** Tells Apio which board you're using and what the top module is called.

**Template:**
```ini
[env:tinyfpga-bx]
board = tinyfpga-bx
top-module = main
```

**CRITICAL NOTES:**
- Board name is **`tinyfpga-bx`** (lowercase, with hyphen)
- Top module **MUST** be named `main`
- Do NOT change these values

### File 2: pins.pcf (Pin Constraints)

**Purpose:** Maps Verilog port names to physical FPGA pins.

**Important Notes:**
- **Pin numbers use FPGA ball names** (like `B3`, `A2`) **NOT physical board pin numbers**
- The on-board LED is at FPGA pin **`B3`** (not pin 6)
- The 16MHz clock is at FPGA pin **`B2`**

**Template:**
```pcf
# Clock (16MHz internal oscillator)
set_io clk B2

# On-board LED (NOT pin 6, it's FPGA ball B3)
set_io led B3

# External pins (example - see pin reference for more)
# set_io button A2
# set_io output_pin H9
```

**Common Mistake:** Using board pin numbers instead of FPGA ball names.
- ❌ WRONG: `set_io led 6`  
- ✅ CORRECT: `set_io led B3`

### File 3: main.v (Top-Level Verilog)

**Purpose:** Your FPGA design code.

**Critical Rules:**
1. **Module MUST be named `main`** (not `top`, not anything else)
2. **All ports here must match pins.pcf exactly**
3. **Port names are case-sensitive**

**Template:**
```verilog
// main.v - Top-level module for TinyFPGA BX
module main (
    input  clk,        // 16MHz clock from B2
    output led         // On-board LED at B3
);

    // Your design code here
    // Example: Blink LED at ~0.6Hz
    reg [23:0] counter = 0;
    
    always @(posedge clk) begin
        counter <= counter + 1;
    end
    
    assign led = counter[23];

endmodule
```



## Development Workflow

### Quick Start: Create New Project

**Open Command Prompt and run:**

```cmd
mkdir my-project
cd my-project

REM Create apio.ini
echo [env:tinyfpga-bx] > apio.ini
echo board = tinyfpga-bx >> apio.ini
echo top-module = main >> apio.ini

REM Create pins.pcf
echo # Pin constraints > pins.pcf
echo set_io clk B2 >> pins.pcf
echo set_io led B3 >> pins.pcf

REM Create main.v (copy template above)
notepad main.v
```

### Standard Development Commands

**Modern Apio 1.2.1 uses simplified commands:**

```cmd
REM 1. CHECK SYNTAX (optional but recommended)
apio lint

REM 2. BUILD & UPLOAD TO FPGA (one command does both!)
apio upload
```

**That's it!** Just two commands.

### Command Details

#### `apio lint` - Check Syntax

- **Purpose:** Validates Verilog syntax before synthesis
- **Speed:** Very fast (~1 second)
- **When to use:** While coding, before uploading
- **Output:** Shows syntax errors and warnings

**Example:**
```cmd
C:\Users\You\my-project> apio lint

[INFO] Linting...
[INFO] main.v: No issues found
[SUCCESS] Lint completed
```

#### `apio upload` - Build & Program FPGA

- **Purpose:** Synthesizes design, generates bitstream, and uploads to FPGA
- **Speed:** 30-90 seconds (depending on design complexity)
- **When to use:** When ready to test on hardware

**What it does automatically:**
1. Runs synthesis (Yosys)
2. Place & route (NextPNR)
3. Generates bitstream (IcePack)
4. Uploads via USB (tinyprog)

**Requirements:**
- Board must be connected
- Press RESET button before upload (boot LED pulses)

**Example:**
```cmd
C:\Users\You\my-project> apio upload

[INFO] Building project...
[INFO] Synthesis (Yosys)...
[INFO] Place & Route (NextPNR)...
Info: Device utilisation:
Info:   ICESTORM_LC:    24/ 7680     0%
Info:   ICESTORM_RAM:    0/   32     0%
Info:   SB_IO:           2/   41     4%
[INFO] Generating bitstream...
[INFO] Uploading to TinyFPGA BX...
[INFO] Programming TinyFPGA BX...
[SUCCESS] Upload complete!
```

### Understanding Build Output

**Resource Utilization:**
```
Info: Device utilisation:
Info:   ICESTORM_LC:   1234/ 7680    16%
Info:   ICESTORM_RAM:     2/   32     6%
Info:   SB_IO:            5/   41    12%
```

**What it means:**
- **ICESTORM_LC:** Logic cells used (each = ~1 LUT + 1 flip-flop)
- **ICESTORM_RAM:** Block RAM usage (128KB total)
- **SB_IO:** I/O pins used

**Limits:**
- Max 7,680 logic cells
- Max 32 RAM blocks (4KB each)
- Max 41 user I/O pins

### Testing Your Design

**After uploading:**
1. **Press RESET button** to exit bootloader
2. **Your design runs immediately**
3. **LED/outputs should activate**

**To reprogram:**
1. **Press RESET button** → Boot LED pulses
2. Run `apio upload` again




## Troubleshooting Guide

### Error: "board 'tinyfpga-bx' not connected"

**Symptoms:**
```
[ERROR] Board 'tinyfpga-bx' not connected
```

**Causes & Solutions:**

**1. Board not in bootloader mode**
- **Fix:** Press RESET button on board
- **Verify:** Boot LED should pulse slowly
- **Then:** Run `apio upload` within 8 seconds

**2. USB cable is charge-only**
- **Fix:** Try a different USB cable
- **Test:** Cable must support data transfer

**3. USB driver not installed (Windows 7/8 only)**
- **Windows 10/11:** Drivers install automatically
- **Windows 7/8:** Install [universal serial driver](https://www.pjrc.com/teensy/serial_install.exe)

**4. Wrong USB port**
```cmd
REM Check which port the board is on
tinyprog -l
```

### Error: "cannot open apio.ini"

**Cause:** `apio.ini` file missing or in wrong directory

**Fix:**
```cmd
REM Make sure you're in the project directory
cd C:\path\to\your\project

REM Verify apio.ini exists
dir apio.ini

REM If missing, recreate it
echo [env:tinyfpga-bx] > apio.ini
echo board = tinyfpga-bx >> apio.ini
echo top-module = main >> apio.ini
```

### Error: "module 'main' not found"

**Cause:** Top module in Verilog isn't named `main`

**Fix:**
```verilog
// WRONG:
module top (...);          // ❌
module blink (...);        // ❌
module TinyFPGA_BX (...);  // ❌

// CORRECT:
module main (...);         // ✅
```

### Error: "can't resolve port 'led'"

**Cause:** Port name mismatch between `main.v` and `pins.pcf`

**Example Problem:**
```verilog
// main.v
module main (
    output LED    // ← Capital "LED"
);
```

```pcf
# pins.pcf
set_io led B3  # ← Lowercase "led"
```

**Fix:** Names must match EXACTLY (case-sensitive):
```verilog
// main.v
module main (
    output led    // ✅ Matches pins.pcf
);
```

### Error: "design does not fit"

**Symptoms:**
```
ERROR: Design does not fit:
       8000/7680 logic cells used
```

**Cause:** Design too large for iCE40LP8K

**Solutions:**
1. Simplify logic
2. Reduce number of registers
3. Use smaller data widths
4. Share resources (muxes instead of parallel logic)

### Board Not Detected by Windows

**Check Device Manager:**
1. Press `Win + X` → Device Manager
2. Look under "Ports (COM & LPT)"
3. Should see "TinyFPGA BX Bootloader (COMx)"

**If not listed:**
- Try different USB port
- Try different USB cable
- Restart computer
- Check board power LED is on

### Bootloader Not Responding

**Recovery Mode:**
1. **Disconnect USB**
2. **Press and HOLD reset button**
3. **Plug in USB** (while holding button)
4. **Release button after 2 seconds**
5. **Boot LED should pulse**

**If still not working:**
- Board may need JTAG recovery (advanced)
- Contact TinyFPGA support



## Pin Reference Guide

### Understanding Pin Naming

**TinyFPGA BX has TWO pin numbering systems:**

1. **Board Pin Numbers (1-41):** Physical pins on the board edges
2. **FPGA Ball Names (A1, B3, etc.):** Internal FPGA pin designations

**⚠️ CRITICAL:** `pins.pcf` uses **FPGA ball names**, NOT board pin numbers!

### Common FPGA Pin Assignments

| Function | FPGA Pin | Board Pin | Notes |
|----------|----------|-----------|-------|
| **16MHz Clock** | `B2` | - | Internal oscillator |
| **On-board LED** | `B3` | - | Active HIGH |
| **USB D+** | `B4` | - | Used by bootloader |
| **USB D-** | `A4` | - | Used by bootloader |
| **User I/O** | `A2`, `A1`, `B1`, `C2`, etc. | Various | See full pinout |

### Full Pin Mapping (FPGA → Board)

For the complete pin mapping, see the [official pins.pcf template](https://github.com/tinyfpga/TinyFPGA-BX/blob/master/apio_template/pins.pcf).

**Most commonly used pins:**

```pcf
# Essential pins
set_io clk B2       # 16MHz clock
set_io led B3       # On-board LED

# Board edge pins (examples)
set_io PIN_1  A2
set_io PIN_2  A1
set_io PIN_3  B1
set_io PIN_4  C2
set_io PIN_5  C1
set_io PIN_6  D2
set_io PIN_7  D1
set_io PIN_8  E2
set_io PIN_9  E1
set_io PIN_10 G2
set_io PIN_11 H1
set_io PIN_12 J1
set_io PIN_13 H2
```

**⚠️ WARNING:** Not all board pins can be used! Pins used by USB, SPI flash, and other functions are reserved.

### Pin Usage Rules

1. **Always start with clock and LED** for testing
2. **Don't use USB pins** (B4, A4) - they're reserved
3. **Don't use SPI flash pins** - board won't boot
4. **3.3V logic only** - do NOT apply 5V to any pin
5. **Check pinout diagram** before wiring external hardware



## Quick Reference

### Installation Commands

```cmd
REM Download installer from:
REM https://github.com/FPGAwars/apio/releases

REM After installation, verify:
apio --version

REM Install tinyprog:
pip install tinyprog
```

### Project Creation

```cmd
mkdir my-project
cd my-project

REM Create required files:
notepad apio.ini     # Add config
notepad pins.pcf     # Add pin mappings
notepad main.v       # Add Verilog code
```

### Development Commands

```cmd
REM Check syntax:
apio lint

REM Build and upload:
apio upload

REM List connected boards:
tinyprog -l

REM Update bootloader:
tinyprog --update-bootloader
```

### Required Files Template

**apio.ini:**
```ini
[env:tinyfpga-bx]
board = tinyfpga-bx
top-module = main
```

**pins.pcf:**
```pcf
set_io clk B2
set_io led B3
```

**main.v:**
```verilog
module main (
    input  clk,
    output led
);
    // Your design here
endmodule
```

### Hardware Checklist

- [ ] TinyFPGA BX board
- [ ] USB data cable (NOT charge-only)
- [ ] Power LED lights up when connected
- [ ] Boot LED pulses after pressing RESET
- [ ] Windows Device Manager shows COM port
- [ ] `tinyprog -l` lists the board

### Common Mistakes

| Mistake | Correction |
|---------|------------|
| Using Apio 0.4.0b5 | Use Apio 1.2.1 |
| `apio verify` command | Use `apio lint` |
| `apio build` separately | Just use `apio upload` |
| `set_io led 6` | Use `set_io led B3` |
| `module top (...)` | Use `module main (...)` |
| Charge-only USB cable | Use data-capable cable |
| Board pin numbers in .pcf | Use FPGA ball names (B3, etc.) |



## Resources & Links

### Official Documentation

- **Apio Installation Guide:** https://fpgawars.github.io/apio/docs/installing-apio-cli/
- **Apio Release Page:** https://github.com/FPGAwars/apio/releases
- **TinyFPGA BX User Guide:** https://tinyfpga.com/bx/guide.html *(use modern commands from this handbook)*
- **TinyFPGA BX GitHub:** https://github.com/tinyfpga/TinyFPGA-BX
- **Project IceStorm:** http://www.clifford.at/icestorm/

### Pin Reference

- **Official pins.pcf Template:** https://github.com/tinyfpga/TinyFPGA-BX/blob/master/apio_template/pins.pcf
- **TinyFPGA BX Pinout Diagram:** https://tinyfpga.com/bx/guide.html#pin-assignment

### Tutorials & Examples

- **TinyFPGA BX Examples:** https://github.com/tinyfpga/TinyFPGA-BX/tree/master/examples
- **Getting Started (Woolsey Workshop):** https://www.woolseyworkshop.com/2019/08/30/getting-started-with-the-tinyfpga-bx/ *(note: uses old Apio version)*
- **FPGA Intro (Instructables):** https://www.instructables.com/INTRODUCTION-TO-FPGAS-USING-TINY-FPGA-BX/ *(note: uses old Apio version)*

### Tools & Extensions

- **VS Code:** https://code.visualstudio.com/
- **VS Code Verilog Extension:** Search "Verilog-HDL" in VS Code marketplace
- **Notepad++:** https://notepad-plus-plus.org/
- **GTKWave (Waveform Viewer):** http://gtkwave.sourceforge.net/

### Community & Support

- **TinyFPGA Discourse Forum:** https://discourse.tinyfpga.com/
- **Reddit r/FPGA:** https://www.reddit.com/r/FPGA/
- **FPGAwars GitHub:** https://github.com/FPGAwars

### Version Information

**This handbook is based on:**
- **Apio CLI Version:** 1.2.1 (Released December 29, 2025)
- **Latest Build:** 2026-01-08
- **Python Version:** 3.14
- **Package:** `apio-cli-windows-amd64-20260108-installer.exe`

**Check for updates:** https://github.com/FPGAwars/apio/releases/latest



## Additional Notes for Other Operating Systems

**This handbook focuses on Windows**, but Apio 1.2.1 also supports:

### macOS

**Installation:**
- Download `.pkg` installer from releases page
- Follow macOS-specific instructions: https://fpgawars.github.io/apio/docs/installing-apio-cli/

### Linux

**Installation:**
- Debian/Ubuntu: Download `.deb` package
- Other: Use pip or binary bundle
- **IMPORTANT:** Add user to `dialout` group:
  ```bash
  sudo usermod -a -G dialout $USER
  logout  # Must logout for changes to take effect
  ```



## About This Handbook

**Created:** 01st January 2026  
**Author:** [Shubham Upadhyay](https://github.com/VLSI-Shubh), Community-maintained guide based on official Apio 1.2.1 documentation  
**License:** [MIT Licence](../../../License.txt) 

**Disclaimer:** TinyFPGA hardware and official documentation are property of TinyFPGA. Apio and IceStorm are open-source projects with respective licenses.

**Contributing:** Found an error or have improvements? The FPGA community welcomes corrections and updates!

---

**Good luck with your FPGA projects! 🚀**

*Remember: Modern tools make FPGA development much easier than it used to be. With Apio 1.2.1, you're just two commands away from running Verilog on hardware!*