<div align="center">
  <br />
  <p>
    <h1> Ashreach/ThLun </h1>
    <img src='./assets/banner.svg' height=300>
    
  </p>
  <br />
  <p align="center">
    <a href="https://github.com/Ashreach/ThLun/stargazers">
      <img src="https://img.shields.io/github/stars/Ashreach/ThLun?colorA=363a4f&colorB=b7bdf8&style=for-the-badge" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/Ashreach/ThLun/issues">
      <img src="https://img.shields.io/github/issues/Ashreach/ThLun?colorA=363a4f&colorB=f5a97f&style=for-the-badge" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/Ashreach/ThLun/contributors">
      <img src="https://img.shields.io/github/contributors/Ashreach/ThLun?colorA=363a4f&colorB=a6da95&style=for-the-badge" alt="GitHub contributors"/>
    </a>
  </p>
</div>

## About

**ThLun** is a Python CLI library for stylish terminal output with ANSI colors, logging, progress bars, and spinners.

## Preview

<div align="center">
  <img src="./assets/preview.gif" alt="ThLun Preview" >
</div>

## Installation

```bash
pip install thlun
```

## Quick Start

```python
from ThLun import bprint, Logger, ProgressBar, Spinner, Spinners
import time

# Basic colored output
bprint("[GREEN]Hello world...[RESET]")

# Logging with levels
logger = Logger('DEBUG')
logger.info("Application started")
logger.error("Something went wrong")

# Progress bar
progress = ProgressBar(total=100)
for i in range(100):
    progress.update(i + 1)
    time.sleep(0.01)

# Spinner for loading
spinner = Spinner(Spinners.dots)
spinner.start("Loading...")
time.sleep(2)
spinner.stop()
```

<img src='./assets/preview.png'>

## Features

- **ANSI Colors**: Full color support with Fore, Back, and Style classes
- **IO Module**: Enhanced printing with color and style support
- **Logger**: Multi-level logging with colored output
- **Progress Bars**: Visual progress indicators
- **Spinners**: Loading animations with customizable styles
- **Screen Control**: Clear screen and cursor positioning


## Colors

<img src='https://cdn.yurba.one/photos/3934.jpg'>