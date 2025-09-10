# 👋 Hi, I'm Shubham Kapil Upadhyay

🚀 **VLSI Design Engineer | MS in Electrical Engineering @ Purdue**  
🔍 *Specializing in RTL Design, FPGA Development & Digital System Architecture*

📧 [Email](mailto:vlsi.shubh@gmail.com)  |  🔗 [LinkedIn](https://linkedin.com/in/shubhamupadhyay0804)  |  📄 [Resume](https://drive.google.com/file/d/1NCIxMmLmM78j3nEdt0lJmdoHUu_N04Ju/view?usp=drive_link)  |  📍 United States


---
 🧭 **Philosophy**

> *"Designing tomorrow’s digital systems today — one clock cycle at a time."*

---
## 🧠 About Me

I’m a passionate digital designer focused on building efficient, scalable, and synthesizable hardware systems. With a strong foundation in **Verilog**, **FPGA development**, and **memory architecture**, I love translating abstract logic into real-world digital hardware.

Whether it’s architecting FSMs, optimizing datapaths, or exploring memory systems, I enjoy solving problems that live at the intersection of **elegant design and timing precision**.

---

## 🛠️ What I Do Best

- ✅ RTL Design & Verification (Verilog, VHDL)
- ✅ FPGA-based System Implementation (Xilinx, Vivado)
- ✅ Memory Architecture & FIFO Buffers
- ✅ FSM Design & Control Logic
- ✅ SoC Integration & Embedded Digital Systems

---

## 🔧 Technical Toolbox

**Hardware Description Languages**  
`Verilog • VHDL • SystemVerilog`

**Programming & Scripting**  
`Python • C • C++ • MATLAB • Tcl/Tk`

**EDA Tools & Synthesis**  
`Vivado • Cadence Virtuoso • Synopsys Design Compiler • GTKWave • Icarus Verilog • Yosys`

**Design & Verification**  
`RTL Design • FSM Architecture • Memory Systems • Functional Verification • Logic Synthesis`

**Protocols & Analysis**  
`UART • SPI • I2C • AXI • STA • CDC • Power Optimization`

---

## 🌟 Featured Projects 

### ⚡ [Asynchronous FIFO Buffer](https://github.com/VLSI-Shubh/Asynchronous-FIFO)
**Cross clock-domain FIFO with Gray code pointers & metastability prevention**  

- Designed a **parameterized dual-clock FIFO** enabling reliable data transfer across independent clock domains (100 MHz → 71.4 MHz).  
- Implemented **Gray code pointer synchronization** with dual flip-flop synchronizers, eliminating metastability and ensuring **0 simulation errors**.  
- Added **extra MSB flag logic** for precise full/empty detection, validated across **100+ corner cases** including rapid write/read bursts.  
- Achieved **zero synthesis warnings** in Vivado and generated post-synthesis schematics confirming correct RTL-to-gate mapping with **CDC-safe structures**.  
- Verified operation with comprehensive **VCD waveform analysis**, demonstrating safe flag propagation delays (1–2 cycles) and glitch-free operation.  
- Applications: **SoC interconnects, network packet buffers, DDR controllers**, and other high-speed CDC use cases.  

### 🔁 [Synchronous FIFO Buffer](https://github.com/VLSI-Shubh/FIFO)
**Parameterized memory buffer with pointer arithmetic & flag detection**  

- Built a **parameterized synchronous FIFO** operating on a single clock domain with configurable depth/width.  
- Designed **read/write pointer arithmetic with extra bit tracking** for accurate full/empty flag detection.  
- Verified functional correctness across **20+ critical transitions**, including back-to-back writes, reads, and empty-to-full cycles.  
- Achieved **zero synthesis warnings** in Vivado and clean RTL-to-gate mapping with no inferred latches.  
- Demonstrated **sequential data integrity** (10 → 20 → 30 …) through waveform analysis, confirming strict FIFO ordering.  
- Applications: **Pipelined data buffering, inter-module communication, and embedded controllers**.  

### 🎨 [Morphological Image Filtering on PYNQ FPGA](https://github.com/VLSI-Shubh/Morphological-Image-Filtering-on-PYNQ-FPGA)  
**Real-time image enhancement with FPGA-accelerated min, max, and median filters**  

- Implemented **morphological filtering (min, max, median)** on a **PYNQ-Z2 FPGA**, processing **64×64 RGB images** via AXI streams and DMA.  
- Designed custom **VHDL IP (`FilterSelect_v1_0`)** with independent R/G/B filter modules using shift registers and bubble sort for median filtering.  
- Integrated **hardware acceleration + Python control**, achieving **<10% LUT usage** while maintaining real-time performance.  
- Enabled **interactive filter selection** with 2 physical board switches, supporting min (00), median (01), and max (10) operations in real time.  
- Validated FPGA outputs against **MATLAB image processing**, confirming pixel-accurate results for noise reduction, edge preservation, and texture segmentation.  
- Overcame design challenges in **RGB channel handling and reconstruction**, ensuring lossless image recombination post-processing.  
- Excluded mean filter due to excessive latency, but maintained project timeline with full feature delivery.  
- Applications: **Biomedical imaging, digital photography, visual inspection systems, and FPGA-accelerated computer vision**.  
  
### 🚦 [Smart Traffic Controller FSM](https://github.com/VLSI-Shubh/Traffic-Controller-using-FSM)
**Sensor-based intelligent traffic management system**  

- Designed a **5-state FSM** that dynamically allocates Green/Yellow/Red signals based on live sensor inputs from 4 roads.  
- Implemented **priority-based state transitions** with configurable timers (55 cycles green, 10 cycles yellow).  
- Verified FSM determinism across **100+ simulation cycles**, ensuring no deadlocks or undefined states.  
- Synthesized in Vivado with **0 timing violations**, producing a clean schematic with state registers and control logic.  
- Demonstrated **real-time congestion reduction** with scalable timing parameters for smart city deployment.  
- Applications: **Intelligent transportation systems, pedestrian-aware traffic controllers, and FPGA-based IoT solutions**.  

### 💾 [Multi-Port SRAM Architectures](https://github.com/VLSI-Shubh/SRAM)
**Complete SRAM collection: Single/Dual Port variants**  

- Implemented **four SRAM designs**: single-port (sync/async read), pseudo dual-port, and true dual-port with independent clocks.  
- Verified **simultaneous read/write** in true dual-port SRAM across independent ports and clock domains.  
- Parameterized **depth and width** for scalable memory solutions, validated up to **256×32-bit arrays**.  
- Conducted **sync vs async read analysis**, showing predictable latency for synchronous reads and immediate access for async reads.  
- Achieved **successful Yosys synthesis** with clean schematics confirming correct memory array inference.  
- Applications: **CPU caches, FPGA memory blocks, dual-core communication buffers**.  

### 🛰️ [UART Communication Protocol](https://github.com/VLSI-Shubh/UART)  
**Parameterized full-duplex UART with baud rate generator and FSM-based TX/RX logic**  

- Designed a **full-duplex UART** with independent **4-state TX FSM** and **5-state RX FSM**, supporting 8N1 protocol.  
- Implemented **baud rate generator with 16× oversampling**, achieving reliable data reception across 9600–115,200 baud rates.  
- Verified **loopback communication** with clean VCD traces: TX complete @ 838,710 ns, RX complete @ 942,710 ns with 0xA5 integrity.  
- Developed **hierarchical RTL modules** for transmitter, receiver, and baud generator, ensuring modularity and reusability.  
- Synthesized and tested on FPGA toolchains with **0 functional mismatches across 50+ test cycles**.  
- Applications: **FPGA-to-PC communication, embedded serial links, SoC peripherals**.  

### 🧮 [8×8 Dadda Multiplier](https://github.com/VLSI-Shubh/Delay-and-Power-Analysis-of-a-Static-8x8-Dadda-Multiplier-Circuit)
**High-performance multiplier with hybrid logic optimization**  

- Designed an **8×8 Dadda multiplier** in 45 nm CMOS using hybrid logic: **Transmission Gate XOR/AND + CMOS OR gates**.  
- Achieved **critical path delay of 0.204 ns** (~2 GHz max frequency) with **power dissipation of 62.47 μW**.  
- Optimized **partial product reduction using 4:2 compressors**, minimizing transistor count while maintaining stability.  
- Compared performance vs **Wallace Tree and Booth multipliers**, demonstrating superior speed-power efficiency.  
- Validated design through **Cadence Virtuoso pre/post-layout simulations**, confirming timing closure and scalability.  
- Applications: **High-speed arithmetic units in DSPs, RISC processors, and low-power accelerators**.  
---

## 💼 Experience

### 💻 Firmware Engineer @ WinWin Labs (Volunteer)  
*Remote, US | Aug 2025 – Present*  
- Developed embedded firmware for IoT systems using **C/C++**, implementing real-time communication protocols (**UART, SPI, I²C**) with interrupt handling and buffer management.  
- Collaborated with hardware teams on board bring-up, interface validation, and system-level debugging of microcontroller-based platforms including **PlatformIO** development environments and **Arduino DevKit** boards.  
- Programmed and tested embedded applications for connected IoT devices, ensuring reliable operation in resource-constrained environments with hands-on experience on **Xilinx Pynq-Z2** development boards and **ESP32** microcontroller platforms.   

### 🎓 Graduate Teaching Assistant @ Purdue University (EPICS)  
*Aug 2024 – May 2025 | Indianapolis, IN*  
- Mentored 35+ engineering students in **AI/ML application development** for *Vaani Connect* speech-to-text translation project.  
- Designed and implemented technical platforms and testing frameworks, improving project development efficiency by **30%**.  
- Provided technical guidance in **digital design, RTL coding, and verification methodologies** across First-Year Engineering programs.  

### 👨‍💻 Engineering Intern @ Thyssenkrupp Crankshaft Company  
*May 2024 – Aug 2024 | Illinois, US*  
- Evaluated **Marposs system components** for electrical compatibility and upgrade planning across critical machines.  
- Created standardized parts lists and collaborated with OEM support for phased system modernization.  

### 🧑‍🏭 Junior Electrical Manager @ 21 Knots Engineering  
*Feb 2022 – July 2023 | Mumbai, IN*  
- Led procurement and execution for major electrical engineering projects  
- Maintained 100% execution success and high client satisfaction

### 🧑‍🔧 Senior Electrical Design Engineer @ Petrocil Engineering  
*June 2019 – Jan 2022 | Mumbai, IN*  
- Delivered over 10 successful electrical design projects  
- Improved on-site technical resolution by 10%

---

## 🎓 Education

**MS Electrical Engineering**  
*Purdue University Indianapolis*  
Specialization: VLSI Design & FPGA Systems

---

## 🏆 Highlights

- 💡 Passionate about crafting efficient, synthesizable hardware that just works  
- 🔍 Continuously learning and mastering complex RTL design and verification techniques  
- 🤝 Enjoy collaborating with cross-disciplinary teams to bring projects to life  
- 🛠️ Experienced in bridging theoretical designs with practical FPGA implementations  
- 🚀 Always pushing boundaries by exploring new architectures and optimization methods  


---



















